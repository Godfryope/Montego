from django.urls import path
from .views import *
from django.contrib.auth.views import *
from allauth.account.views import LoginView, SignupView

urlpatterns = [
    # Product List View
    path('', ProductListView.as_view(), name='product_list'),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    path('accounts/signup/', SignupView.as_view(template_name='accounts/signup.html'), name='account_signup'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/payment/', PaymentStatusView.as_view(), name='payment_status'),
    path('order/<slug:slug>/', OrderDetailView.as_view(), name='order_detail'),
]
