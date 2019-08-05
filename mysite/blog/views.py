from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import UserCreationFormWithEmail
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogCreateView(SuccessMessageMixin, CreateView):
    model = Post
    fields = ['autor', 'titulo', 'conteudo']
    template_name = 'blog/post_new.html'
    # context_object_name = 'post'
    success_message = "%(field)s - criado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['autor', 'titulo', 'conteudo']
    template_name = 'blog/post_edit.html'
    success_message = "%(field)s - alterado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)


class BlogSignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'
