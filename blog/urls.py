from django.urls import path
from .views import IndexView, detail, category

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', detail, name='detail'),
    path('<category_name>/', category, name='category'),
]

