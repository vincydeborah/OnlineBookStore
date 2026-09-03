from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart, CartItem, Subscriber
from .recommendations import get_recommendations

def book_list(request):
    books = Book.objects.all()

    return render(request, 'books/book_list.html', {
        'books': books,
    })


def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    items = CartItem.objects.filter(cart=cart)

    total = sum(item.book.price * item.quantity for item in items)

    return render(request, 'books/cart.html', {
        'cart': cart,
        'items': items,
        'total': total,
    })


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book
    )

    if not created:
        item.quantity += 1

    item.save()

    return redirect('cart')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            Subscriber.objects.get_or_create(email=email)

        return redirect('home')

    return redirect('home')

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    recommended_books = get_recommendations(book)

    return render(request, 'books/book_detail.html', {
        'book': book,
        'recommended_books': recommended_books,
    })