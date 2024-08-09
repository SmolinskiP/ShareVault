from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='create_user'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('test-email/', views.test_email, name='test_email'),
]

handler404 = views.error_404
handler500 = views.error_500
