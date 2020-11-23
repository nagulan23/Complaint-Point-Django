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
        fields = ['grievance_id', 'subject','grievance','g_department_id','upvote','downvote','current_status','arg_id','pg_id']
        
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('aadhaar_number','first_name','last_name','date_of_birth','gender','salary_pa','job','door_no','street','zip_code')
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id','department_name','bio','dep_street','d_zip_code','no_of_reports')
        
class PeopleSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('aadhaar_number','first_name','last_name','date_of_birth','gender','salary_pa','job','door_no','street','zip_code')        
        
class SignInSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = ('email_id','password','aadhaar_number','department_id')
        
class MobileNumberMapSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileNumberMap
        fields = ('m_aadhaar_number','mobile_number')
        
class AddressSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('zip_code','city','state')
        
class VotesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotesList
        fields = ('g_aadhaar_number','a_grievance_id','type')
        

class GrievancePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = ('subject','grievance','upvote','downvote','current_status','arg','pg','g_department_id')

class PGrievancePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = ('pg_id','zip_code','period')
        
class AGrievancePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeReforms
        fields = ('arg_id','reforms_type','person_concerned')
        
class ImportantDatesMapPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantDatesMap
        fields = ('i_grievance_id','important_dates')
        
class ProofsMapPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProofsMap
        fields = ('p_grievance','proofs')