from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post, Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

# dummy Query set below #
""" posts =[
  {
    'author': 'Abhishek Choudhury',
    'title': 'First Blog Post',
    'message': 'Hello there I am using this app!',
    'date_posted': '19th July 2020' 
  },
  {
    'author': 'Rajat Sharma',
    'title': 'First Blog Post',
    'message': 'Hello there I am using this app!',
    'date_posted': '19th July 2020'
  }
] """


""" @login_required
def home(request):
    
    context = {
        'posts': Post.objects.all()
        
    }

    return render(request, 'Blog/home.html', context) """


class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'  # app/model_viewtype.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    #paginate_by = 8


class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'  # app/model_viewtype.html
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'message']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'message']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'Blog/About.html', {'title': 'About Us'})


@login_required
def security(request):
    user = request.user
    return render(request, 'Blog/settings.html', {'title': 'Settings'})


""" def default(request):
  return render(request, 'Blog/default.html' ) """
""" 
def active(request):
  return user.is_authenticated

 """

""" Like code goes here  """


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('blog-home')


""" Like code ends here  """
