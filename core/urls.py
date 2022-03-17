from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from pages.views import homepage, courier, customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('customer/', customer, name='customer'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name="account/login.html"),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('courier/', courier, name='courier'),

]
