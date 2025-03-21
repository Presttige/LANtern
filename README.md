# LANtern
Wake on lan from web interface

# 💡 LANtern – Wake-on-LAN Web App

**LANtern** is a lightweight, user-friendly web application that allows you to power on computers or devices in your local network using **Wake-on-LAN (WoL)** magic packets. Built with Flask (Python) and SQLite, it gives you a simple interface to store device info and trigger wakeups from any browser on your network.

---

## 🚀 Features

- 🌐 Web-based interface – access from any device in your LAN
- 💾 Save multiple devices (name, IP, MAC address)
- 🔘 Wake any device with a single click
- 🗑️ Delete devices with a confirmation popup (poka-yoke safety)
- 🧠 Auto-start on boot using `systemd` on Linux
- 📦 No Docker needed – runs directly on your PC

---

## 📷 Screenshot

> *(Add your screenshot here when ready)*

---

## 🛠️ Requirements

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Wakeonlan (Python module)
- Linux (Ubuntu recommended) or Windows

---

## 🧰 Installation (Linux)

### 1. Install Python & required packages

sudo apt update
sudo apt install python3 python3-venv python3-pip


### 2. Clone the project and set it up

git clone https://github.com/presttige/LANtern.git
cd LANtern
python3 -m venv venv
source venv/bin/activate
pip install flask flask_sqlalchemy wakeonlan

### 3. Run the app

python app/main.py

### 4. Access the interface

On the host machine: http://localhost:4040
From another device in the network: http://<your-pc-ip>:4040


Optional: Run it in the Background (Forever)
sudo apt install tmux
tmux
source venv/bin/activate
python app/main.py

