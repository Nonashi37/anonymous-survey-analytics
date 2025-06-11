from django.db import models


class AnalyticsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=300)
    survey = models.ForeignKey('AnalyticsSurvey', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'analytics_question'


class AnalyticsStudent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    academic_year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_student'


class AnalyticsSurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'analytics_survey'


class AnalyticsSurveyresponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    response = models.IntegerField()
    question = models.ForeignKey(AnalyticsQuestion, models.DO_NOTHING)
    student = models.ForeignKey(AnalyticsStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'analytics_surveyresponse'


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
    course = models.ForeignKey(Course, models.DO_NOTHING)
    faculty = models.TextField()
    academic_year = models.TextField()
    study_mode = models.TextField()

    class Meta:
        managed = False
        db_table = 'course_assignment'
        unique_together = (('course', 'faculty', 'academic_year', 'study_mode'),)


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
    question = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
    text = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    option_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'question_option'
        unique_together = (('question', 'option_order'),)


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
    student = models.ForeignKey(Student, models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    enrolled_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'student_course'
        unique_together = (('student', 'course'),)


class Survey(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
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
    prepod_id = Professor()
    anonymous_id = models.CharField(max_length=255, primary_key=True)
    question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)
    survey = models.ForeignKey(Survey, models.DO_NOTHING)
    content = models.TextField()
    response_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_response'

