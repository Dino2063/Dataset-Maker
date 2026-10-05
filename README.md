# 📸 Webcam Dataset Maker

A simple Python program for creating custom image datasets using a webcam.

The program allows you to create multiple classes, choose an image format and image type, and capture images directly into separate directories for each class.

## ✨ Features

* 📷 Capture images using a webcam
* 🗂️ Create datasets with multiple classes
* 📁 Automatically create directories for each class
* 🎨 Save images in:

  * Grayscale
  * BGR
* 🖼️ Support multiple image formats:

  * JPG
  * JPEG
  * PNG
  * WEBP
* 🔢 Capture 20 frames per capture
* 🔤 Generate random filenames for captured images
* 🟩 Display a capture region on the webcam feed
* 📊 Display the number of images captured
* 🔄 Capture multiple batches for each class

## 🛠️ Requirements

Make sure Python is installed, then install OpenCV:

```bash
pip install opencv-python
```

The following modules are part of Python's standard library and require no additional installation:

* `pathlib`
* `time`
* `random`
* `string`

## 🚀 Usage

Run the Python script:

```bash
python dataset_maker.py
```

The program will ask you for:

* Number of classes
* Image format
* Image type (Grayscale or BGR)
* Name of each class

A directory named `Webcam_recog` will automatically be created to store the dataset.

## 🎮 Controls

| Key | Action                       |
| --- | ---------------------------- |
| `Z` | Capture a batch of 20 frames |
| `Q` | Finish the current class     |

Make sure the webcam window is focused before using the keyboard controls.

## 📂 Dataset Structure

The generated dataset will look similar to:

```text
Webcam_recog/
│
├── class1/
│   ├── abcde.jpg
│   ├── fghij.jpg
│   └── ...
│
├── class2/
│   ├── klmno.jpg
│   ├── pqrst.jpg
│   └── ...
│
└── class3/
    ├── uvwxy.jpg
    └── ...
```

Each class has its own directory, making the dataset easy to use for machine learning and computer vision projects.

## 🖼️ Capture Region

The program captures only the area inside the rectangle displayed on the webcam feed.

The current capture coordinates are:

```python
p1 = (170, 90)
p2 = (470, 390)
```

With a webcam resolution of `640 × 480`, this creates a `300 × 300` pixel capture region.

## 🧠 Use Cases

This project can be useful for creating custom datasets for:

* Image classification
* Computer vision experiments
* Machine learning projects
* Gesture recognition
* Object recognition
* Custom image-based models

## 🧰 Built With

* **Python**
* **OpenCV**
* **Pathlib**

---

A lightweight tool for quickly creating organized webcam datasets for computer vision projects. 📸
