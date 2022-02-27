from django.urls import path
from .views import index

urlpatterns = [
    # other patterns
    path("", index)
]