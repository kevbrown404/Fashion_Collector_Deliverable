from django.shortcuts import redirect
from django.views import View # <- View class to handle requests
#...
# import models
from .models import Brand, Collection, Favorites
#from django.views.generic import DetailView
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.urls import reverse


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorites.objects.all
        return context

class About(TemplateView):
    template_name = "about.html"

class BrandCreate(CreateView):

    model = Brand
    fields = ['name', 'img', 'bio', 'verified_brand']
    template_name = "brand_create.html"
    success_url = "/brands/"
    # this will get the pk from the route and redirect to brand view
    def get_success_url(self):
        return reverse('brand_detail', kwargs={'pk': self.object.pk})
    
class BrandDetail(DetailView):
    model = Brand
    template_name = "brand_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorites.objects.all()
        return context

class BrandUpdate(UpdateView):
    model = Brand
    fields = ['name', 'img', 'bio', 'verified_brand']
    template_name = "brand_update.html"
    success_url = "/brands/"

    def get_success_url(self):
        return reverse('brand_detail', kwargs={'pk': self.object.pk})

class BrandDelete(DeleteView):
    model = Brand
    template_name = "brand_delete_confirmation.html"
    success_url = "/brands/"

class CollectionCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        brand = Brand.objects.get(pk=pk)
        Collection.objects.create(title=title, length=length, brand=brand)
        return redirect('brand_detail', pk=pk)

class BrandsList(TemplateView):
    template_name = "brands_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["brands"] = Brand.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["brands"] = Brand.objects.all() # Here we are using the model to query the database for us.
                        # default header for not searching 
            context["header"] = "Trending Brands"
        return context

class FavoriteCollectionAssoc(View):

    def get(self, request, pk, collection_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Favorites.objects.get(pk=pk).collections.remove(collection_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Favorites.objects.get(pk=pk).collections.add(collection_pk)
        return redirect('home')

#class Collection:
    #def __init__(self, name, year, info):
        #self.name = name
        #self.year = year
        #self.info = info


