from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:id>', views.add, name='add'),
    path('add/addtocart/', views.addtocart, name='addtocart'),
    path('viewcart/',views.viewcart,name='viewcart'),
    path('viewcart/delete/<int:id>',views.delete,name='delete'),
    path('uploadapps/',views.uploadapps,name='uploadapps'),
    path('login/',views.loginUser,name='login'),
    path('register/',views.registerUser,name='register'),
]