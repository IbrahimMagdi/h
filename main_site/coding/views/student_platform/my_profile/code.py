"""
    Create by Ahmad Ibrahim
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render, redirect
from codes_source.settings import *
from main_site.models import UserProfile, Student


def my_profile_web(request):
    if request.user.is_authenticated:
        get_ln = request.GET.get('ln')
        user_object = UserProfile.objects.get(id=request.user.id)
        user_student = Student.objects.get(user=request.user)
        send_data = {
            'nameSite': nameSite['ar'],
            'user_object': user_object,
            'user_student': user_student,
        }
        return render(request, 'student_platform/my_profile/main.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')