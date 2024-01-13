from django.urls import path
from .views import BooklListCreateView

urlpatterns = [
    path('api/your_model/', BooklListCreateView.as_view(), name='book_list_create_view'),
]