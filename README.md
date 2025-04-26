# Twitter Django Clone

A basic Twitter-like web application built with Django.

This project allows users to register, log in, create tweets, and view posts — providing the core functionality of a minimal Twitter clone.

---

## 🚀 Features

- User registration and authentication
- Posting tweets
- Viewing all tweets
- User profile management
- Simple, clean UI (extensible for future improvements)

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** SQLite (default Django database)

---

## 📦 Setup Instructions

Follow these steps to run the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aarushi0010/twitter_django.git
   cd twitter_django
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Visit the application:**

   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Project Structure

```
twitter_django/
├── twitter/        # Main Django app (tweets, users)
├── twitter_django/  # Project settings
├── manage.py        # Django management script
├── templates/       # HTML templates
└── static/          # Static files (CSS, JS, images)
```

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests to improve the project.

---
