from django.urls import path 
from .views import BookList 

urlpatterns = [
    path('books/', BookList.as_view(), name ='book-list'),

]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# create a router and register our viewset with it.
router =DefaultRouter()
router.register(r'books', BookViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]