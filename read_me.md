# Dataset Maker

I made this project while learning OpenCV because I got tired of manually creating folders and saving webcam images whenever I wanted to train an image classification model.

This script lets you create datasets for multiple classes using your webcam. It automatically creates folders, crops the selected region, and saves the images after a short countdown.

## Features

- Supports multiple classes
- Saves grayscale or color images
- Countdown before capture
- Random filenames
- Live image counter
- ROI cropping

## How to run

Install OpenCV:

```bash
pip install opencv-python
```

Run:

```bash
python dataset_maker.py
```

Follow the prompts in the terminal.

### Controls

- **Z** → Start the countdown and capture an image
- **Q** → Finish capturing images for the current class

## Why I made this

I built this to speed up creating datasets for my computer vision projects, especially hand gesture recognition. Instead of manually taking pictures and organizing them into folders, the program does it automatically by storing the pics taking through webcam in a seperate sub directory .