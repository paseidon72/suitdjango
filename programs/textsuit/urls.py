from django.urls import path
from . import views

urlpatterns = [
    path('', views.textsuit_home, name='textsuit_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete')
]
