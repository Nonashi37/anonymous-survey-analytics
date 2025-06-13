# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    professor = models.ForeignKey('Professor', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course'


class CourseAssignment(models.Model):
    pk = models.CompositePrimaryKey('course_id', 'faculty', 'academic_year', 'study_mode')
    course = models.ForeignKey(Course, models.DO_NOTHING)
    faculty = models.TextField()
    academic_year = models.TextField()
    study_mode = models.TextField()

    class Meta:
        managed = False
        db_table = 'course_assignment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class FlywaySchemaHistory(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'flyway_schema_history'


class Professor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    avatar_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'


class QuestionOption(models.Model):
    pk = models.CompositePrimaryKey('question_id', 'option_order')
    question = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
    text = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    option_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'question_option'


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    gender = models.TextField()
    faculty = models.TextField()
    academic_year = models.TextField()
    mode_of_study = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'student'


class StudentCourse(models.Model):
    pk = models.CompositePrimaryKey('student_id', 'course_id')
    student = models.ForeignKey(Student, models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    enrolled_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'student_course'


class Survey(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.TextField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'


class SurveyQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey = models.ForeignKey(Survey, models.DO_NOTHING)
    text = models.CharField(max_length=255)
    question_type = models.TextField()
    question_category = models.TextField()
    question_order = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveyResponse(models.Model):
    pk = models.CompositePrimaryKey('anonymous_id', 'question_id', 'survey_id')
    anonymous_id = models.CharField(max_length=255)
    question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)
    survey = models.ForeignKey(Survey, models.DO_NOTHING)
    professor_id = models.BigIntegerField()
    content = models.TextField()
    response_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_response'
