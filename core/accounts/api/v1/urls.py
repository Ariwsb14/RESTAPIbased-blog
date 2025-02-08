from django.urls import path , include
from . import views
from  django.views.generic import TemplateView
app_name = 'api-v1'
urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout',views.CustomDiscardAuthToken.as_view(),name ='token-logout')

]