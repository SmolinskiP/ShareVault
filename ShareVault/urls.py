from django.contrib import admin
from django.urls import include, path
from filemanager.admin import admin_site
from django.conf import settings
from django.conf.urls.static import static
from filemanager import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.redirect_to_login),
    path('admin/', admin_site.urls),
    path('files/', include('filemanager.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='create_user'),
    path('test-email/', views.test_email, name='test_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

