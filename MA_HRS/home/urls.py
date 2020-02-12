from django.urls import path, include
from home import views


app_name = 'home'

urlpatterns=[
        path('en/', views.viewEN, name='en'),
        path('ar/', views.viewAR, name='ar'),
        # path('login', views.user_login, name='user-login'),
        # path('logout/', views.user_logout, name='logout'),
        # path('add-user/', views.addUserView, name='new-user'),
        # path('register/', views.register, name='register'),
        path('', views.homepage, name='homepage'),
]
