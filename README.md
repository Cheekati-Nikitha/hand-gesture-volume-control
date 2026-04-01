# 🖐️ Hand Gesture-Based Volume Control System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A real-time computer vision project that allows users to control system volume using hand gestures by detecting the distance between the thumb and index finger.

---

## 📖 Project Overview

This project provides a **touchless and intuitive way to control system volume** using a webcam. It tracks hand landmarks and converts finger movements into volume commands in real time.

---

## 🎥 Demo

![Demo](demo.gif)

---

## 🛠️ Tech Stack

- Python  
- OpenCV  
- MediaPipe  
- PyAutoGUI  

---

## ✨ Features

- Real-time hand gesture detection  
- Touchless volume control  
- Lightweight and fast  
- Works with standard webcams  

---

## ⚙️ How It Works

Webcam → Hand Detection → Landmark Extraction → Distance Calculation → Volume Control  

- Detects:
  - Thumb tip (ID 4)  
  - Index finger tip (ID 8)  
- Calculates distance between fingers  
- Controls volume based on distance  

---

## ⚡ Installation

### Install Dependencies
```bash
pip install opencv-python mediapipe pyautogui
