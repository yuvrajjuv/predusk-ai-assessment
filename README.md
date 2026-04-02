Multi-Object Detection & Tracking (YOLOv8)

📌 Overview

This project implements multi-object detection and tracking using YOLOv8 on a sports video.

🚀 Approach

- Used YOLOv8 (Ultralytics) for object detection
- Used built-in tracking ("model.track") for persistent IDs
- Processed video frame-by-frame using OpenCV
- Saved annotated output video with bounding boxes and IDs

🛠️ Setup Instructions

pip install ultralytics opencv-python

▶️ How to Run

- Place video in "data/"
- Run notebook: "ai_assessment.ipynb"

📁 Output

- Output video saved in: "outputs/output.mp4"

⚠️ Assumptions

- Public sports video used
- Objects include players and ball

❌ Limitations

- ID switching may occur in occlusion
- Small objects detection not always accurate

🤖 Model Used

- YOLOv8n (lightweight model)