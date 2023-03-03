from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Item
from .forms import NewItemForm, EditItemForm
from django.shortcuts import redirect
from django.db.models import Q
# Create your views here.

def browse(request):
    query = request.GET.get("q", "")
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    # Check if category_id exist:
    if category_id:
        items = items.filter(category_id = category_id)

    # Check if query exist:
    if query:
        items = items.filter(Q(name__icontains=query)|Q(description__icontains=query))

    content = {
         'items': items,
         'categories':categories,
         'category_id': int(category_id),
         'query': query
    }
    return render(request, 'item/browse.html', content)


def ItemDetail(request, pk):
    # item = get_object_or_404(item, pk=pk)
        # try except logic

    product = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)
    content = {
            'product': product,
            'related_items': related_items
    }
    return render(request, 'item/detail.html', content)

# Note: The user must be logged in to add new Items.
@login_required
def NewItem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    content = {
          'form': form,
          'title': 'New Item'
    }
    return render(request, 'item/form.html', content)


def updateItem(request, pk):
    product = get_object_or_404(Item, pk=pk, created_by=request.user)

    content = {}

    if request.method == 'POST':
        content['form'] = NewItemForm(request.POST, request.FILES, instance=product)

        if content['form'].is_valid():
            content['form'].save()

            return redirect('item:detail', pk=product.id)
    else:
        content['form'] = EditItemForm(instance=product)
    content['title'] = 'New Item'

    return render(request, 'item/form.html', content)


@login_required
def deleteItem(request, pk):
    content = {}
    data = Item.objects.get(pk=pk, created_by=request.user)
    content['title'] = 'DeleteItemPage'
    content['data'] = data
    if request.method =="POST":
        # delete object
        data.delete()
        # after deleting redirect to
        # home page
        return redirect('/')
    return render(request, 'item/delete.html', content)
