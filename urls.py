from django.urls import path
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('profile',views.profile,name='profile'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    
]
