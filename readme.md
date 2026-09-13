"""# 🚨 Windows Intruder Catcher (Dual-Channel Failover)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Windows](https://img.shields.io/badge/Windows-Security-blue?style=for-the-badge&logo=windows)
![OpenCV](https://img.shields.io/badge/OpenCV-Camera-green?style=for-the-badge&logo=opencv)

A stealthy, OS-level security tool for Windows that automatically captures a photo of anyone trying to unlock your laptop with a wrong password. Built with a **dual-channel failover system** to bypass restricted hostel/corporate Wi-Fi networks.

## ✨ Features
* **OS-Level Integration**: Uses Windows Security Audit Policy (Event ID 4625) to detect failed login attempts instantly.
* **Stealth Capture**: Silently activates the webcam via OpenCV without any visible UI.
* **Dual-Channel Alerts**: 
  * Primary: Telegram Bot API (for fast, instant delivery).
  * Failover: SMTP Email (automatically triggers if Telegram is blocked by firewall/hostel Wi-Fi).
* **Self-Cleaning**: Deletes local photo traces immediately after sending the alert.

## 🛠️ Prerequisites
* Windows OS (10/11)
* Python 3.13+
* A Telegram Bot Token & Chat ID
* A Gmail App Password

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone "https://github.com/samit0714/Windows_Intruder_Catcher"
cd intruder-catcher