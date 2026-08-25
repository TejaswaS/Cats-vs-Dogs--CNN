import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#Define paths
BASE_DIR = "C:/Users/TEJASWA SHARMA/OneDrive/Desktop/Projects/CatsVsDogs-CNN"

TRAIN_DIR = BASE_DIR + "/dataset/train"
VAL_DIR = BASE_DIR +"/dataset/validation"

#Image Preprocessing 
train_datagen = ImageDataGenerator(
    rescale = 1./255,
    rotation_range = 20,
    zoom_range = 0.2,
    horizontal_flip = True
)

val_datagen = ImageDataGenerator(rescale = 1./255)

#Load images
train_data = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size = (150,150),
    batch_size = 32,
    class_mode = 'binary'
)

val_data = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size = (150,150),
    batch_size = 32,
    class_mode = 'binary'
)
print(train_data.class_indices)


#Build CNN Model(the BRAIN)
from  tensorflow.keras import layers, models

model = models.Sequential([

    #1st conv block
    layers.Conv2D(32, (3,3), activation='relu', input_shape = (150,150,3)),
    layers.MaxPooling2D(2,2),

    #2nd Conv block
    layers.Conv2D(64, (3,3), activation= 'relu'),
    layers.MaxPooling2D(2,2),

    #3rd Conv block
    layers.Conv2D(128, (3,3), activation= 'relu'),
    layers.MaxPooling2D(2,2),

    #Flatten 
    layers.Flatten(),

    #Dense layers
    layers.Dense(128, activation= 'relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation= 'sigmoid') #binary output

])


#Compile Model
model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

#Print Model Summary
model.summary()

#train the model timing
history = model.fit(
    train_data,
    epochs = 10,
    validation_data = val_data,
    verbose = 1
)

print("✅ Training finished")
#Save model
import os
os.makedirs("C:/Users/TEJASWA SHARMA/OneDrive/Desktop/Projects/CatsVsDogs-CNN/outputs/model", exist_ok=True)
print("💾 Saving model...")
model.save("C:/Users/TEJASWA SHARMA/OneDrive/Desktop/Projects/CatsVsDogs-CNN/outputs/model/cat_dog_model.h5")
print("✅ Model saved!")

#Plot the results
import matplotlib.pyplot as plt

print("📊 Plotting...")
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
os.makedirs("C:/Users/TEJASWA SHARMA/OneDrive/Desktop/Projects/CatsVsDogs-CNN/outputs/plots", exist_ok=True)
plt.plot(acc, label = 'TRAIN ACCURACY')
plt.plot(val_acc, label = 'VALIDATION ACCURACY')
plt.legend()
plt.savefig("C:/Users/TEJASWA SHARMA/OneDrive/Desktop/Projects/CatsVsDogs-CNN/outputs/plots/accuracy_plot.png")
print("✅ Plot saved!")
plt.show()




