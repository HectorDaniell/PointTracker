# Scuba Cat & Friends - Hand Tracking Animation 🐱🦊

A computer vision project that uses **MediaPipe** and **OpenCV** to track hand movements and trigger dancing GIFs. Featuring the classic Scuba Cat and Nick Wilde from Zootopia.

## Features
- **Dual Hand Tracking:** Independent movement detection for two simultaneous hands.
- **Smart Windows:** Windows automatically open when movement is detected and close after 0.5s of inactivity.
- **Optimized Rendering:** GIF frames are pre-processed to eliminate ghosting and background artifacts.
- **Performance Focused:** Scaled and cached frames to ensure a smooth experience even with high-resolution GIFs.

## Tech Stack
- **Python 3.11** (Required for MediaPipe stability on Windows)
- **MediaPipe 0.10.11** (Hand Tracking)
- **OpenCV** (Camera and Window management)
- **Pillow** (GIF processing)

## Prerequisites
Due to specific library dependencies (especially MediaPipe), it is highly recommended to use **Python 3.11**. Newer versions (like 3.13) may encounter compatibility issues with binary extensions.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SCUBA_CAT.git](https://github.com/YOUR_USERNAME/SCUBA_CAT.git)
   cd SCUBA_CAT