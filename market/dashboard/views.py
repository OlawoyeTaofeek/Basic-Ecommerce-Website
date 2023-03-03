from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item, Category

# Create your views here.
@login_required
def Index(request):

    content = {}

    content['items'] = Item.objects.filter(created_by = request.user)
    content['categories'] = Category.objects.filter(name = content['items'][0].category)

    return render(request, 'dashboard/Index.html', content)
