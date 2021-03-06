from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
        path('admin/', admin.site.urls),
        path('register/', user_views.register, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
        path('cart/', include('cart.urls')),
        path('orders/', include('orders.urls')),
        path('', include('pizza_products.urls')),
        path('', include('users.urls', namespace='accounts')),
      ] \
          + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
          + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
