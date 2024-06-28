from django.urls import path
from .views import blog_view,blog_detail_view,contact_views

urlpatterns = [
    path('', blog_view,name='blog-page'),
    path('blog/<int:id>', blog_detail_view,name='blog-detail'),
    path('contact/',contact_views,name='contact-page')

]
