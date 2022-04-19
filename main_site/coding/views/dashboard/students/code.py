"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render, redirect
from codes_source.settings import *
from main_site.models import UserProfile as Students, Student, Nationalities, Systems, Teams
from django.http import Http404


def all_web(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        get_items = Students.objects.filter(is_student=True)
        items = []
        for item in get_items:
            get_student = Student.objects.get(user=item)
            send_item = {
                'id': item.id,
                'username': item.username,
                'email': item.email,
                'name': item.first_name,
                'pending': item.pending,
                'system': get_student.system.name_ar,
                'team': get_student.team.name_ar,
                'created_at': item.created_at,
                'created_by': item.created_by,
                'updated_at': item.updated_at,
                'updated_by': item.updated_by,
            }
            items.append(send_item)
        send_data = {
            'nameSite': nameSite[get_ln],
            'items': items
        }
        return render(request, 'pages/dashboard/students/all/{}.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')


def add_web(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        get_nationalities = Nationalities.objects.filter(status=True)
        get_systems = Systems.objects.filter(status=True)
        send_data = {
            'nameSite': nameSite[get_ln],
            'get_nationalities': get_nationalities,
            'get_systems': get_systems,
        }
        return render(request, 'pages/dashboard/students/add/{}.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')


def edit_web(request, id):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        try:
            item = Students.objects.get(id=id)
        except:
            item = None
        if item:
            get_systems = Systems.objects.filter(status=True)
            get_student = Student.objects.get(user=item)
            get_team = Teams.objects.filter(system_id=get_student.system.id, status=True)
            get_nationalities = Nationalities.objects.filter(status=True)
            send_data = {
                'nameSite': nameSite[get_ln],
                'get_systems': get_systems,
                'system_id': get_student.system.id,
                'team_id': get_student.team.id,
                'army_status': int(get_student.army_status),
                'student_type': int(get_student.student_type),
                'recording_type': int(get_student.recording_type),
                'religion': int(get_student.religion),
                'social_status': int(get_student.social_status),
                'educational_qualification': int(get_student.educational_qualification),
                'item': item,
                'get_team': get_team,
                'nationalities_id': get_student.nationality.id,
                'get_nationalities': get_nationalities,
            }
            return render(request, 'pages/dashboard/students/edit/{}.html'.format(get_ln), send_data)
        else:
            raise Http404
    else:
        return redirect('login_web')
