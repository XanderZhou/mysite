from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.blog_detail, name="blog_detail"),
    path('<int:blog_type_pk>', views.blog_with_type, name="blog_with_type"),

]