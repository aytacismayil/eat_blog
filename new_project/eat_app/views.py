from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')
def strories(request):
    return render(request, 'strories.html')
def recipes(request):
    return render(request, 'recipes.html')
def contact(request):
    return render(request, 'contact.html')

