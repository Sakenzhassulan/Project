from django.conf.urls import url
from rest_framework import routers
from authe import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'profile', views.UserViewSet)

urlpatterns = [
    url(r'^login/', obtain_auth_token)
]

urlpatterns += router.urls

