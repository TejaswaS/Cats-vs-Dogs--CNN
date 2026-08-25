import numpy as np
import os
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt


print("\n🔍 Loding AI model...")
time.sleep(1)

#load model
model = load_model("outputs/model/cat_dog_model.h5")

print("✅ Model Loaded!\n")

#Folder containing test images
folder_path = "C:/Users/TEJASWA SHARMA/OneDrive/Desktop/Projects/CatsVsDogs-CNN/test_images"
print("🖼️ Scanning images...\n")

for img_name in os.listdir(folder_path):
    img_path = os.path.join(folder_path,img_name)

    #skip non-images files
    if not img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    #load image
    img = image.load_img(img_path, target_size = (150,150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis = 0)

    #Predict
    prediction = model.predict(img_array)
    confidence = prediction[0][0]

    #output 
    print(f"📁 {img_name}")

    if confidence > 0.5: 
        label = f"🐶 Dog (confidence: {confidence:.2f})\n"

    else:
        label = f"🐱 Cat (Confidence: {1- confidence:.2f})\n"

    #show image
    plt.imshow(image.load_img(img_path))
    plt.title(label)
    plt.axis('off')
    plt.show()


print("🎉 All predictions completed!")