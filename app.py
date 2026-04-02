import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO

st.title("YOLOv8 Object Detection & Tracking")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    st.video(tfile.name)

    if st.button("Run Detection"):
        model = YOLO("yolov8n.pt")

        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model.track(frame, persist=True)
            annotated_frame = results[0].plot()

            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            stframe.image(annotated_frame)

        cap.release()
        st.success("Processing Done!")