# Azania Network Security Scanner

Azania Network Security Scanner is a lightweight, user-friendly web app designed to scan open ports within a custom range on a given IP address or domain.

## 🚀 Features

- Clean UI optimized for non-technical users
- Input target IP or domain and port range
- Displays open ports in real-time
- Brand-ready for African markets
- Easily embeddable into client-facing networks (e.g. homes using Vuma WiFi)

## 🧪 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend (optional):** Flask / FastAPI (for hosting Python scanning logic)
- **Deployment:** GitHub + Render (free tier)

## 🖥 How To Use

1. Enter the target IP or domain (e.g. `192.168.1.1` or `example.com`)
2. Enter port range (e.g. `20` to `1024`)
3. Click **Scan**
4. View results below

## 📦 Installation (Dev)

```bash
git clone https://github.com/Thami-code305/home-port-scanner2.git
cd home-port-scanner2
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py

