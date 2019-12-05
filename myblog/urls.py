from django.urls import path
from . import views


app_name = 'myblog'

urlpatterns = [
    # ex：/myblog/
    path('myblog/', views.homepage, name='homepage'),
    # ex：/myblog/bikapi_introduction/
    path('myblog/<slug:slug>/', views.detail, name='detail'),

]