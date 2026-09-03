
from .models import Book


def get_recommendations(book):
    """
    Recommend books from the same category.
    """

    if not book.category:
        return Book.objects.exclude(id=book.id)[:3]

    recommendations = Book.objects.filter(
        category=book.category
    ).exclude(
        id=book.id
    )[:3]

    return recommendations