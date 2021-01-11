from django.urls import path

from api import views

urlpatterns = [
    # path('books/',views.BookAPIView.as_view()),
    # path('books/<str:id>/',views.BookAPIView.as_view()),

    path('books/',views.BookAPIViewV2.as_view()),
    path('books/<str:id>/',views.BookAPIViewV2.as_view()),
]