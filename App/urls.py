from django.urls import include, path
from rest_framework import routers
from . import views
from .views import SignInViewSet
from .views import GrievanceViewSet
from .views import ProofsMapViewSet
from .views import ImportantDatesMapViewSet
from .views import MobileNumberMapViewSet
from .views import PhoneNumberMapViewSet
from .views import PeopleViewSet

router = routers.DefaultRouter()
router.register(r'Complaint Point', views.SignInViewSet)
user_login = SignInViewSet.as_view({
    'post': 'login',
})

public_feed = GrievanceViewSet.as_view({
    'get': 'publicFeed',
})

grievance_proofs = ProofsMapViewSet.as_view({
    'post': 'gProofs',
})

grievance_dates = ImportantDatesMapViewSet.as_view({
    'post': 'gDates',
})

people_mobile = MobileNumberMapViewSet.as_view({
    'post': 'pMobileNo',
})

department_phone = PhoneNumberMapViewSet.as_view({
    'post': 'dPhoneNo',
})

people_detail = PeopleViewSet.as_view({
    'post': 'pDetail',
})

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Complaint-Point/login/', user_login, name='user-login'),
    path('Complaint-Point/publicFeed/', public_feed, name='public-feed'),
    path('Complaint-Point/gProofs/', grievance_proofs, name='grievance-proofs'),
    path('Complaint-Point/gDates/', grievance_dates, name='grievance-dates'),
    path('Complaint-Point/pMobileNo/', people_mobile, name='people-mobile'),
    path('Complaint-Point/dPhoneNo/', department_phone, name='department-phone'),
    path('Complaint-Point/pDetail/', people_detail, name='people-detail'),
]