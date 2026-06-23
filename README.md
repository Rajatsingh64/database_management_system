<div align="center">

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

---
# 🛠️ Technology Stack

| 🏷️ Layer | ⚡ Stack |
|----------|----------|
| 🐍 Backend | Python 3.11 • Flask • REST APIs |
| 🎨 Frontend | HTML5 • CSS3 • Responsive Design |
| 🗄️ Databases | MySQL • MongoDB • Cassandra |
| 🔧 Utilities | Pandas • Docker • CSV Processing |

# 🎮 Operations

<p align="center">
  <img src="https://img.shields.io/badge/Create-28a745?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Insert-007bff?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Update-f39c12?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Delete-dc3545?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Fetch-6f42c1?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Bulk_Upload-20c997?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/CSV_Export-ffc107?style=for-the-badge"/>
</p>

---
# 🗄️ Supported Databases

<div align="center">

<img src="https://img.shields.io/badge/🐬_MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
&nbsp;
<img src="https://img.shields.io/badge/🍃_MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
&nbsp;
<img src="https://img.shields.io/badge/👑_Cassandra-1287B1?style=for-the-badge&logo=apachecassandra&logoColor=white"/>

</div>

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
│   └──demo.gif
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
git clone https://github.com/Rajatsingh64/database_web_app.git

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
docker pull cassandra:4.1
```

Run Cassandra Container

```bash
docker run --name cassandra-db -p 9042:9042 -d cassandra:4.1
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



# 👨‍💻 Author

## Rajat Singh

<div align="center">

## ⭐ Star this repository if you found it useful!

🚀 Happy Coding 🚀

</div>
