<div align="center">

# 🗄️ Database Management System

### 🚀 One Platform • Three Databases • Unlimited Possibilities

<img src="assets/demo.gif" width="100%" alt="Application Demo"/>

<br>

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
<img src="https://img.shields.io/badge/Cassandra-1287B1?style=for-the-badge&logo=apachecassandra&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>

<br><br>

A Modern Multi-Database Management Application built using Python 3.11 and Flask that allows users to perform database operations on MySQL, MongoDB, and Cassandra through a single beautiful interface.

</div>

---

# 🎯 Project Overview

Managing multiple databases often requires different tools and interfaces.

This application provides a unified web interface where users can:

✅ Create Tables / Collections

✅ Insert Data

✅ Update Records

✅ Delete Records

✅ Fetch Records

✅ Upload CSV Files

✅ Download Data

✅ Manage Multiple Databases

All from one responsive and modern web application.

---

# 🎥 Application Demo

> Replace with your application GIF

```text
assets/demo.gif
```

<img src="assets/demo.gif" alt="Demo"/>

---

# 🛠️ Technology Stack

<div align="center">

| Backend | Frontend | Databases | Utilities |
|----------|----------|------------|------------|
| Python 3.11 | HTML5 | MySQL | Pandas |
| Flask | CSS3 | MongoDB | Docker |
| REST APIs | Responsive UI | Cassandra | CSV Processing |

</div>

---

# 🎮 Supported Operations

<div align="center">

## 🟢 Create

<img src="https://img.shields.io/badge/CREATE-Supported-success?style=for-the-badge"/>

## 🔵 Insert

<img src="https://img.shields.io/badge/INSERT-Supported-blue?style=for-the-badge"/>

## 🟠 Update

<img src="https://img.shields.io/badge/UPDATE-Supported-orange?style=for-the-badge"/>

## 🔴 Delete

<img src="https://img.shields.io/badge/DELETE-Supported-red?style=for-the-badge"/>

## 🟣 Fetch

<img src="https://img.shields.io/badge/FETCH_DATA-Supported-purple?style=for-the-badge"/>

## 🟢 Bulk Upload

<img src="https://img.shields.io/badge/BULK_UPLOAD-Supported-brightgreen?style=for-the-badge"/>

## 🟡 CSV Download

<img src="https://img.shields.io/badge/CSV_EXPORT-Supported-yellow?style=for-the-badge"/>

</div>

---

# 🗄️ Supported Databases

<div align="center">

<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>

<br><br>

<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>

<br><br>

<img src="https://img.shields.io/badge/Cassandra-1287B1?style=for-the-badge&logo=apachecassandra&logoColor=white"/>

</div>

---

# 📸 Screenshots

## 🏠 Dashboard

<img src="assets/images/dashboard.png"/>

---

## 🐬 MySQL Operations

<img src="assets/images/mysql.png"/>

---

## 🍃 MongoDB Operations

<img src="assets/images/mongodb.png"/>

---

## 👑 Cassandra Operations

<img src="assets/images/cassandra.png"/>

---

## 📁 Bulk Upload

<img src="assets/images/bulk_upload.png"/>

---

## 📊 Results

<img src="assets/images/results.png"/>

---

# 🌟 Features

### 🐬 MySQL

- Create Tables
- Insert Records
- Update Records
- Delete Records
- Bulk CSV Upload
- CSV Export

---

### 🍃 MongoDB

- Create Collections
- Insert Documents
- Update Documents
- Delete Documents
- Bulk CSV Upload
- CSV Export

---

### 👑 Cassandra

- Create Keyspaces
- Create Tables
- Insert Records
- Update Records
- Delete Records
- Bulk CSV Upload
- Fetch Records
- CSV Export

---

# 🏗️ System Architecture

```text
                    👤 USER
                       │
                       ▼
         🎨 HTML + CSS Frontend
                       │
                       ▼
             ⚡ Flask Application
                   (app.py)
                       │
       ┌───────────────┼───────────────┐
       │               │               │
       ▼               ▼               ▼

   🐬 MySQL      🍃 MongoDB      👑 Cassandra
                                        │
                                        ▼
                                   🐳 Docker
```

---

# 📂 Project Structure

<details>

<summary>📁 Click to Expand</summary>

```text
database_web_app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   │
│   ├── demo.gif
│   │
│   └── images/
│       │
│       ├── dashboard.png
│       ├── mysql.png
│       ├── mongodb.png
│       ├── cassandra.png
│       ├── bulk_upload.png
│       └── results.png
│
└── templates/
    │
    └── index.html
```

</details>

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/database_web_app.git

cd database_web_app
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🐬 MySQL Setup

```text
Host : localhost
Port : 3306
```

Ensure MySQL Server is running.

---

# 🍃 MongoDB Setup

```text
mongodb://localhost:27017
```

Ensure MongoDB is running.

---

# 👑 Cassandra Setup (Docker)

Pull Cassandra Image

```bash
docker pull cassandra
```

Run Cassandra Container

```bash
docker run --name cassandra-db -p 9042:9042 -d cassandra
```

Check Container

```bash
docker ps
```

Wait a few minutes for Cassandra initialization.

---

# ▶️ Run Application

```bash
python app.py
```

Open Browser:

```text
http://127.0.0.1:5000
```

---

# 📈 Learning Outcomes

This project demonstrates:

✅ Flask Development

✅ Database Connectivity

✅ Multi Database Architecture

✅ REST API Design

✅ CSV Processing

✅ Docker Integration

✅ Frontend Development

✅ Backend Development

✅ Full Stack Development

---

# 🔮 Future Enhancements

🔐 Authentication System

🌙 Dark Mode

📊 Dashboard Analytics

📈 Query History

📄 Excel Export

☁️ Cloud Database Support

👥 Multi User Support

📉 Database Monitoring

---

# 👨‍💻 Author

## Rajat Singh

### Designed & Developed with ❤️

Python • Flask • HTML • CSS • MySQL • MongoDB • Cassandra • Docker

---

<div align="center">

## ⭐ Star this repository if you found it useful!

🚀 Happy Coding 🚀

</div>