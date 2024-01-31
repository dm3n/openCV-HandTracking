

---

# Hand Tracker

## Overview
Hand Tracker is a Python application that utilizes computer vision techniques to track hand movements in real-time. Leveraging the OpenCV library and cvzone's HandTrackingModule, this tool is capable of detecting and tracking multiple hands through a webcam feed.

## Features
- **Real-Time Hand Tracking**: Detects and tracks hand movements in real-time.
- **Multiple Hand Support**: Capable of tracking multiple hands simultaneously.
- **Customizable Detection Confidence**: Allows adjustment of hand detection confidence levels.

## Prerequisites
Before you can run Hand Tracker, ensure you have the following installed:
- Python 3.x
- OpenCV (`opencv-python`)
- cvzone

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/dm3n/openCV-HandTracking.git
   ```
2. Install the required libraries:
   ```
   pip install opencv-python
   pip install cvzone
   ```

## Usage
To start hand tracking, run the script from your command line:
```
python Handtracker.py
```
Make sure your webcam is connected and enabled for the application to work correctly.

## How It Works
Hand Tracker utilizes the webcam to capture video frames. The HandTrackingModule from cvzone processes these frames to detect and track hands. Coordinates and tracking details are displayed in real-time.

## Customization
You can adjust the detection confidence and other parameters in the script to suit your specific needs.
---
