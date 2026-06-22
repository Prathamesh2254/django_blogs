from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Blog
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status='Published')
    '''try:

        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')  # Redirect to home if category not found:
    '''
    #category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts_by_category.html', context)
    #return HttpResponse(posts)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': blog,
    }
    return render(request, 'blogs.html', context)



def search(request):
    keyword = request.GET.get('keyword')
    posts = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(body_description__icontains=keyword), status='Published')
    context = {
        'posts': posts,
        'keyword': keyword
    }
    return render(request, 'search.html', context)