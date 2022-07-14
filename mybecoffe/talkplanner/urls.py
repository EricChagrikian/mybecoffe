from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='talkplanner'),
    path('del/<str:item_id>',views.remove, name="del"),
]