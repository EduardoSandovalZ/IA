import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt


train_df = pd.read_csv("/home/eduardo/Documents/IA/practica8/Results/train.csv")

labels = train_df['label'].values
features = train_df.iloc[:, 1:].values / 255

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=(784,), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(features, labels, epochs=10, validation_split=0.1)

test_df = pd.read_csv("/home/eduardo/Documents/IA/practica8/Results/test.csv")
test_features = test_df.values / 255

test_preds = model.predict(test_features)
test_preds = np.argmax(test_preds, axis=1)

new_img = test_df.iloc[149, :].values.reshape(28, 28)

new_img = new_img.reshape(1, 784) / 255
'''
for i in range(len(test_df)):
    img = test_df.iloc[i].values.reshape(28, 28)
    filename = f"imagen_{i}.png"
    plt.imsave(f"/home/eduardo/Documents/IA/practica8/Results/imagenes/{filename}", img, cmap='gray')
'''




new_pred = model.predict(new_img)
new_pred = np.argmax(new_pred, axis=1)[0]

new_img = new_img.reshape(28, 28)
#plt.imsave('/home/eduardo/Documents/IA/practica8/Results/imagenes/test2.png', new_img, cmap='gray')
print("La predicción del modelo es:", new_pred)
print("La imagen es:")
plt.imshow(new_img, cmap="gray")
plt.show()
