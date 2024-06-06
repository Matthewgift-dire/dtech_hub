from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from blog.models import Post, Comment, Category
from blog.forms import CommentForm, ContactForm, SearchForm
# Create your views here.
# blog/views.py
	
def blog_index(request):
      posts = Post.objects.all().order_by("-created_on")
      category = Category.objects.all()
      featured_posts = Post.objects.filter(featured__icontains="yes") [:5]
      context = {
	     "posts": posts,
	     'featured_posts': featured_posts,
	     "categories_list":category
     }
      return render(request, "index.html", context)
	
def blog_category(request, category):
    category_ = Category.objects.exclude(name=category)
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page", 1)
    print(category)
    try:
    	posts = paginator.page(page_number)
    except EmptyPage:
    	posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
    	posts = paginator.page(1)
    context = {
    	"category": category,
        "posts": posts,
        "categories_list":category_,
    }
    return render(request, "category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    posts = Post.objects.exclude(title=post.title)[:4]
    category = Category.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
    	"posts": posts,
        "post": post,
        "comments": comments,
        "form": CommentForm(),
        "categories_list":category,
    }
    return render(request, "detail.html", context)
    
def blog_contact(request):
	form = ContactForm()
	if request.method == 'POST':
	       form = ContactForm(request.POST)
	       if form.is_valid():
	           email = form.cleaned_data['Email']
	           name = form.cleaned_data['Name']
	           subject = form.cleaned_data['Subject']
	           message = form.cleaned_data['Message']
	           
	           EmailMessage(
	           	"{} from, {}".format(subject,name), message,
	           	'DTech-Hub.com',
	           	['dtechub24@gmail.com'],
	           	[],
	           	reply_to=[email]
	           ).send()
	           return redirect('success')
	           
	       else:
	           form = ContactForm()
	return render(request, "contact.html", {"form": form})

	
def blog_search(request):
    form = SearchForm()
    query = None
    results = []
    
    if request.method == "GET":
    	form = SearchForm(request.GET)
    	if form.is_valid():
    		category = Category.objects.all()
    		query = form.cleaned_data['query']
    		print(query)
    		results = Post.objects.filter(Q(title__icontains=query) | Q(categories__name__icontains=query)).order_by('-created_on')
    		#paginator = Paginator(results, 1)
#    		page_number = request.GET.get("page", 1)
#    		print(paginator.count)
#    		try:
#		    	results = paginator.page(page_number)
#    		except EmptyPage:
#		    	results = paginator.page(paginator.num_pages)
#    		except PageNotAnInteger:
#		    	results = paginator.page(1)
    	context = {
        	'form': form,
        	'query': query,
        	'results': results,
        }
    
    return render(request, "search.html", context)
				
def blog_about(request):
	return render(request, "about.html")
	
def blog_dev_bio(request):
	return render(request, "dev_bio.html")
	
def success(request):
	return render(request, "success.html")