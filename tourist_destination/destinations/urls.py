from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('destinations/<int:pk>/update/', views.destination_update, name='destination_update'),
    path('destinations/<int:pk>/delete/', views.destination_delete, name='destination_delete'),
    path('destinations/create/', views.destination_create, name='destination_create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
