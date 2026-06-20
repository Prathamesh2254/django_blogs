from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Blog
from django.http import HttpResponse
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