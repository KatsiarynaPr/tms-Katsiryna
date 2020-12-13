from typing import Dict

from django import forms
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from applications.blog.models import Post


class AllPostsView(ListView):
    template_name = "blog/blog.html"
    model = Post

    def get_extended_context(self) -> Dict:
        context = {"form": PostForm()}

        return context


class NewPostView(CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = "/b/"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user

        return super().form_valid(form)


class WipeAllPostsView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        Post.objects.all().delete()
        return "/b/"


class PostView(DetailView):
    template_name = "blog/singl_post.html"
    model = Post

    def form_valid(self, form):
        self.object.edited = True
        return super().form_valid(form)


class DeletePostView(DeleteView):
    http_method_names = "post"
    model = Post
    success_url = "/b/"


class UpdatePostView(UpdateView):
    template_name = "blog/update_post.html"
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        self.object.edited = True
        return super().form_valid(form)

    # def update_url(self):
    #     success_url = reverse_lazy("blog:post", kwargs={"pk": self.object.pk})
    #     return success_url


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": 2})}
