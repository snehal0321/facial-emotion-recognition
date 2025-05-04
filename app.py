import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
import cv2

# Load your trained model
model = tf.keras.models.load_model('emotion_cnn_model2.h5')

# Define emotion labels (same order as your training)
emotion_labels = {
    0: 'Angry 😠',
    1: 'Disgust 🤢',
    2: 'Fear 😨',
    3: 'Happy 😄',
    4: 'Sad 😢',
    5: 'Surprise 😲',
    6: 'Neutral 😐'
}

# Streamlit UI
st.title("Facial Emotion Recognition")
st.write("Upload an image and the model will predict the emotion!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    image2 = Image.open(uploaded_file)
    
    
    # Preprocess the image
    image = ImageOps.fit(image, (48, 48), method=Image.LANCZOS) # Resize to 48x48
    img_array = np.array(image)
    img_array = img_array.reshape(1, 48, 48, 1) / 255.0  # Normalize

    # Predict
    pred = model.predict(img_array)
    predicted_class = np.argmax(pred)
    predicted_emotion = emotion_labels[predicted_class]
    confidence = pred[0][predicted_class] * 100
    col1, col2 = st.columns(2)

    with col1:
      st.image(image2, caption='Uploaded Image', width=300)

    with col2:
      st.success(f"**Predicted Emotion:** {predicted_emotion}")
      st.info(f"Confidence: {confidence:.2f}")
      
    
