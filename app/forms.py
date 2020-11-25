"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка",}

class Support(forms.Form):
        name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
        city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
        gender = forms.ChoiceField(label='Ваш пол',
                                  choices=[('1','Мужской'),('2','Женский')],
                                  widget=forms.RadioSelect, initial=1)
        abilities = forms.ChoiceField(label='Вы знаете английский', 
                                     choices=(('1','Не знаю'),
                                     ('2','Только основы'),
                                     ('3','Могу читать на английском'),
                                     ('4','Могу говорить на английском')), initial=1)
        email = forms.BooleanField(label='Получать нвости на e-mail', required=False)
        email = forms.EmailField(label='Ваш e-mail', min_length=7)
        message = forms.CharField(label='О себе', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))