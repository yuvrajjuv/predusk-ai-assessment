🚀 YOLOv8 Object Detection & Tracking

A real-time multi-object detection and tracking system built using YOLOv8 and deployed with a Streamlit web app.

---

🌐 Live Demo

👉 https://yolo-tracking-app.streamlit.app/

---

📂 GitHub Repository

👉 https://github.com/yuvrajjuv/predusk-ai-assessment

---

🎯 Project Overview

This project implements real-time object detection and tracking using YOLOv8.
Users can upload a video, and the system processes it to detect and track multiple objects (like people, balls, etc.) with bounding boxes and IDs.

---

✨ Features

- 🎯 YOLOv8-based object detection
- 🔄 Multi-object tracking using "persist=True"
- 📹 Upload video for processing
- 🧠 Real-time inference with bounding boxes
- 🌐 Streamlit web interface
- 💾 Processed video output generation

---

🛠️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Streamlit
- NumPy

---

⚙️ Installation (Local Setup)

git clone https://github.com/yuvrajjuv/predusk-ai-assessment
cd predusk-ai-assessment

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

---

▶️ Run Locally

streamlit run app.py

---

📁 Project Structure

predusk-ai-assessment/
│
├── data/                # Input video
├── outputs/             # Processed video output
├── notebooks/           # Jupyter notebook (development)
├── app.py               # Streamlit app
├── requirements.txt     # Dependencies
└── README.md

---

📸 Sample Output

- Detects multiple objects (e.g., persons, sports ball)
- Assigns tracking IDs
- Displays bounding boxes on video frames

---

🚀 Deployment

The app is deployed using Streamlit Cloud.

---

👨‍💻 Author

Yuvraj Malviya
GitHub: https://github.com/yuvrajjuv

---

⭐ If you like this project

Give it a star ⭐ on GitHub!
