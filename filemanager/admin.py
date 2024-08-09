from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import File
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .forms import AdminFileForm

class UserCreationFormWithEmail(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserChangeFormWithEmail(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationFormWithEmail
    form = UserChangeFormWithEmail
    list_display = ('username', 'email', 'is_superuser', 'last_login')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'user', 'upload_date', 'expiration_date')
    search_fields = ('filename', 'user__username')
    list_filter = ('upload_date', 'expiration_date')
    fieldsets = (
        (None, {
            'fields': ('user', 'filename', 'file', 'expiration_date')
        }),
    )
    verbose_name = _("Plik")
    verbose_name_plural = _("Pliki")

#class FileAdmin(admin.ModelAdmin):
#    form = AdminFileForm

#admin.site.register(File, FileAdmin)

class MyAdminSite(admin.AdminSite):
    site_header = 'ShareVault Administration'
    site_title = 'ShareVault Admin'
    index_title = 'Welcome to ShareVault Admin'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('my_view/', self.admin_view(self.my_view))
        ]
        return custom_urls + urls

    def my_view(self, request):
        context = dict(
            self.each_context(request),
            title='My Custom View',
        )
        return TemplateResponse(request, "admin/my_view.html", context)

    def create_user_view(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:user_list')
        else:
            form = UserCreationForm()
        context = dict(
            self.each_context(request),
            form=form,
        )
        return TemplateResponse(request, 'admin/create_user.html', context)

    def user_list_view(self, request):
        users = User.objects.all()
        context = dict(
            self.each_context(request),
            users=users,
        )
        return TemplateResponse(request, 'admin/user_list.html', context)

admin_site = MyAdminSite(name='myadmin')
admin_site.register(File, FileAdmin)
admin_site.register(User, UserAdmin)

