from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.createuser,name='create'),
    path('update',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]
