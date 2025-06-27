# 📚 FunBookstore

FunBookstore is a web-based book listing platform built using Django. It allows users to register, log in, and manage their own collection of books. The app is designed with a clean and responsive UI using Bootstrap 5.

---

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 📖 List books with:
  - Title
  - Author
  - Genre
  - Publish date
  - Cover image
- 👤 Users can:
  - Add new books
  - Edit their listed books
  - Delete their listed books
- 🌐 View all listed books
- 📄 Pagination for long lists
- 🎨 Responsive UI with Bootstrap
- 🔔 Toast notifications for unauthenticated access (optional)
  
---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default)
- **Template Engine**: Django Templates

---

## 📂 Folder Structure
simple-library-management/
│
├── .venv/                         # Virtual environment (not pushed to GitHub)
│
├── books/                         # Django app: books
│   ├── __pycache__/              # Compiled bytecode
│   ├── migrations/               # Django migrations
│   ├── templates/                # All HTML templates grouped by feature
│   │   ├── accounts/
│   │   │   ├── login.html        # User login page
│   │   │   └── register.html     # User registration page
│   │   ├── books/
│   │   │   ├── add_books.html    # Form to add a book
│   │   │   ├── book_list.html    # Lists all books
│   │   │   ├── edit_book.html    # Edit book form
│   │   │   └── my_books.html     # List of books added by the logged-in user
│   │   ├── homepage/
│   │   │   └── homepage.html     # Main homepage content
│   │   └── base.html             # Base template for layout (navbar, etc.)
│   │
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # App configuration
│   ├── forms.py                  # Django forms
│   ├── models.py                 # Database models
│   ├── tests.py                  # Unit tests
│   ├── urls.py                   # App-level URL routes
│   └── views.py                  # View logic
│
├── funbookstore/                 # Project settings folder
│   ├── __pycache__/             
│   ├── __init__.py              
│   ├── asgi.py                   # ASGI config
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Root URL configuration
│   └── wsgi.py                   # WSGI config
│
├── media/book_covers/images                        # Media files (user uploaded images)
│
├── db.sqlite3                    # SQLite database file
├── manage.py                     # Django CLI tool
└── requirements.txt              # List of Python dependencies
