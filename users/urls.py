from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .import views

app_name = "accounts"

urlpatterns = [
    url(r"^(?P<user_id>[-\w]+)$", views.account, name="account"),
]