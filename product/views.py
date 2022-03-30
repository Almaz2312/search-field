from itertools import product
from django.shortcuts import render
from product.forms import SearchForm

from product.models import Product, Manufacturer


# Create your views here.
def index(request):
    form = SearchForm() 
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            text = form.cleaned_data.get('text')
            products = Product.objects.filter(name__icontains=text)
            # redirect to a new URL:
            return render(request, 'search-result.html', {'products': products})
        

    return render(request, 'index.html', {'form': form}) 