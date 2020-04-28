from django.urls import path
from .views import LoginPageView, RegisterPageView

urlpatterns = [

    path('', LoginPageView.as_view(), name='login'),
    path('registro/', RegisterPageView.as_view(), name='registro')

]
