# 🏭 SteelScan AI – Surface Defect Detection in Steel Using Deep Learning

[![MIT License](https://img.shields.io/github/license/Jatin-GI/SteelVision?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Jatin-GI/SteelVision?style=social)](https://github.com/Jatin-GI/SteelVision/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Jatin-GI/SteelVision?style=flat-square)](https://github.com/Jatin-GI/SteelVision/commits/main)
[![Streamlit App](https://img.shields.io/badge/🚀%20Open%20App-SteelScan%20AI-brightgreen?style=flat-square&logo=streamlit)](https://steelvision.streamlit.app)


---

**SteelScan AI** is an AI-powered computer vision system designed to detect and classify surface defects in steel products with high precision. Leveraging **transfer learning** and the power of **ResNet101V2**, the model identifies visual imperfections that are often difficult for the human eye to catch during manufacturing quality checks.

🔗 **Live Demo**: [steelvision.streamlit.app](https://steelvision.streamlit.app)

---

## 🧠 What It Does

SteelScan AI uses **deep convolutional neural networks (CNNs)** to analyze high-resolution steel surface images. The model is trained to classify each image into:
- ✅ **Non-Defective** (clean surface)
- ❌ **Defective** (surface cracks, dents, holes, scratches, etc.)

By applying **transfer learning** on **ResNet101V2 (ImageNet pre-trained)**, SteelScan AI drastically reduces training time while achieving high accuracy on industrial defect data.

---

## 🔬 Key Features

- 🔍 Detects micro-level surface defects from steel images
- 🧠 Transfer learning with **ResNet101V2**
- 📉 Real-time inference via **Streamlit Web App**
- 📷 Image preprocessing: histogram equalization, resizing
- 💾 Trained on labeled steel surface image datasets

---

## 🛠️ Tech Stack

| Tool/Library     | Purpose                                |
|------------------|-----------------------------------------|
| Python           | Programming language                    |
| TensorFlow/Keras | Deep learning & transfer learning       |
| ResNet101V2      | Pre-trained CNN for feature extraction  |
| OpenCV           | Image preprocessing                     |
| Streamlit        | Web app frontend                        |
| Matplotlib       | Image visualization (optional)          |

---

## 💻 How to Run Locally

```bash
git clone https://github.com/Jatin-GI/SteelScan-AI.git
cd SteelScan-AI

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📄 License

[![MIT License](https://img.shields.io/github/license/Jatin-GI/SteelScan-AI?style=flat-square)](LICENSE)

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Author

**Developed by [Jatin Gupta](https://github.com/Jatin-GI)**  
[![Email](https://img.shields.io/badge/Email-guptajatin0416%40gmail.com-red?style=flat-square&logo=gmail)](mailto:guptajatin0416@gmail.com)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Jatin%20Gupta-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/jatin-gupta-b02b37292)

---

## 🌐 Live Demo

[![Streamlit](https://img.shields.io/badge/🚀%20Live%20App-SteelScan%20AI-brightgreen?style=flat-square&logo=streamlit)](https://steelvision.streamlit.app)

---

## 🙌 Contributing

[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Jatin-GI/SteelScan-AI?style=flat-square)](https://github.com/Jatin-GI/SteelScan-AI/pulls)  
[![GitHub Issues](https://img.shields.io/github/issues/Jatin-GI/SteelScan-AI?style=flat-square)](https://github.com/Jatin-GI/SteelScan-AI/issues)

Contributions, suggestions, and improvements are always welcome!  
Feel free to open an issue or a pull request to collaborate.

---

## ⭐ Support

[![GitHub Stars](https://img.shields.io/github/stars/Jatin-GI/SteelScan-AI?style=social)](https://github.com/Jatin-GI/SteelScan-AI/stargazers)

If you found this project helpful or inspiring, please consider giving it a ⭐ on GitHub.  
It motivates me to keep improving and building more AI-based tools like this.

---

## 💬 Feedback

💬 Have ideas, feature requests, or just want to say hi?  
[![LinkedIn](https://img.shields.io/badge/Connect%20on%20LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/jatin-gupta-b02b37292)  
[![Email](https://img.shields.io/badge/Email-me-red?style=flat-square&logo=gmail)](mailto:guptajatin0416@gmail.com)

---

Thanks for checking out **SteelScan AI**!  
Let’s build smarter, safer, and more efficient industrial solutions together. 🚀
