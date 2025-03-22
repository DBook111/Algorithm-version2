import numpy as np
import cv2

def apply_palette(label, palette):
    color_label = np.zeros((label.shape[0], label.shape[1], 4), dtype=np.uint8)  # 4 channels for RGBA
    for i in range(len(palette)):
        color_label[label == i, :3] = palette[i]  # Set RGB channels
        color_label[label == i, 3] = 255  # Set alpha channel to 255 (opaque)
    # Set the alpha channel to 0 for [0, 0, 0] parts
    color_label[(label == 0), 3] = 0
    return color_label

def overlay_images(image, color_label, alpha=0.6):
    # Ensure the input image has 4 channels (RGBA)
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
    # Blend the images
    overlay = cv2.addWeighted(image, 1 - alpha, color_label, alpha, 0)
    
    # Set the alpha channel to 0 where the color_label is transparent
    overlay[color_label[:, :, 3] == 0, 3] = 0

    transparent_mask = overlay[:, :, 3] == 0
    overlay[transparent_mask] = image[transparent_mask]
    
    return overlay

# Example usage
if __name__ == "__main__":
    # Load the single-channel medical image and label image
    image = cv2.imread(r'C:\Yan3\Algorithm-version2\Painting\DukeDME\image.png', cv2.IMREAD_GRAYSCALE)
    label = cv2.imread(r'C:\Yan3\Algorithm-version2\Painting\DukeDME\new_label.png', cv2.IMREAD_GRAYSCALE)
    
    # Define a custom palette (example with 3 classes)
    palette = np.array([
                        [0, 0, 0],
                        [255, 153, 204],
                        [153, 204, 255],
                        [204, 204, 51], # 浅蓝
                        [193, 182, 255], # 浅粉
                        [0, 204, 153],  # 深绿                                              
                        [0, 204, 255],  # 浅黄                                           
                        [0, 102, 255],   # 橘色
                        [255, 102, 51], # 深蓝
                        [255, 204, 0],   # 中蓝                     
                        [152, 102, 102], # 灰色
                        [0, 153, 155], # 绿色                      
                        ], 
                        dtype=np.uint8)
    
    # Apply the palette to the label image
    color_label = apply_palette(label, palette)
    
    # Convert the original image to 3 channels
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    
    # Overlay the color label image on the original image
    weighted_image = overlay_images(image_color, color_label, alpha=0.7)
    
    # Save the result
    cv2.imwrite(r'C:\Yan3\Algorithm-version2\Painting\DukeDME\weight.png', weighted_image)