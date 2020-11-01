from rest_framework import serializers
from .models import Address
from .models import AdministrativeReforms
from .models import Department
from .models import Grievance
from .models import ImportantDatesMap
from .models import MobileNumberMap
from .models import People
from .models import PhoneNumberMap
from .models import ProofsMap
from .models import Public
from .models import SignIn
from .models import VotesList

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = ['email_id', 'password','department_id','aadhaar_number']
        
class PublicFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = ['grievance_id', 'subject','grievance','g_department','upvote','downvote','current_status','arg_id','pg_id']
        
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['aadhaar_number', 'first_name','last_name','date_of_birth','gender','salary_pa','job','door_no','street','p_zip_code'],