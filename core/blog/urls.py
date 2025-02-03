from django.urls import path , include
from  django.views.generic import TemplateView
app_name = 'blog'
urlpatterns = [
    path('api/',include('blog.api.v1.urls'))
]