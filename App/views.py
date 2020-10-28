from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SignInSerializer
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

class SignInViewSet(viewsets.ModelViewSet):
    queryset = SignIn.objects.all()
    serializer_class = SignInSerializer
    
    def list(self, request):
        queryset = SignIn.objects.all()
        serializer = SignInSerializer(queryset, many=True)
        return Response(serializer.data)
    
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
            print("==============")
            print(serializer.data)
            return Response({'status':'success','msg':'a'+serializer.data["aadhaar_number"]},status=200)