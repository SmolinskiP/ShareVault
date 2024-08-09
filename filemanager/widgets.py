from django import forms

class AdminFileWidget(forms.ClearableFileInput):
    template_name = 'filemanager/widgets/admin_file_widget.html'

