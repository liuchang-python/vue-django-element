from django.urls import path

from app import views

appname = 'app'

urlpatterns = [
    # DRF路由的定义
    # path("stu/", views.StuAPIView.as_view()),
    # path("stu/<str:id>/", views.StuAPIView.as_view()),
    path("stu/", views.StuAPIViewV2.as_view()),
    path("stu/<str:id>/", views.StuAPIViewV2.as_view()),
]
