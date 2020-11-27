
from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from .models import Post , Category
from .forms import PostForm
from users.models import Signup
from .forms import EmailSignupForm
from django.urls import reverse_lazy
from django.contrib import messages



 #Create your views here.
"""
def get_category_count():
	queryset = Post.objects.values('category__title').annotate(Count('category__title'))
	return queryset

def home(request, category_slug = None):
	category = None
	categories = Category.objects.all()
	posts = Post.objects.all()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		posts =post.filter(category = category)
	context ={
	   'categories': categories,
	   'category': category,
	   'posts': posts

	}
	return render(request,'blog/home.html',context)
"""
"""
def post_list(request,category_slug=None):
    queryset = Post.objects.all()
    category_count = get_category_count()
    paginator = Paginator(queryset, 3)
    page_request_var = 'page'
    page =request.GET.get(page_request_var)
    try:
    	paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
    	paginated_queryset = paginator.page(1)
    except EmptyPage:
    	paginated_queryset = paginator.page(paginator.num_pages)
	

    context ={
       #'queryset':posts,
		'queryset':paginated_queryset,
		'page_request_var':page_request_var,
		#'most_recent':most_recent,
		'category_count':category_count
    }

    return render(request, 'blog/home.html', context) 

def article_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
	    email = request.POST["email"]

	    ew_signup = Signup()
	    ew_signup.email = email
	    ew_signup.save()
	    
    return render(request,'blog/article.html',{'post':post})

def category(request, slug):
	category = Category.objects.get(slug=slug)

	context={
	   'category':category
	}
	return renser(request, 'blog/category.html', context)


class AddPostView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	#field = ('title', 'overview', 'image')
	template_name = 'blog/post_create.html'

class UpdatePostView(LoginRequiredMixin, UpdateView):
	model = Post
	template_name = 'blog/update.html'
	fields ='__all__'
	#fields = ['title','overview','image']

class DeletePostView(LoginRequiredMixin,DeleteView):
	model = Post
	template_name = 'blog/delete.html'
	success_url = reverse_lazy('blog:post-list')



def category_list(request, category_slug, slug):
	categories =Category.objects.all()
	post = Post.objects.filter(category=category)
	if category_slug:
		category =get_object_or_404(Category, slug=category_slug)
		post = post.filter(category=category)

	context={
	   'categories':categories,
	   'category': category,
	   'post':post,
	}
	return render(request, 'category/post_by_category.html',context)

def article_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)

	context={
	   'post': post
	}
	return render(request, 'blog/article.html', context)


"""
class HomeView(ListView):
	model =  Post
	paginate_by = 3
	template_name = 'blog/home.html'
	ordering = ['-id']

class ArticleDetailView(DetailView):
	model = Post
	def post(request):
		post=get_object_or_404(Post,pk=pk)	
		form = EmailSignupForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			if Signup.objects.filter(email=instance.email).exists():
				messages.warning(request,"Sorry! your email already exists!")
			else:
				instance.save()
				messages.success(request,"Thank You For Subscribing!")
				return redirect('users:about')
		
	template_name = 'blog/article.html'

def newsletter_signup(request):
	form = EmailSignupForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		if Signup.objects.filter(email=instance.email).exists():
			messages.warning(request,"Sorry! your email already exists!")
		else:
			instance.save()
			messages.success(request,"Thank You For Subscribing!")
			return redirect('users:about')

	context={
	  'form': form
	}
	return render(request,'accounts/newsletter_signup.html',context)




"""
class AddPostView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	#field = ('title', 'overview', 'image')
	template_name = 'blog/post_create.html'

class UpdatePostView(LoginRequiredMixin, UpdateView):
	model = Post
	template_name = 'blog/update.html'
	fields ='__all__'
	#fields = ['title','overview','image']

class DeletePostView(LoginRequiredMixin,DeleteView):
	model = Post
	template_name = 'blog/delete.html'
	success_url = reverse_lazy('blog:post-list')


def CategoryView(request, slug):
	category = get_object_or_404(Category, slug=slug)
	posts = category.posts.all()

	context={
	    'category':category,
	    'posts': posts
	}
	return render(request, 'blog/category.html',context)

def category_list(request, slug):
	category =Category.objects.get(slug=slug)

	context={
	   'category': category
	}
	return render(request, 'blog/category.html',context)


class CatListView(ListView):
	model= Post
	template_name ='blog/category.html'

	def get_queryset(self):
		category = self.get_object_or_404(Category, pk=self.kwargs['pk'])
		return Post.objects.filter(category=self.category)

	def get_context_data(self, **kwargs):
		context = super(CatListView, self).get_context_data(**kwargs)
		context['category'] =self.category
		return context

def PostCategory(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	post = Post.objects.all()
	if category_slug:
		category = get_object_or_404(Category,slug=category_slug)
		post = Post.filter(category=category)
	context ={
	 'categories': categories,
	 'post': post,
	 'category': category
	}
	return render(request, 'blog/category.html', context)
"""



@login_required
def post_create(request):
	form = PostForm()
	if request.method== "POST":
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
		   form.save()
		return redirect('blog:post-list')
	context ={
	'form':form
	}
	return render(request,'blog/post_create.html',context)

@login_required
def post_update(request, pk):
	post =Post.objects.get(id=pk)
	form = PostForm(instance=post)
	if request.method== "POST":
		form = PostForm(request.POST, instance=post) #or None, request.FILES or None)
		if form.is_valid():
		   form.save()
		return redirect('blog:post-list')
	context ={
	'form':form
	}
	return render(request,'blog/post_create.html',context)

@login_required
def post_delete(request, pk):
	post =Post.objects.get(id=pk)
	#form = PostForm(instance=post)
	if request.method== "POST":
		post.delete()
		#form = PostForm(request.POST, instance=post)
		#if form.is_valid():
		   #form.save()
		return redirect('blog:post-list')
	context ={
	'post':post
	}
	return render(request,'blog/delete.html',context)

