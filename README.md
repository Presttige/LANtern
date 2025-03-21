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

### 1. Clone the project and navigate into it

```
cd ~/Documents
git clone https://github.com/yourusername/lantern.git
cd lantern
```
### 2. Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```
pip install flask flask_sqlalchemy wakeonlan
```
### 4. Start the application
```
python app/main.py
```
Then open your browser and go to: ```http://localhost:4040``` Or from another device on your LAN: ```http://<your-host-ip>:4040```

### Optional: Run it in the Background (Forever)
```
sudo apt install tmux
tmux
source venv/bin/activate
python app/main.py
```
Then press Ctrl+B, then D to detach.

