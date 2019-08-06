from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import UserCreationFormWithEmail, PostForm, ContactForm
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_new.html'
    # context_object_name = 'post'
    success_message = "%(field)s, criado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_message = "%(field)s, alterado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)


class BlogSignUpView(LoginRequiredMixin, CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'


def contact(request):
    send = False

    form = ContactForm(request.POST or None)
    if form.is_valid():
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')
        email = EmailMessage(
            'Mensagem do Blog Django',
            f'De {nome} <{email}> Escreveu: \n\n {mensagem}',
            'no-reply',
            ['django@gmail.com'],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False

    context = {
        'form': form,
        'success': send
    }

    return render(request, 'blog/contact.html', context)
