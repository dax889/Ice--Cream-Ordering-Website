from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ("", views.index, name='Home'),
    path ("about", views.about, name='about'),   
    path ("services", views.services, name='services'),   
    path ("feedbackform", views.feedbackform, name='feedbackform'),   
    path ("contact", views.contact, name='contact'),   

    # user only
    path('orders/', views.my_orders, name='my_orders'),
    path('wishlist/', views.my_wishlist, name='wishlist'),
    path('settings/', views.account_settings, name='account_settings'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),

    path('icecreams/', views.icecream_list, name='icecream_list'),
    path('icecream/<int:item_id>/', views.icecream_detail, name='icecream_detail'),
    path('icecream/<str:flavour>/', views.category, name='category'),
    path('Ordernow/', views.Ordernow, name='Ordernow'),
    path('offers/', views.offers, name='offers'),
    # path('cart/', views.cart, name='cart'),
    # path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('pay_now/', views.pay_now, name='pay_now'),
    path('cart', views.add_to_cart, name='cart'),
    # path('pay-now/', views.pay_now, name='pay_now'),
    # path('cart/', views.show_cart, name='show_cart'),
    # path ("Contact", views.contact),   
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)