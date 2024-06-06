from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('about/', views.cg, name='about'),
    path('cart/', views.cg1, name='cart'),
    path('checkout/', views.cg2, name='checkout'),
    path('contact-us/', views.cg3, name='contact-us'),
    path('gallery/', views.cg4, name='gallery'),
    path('index', views.cg5, name='index'),
    path('my-account/', views.cg6, name='my-account'),
    path('shop-detail/', views.cg7, name='shop-detail'),
    path('shop/', views.shop, name='shop'),      
    path('wishlist/', views.cg9, name='wishlist'),
    path('', views.login_view, name='login'),  # New URL pattern for login
    path('signup/', views.signup_view, name='signup'),  # New URL pattern for signup
    path('s1/', views.cg11, name='s1'),
    path('s2/', views.cg12, name='s2'),
    path('s3/', views.cg13, name='s3'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
