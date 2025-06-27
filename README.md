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

## 📁 Project Structure
<pre>
project-name/
│
├── books/
│ ├── templates/
│ │ ├── accounts/
│ │ │ ├── login.html
│ │ │ └── register.html
│ │ ├── books/
│ │ │ ├── add_books.html
│ │ │ ├── book_list.html
│ │ │ ├── edit_book.html
│ │ │ └── my_books.html
│ │ └── homepage/
│ │ └── homepage.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── funbookstore/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── templates/
│ └── base.html
│
├── media/
├── db.sqlite3
├── manage.py
└── requirements.txt

</pre>
