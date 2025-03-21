# app/main.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wakeonlan import send_magic_packet
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devices.db"
app.config["SECRET_KEY"] = "your_secret_key"  # Replace with a secure key in production
db = SQLAlchemy(app)

# Importing Device model (you can also import from database.py)
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)
    mac_address = db.Column(db.String(17), nullable=False)

@app.route("/")
def index():
    devices = Device.query.all()
    return render_template("index.html", devices=devices)

@app.route("/add", methods=["POST"])
def add_device():
    name = request.form["name"]
    ip = request.form["ip"]
    mac = request.form["mac"]
    new_device = Device(name=name, ip_address=ip, mac_address=mac)
    db.session.add(new_device)
    db.session.commit()
    flash("Device added successfully!")
    return redirect(url_for("index"))

@app.route("/wake/<int:device_id>")
def wake(device_id):
    device = Device.query.get(device_id)
    if device:
        send_magic_packet(device.mac_address)
        flash(f"Sent WoL packet to {device.name}")
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=4040, debug=True)
