# 💡 LANtern – Wake-on-LAN Web App

LANtern is a lightweight web application that lets you power on computers and other devices in your local network using Wake-on-LAN magic packets. It provides a simple, browser-based interface to store device info (IP + MAC) and wake them with a single click.

You can run LANtern:

✅ Without Docker — directly on any system with Python 3 (Linux or Windows)
🐳 With Docker — isolated and easy to deploy using Docker & Docker Compose
Whether you prefer running it as a local Python app or inside a container, LANtern gives you flexible deployment options.

---

## 🚀 Features

- 🌐 Web-based interface – access from any device in your LAN
- 💾 Save multiple devices (name, IP, MAC address)
- 🔘 Wake any device with a single click
- 🗑️ Delete devices with a confirmation popup (poka-yoke safety)
- 🧠 Auto-start on boot using `systemd` on Linux
- 📦 Run with Docker or runs directly on your PC

---

## 🛠️ Requirements

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Wakeonlan (Python module)
- Linux (Ubuntu recommended) or Windows

---

## 🧰 Installation (Linux) ** NO DOCKER ** 

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

---
## Running LANtern **WITH Docker**
---
### Make sure you have:
```
sudo apt update
sudo apt install docker.io docker-compose -y
```
### Enable and start Docker:
```
sudo systemctl enable docker
sudo systemctl start docker
```
### 1. Clone the project and navigate into it
```
cd ~/Documents
git clone https://github.com/presttige/lantern.git
cd lantern
docker-compose up --build -d
```
2. Access the app
On the host machine:
```http://localhost:4040```

From another device on the LAN:
```http://<your-host-ip>:4040```

🧪 To View Logs
```docker-compose logs -f```

---
⚠️ Note on Docker and Magic Packet Limitations
While LANtern can be run via Docker, I personally chose to run it directly using Python on my host system.

This is because magic packets sent from inside a Docker container originate from a different internal IP address (e.g., 172.x.x.x), which is part of Docker’s internal network. In my setup, the target device’s Wake-on-LAN functionality only accepts magic packets from the same LAN subnet (e.g., 192.168.x.x), and ignores anything from outside that range — including Docker.

To ensure reliable device wakeups, I run main.py directly on my Ubuntu machine. This way, the packets are sent from my actual LAN IP, and the devices receive and respond to them correctly.

If your Wake-on-LAN devices require the packet to come from the same subnet, you may encounter the same issue — in which case, running LANtern natively (without Docker) is recommended.
---
---
🛠️ Advanced: Make Docker Send Packets from the Same LAN Subnet
If you still want to run LANtern in Docker, but need it to send packets from your LAN subnet, you can:

Use Docker’s advanced macvlan network mode
Assign your container a real IP from your LAN (like 192.168.1.250)
Allow it to broadcast magic packets just like any other device on your network
This requires more setup and might not be compatible with all network environments or routers — but it's a powerful option if you prefer containerized deployment.
---
