# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    zip_code = models.IntegerField(db_column='Zip_code', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class AdministrativeReforms(models.Model):
    arg_id = models.IntegerField(db_column='ARG_ID', primary_key=True)  # Field name made lowercase.
    reforms_type = models.CharField(db_column='Reforms_type', max_length=30)  # Field name made lowercase.
    person_concerned = models.CharField(db_column='Person_concerned', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrative_reforms'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Department(models.Model):
    department_id = models.CharField(db_column='Department_ID', primary_key=True, max_length=12)  # Field name made lowercase.
    department_name = models.CharField(db_column='Department_name', max_length=30)  # Field name made lowercase.
    bio = models.CharField(db_column='Bio', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo = models.TextField(db_column='Photo')  # Field name made lowercase.
    dep_street = models.CharField(db_column='Dep_street', max_length=45)  # Field name made lowercase.
    d_zip_code = models.ForeignKey(Address, models.DO_NOTHING, db_column='D_Zip_code')  # Field name made lowercase.
    no_of_reports = models.IntegerField(db_column='No_of_reports')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Grievance(models.Model):
    grievance_id = models.AutoField(db_column='Grievance_ID', primary_key=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=30)  # Field name made lowercase.
    grievance = models.CharField(db_column='Grievance', max_length=200)  # Field name made lowercase.
    upvote = models.IntegerField(db_column='Upvote')  # Field name made lowercase.
    downvote = models.IntegerField(db_column='Downvote')  # Field name made lowercase.
    current_status = models.CharField(db_column='Current_status', max_length=20)  # Field name made lowercase.
    arg = models.ForeignKey(AdministrativeReforms, models.DO_NOTHING, db_column='ARG_ID', blank=True, null=True)  # Field name made lowercase.
    pg = models.ForeignKey('Public', models.DO_NOTHING, db_column='PG_ID', blank=True, null=True)  # Field name made lowercase.
    g_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='G_Department_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grievance'


class ImportantDatesMap(models.Model):
    i_grievance = models.ForeignKey(Grievance, models.DO_NOTHING, db_column='I_Grievance_ID')  # Field name made lowercase.
    important_dates = models.CharField(db_column='Important_dates', unique=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'important_dates_map'


class MobileNumberMap(models.Model):
    m_aadhaar_number = models.ForeignKey('People', models.DO_NOTHING, db_column='M_Aadhaar_number')  # Field name made lowercase.
    mobile_number = models.CharField(db_column='Mobile_number', unique=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mobile_number_map'


class People(models.Model):
    aadhaar_number = models.CharField(db_column='Aadhaar_number', primary_key=True, max_length=12)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=20)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=20)  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date_of_birth')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=15)  # Field name made lowercase.
    salary_pa = models.IntegerField(db_column='Salary_pa')  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=45)  # Field name made lowercase.
    door_no = models.CharField(db_column='Door_no', max_length=10)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=45)  # Field name made lowercase.
    p_zip_code = models.ForeignKey(Address, models.DO_NOTHING, db_column='P_Zip_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'people'


class PhoneNumberMap(models.Model):
    p_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='P_Department_ID')  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', unique=True, max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phone_number_map'


class ProofsMap(models.Model):
    p_grievance = models.ForeignKey(Grievance, models.DO_NOTHING, db_column='P_Grievance_ID')  # Field name made lowercase.
    proofs = models.CharField(db_column='Proofs', unique=True, max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proofs_map'


class Public(models.Model):
    pg_id = models.IntegerField(db_column='PG_ID', primary_key=True)  # Field name made lowercase.
    zip_code = models.ForeignKey(Address, models.DO_NOTHING, db_column='Zip_code')  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'public'


class SignIn(models.Model):
    email_id = models.CharField(db_column='Email_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    aadhaar_number = models.ForeignKey(People, models.DO_NOTHING, db_column='Aadhaar_number', blank=True, null=True)  # Field name made lowercase.
    department_id = models.ForeignKey(Department, models.DO_NOTHING, db_column='Department_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sign_in'


class VotesList(models.Model):
    g_aadhaar_number = models.OneToOneField(People, models.DO_NOTHING, db_column='G_Aadhaar_number', primary_key=True)  # Field name made lowercase.
    a_grievance = models.ForeignKey(Grievance, models.DO_NOTHING, db_column='A_Grievance_ID')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'votes_list'
        unique_together = (('g_aadhaar_number', 'a_grievance'),)
