# Parking Space Counter - Computer Vision Project

A real-time parking space detection system using OpenCV that analyzes video footage to determine which parking spots are occupied or free.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Files Description](#files-description)
- [Technical Details](#technical-details)
- [Requirements](#requirements)
- [Future Enhancements](#future-enhancements)

## 🎯 Overview

This project implements an intelligent parking space monitoring system that:

- Processes video footage of a parking lot
- Automatically detects occupied vs. free parking spaces
- Provides real-time visual feedback with colored rectangles
- Displays a live count of available parking spots

## ✨ Features

- **Real-time Detection**: Processes video frames in real-time
- **Visual Indicators**:
  - Green rectangles for free spaces
  - Red rectangles for occupied spaces
- **Live Counter**: Displays current free spots count
- **Interactive Setup**: Manual parking space selection tool
- **Persistent Storage**: Saves parking space coordinates for reuse
- **Video Looping**: Automatically restarts video when it ends

## 📁 Project Structure

```
2_Space_Counter/
├── 1_draw_rectangle.py     # Basic rectangle drawing demo
├── 2_posfinder.py         # Interactive parking space selector
├── 3_main.py              # Main detection system
├── 4_Theory.ipynb         # Detailed explanations and theory
├── carparkpos             # Saved parking positions (pickle file)
├── carparkposnew          # Alternative parking positions file
├── Image_Video/
│   ├── image.png          # Reference parking lot image
│   └── video.mp4          # Video footage for analysis
└── README.md              # This file
```

## 🚀 Installation

1. **Clone or download the project**
2. **Install required dependencies**:
   ```bash
   pip install opencv-python numpy
   ```
3. **Ensure you have the video file**:
   - Place your parking lot video as `Image_Video/video.mp4`
   - Place a reference image as `Image_Video/image.png`

## 💻 Usage

### Step 1: Define Parking Spaces (First Time Setup)

```bash
python 2_posfinder.py
```

- **Left-click and drag**: Create parking space rectangles
- **Right-click**: Delete existing rectangles
- **Press '1'**: Save and exit

### Step 2: Run the Detection System

```bash
python 3_main.py
```

- The system will automatically load saved parking positions
- Watch real-time detection with colored indicators
- **Press '1'**: Exit the program

## 🔧 How It Works

### Image Processing Pipeline

1. **Grayscale Conversion**: Converts RGB to grayscale for easier processing
2. **Gaussian Blur**: Reduces noise with a 3x3 kernel
3. **Adaptive Thresholding**: Separates foreground/background using local pixel intensities
4. **Median Blur**: Removes salt-and-pepper noise
5. **Dilation**: Enhances object boundaries with morphological operations

### Detection Algorithm

1. **Region of Interest**: Crops each parking space area
2. **Pixel Counting**: Uses `cv2.countNonZero()` to count white pixels
3. **Threshold Decision**:
   - `< 900 white pixels` → Free space (Green)
   - `≥ 900 white pixels` → Occupied space (Red)
4. **Visual Feedback**: Draws colored rectangles and displays counts

## 📄 Files Description

### `1_draw_rectangle.py`

- Basic OpenCV demonstration
- Shows how to draw rectangles on images
- Foundation for understanding coordinate systems

### `2_posfinder.py`

- Interactive parking space selection tool
- Mouse-based rectangle drawing interface
- Saves coordinates using Python's pickle module
- Supports both addition and deletion of parking spaces

### `3_main.py`

- Main detection and analysis system
- Implements complete image processing pipeline
- Real-time video analysis with visual feedback
- Automatic video looping functionality

### `4_Theory.ipynb`

- Comprehensive explanations of concepts
- Step-by-step algorithm breakdown
- Theory behind image processing techniques
- Code documentation and examples

## ⚙️ Technical Details

### Key Parameters

- **Parking Space Dimensions**: 107 x 48 pixels
- **Detection Threshold**: 900 white pixels
- **Gaussian Blur Kernel**: 3x3 with sigma=1
- **Dilation Kernel**: 3x3, 1 iteration
- **Median Blur Kernel**: 5x5

### Color Coding

- **Green (100, 255, 100)**: Free parking space
- **Red (100, 100, 255)**: Occupied parking space
- **Magenta (255, 0, 255)**: Information display background

### Performance Considerations

- Processes video at original frame rate
- Lightweight algorithms for real-time performance
- Efficient pixel counting with OpenCV optimizations

## 📋 Requirements

- Python 3.6+
- OpenCV (cv2) 4.x
- NumPy 1.19+
- Pickle (built-in Python module)

## 🔮 Future Enhancements

- [ ] **Deep Learning Integration**: Use YOLO/SSD for better vehicle detection
- [ ] **Multiple Camera Support**: Handle multiple parking lot views
- [ ] **Database Integration**: Store historical parking data
- [ ] **Web Interface**: Real-time web dashboard
- [ ] **Mobile App**: Smartphone notifications for available spaces
- [ ] **Advanced Analytics**: Peak hours analysis, occupancy patterns
- [ ] **Weather Adaptation**: Adjust thresholds based on lighting conditions
- [ ] **License Plate Recognition**: Track specific vehicles
