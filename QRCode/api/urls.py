from django.urls import path

from .views import ListTables

urlpatterns = [
    path('list/', ListTables.as_view(), name="list"),
]
