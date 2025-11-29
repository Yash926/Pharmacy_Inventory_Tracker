# 🏥 Pharmacy Inventory Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=flat&logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap_5-purple?style=flat&logo=bootstrap)

## 📖 Project Overview

The **Pharmacy Inventory System** is a full-stack web application designed to streamline the tracking of medical supplies in a healthcare setting. It addresses the challenge of manual stock management by providing a centralized digital interface for pharmacists to add, update, and monitor medicine levels in real-time.

This project was built to demonstrate core **Backend Engineering** competencies, including RESTful API development, database management, and data integrity validation.

---

## 📸 Project Screenshots

![Dashboard Preview](screenshot.png)
*Replace with your actual dashboard screenshot*

---

## 🛠️ Tech Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| **Backend** | Python & Flask | Lightweight server handling API requests and business logic |
| **Database** | SQLite3 | Relational database for persistent storage of inventory records |
| **Frontend** | HTML5 / Bootstrap 5 | Responsive user interface for easy interaction |
| **Scripting** | Vanilla JavaScript (ES6) | Handles async fetch requests to update the UI without reloading |

---

## ⚡ Key Features

- **CRUD Operations:** Full capability to **C**reate, **R**ead, **U**pdate, and **D**elete inventory items
- **Data Integrity:** Backend logic ensures validity of data (e.g., prevents negative stock values)
- **Real-time Interaction:** The frontend updates dynamically using JavaScript Fetch API
- **Responsive Design:** Optimized for viewing on different screen sizes using Bootstrap

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Pharmacy_Inventory_Tracker.git
cd Pharmacy_Inventory_Tracker
```

### 2. Set Up Virtual Environment (Recommended)

It is best practice to run Python projects in an isolated environment.

```bash
# Create environment
python3 -m venv venv

# Activate environment (Linux/Mac)
source venv/bin/activate

# Activate environment (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000/`

---

## 🔌 API Endpoints Documentation

The backend exposes the following REST endpoints:

| Method | Endpoint | Description | Payload Example |
|--------|----------|-------------|-----------------|
| **GET** | `/inventory` | Retrieve all items | N/A |
| **POST** | `/add` | Add a new medicine | `{"name": "Aspirin", "stock": 50}` |
| **PUT** | `/update/<id>` | Update stock count | `{"stock": 45}` |
| **DELETE** | `/delete/<id>` | Remove an item | N/A |

---

## 📂 Project Structure

```
/Pharmacy_Inventory_Tracker
│
├── app.py                # Main application entry point (Backend Logic)
├── pharmacy.db           # SQLite Database (Auto-generated)
├── requirements.txt      # Project dependencies
├── README.md             # Project Documentation
│
└── templates/            # Frontend HTML files
    └── index.html        # Main Dashboard Interface
```

---

## 🔮 Future Improvements

To scale this application for a larger hospital environment, I plan to implement:

- **Authentication (JWT):** Restrict access so only authorized personnel can modify stock
- **Low Stock Alerts:** Automated email notifications when stock dips below a critical threshold
- **Dockerization:** Containerizing the app for seamless deployment across different environments
- **Analytics Dashboard:** Visual charts and graphs for inventory trends and usage patterns
- **Multi-location Support:** Track inventory across multiple pharmacy locations

---

## 👨‍💻 Author

**[Your Name]**

- 🔗 [LinkedIn Profile](https://linkedin.com/in/your-profile)
- 💻 [GitHub Profile](https://github.com/YOUR_USERNAME)
- 📧 [Email](mailto:your.email@example.com)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) web framework
- UI components from [Bootstrap 5](https://getbootstrap.com/)
- Icons from [Bootstrap Icons](https://icons.getbootstrap.com/)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
