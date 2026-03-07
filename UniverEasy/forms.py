from django import forms
from .models import FileWork

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileWork
        fields = ['theme', 'variant','faculty', 'degree', 'course', 'edu_form', 'discipline', 'file']
        labels = {
            'theme': 'Введите тему работы (или темы, если их несколько. Перечислите через запятую, чтобы их было проще найти)',
            'faculty': 'Факультет',
            'degree': 'Степень',
            'course': 'Курс',
            'edu_form': 'Форма обучения',
            'file': 'Файл',
            'discipline': 'Дисциплина',
            'variant': 'Вариант (если есть)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
