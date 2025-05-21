# 从Google学术链接中提取论文信息的PowerShell脚本

# 禁用证书验证警告
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

function Get-PaperInfo {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Url,
        [bool]$VerifySsl = $true,
        [int]$MaxRetries = 3
    )

    # 设置请求头，模拟浏览器访问
    $headers = @{
        'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        'Accept' = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        'Accept-Language' = 'zh-CN,zh;q=0.9,en;q=0.8'
    }

    $paperInfo = @{}
    $retryCount = 0
    $success = $false

    while (-not $success -and $retryCount -lt $MaxRetries) {
        try {
            # 设置SSL验证
            if (-not $VerifySsl) {
                [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
            }

            # 发送HTTP请求
            $response = Invoke-WebRequest -Uri $Url -Headers $headers -UseBasicParsing -TimeoutSec 10
            $success = $true

            # 使用正则表达式提取信息
            # 提取标题
            $titleMatch = [regex]::Match($response.Content, '<h1\s+class="title"[^>]*>(.*?)</h1>')
            if ($titleMatch.Success) {
                $paperInfo.title = $titleMatch.Groups[1].Value.Trim()
            } else {
                # 尝试其他可能的标题标签
                $titleMatch = [regex]::Match($response.Content, '<div\s+class="gs_ri"[^>]*>.*?<h3[^>]*>(.*?)</h3>')
                if ($titleMatch.Success) {
                    $paperInfo.title = $titleMatch.Groups[1].Value.Trim()
                }
            }

            # 提取作者列表
            $authorsMatch = [regex]::Match($response.Content, '<div\s+class="gs_a"[^>]*>(.*?)</div>')
            if ($authorsMatch.Success) {
                $authorsText = $authorsMatch.Groups[1].Value.Trim()
                # 通常作者在第一个 '-' 之前
                if ($authorsText -match '(.+?)\s*-\s*') {
                    $authors = $matches[1].Trim()
                    $paperInfo.authors = $authors -split ',' | ForEach-Object { $_.Trim() }
                }
            }

            # 提取期刊/会议名称
            if ($authorsMatch.Success) {
                $venueText = $authorsMatch.Groups[1].Value.Trim()
                # 期刊/会议名称通常在第一个和第二个 '-' 之间
                if ($venueText -match '-.+?-') {
                    $venue = $venueText -replace '^.+?-\s*(.+?)\s*-.*$', '$1'
                    $paperInfo.venue = $venue.Trim()
                }
            }

            # 提取发表年份
            $yearMatch = [regex]::Match($venueText, '\b(19|20)\d{2}\b')
            if ($yearMatch.Success) {
                $paperInfo.year = $yearMatch.Value
            }

            # 提取引用次数
            $citationsMatch = [regex]::Match($response.Content, '被引用次数：(\d+)')
            if ($citationsMatch.Success) {
                $paperInfo.citations = [int]$citationsMatch.Groups[1].Value
            }

        } catch [System.Net.WebException] {
            $retryCount++
            Write-Host "请求错误: $_"
            if ($retryCount -lt $MaxRetries) {
                Write-Host "重试 $retryCount/$MaxRetries..."
                Start-Sleep -Seconds (2 * $retryCount)
            }
            # 如果是SSL错误并且启用了验证，尝试禁用验证重试
            if ($VerifySsl -and $_.Exception.Message -match "SSL|证书") {
                Write-Host "尝试禁用SSL验证重试..."
                $VerifySsl = $false
                $retryCount--
            }
        } catch {
            Write-Host "处理错误: $_"
            $retryCount++
            if ($retryCount -lt $MaxRetries) {
                Write-Host "重试 $retryCount/$MaxRetries..."
                Start-Sleep -Seconds (2 * $retryCount)
            }
        }
    }

    return $paperInfo
}

function ConvertTo-Markdown {
    param (
        [hashtable]$PaperInfo
    )

    if ($null -eq $PaperInfo -or $PaperInfo.Count -eq 0) {
        return "无法获取论文信息"
    }

    $markdown = New-Object System.Collections.ArrayList

    # 添加标题
    if ($PaperInfo.ContainsKey('title')) {
        [void]$markdown.Add("# $($PaperInfo.title)")
        [void]$markdown.Add("")
    }

    # 添加作者
    if ($PaperInfo.ContainsKey('authors')) {
        [void]$markdown.Add("**作者**: $($PaperInfo.authors -join ', ')")
    }

    # 添加发表信息
    $pubInfo = New-Object System.Collections.ArrayList
    if ($PaperInfo.ContainsKey('venue')) {
        [void]$pubInfo.Add("**期刊/会议**: $($PaperInfo.venue)")
    }
    if ($PaperInfo.ContainsKey('year')) {
        [void]$pubInfo.Add("**年份**: $($PaperInfo.year)")
    }
    if ($pubInfo.Count -gt 0) {
        [void]$markdown.Add($pubInfo -join "`n")
        [void]$markdown.Add("")
    }

    # 添加引用信息
    if ($PaperInfo.ContainsKey('citations')) {
        [void]$markdown.Add("**引用次数**")
        [void]$markdown.Add("$($PaperInfo.citations)")
        [void]$markdown.Add("")
    }

    return $markdown -join "`n"
}

function Save-MarkdownToFile {
    param (
        [string]$MarkdownContent,
        [string]$Filename
    )

    $MarkdownContent | Out-File -FilePath $Filename -Encoding UTF8
    Write-Host "已保存到文件: $Filename"
}

# 主函数
function Main {
    param (
        [string[]]$Urls,
        [string]$File,
        [string]$Output,
        [switch]$Quiet
    )

    $urlList = @()

    # 从命令行参数获取URLs
    if ($Urls) {
        $urlList += $Urls
    }

    # 从文件读取URLs
    if ($File) {
        try {
            $fileUrls = Get-Content -Path $File | Where-Object { $_ -match '\S' }
            $urlList += $fileUrls
        } catch {
            Write-Host "读取文件出错: $_"
            exit 1
        }
    }

    # 如果没有提供URLs，显示帮助信息
    if ($urlList.Count -eq 0) {
        # 默认使用一个示例URL
        if (-not $Quiet) {
            Write-Host "未提供URLs，使用默认示例链接..."
        }
        $urlList = @(
            "https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Joint+Modeling+of+Image+and+Label+Statistics+for+Enhancing+Model+Generalizability+of+Medical+Image+Segmentation&btnG="
        )
    }

    if (-not $Quiet) {
        Write-Host "Google学术论文信息提取工具"
        Write-Host ("=" * 40)
    }

    $urlIndex = 0
    foreach ($url in $urlList) {
        if (-not $Quiet) {
            Write-Host "`n处理链接: $url"
            Write-Host "正在获取论文信息..."
        }

        $paperInfo = Get-PaperInfo -Url $url

        if ($paperInfo -and $paperInfo.Count -gt 0) {
            # 生成markdown格式
            $markdownContent = ConvertTo-Markdown -PaperInfo $paperInfo

            if (-not $Quiet) {
                Write-Host "`nMarkdown格式:"
                Write-Host ("-" * 40)
                Write-Host $markdownContent
            }

            # 确定输出文件名
            if ($Output) {
                $filename = $Output
            } elseif ($paperInfo.ContainsKey('title')) {
                # 使用论文标题的前20个字符作为文件名
                $safeTitle = $paperInfo.title.Substring(0, [Math]::Min(20, $paperInfo.title.Length))
                $safeTitle = [regex]::Replace($safeTitle, '[^\w\s]', '')
                $safeTitle = $safeTitle.Trim().Replace(" ", "_")
                $filename = "$safeTitle.md"
            } else {
                $filename = "paper_info.md"
            }

            # 如果处理多个URL并使用自定义输出名称，添加序号
            if ($Output -and $urlList.Count -gt 1) {
                $name = [System.IO.Path]::GetFileNameWithoutExtension($filename)
                $ext = [System.IO.Path]::GetExtension($filename)
                $filename = "${name}_$($urlIndex + 1)$ext"
            }

            Save-MarkdownToFile -MarkdownContent $markdownContent -Filename $filename
            if (-not $Quiet) {
                Write-Host "已保存到文件: $filename"
            }
        } else {
            if (-not $Quiet) {
                Write-Host "无法获取论文信息，请检查链接是否正确。"
            }
        }

        # 多个链接之间添加随机延迟
        if ($urlIndex -lt $urlList.Count - 1) {
            $delay = Get-Random -Minimum 2 -Maximum 5
            Start-Sleep -Seconds $delay
        }

        $urlIndex++
    }
}

# 处理命令行参数
$params = @{}
$remainingArgs = $args

for ($i = 0; $i -lt $remainingArgs.Count; $i++) {
    switch -regex ($remainingArgs[$i]) {
        '--urls' {
            $urls = @()
            $i++
            while ($i -lt $remainingArgs.Count -and $remainingArgs[$i] -notlike '--*') {
                $urls += $remainingArgs[$i]
                $i++
            }
            $i--
            $params.Urls = $urls
        }
        '--file' {
            $i++
            $params.File = $remainingArgs[$i]
        }
        '--output' {
            $i++
            $params.Output = $remainingArgs[$i]
        }
        '--quiet' {
            $params.Quiet = $true
        }
        '--help' {
            Write-Host "从Google学术链接中提取论文信息"
            Write-Host "用法:"
            Write-Host "  .\GetPaperInfo.ps1 [--urls url1 url2 ...] [--file urlFile] [--output outputFile] [--quiet]"
            Write-Host "参数:"
            Write-Host "  --urls     Google学术论文链接列表"
            Write-Host "  --file     包含Google学术论文链接的文件，每行一个链接"
            Write-Host "  --output   输出的Markdown文件名（默认使用论文标题）"
            Write-Host "  --quiet    安静模式，不打印详细信息到控制台"
            exit 0
        }
    }
}

# 运行主函数
Main @params 