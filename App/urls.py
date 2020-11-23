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
from .views import VotesListViewSet
from .views import DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'Complaint Point', views.SignInViewSet)

user_checkMail = SignInViewSet.as_view({
    'post': 'checkMail',
})

user_login = SignInViewSet.as_view({
    'post': 'login',
})

public_feed = GrievanceViewSet.as_view({
    'post': 'publicFeed',
})

department_feed = GrievanceViewSet.as_view({
    'post': 'departmentFeed',
})

grievance_detail = GrievanceViewSet.as_view({
    'post': 'gDetail',
})

grievance_post = GrievanceViewSet.as_view({
    'post': 'grievance',
})

my_grievance = GrievanceViewSet.as_view({
    'post': 'myGrievance',
})

u_grievance = GrievanceViewSet.as_view({
    'post': 'uGrievance',
})

d_grievance = GrievanceViewSet.as_view({
    'post': 'dGrievance',
})

g_status = GrievanceViewSet.as_view({
    'post': 'updateStatus',
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

department_detail = DepartmentViewSet.as_view({
    'post': 'dDetail',
})

aadhaar_check = PeopleViewSet.as_view({
    'post': 'aCheck',
})

people_create = PeopleViewSet.as_view({
    'post': 'pSignup',
})

grievance_vote = VotesListViewSet.as_view({
    'post': 'vote',
})

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Complaint-Point/checkMail/', user_checkMail, name='user-checkMail'),
    path('Complaint-Point/login/', user_login, name='user-login'),
    path('Complaint-Point/publicFeed/', public_feed, name='public-feed'),
    path('Complaint-Point/departmentFeed/', department_feed, name='department-feed'),
    path('Complaint-Point/gDetail/', grievance_detail, name='grievance-detail'),
    path('Complaint-Point/gProofs/', grievance_proofs, name='grievance-proofs'),
    path('Complaint-Point/gDates/', grievance_dates, name='grievance-dates'),
    path('Complaint-Point/grievance/', grievance_post, name='grievance-post'),
    path('Complaint-Point/myGrievance/', my_grievance, name='my-grievance'),
    path('Complaint-Point/uGrievance/', u_grievance, name='d-grievance'),
    path('Complaint-Point/dGrievance/', d_grievance, name='d-grievance'),
    path('Complaint-Point/updateStatus/', g_status, name='g-status'),
    path('Complaint-Point/pMobileNo/', people_mobile, name='people-mobile'),
    path('Complaint-Point/dPhoneNo/', department_phone, name='department-phone'),
    path('Complaint-Point/pDetail/', people_detail, name='people-detail'),
    path('Complaint-Point/dDetail/', department_detail, name='department-detail'),
    path('Complaint-Point/aCheck/', aadhaar_check, name='aadhaar-check'),
    path('Complaint-Point/pSignup/', people_create, name='people-create'),
    path('Complaint-Point/vote/', grievance_vote, name='grievance-vote'),
]