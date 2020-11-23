from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SignInSerializer
from .serializers import PublicFieldSerializer
from .serializers import PeopleSerializer
from .serializers import PeopleSignupSerializer
from .serializers import SignInSignupSerializer
from .serializers import AddressSignupSerializer
from .serializers import VotesListSerializer
from .serializers import GrievancePostSerializer
from .serializers import PGrievancePostSerializer
from .serializers import AGrievancePostSerializer
from .serializers import ImportantDatesMapPostSerializer
from .serializers import ProofsMapPostSerializer
from .serializers import  MobileNumberMapSignupSerializer
from .serializers import DepartmentSerializer
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
from rest_framework import status
from rest_framework.response import Response
import datetime

class SignInViewSet(viewsets.ModelViewSet):
    queryset = SignIn.objects.all()
    serializer_class = SignInSerializer
    
    def checkMail(self,request):
        if SignIn.objects.filter(email_id=request.data["email_id"]).exists():
            return Response({'status':'success'},status=200)
        else:
            return Response({'status':'fail'},status=200)
            
    
    def login(self, request):
        try:
            if not SignIn.objects.filter(email_id=request.data["email_id"]).exists():
                return Response({'status':'fail','msg':'User doesnot exist'},status=200)
        except:
            return Response({'status':'fail','msg':'EMAIL ID IS REQUIRED TO LOGIN'},status=200)
        try:
            if not SignIn.objects.filter(email_id=request.data["email_id"],password=request.data["password"]).exists():
                return Response({'status':'fail','msg':'Password incorrect'},status=200)
        except:
            return Response({'status':'fail','msg':'PASSWORD IS REQUIRED TO LOGIN'},status=200)
        if SignIn.objects.get(email_id=request.data["email_id"],password=request.data["password"]).aadhaar_number==None:
            instance = SignIn.objects.get(email_id=request.data["email_id"],password=request.data["password"])
            serializer = self.get_serializer(instance,many=False)
            return Response({'status':'success','msg':'d'+serializer.data["department_id"]},status=200)
        else:
            instance = SignIn.objects.get(email_id=request.data["email_id"],password=request.data["password"])
            serializer = self.get_serializer(instance,many=False)
            return Response({'status':'success','msg':'a'+serializer.data["aadhaar_number"]},status=200)
        
class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    
    def pDetail(self, request):
        queryset = People.objects.get(aadhaar_number=request.data["aadhaar_number"])
        serializer = PeopleSerializer(queryset)
        return Response(serializer.data)
    
    def aCheck(self,request):
        if People.objects.filter(aadhaar_number=request.data['aadhaar_number']).exists():
            return Response({'status':'fail'}, status=200)
        return Response({'status':'success'}, status=200)
    
    def pSignup(self,request):
        serializer1 = SignInSignupSerializer(data={key: request.data[key] for key in ['email_id','password','aadhaar_number','department_id']})
        if not Address.objects.filter(zip_code=request.data['zip_code']).exists():
            serializer2 = AddressSignupSerializer(data={key: request.data[key] for key in ['zip_code','city','state']})
            serializer2.is_valid(raise_exception=True)
            serializer2.save()
        serializer3 = PeopleSignupSerializer(data={key: request.data[key] for key in ['aadhaar_number','first_name','last_name','date_of_birth','gender','salary_pa','job','door_no','street','zip_code']})
        serializer3.is_valid(raise_exception=True)
        serializer3.save()
        serializer1.is_valid(raise_exception=True)
        serializer1.save()
        serializer4 = MobileNumberMapSignupSerializer(data={'m_aadhaar_number' if(key=='aadhaar_number') else key: request.data[key] for key in ['aadhaar_number','mobile_number']})
        serializer4.is_valid(raise_exception=True)
        serializer4.save()
        return Response({'status':'success'}, status=200)

class DepartmentViewSet(viewsets.ModelViewSet):
    
    def dDetail(self,request):
        queryset = Department.objects.get(department_id=request.data["department_id"])
        serializer = DepartmentSerializer(queryset)
        return Response(serializer.data)


class GrievanceViewSet(viewsets.ModelViewSet):
    #queryset = Grievance.objects.all()
    #serializer_class = PublicFieldSerializer
    
    def publicFeed(self, request):
        queryset = Grievance.objects.order_by("upvote").reverse()
        queryset1=queryset.values('grievance_id', 'subject','grievance','g_department_id','upvote','downvote','current_status','arg_id','pg_id')
        for g in queryset1:
            q=list(VotesList.objects.filter(a_grievance_id=g['grievance_id']).filter(g_aadhaar_number=request.data['aadhaar_number']).values('type'))
            if(len(q)==0):
                g['block']=False
                g['btype']=0
            else:
                g['block']=True
                t=q[0]['type']
                if(t=='upvote'):
                    g['btype']=1
                elif(t=='downvote'):
                    g['btype']=2
                else:
                    g['btype']=3
            g['aadhaar_number']=list(VotesList.objects.filter(a_grievance_id=g['grievance_id']).filter(type='report').values('g_aadhaar_number'))[0]['g_aadhaar_number']
            g['name']=People.objects.get(aadhaar_number=g['aadhaar_number']).first_name+" "+People.objects.get(aadhaar_number=g['aadhaar_number']).last_name
            p_zip_code=People.objects.get(aadhaar_number=g['aadhaar_number']).zip_code.zip_code
            g['city']=Address.objects.get(zip_code=p_zip_code).city
            g['state']=Address.objects.get(zip_code=p_zip_code).state
        return Response(queryset1)
    
    def gDetail(self, request):
        queryset = Grievance.objects.get(grievance_id=request.data["grievance_id"])
        serializer = PublicFieldSerializer(queryset)
        return Response(serializer.data)
    
    def departmentFeed(self, request):
        queryset = Grievance.objects.filter(g_department_id=request.data['department_id']).order_by("upvote").reverse()
        queryset1=queryset.values('grievance_id', 'subject','grievance','upvote','downvote','current_status','arg_id','pg_id')
        return Response(queryset1)
    
    def grievance(self,request):
        data=request.data.copy()
        print("===============")
        print(data)
        print(data['subject'])
        serializer1 = GrievancePostSerializer(data={key: data[key] for key in ['subject','grievance','upvote','downvote','current_status','arg','pg','g_department_id']})
        serializer1.is_valid(raise_exception=True)
        gno=serializer1.save().grievance_id
        t=Grievance.objects.get(grievance_id=gno)
        impdates={}
        impdates['i_grievance_id']=gno
        impdates['important_dates']='p-'+str(datetime.date.today())
        data['a_grievance_id']=gno
        print(data['a_grievance_id'],"======")
        if(len(str(data['pg']))!=0):
            data['pg']=gno
            if not Address.objects.filter(zip_code=data['zip_code']).exists():
                serializer2 = AddressSignupSerializer(data={key: data[key] for key in ['zip_code','city','state']})
                serializer2.is_valid(raise_exception=True)
                serializer2.save()
            serializer3 = PGrievancePostSerializer(data={ key if(key!='pg') else 'pg_id': data[key] for key in ['pg','zip_code','period']})
            serializer3.is_valid(raise_exception=True)
            #serializer3.save()
            t.pg=serializer3.save()
            t.save()
        else:
            data['arg']=gno
            serializer4 = AGrievancePostSerializer(data={key if(key!='arg') else 'arg_id': data[key] for key in ['arg','reforms_type','person_concerned']})
            serializer4.is_valid(raise_exception=True)
            #serializer4.save()
            t.arg=serializer4.save()
            t.save()
        print("------=======--------")
        serializer5 = VotesListSerializer(data={key: data[key] for key in ['g_aadhaar_number','a_grievance_id','type']})
        serializer5.is_valid(raise_exception=True)
        serializer5.save()
        serializer6 = ImportantDatesMapPostSerializer(data=impdates)
        serializer6.is_valid(raise_exception=True)
        serializer6.save()
        t1=Department.objects.get(department_id=request.data['g_department_id'])
        t1.no_of_reports=t1.no_of_reports+1
        t1.save()
        proof={}
        proof['p_grievance']=gno
        if(len(request.data['proof1'])!=0):
            proof['proofs']=request.data['proof1']
            serializer7=ProofsMapPostSerializer(data=proof)
            serializer7.is_valid(raise_exception=True)
            serializer7.save()
        if(len(request.data['proof2'])!=0):
            proof['proofs']=request.data['proof2']
            serializer7=ProofsMapPostSerializer(data=proof)
            serializer7.is_valid(raise_exception=True)
            serializer7.save()
        if(len(request.data['proof3'])!=0):
            proof['proofs']=request.data['proof3']
            serializer7=ProofsMapPostSerializer(data=proof)
            serializer7.is_valid(raise_exception=True)
            serializer7.save()
        return Response({'status':'success'}, status=200)
    
    def myGrievance(self,request):
        queryset = Grievance.objects.all()
        queryset1=queryset.values('grievance_id', 'subject','grievance','g_department_id','upvote','downvote','current_status','arg_id','pg_id')
        result=[]
        q=list(VotesList.objects.filter(type="report").filter(g_aadhaar_number=request.data['aadhaar_number']).values('a_grievance_id'))
        for g in queryset1:
            present=False
            for gg in q :
                if(gg['a_grievance_id'] is g['grievance_id']):
                    present=True
            if(present):
                g['aadhaar_number']=list(VotesList.objects.filter(a_grievance_id=g['grievance_id']).filter(type='report').values('g_aadhaar_number'))[0]['g_aadhaar_number']
                g['name']=People.objects.get(aadhaar_number=g['aadhaar_number']).first_name+" "+People.objects.get(aadhaar_number=g['aadhaar_number']).last_name
                p_zip_code=People.objects.get(aadhaar_number=g['aadhaar_number']).zip_code.zip_code
                g['city']=Address.objects.get(zip_code=p_zip_code).city
                g['state']=Address.objects.get(zip_code=p_zip_code).state
                result.append(g)
        return Response(result)

    def uGrievance(self,request):
        queryset = Grievance.objects.all()
        queryset1=queryset.values('grievance_id', 'subject','grievance','g_department_id','upvote','downvote','current_status','arg_id','pg_id')
        result=[]
        q=list(VotesList.objects.filter(type="upvote").filter(g_aadhaar_number=request.data['aadhaar_number']).values('a_grievance_id'))
        for g in queryset1:
            present=False
            for gg in q :
                if(gg['a_grievance_id'] is g['grievance_id']):
                    present=True
            if(present):
                g['aadhaar_number']=list(VotesList.objects.filter(a_grievance_id=g['grievance_id']).filter(type='report').values('g_aadhaar_number'))[0]['g_aadhaar_number']
                g['name']=People.objects.get(aadhaar_number=g['aadhaar_number']).first_name+" "+People.objects.get(aadhaar_number=g['aadhaar_number']).last_name
                p_zip_code=People.objects.get(aadhaar_number=g['aadhaar_number']).zip_code.zip_code
                g['city']=Address.objects.get(zip_code=p_zip_code).city
                g['state']=Address.objects.get(zip_code=p_zip_code).state
                result.append(g)
        return Response(result)
    
    def dGrievance(self,request):
        queryset = Grievance.objects.all()
        queryset1=queryset.values('grievance_id', 'subject','grievance','g_department_id','upvote','downvote','current_status','arg_id','pg_id')
        result=[]
        q=list(VotesList.objects.filter(type="downvote").filter(g_aadhaar_number=request.data['aadhaar_number']).values('a_grievance_id'))
        for g in queryset1:
            present=False
            for gg in q :
                if(gg['a_grievance_id'] is g['grievance_id']):
                    present=True
            if(present):
                g['aadhaar_number']=list(VotesList.objects.filter(a_grievance_id=g['grievance_id']).filter(type='report').values('g_aadhaar_number'))[0]['g_aadhaar_number']
                g['name']=People.objects.get(aadhaar_number=g['aadhaar_number']).first_name+" "+People.objects.get(aadhaar_number=g['aadhaar_number']).last_name
                p_zip_code=People.objects.get(aadhaar_number=g['aadhaar_number']).zip_code.zip_code
                g['city']=Address.objects.get(zip_code=p_zip_code).city
                g['state']=Address.objects.get(zip_code=p_zip_code).state
                result.append(g)
        return Response(result)
    
    def updateStatus(self,request):
        t=Grievance.objects.get(grievance_id=request.data['grievance_id'])
        t.current_status='resolved'
        t.save()
        return Response({'status':'success'}, status=200)
        
    
class ProofsMapViewSet(viewsets.ModelViewSet):
    
    def gProofs(self, request):
        queryset = ProofsMap.objects.filter(p_grievance_id=request.data["grievance_id"]).values('proofs')
        return Response(queryset)
    
class ImportantDatesMapViewSet(viewsets.ModelViewSet):
    
    def gDates(self, request):
        queryset = ImportantDatesMap.objects.filter(i_grievance_id=request.data["grievance_id"]).values('important_dates')
        return Response(queryset)

class MobileNumberMapViewSet(viewsets.ModelViewSet):
    
    def pMobileNo(self, request):
        queryset = MobileNumberMap.objects.filter(m_aadhaar_number=request.data["aadhaar_number"]).values('mobile_number')
        return Response(queryset)
    
class PhoneNumberMapViewSet(viewsets.ModelViewSet):
    
    def dPhoneNo(self, request):
        queryset = PhoneNumberMap.objects.filter(p_department_id=request.data["department_id"]).values('phone_number')
        return Response(queryset)
    
class VotesListViewSet(viewsets.ModelViewSet):
    
    def grievanceList(self, request):
        queryset = VotesList.objects.filter(g_aadhaar_number=request.data["aadhaar_number"]).filter(type=request.data["type"]).values('a_grievance_id')
        return Response(queryset)
    
    def vote(self,request):
        serializer = VotesListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if(request.data['type']=='upvote'):
            t=Grievance.objects.get(grievance_id=request.data['a_grievance_id'])
            t.upvote=t.upvote+1
            t.save()
        else:
            t=Grievance.objects.get(grievance_id=request.data['a_grievance_id'])
            t.downvote=t.downvote+1
            t.save()
        return Response({'status':'success'}, status=200)