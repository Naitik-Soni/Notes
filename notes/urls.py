from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", notes, name="notes"),
    path("addnotes/", addnotes),
    path("updatenote/<int:id>", updatenotes),
    path("delete/<int:id>", delete),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
