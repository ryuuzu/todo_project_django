from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', home, name="home"),

    path('register/', register, name="register"),

    path('collection/<int:pk>/', collection, name="collection"),
    path('collection/add_collection', add_collection, name="add_collection"),
    path('collection/<int:pk>/add_todo',
         add_to_collection, name="add_to_collection"),
    path('collection/<int:pk>/delete',
         delete_collection, name="delete_collection"),

    path('todo/<int:pk>/', todo, name="todo"),
    path('todo/<int:pk>/delete_todo', delete_todo, name="delete_todo"),
    path('todo/<int:pk>/update_todo', update_todo, name="update_todo"),
    path('todo/<int:pk>/mark_pending', mark_pending, name="mark_pending"),
    path('todo/<int:pk>/mark_complete', mark_complete, name="mark_complete"),
]
