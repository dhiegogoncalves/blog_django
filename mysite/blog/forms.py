from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Form

from .models import Post


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Digite um e-mail válido')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado, por favor utilize outro.')


class PostForm(ModelForm):
    titulo = forms.CharField(max_length=100)
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'categoria', 'imagem', 'status']


class ContactForm(Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'Digite seu e-mail'}))
    mensagem = forms.CharField(label='Assunto', widget=forms.Textarea(attrs={'placeholder': 'Digite o assunto'}))
