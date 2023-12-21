from django.urls import path
from .views import createBook, deleteView, detailsView, editBook, indexView
app_name='index'

urlpatterns = [
    
    path('', indexView, name='index'),
    path('details/<int:id>/', detailsView, name='details'),
    path('create-book/', createBook, name='create_book'),
    path('edit-book/<int:book_id>/', editBook, name='edit_book'),
    path('delete-book/<int:book_id>/', deleteView, name='delete_book'),
    


]