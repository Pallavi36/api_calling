from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('addpro',views.addpro),
    path('delete',views.delete),
    path('update',views.update),
]
