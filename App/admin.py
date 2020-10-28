from django.contrib import admin
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

admin.site.register(SignIn)
admin.site.register(People)
admin.site.register(Department)
admin.site.register(Grievance)
admin.site.register(ProofsMap)
admin.site.register(PhoneNumberMap)
admin.site.register(MobileNumberMap)
admin.site.register(ImportantDatesMap)
admin.site.register(Address)
admin.site.register(AdministrativeReforms)
admin.site.register(Public)
admin.site.register(VotesList)