from django.urls import path

from store.views import *

urlpatterns = [
    path("", ProductList.as_view(), name="index"),
    path("category/<slug:slug>/", ProductListByCategory.as_view(), name="category"),
    path("product/<slug:slug>/", ProductDetail.as_view(), name="product"),
    path("login_register/", login_register, name="login_register"),
    path("user_register/", user_register, name="user_register"),
    path("user_login/", user_login, name="user_login"),
    path("user_logout/", user_logout, name="user_logout"),
    path("likes/", LikeView.as_view(), name="likes"),
    path("user_like/<slug:product_slug>/", user_like, name="user_like"),
    path("cart/", cart, name="cart"),
    path("to_cart/<int:product_id>/<str:action>/", to_cart, name="to_cart"),
    path("payment/", payment, name="payment"),
    path("success/", success_payment, name="success"),
    path("contact/", contact, name="contact"),
]
