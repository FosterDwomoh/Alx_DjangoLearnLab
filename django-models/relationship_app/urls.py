from django.urls import path
from .Views import list_books, LibraryDetailView
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


# relationship_app
from django.urls import path
from . import views

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    
]

# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    
]

# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('view.register/', views.register, name='register'),
    path('loginView.as_view/', loginView.as_view, template_name='login'),
    path('logoutView.as_view/', logoutViews.as_view, template_name='logout'),
]

