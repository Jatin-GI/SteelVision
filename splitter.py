import os
import random
import shutil

# Input and output paths
input_root = "dataset"        # Contains "damaged/" and "intact/"
output_root = "train_test_val"

# Split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Class names (folders)
classes = ["def_front", "ok_front"]

for class_name in classes:
    class_dir = os.path.join(input_root, class_name)
    images = [f for f in os.listdir(class_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    random.shuffle(images)

    total = len(images)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    train_imgs = images[:train_end]
    val_imgs = images[train_end:val_end]
    test_imgs = images[val_end:]

    # Copy files into the appropriate folders
    for split, split_imgs in [("train", train_imgs), ("val", val_imgs), ("test", test_imgs)]:
        split_dir = os.path.join(output_root, split, class_name)
        os.makedirs(split_dir, exist_ok=True)
        for img in split_imgs:
            src = os.path.join(class_dir, img)
            dst = os.path.join(split_dir, img)
            shutil.copy(src, dst)

print("✅ Dataset split complete! Folder structure ready for Keras or PyTorch.")
