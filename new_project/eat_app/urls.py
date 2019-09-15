from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home, name='home_index'),
    path('about/',about,name='about_index'),
    path('strories/',strories,name='strories_index'),
    path('recipes/',recipes,name='recipes_index'),
    path('contact/',contact,name='contact_index'),

]