from django.urls import path , include
from  django.views.generic import TemplateView

urlpatterns = [
    path('api/',include('blog.api.v1.urls'))
]