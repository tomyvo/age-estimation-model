# 👵 Age Estimation with Deep Learning

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-red?logo=pytorch" />
  <img src="https://img.shields.io/badge/Gradio-Interface-orange?logo=gradio" />
  <img src="https://img.shields.io/badge/Computer%20Vision-blue?logo=opencv" />
</p>

## 🧠 Overview
This project demonstrates a **deep learning model** that predicts a person’s **age based on facial images**.  
The system uses a **convolutional neural network (CNN)** trained on face datasets and integrates with a **Gradio interface** for real-time predictions.

---

## 🚀 Features
- 🖼️ Upload one or multiple face images  
- 🔍 Automatic face detection & cropping (MTCNN)  
- 🎯 Predicts approximate **age** of the person  
- 📊 Displays results in both a **gallery** and a **data table**  
- 🌐 Simple, interactive **Gradio web app**

---

## 🧩 Tech Stack
| Component | Description |
|------------|-------------|
| **Python** | Main programming language |
| **PyTorch** | Model training and inference |
| **Gradio** | Interactive web UI |
| **MTCNN** | Face detection & cropping |
| **Pandas** | Data handling and result formatting |

---

## ⚙️ Installation
```bash
# Clone this repository
git clone https://github.com/tomyvo/age-estimation-model.git
cd age-estimation-model

# Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate  # (on Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt
