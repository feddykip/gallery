from django.shortcuts import render
from .models import Category, Photo

# Create your views here.
def index(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)


        
    categories = Category.objects.all()

    context = {'categories': categories, 'photos':photos}
    
    return render(request, 'index.html', context)

def photos(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(request, 'photos.html',{'photo':photo})

def search_results(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_location(search_term)
        message = f"{search_term}"

        return render (request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})