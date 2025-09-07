# 👁️ Face Detection with Arduino Control

This project combines **Computer Vision** (via OpenCV & MediaPipe) with **Arduino hardware control** (via PyFirmata).  
It detects faces in real-time from images, video, or webcam and triggers LEDs + buzzer based on detection results.

---

## 🚀 Features
- Face detection using **MediaPipe**.
- Supports **image**, **video**, and **real-time webcam** modes.
- Arduino control via **PyFirmata**:
  - LED1, LED2, and Buzzer toggle based on face detection.
- Saves processed images and videos to the `output/` directory.

---

## 🛠️ Requirements
Make sure you have the following installed:

- Python 3.8+
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://developers.google.com/mediapipe)
- [PyFirmata](https://pypi.org/project/pyFirmata/)
- Arduino with **StandardFirmata** uploaded

Install dependencies:
```bash
pip install -r requirements.txt
```

## ⚡ Hardware Setup

- **LED1** → Pin **3**  
- **LED2** → Pin **7**  
- **Buzzer** → Pin **11**  
- **Common GND** shared with Arduino  

> **Note:** Upload the `StandardFirmata.ino` sketch (included in the repo) to your Arduino using the Arduino IDE.

## 📂 Project Structure

- ├── controler.py # Arduino control functions (LEDs, buzzer)
- ├── face_detection.py # Face detection + processing logic
- ├── StandardFirmata.ino # Arduino sketch for Firmata
- ├── README.md # Project documentation
- ├── LICENSE # License file
- ├── .gitignore # Git ignore file


---

## ▶️ Usage

Run the project in different modes:

### 1️⃣ Image Mode
```bash
python face_detection.py --mode image --filepath path/to/image.jpg
```


# 👨‍💻 Author

- **Ahmed Gwely**  
- Passionate about Computer Vision, Embedded Systems, and AI-driven IoT.  
- 🌐 [LinkedIn Profile](https://www.linkedin.com/in/ahmed-gwely-2589611b0/)  
