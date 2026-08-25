import os
import shutil
import random

# ✅ Correct path (use forward slashes)
BASE_DIR = "C:/Users/TEJASWA SHARMA/OneDrive/Desktop/Projects/CatsVsDogs-CNN"

SOURCE_DIR = BASE_DIR + "/original_dataset/train"
TRAIN_DIR = BASE_DIR + "/dataset/train"
VAL_DIR = BASE_DIR + "/dataset/validation"
# Create folders
for category in ['cats', 'dogs']:
    os.makedirs(os.path.join(TRAIN_DIR, category), exist_ok=True)
    os.makedirs(os.path.join(VAL_DIR, category), exist_ok=True)

# Get files
files = os.listdir(SOURCE_DIR)

# Separate
cats = [f for f in files if f.lower().startswith('cat')]
dogs = [f for f in files if f.lower().startswith('dog')]

print(f"Total Cats: {len(cats)}")
print(f"Total Dogs: {len(dogs)}")

# Shuffle
random.shuffle(cats)
random.shuffle(dogs)

# Split
split_ratio = 0.8

cat_split = int(len(cats) * split_ratio)
dog_split = int(len(dogs) * split_ratio)

train_cats = cats[:cat_split]
val_cats = cats[cat_split:]

train_dogs = dogs[:dog_split]
val_dogs = dogs[dog_split:]

# Copy function
def copy_files(file_list, src_folder, dst_folder):
    for file in file_list:
        shutil.copy(
            os.path.join(src_folder, file),
            os.path.join(dst_folder, file)
        )

# Copy data
copy_files(train_cats, SOURCE_DIR, os.path.join(TRAIN_DIR, 'cats'))
copy_files(val_cats, SOURCE_DIR, os.path.join(VAL_DIR, 'cats'))

copy_files(train_dogs, SOURCE_DIR, os.path.join(TRAIN_DIR, 'dogs'))
copy_files(val_dogs, SOURCE_DIR, os.path.join(VAL_DIR, 'dogs'))

print("✅ Dataset split completed!")