from django.urls import path , include
from  django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('api/v1/',include('accounts.api.v1.urls'))
]