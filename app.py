import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np

# Load your trained model
model = load_model("resnet_faulty_detector_v1.h5")

# Streamlit app title
st.title("🧠 Steel Defect Classifier")
st.markdown("Upload an image to detect whether it's **Defect** or **No Defect**.")

# Upload file
uploaded_file = st.file_uploader("Choose a steel surface image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    img = img.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)
    confidence = prediction[0][0]

    # Display result
    if confidence > 0.5:
        st.success(f"✅ No Defect Detected")
        st.info(f"Confidence: {confidence * 100:.2f}%")
    else:
        st.error(f"⚠️ Defect Detected")
        st.info(f"Confidence: {(1 - confidence) * 100:.2f}%")
