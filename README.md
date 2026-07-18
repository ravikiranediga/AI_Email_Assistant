# 📧 AI Email Assistant

An AI-powered email generation platform built using **Streamlit, FastAPI, Google Gemini API, and SQLite**. The application enables users to generate professional emails in multiple tones, maintain email history, download generated content, and analyze usage through an interactive analytics dashboard.

---

## 🚀 Features

### AI Email Generation

* Generate complete professional emails using Google Gemini.
* Support for multiple writing tones:

  * Professional
  * Formal
  * Friendly
  * Polite
  * Confident

### Email Templates

* Predefined templates for common use cases:

  * Internship Follow-Up
  * Job Application
  * Leave Request
  * Meeting Request
  * Thank You Email

### History Tracking

* Automatically stores generated emails.
* Persistent storage using SQLite.
* View previous emails directly from the sidebar.

### Analytics Dashboard

* Total emails generated.
* Most frequently used tone.
* Tone distribution chart.
* Recent email activity.

### Download Support

* Download generated emails as text files.

### User-Friendly Interface

* Built using Streamlit.
* Responsive two-column layout.
* Real-time email generation.

---

## 🏗️ System Architecture

User Input (Streamlit)

↓

FastAPI Backend

↓

Gemini API

↓

Generated Email

↓

SQLite Database

↓

Analytics Dashboard

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI Model

* Google Gemini API

### Database

* SQLite

### Libraries

* Requests
* Python Dotenv
* Collections
* SQLite3

---

## 📂 Project Structure

AI_Email_Assistant/

├── api/

│   └── main.py

│

├── database/

│   ├── db.py

│   └── analytics.py

│

├── services/

│   └── email_generator.py

│

├── app.py

├── config.py

├── requirements.txt

├── .env

├── emails.db

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>

cd AI_Email_Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## ▶️ Running the Backend

```bash
uvicorn api.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Running the Frontend

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 📊 Analytics Module

The analytics system provides:

* Total Emails Generated
* Most Used Tone
* Tone Distribution Visualization
* Recent Email Activity

This enables basic usage monitoring and user behavior analysis.

---

## 🗄️ Database Design

Table: emails

| Column     | Type      |
| ---------- | --------- |
| id         | INTEGER   |
| prompt     | TEXT      |
| tone       | TEXT      |
| email      | TEXT      |
| created_at | TIMESTAMP |

---

## 🔄 Application Workflow

1. User enters email requirements.
2. User selects tone.
3. Streamlit sends request to FastAPI.
4. FastAPI calls Gemini API.
5. Gemini generates professional email.
6. Response is returned to Streamlit.
7. Email is stored in SQLite.
8. Analytics dashboard updates automatically.

---

## 🎯 Learning Outcomes

Through this project:

* Built REST APIs using FastAPI
* Integrated Generative AI APIs
* Developed interactive UIs using Streamlit
* Worked with SQLite databases
* Implemented analytics dashboards
* Managed environment variables securely
* Structured a full-stack AI application

---

## 🔮 Future Enhancements

* User Authentication
* PostgreSQL Integration
* PDF Export
* Email Sending via SMTP
* Multi-Language Support
* Docker Deployment
* Cloud Deployment (Render / Streamlit Cloud)

---

## 👨‍💻 Author

E Ravi Kiran

B.Tech – Computer Science (AI)

Sri Venkatesa Perumal College of Engineering

GitHub: https://github.com/ravikiranediga

LinkedIn: https://www.linkedin.com/in/ravikiranediga
