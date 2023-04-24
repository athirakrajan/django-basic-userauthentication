from django.urls import path
from.import views

urlpatterns=[
    path('',views.first,name='first'),
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout')
]