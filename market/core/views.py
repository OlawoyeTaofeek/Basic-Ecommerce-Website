from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm, ContactForm
from django.views.generic import ListView
from django.contrib import messages

# Create your views here.

# List view with both function and Class method
# def index(request):
#     items = Item.objects.filter(is_sold=False)
#     categories = Category.objects.all()
#     content = {
#            'items':items,
#            'categories':categories
#     }
#     return render(request, 'core/index.html', content)

class IndexView(ListView):
    template_name = 'core/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['items'] = Item.objects.filter(is_sold=False)
        return context



def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Your message was received, You can now wait to get an email or sms from us')
            return redirect('/') 
    else:
        form = ContactForm()

    content = {
            'form':form
    }
    return render(request, 'core/contact.html', content)



def login(request):
    return render(request, 'core/login.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/login/')
    else:
        form = SignUpForm()

    content = {
            'form':form,
            'title':'New Item'
    }
    return render(request, 'core/signup.html', content)
