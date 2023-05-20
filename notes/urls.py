from django.urls import path
from .views import *

urlpatterns = [
    path("", notes, name="notes"),
    path("addnotes/", addnotes),
    path("updatenote/<int:id>", updatenotes),
    path("delete/<int:id>", delete),
]
