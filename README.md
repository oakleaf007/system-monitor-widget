# 🖥️ System Monitor

A lightweight **system monitoring tool** built using **Python** and **Tkinter**.  
It provides real-time statistics for CPU, RAM, and GPU (NVIDIA only) in a simple, draggable widget interface.

---

## ✨ Features
- **CPU Usage** – Live CPU usage percentage.  
- **RAM Usage** – Total memory and current usage percentage.  
- **GPU Usage (NVIDIA only)** – GPU load percentage and VRAM usage.  
- **Widgets** – Separate draggable CPU and GPU widgets (right-click to close).  
- **Simple UI** – Minimal design with low resource usage.  

---

## 🛠️ Built With
- [Python 3](https://www.python.org/)  
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – GUI framework  
- [psutil](https://pypi.org/project/psutil/) – For CPU and RAM stats  
- [GPUtil](https://pypi.org/project/GPUtil/) – For GPU stats  
- [WMI](https://pypi.org/project/WMI/) – For Windows hardware info  

---

## 📥 Download
Download the latest `.exe` release from the **[Releases](../../releases)** section.  
No Python installation required — just run the `.exe`.  

---

## ⚠️ Notes
- GPU monitoring works only with **NVIDIA GPUs** (via `nvidia-smi`).  
- On systems without NVIDIA GPUs, GPU usage will show as **N/A**.  
- Antivirus software may flag unsigned `.exe` files — this is a false positive.  

---

## 📸 Screenshot
*(Optional: Add a screenshot of your app here)*  

---

## 📜 License
This project is open source and free to use.  
