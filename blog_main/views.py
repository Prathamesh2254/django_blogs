from django.shortcuts import render
from blogs.models import Category, Blog
from .forms import UserRegisterForm

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True, status='Published').order_by('-created_at')[:5]
    context = {
        'categories': categories,
        'featured_blogs': featured_blogs
    }
    return render(request, 'home.html', context)
    


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register_success.html')
        else:
            print(form.errors)  # Print form errors to the console for debugging



    else:
        form = UserRegisterForm()
    context = {
        'form': form,
               }
    return render(request, 'register.html', context)