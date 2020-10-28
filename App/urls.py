from django.urls import include, path
from rest_framework import routers
from . import views
from .views import SignInViewSet

router = routers.DefaultRouter()
router.register(r'Complaint Point', views.SignInViewSet)
user_login = SignInViewSet.as_view({
    'post': 'login',
})

user_list = SignInViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Complaint-Point/login/', user_login, name='user-login'),
    path('Complaint-Point/list/', user_list, name='user-list'),
]