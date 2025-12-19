from django.urls import path
from .views import login_view, profile,about,logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
    path('logout/', logout_view, name='logout'),
]

urlpatterns = [
    path('', login_view, name='login'),
    path('hello/', profile, name='profile'),
    path('about/', about, name='about'),
    path('logout/', logout_view, name='logout'),
]


"""
urlpatterns = [
    path('', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
    path('logout/', logout_view, name='logout'),
]
from .views import LoginTokenAPI"""

urlpatterns = [
    path('', login_view, name='login'),
    path('hello/', profile, name='profile'),
    path('about/', about, name='about'),
    path('logout/', logout_view, name='logout'),
]

"""
urlpatterns = [
    path('', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
    path('logout/', logout_view, name='logout'),
]
from .views import LoginTokenAPI"""

urlpatterns = [
    path('', login_view, name='login'),
    path('hello1/', profile, name='profile'),
    path('about/', about, name='about'),
    path('logout/', logout_view, name='logout'),
]
