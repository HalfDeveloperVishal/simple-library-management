from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm , BookForm
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "User logged in successfully.")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "User logged out successfully.")
    return redirect('home')

def home_view(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'homepage/homepage.html', {'books': books})
    

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.listed_by = request.user
            book.save()
            return redirect('home')  
    else:
        form = BookForm()
    return render(request, 'books/add_books.html', {'form': form})

def book_list(request):
    books = Book.objects.all().order_by('-created_at')  
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def my_books(request):
    books = Book.objects.filter(listed_by=request.user).order_by('-created_at')
    return render(request, 'books/my_books.html', {'books': books})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk, listed_by=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('my_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, listed_by=request.user)
    if request.method == "POST":
        book.delete()
        return redirect('my_books')
    return redirect('my_books')