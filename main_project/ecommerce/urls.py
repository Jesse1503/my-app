from django.urls import path
from .import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout),
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup,name='signup')



]