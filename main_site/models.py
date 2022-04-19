from django.db import models
from django.contrib.auth.models import AbstractUser
from .order_path import *


class UserProfile(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    ln = models.CharField(max_length=5, null=True, blank=True, default='ar')
    new_pass = models.TextField(max_length=200, null=True, blank=True)
    new_pass_as = models.BooleanField(default=True)
    address = models.TextField(max_length=256, null=True, blank=True)
    phone = models.BigIntegerField(default=0)
    national_id = models.BigIntegerField(default=0)
    profile_image = models.ImageField(upload_to=get_profile_image, blank=True, null=True)
    use_case = models.IntegerField(default=0)
    pending = models.BooleanField(default=False)
    Backup = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="UserProfile_created_by")
    updated_by = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="UserProfile_updated_by")

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ['-created_at', '-updated_at']


class Nationalities(models.Model):
    name_ar = models.CharField(max_length=49, null=True, blank=True)
    name_en = models.CharField(max_length=49, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Nationalities_created_by")
    updated_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Nationalities_updated_by")

    status = models.BooleanField(default=False)


class Systems(models.Model):
    name_ar = models.CharField(max_length=49, null=True, blank=True)
    name_en = models.CharField(max_length=49, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Systems_created_by")
    updated_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Systems_updated_by")

    teams = models.BooleanField(default=False)
    section = models.BooleanField(default=False)
    status = models.BooleanField(default=False)


class Sections(models.Model):
    system = models.ForeignKey(Systems, blank=True, null=True, on_delete=models.CASCADE, related_name="Sections_system")
    name_ar = models.CharField(max_length=49, null=True, blank=True)
    name_en = models.CharField(max_length=49, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Sections_created_by")
    updated_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Sections_updated_by")

    more_one = models.BooleanField(default=False)
    status = models.BooleanField(default=False)


class Teams(models.Model):
    system = models.ForeignKey(Systems, blank=True, null=True, on_delete=models.CASCADE, related_name="Teams_system")
    section = models.ForeignKey(Sections, blank=True, null=True, on_delete=models.CASCADE, related_name="Teams_section")
    name_ar = models.CharField(max_length=49, null=True, blank=True)
    name_en = models.CharField(max_length=49, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Teams_created_by")
    updated_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Teams_updated_by")

    status = models.BooleanField(default=False)


class Army(models.Model):
    name_ar = models.CharField(max_length=49, null=True, blank=True)
    name_en = models.CharField(max_length=49, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Army_created_by")
    updated_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Army_updated_by")

    status = models.BooleanField(default=False)


class Student(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Student_user")
    religion = models.TextField(max_length=10, blank=True, null=True)
    social_status = models.TextField(max_length=10, blank=True, null=True)
    date_birth = models.DateField(auto_now=False, blank=True, null=True)
    nationality = models.ForeignKey(Nationalities, blank=True, null=True, on_delete=models.CASCADE, related_name="Student_nationality")
    educational_qualification = models.TextField(max_length=40, blank=True, null=True)
    total_qualification = models.FloatField(default=0, blank=True, null=True)
    recording_type = models.TextField(max_length=10, blank=True, null=True)
    transfer_destination = models.TextField(max_length=200, blank=True, null=True)
    student_type = models.TextField(max_length=10, blank=True, null=True)
    army_status = models.TextField(max_length=10, blank=True, null=True)
    system = models.ForeignKey(Systems, blank=True, null=True, on_delete=models.CASCADE, related_name="Student_system")
    team = models.ForeignKey(Teams, blank=True, null=True, on_delete=models.CASCADE, related_name="Student_team")

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Student_created_by")
    updated_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE, related_name="Student_updated_by")

    status = models.BooleanField(default=False)