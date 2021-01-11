from django.urls import path

from user import views

appname = 'user'

urlpatterns = [
    path('users/',views.users,name='users'),
    path('del_user/',views.del_user,name='del_user'),
    path('get_user/',views.get_user,name='get_user'),
    path('add_user/',views.add_user,name='add_user'),
    path('alter_user/',views.alter_user,name='alter_user'),

    path('the_users/',views.UserView.as_view()),
    path('the_users/<str:id>/',views.UserView.as_view()),

    # DRF路由的定义
    path("employees/", views.UsersAPIView.as_view()),
    path("employees/<str:id>/", views.UsersAPIView.as_view()),



]