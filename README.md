## 📚 School Management System (Django)

A comprehensive school management system built with Django.
It allows administrators to manage students, parents, authentication, notifications, and more from a centralized dashboard.

---

### 🚀 Features

* ✅ User Authentication (Login, Signup, Logout)
* 🧑‍🎓 Student Management (Add, View, Filter)
* 👨‍👩‍👧 Parent Details Linked to Each Student
* 🔔 Notifications System (with mark-as-read)
* 🔒 Access Control using Django's permission system
* 📸 Student Image Upload Support
* 📦 Modular Code Structure
* 📄 Clean and responsive templates (HTML, CSS, Bootstrap)

---

### 🛠 Tech Stack

* **Framework**: Django (v5.1+)
* **Language**: Python 3.13
* **Database**: SQLite3
* **Frontend**: HTML, CSS, Bootstrap
* **Backend**: Django Views, Models, Templates
* **Others**: Django Admin, Django Forms, CSRF protection

---

### 📂 Project Structure

```
SchoolSystem/
│
├── Home/                  # Main Django app
│   ├── migrations/
│   ├── static/            # Static files (CSS/JS/images)
│   ├── templates/         # All HTML templates
│   ├── models.py          # Student & Parent models
│   ├── views.py           # Core logic for each page
│   └── urls.py            # App-level URL routing
│
├── SchoolSystem/          # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3             # Database
├── manage.py              # Django CLI
└── README.md              # Project info (this file)
```

---

### ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/itz-sidd/SchoolSystem.git
cd SchoolSystem
```

2. **Create Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

> If you don't have `requirements.txt`, manually install Django:

```bash
pip install django
```

4. **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create Superuser (for admin login)**

```bash
python manage.py createsuperuser
```

6. **Run the Server**

```bash
python manage.py runserver
```

7. **Open in Browser**

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---



### 🤝 Contributions

Contributions are welcome! Feel free to fork this repo, open issues, or submit pull requests.

---

### 📄 License

This project is open source and available under the [MIT License](LICENSE).


