import os
import random
import shutil

# Define paths
train_image_dir = 'C:/Users/ASUS/Desktop/Python/u net implementation/data/train_images'  # Path to your train images
train_mask_dir = 'C:/Users/ASUS/Desktop/Python/u net implementation/data/train_masks'  # Path to your train masks
val_image_dir = 'C:/Users/ASUS/Desktop/Python/u net implementation/data/val_images'  # Path to your val images
val_mask_dir = 'C:/Users/ASUS/Desktop/Python/u net implementation/data/val_masks'  # Path to your val masks

# Create val directories if they don't exist
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_mask_dir, exist_ok=True)


# Get list of all image files in train directory
image_files = [f for f in os.listdir(train_image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Randomly select 50 images
random.seed(42)  # Set a seed for reproducibility
selected_images = random.sample(image_files, 50)

# Move selected images and corresponding masks to val directories
for image_name in selected_images:
    # Move image
    src_image_path = os.path.join(train_image_dir, image_name)
    dst_image_path = os.path.join(val_image_dir, image_name)
    shutil.move(src_image_path, dst_image_path)
    
    # Move corresponding mask
    mask_name = image_name.replace(".jpg","_mask.gif")  # Assuming mask filenames match image filenames
    src_mask_path = os.path.join(train_mask_dir, mask_name)
    dst_mask_path = os.path.join(val_mask_dir, mask_name)
    shutil.move(src_mask_path, dst_mask_path)

print(f"Moved {len(selected_images)} images and masks to validation set.")