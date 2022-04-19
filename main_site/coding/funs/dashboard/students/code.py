"""
    Create by Ahmad Ibrahim 
    at ١٢‏/٣‏/٢٠٢٢ - ١٢:٣١ ص
"""
from main_site.models import Teams, Systems, Nationalities, UserProfile, Student
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
import string


@csrf_exempt
def add_fun(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser:
        ln = request.user.ln
        try:
            name = request.POST.get('name').strip()
        except:
            name = ''
        try:
            national_id = int(request.POST.get('national_iD'))
        except:
            national_id = ''
        try:
            national_else = UserProfile.objects.get(national_id=national_id)
        except:
            national_else = None
        try:
            address = request.POST.get('address').strip()
        except:
            address = ''
        try:
            religion = request.POST.get('religion').strip()
        except:
            religion = ''
        try:
            social_status = request.POST.get('social_status').strip()
        except:
            social_status = ''
        try:
            date_birth = request.POST.get('date_birth').strip()
        except:
            date_birth = ''
        try:
            nationality_id = request.POST.get('nationality').strip()
            nationality = Nationalities.objects.get(id=nationality_id)
        except:
            nationality = ''
        try:
            educational_qualification = request.POST.get('educational_qualification').strip()
        except:
            educational_qualification = ''
        try:
            total_qualification = request.POST.get('total_qualification').strip()
        except:
            total_qualification = ''
        try:
            recording_type = request.POST.get('recording_type').strip()
        except:
            recording_type = ''
        try:
            transfer_destination = request.POST.get('transfer_destination').strip()
        except:
            transfer_destination = ''
        try:
            student_type = request.POST.get('student_type').strip()
        except:
            student_type = ''
        try:
            army_status = request.POST.get('army_status').strip()
        except:
            army_status = ''
        try:
            system_id = request.POST.get('systems').strip()
            system = Systems.objects.get(id=system_id)
        except:
            system = ''
        try:
            teams_id = request.POST.get('teams').strip()
            team = Teams.objects.get(id=teams_id)
        except:
            team = ''
        try:
            phone = int(request.POST.get('phone'))
        except:
            phone = ''
        try:
            email = request.POST.get('email').lower().strip()
        except:
            email = ''
        # name
        if len(str(name)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'برجاء ادخال اسم الطالب '
            else:
                re_message = 'Please enter the student\'s name'
            re_data = None
        elif len(str(name)) < 10:
            re_status = 103
            if ln == 'ar':
                re_message = 'اسم الطالب قصير جدا'
            else:
                re_message = 'The student\'s name is too short'
            re_data = None
        elif len(str(name)) > 100:
            re_status = 103
            if ln == 'ar':
                re_message = 'اسم الطالب كبير جدا'
            else:
                re_message = 'The student\'s name is too big'
            re_data = None
        # national_id
        elif national_else is not None:
            re_status = 103
            if ln == 'ar':
                re_message = 'هذا الطالب مسجل من قبل'
            else:
                re_message = 'This student is already registered'
            re_data = None
        elif len(str(national_id)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء إدخال الرقم القومي للطالب'
            else:
                re_message = 'Please enter the student\'s national number'
            re_data = None
        elif len(str(national_id)) < 10:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرقم القومي قصير جدا'
            else:
                re_message = 'The national number is too short'
            re_data = None
        elif len(str(national_id)) > 15:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرقم القومي كبير جدا'
            else:
                re_message = 'The national number is too big'
            re_data = None
        # address
        elif len(str(address)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء إدخال العنوان'
            else:
                re_message = 'Please enter the address'
            re_data = None
        elif len(str(address)) < 10:
            re_status = 103
            if ln == 'ar':
                re_message = 'العنوان قصير جدا'
            else:
                re_message = 'The address is too short'
            re_data = None
        elif len(str(address)) > 100:
            re_status = 103
            if ln == 'ar':
                re_message = 'العنوان كبير جدا'
            else:
                re_message = 'The address is too big'
            re_data = None
        # date_birth
        elif len(str(date_birth)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء تحديد تاريخ ميلاد الطالب'
            else:
                re_message = 'Please select the student\'s date of birth'
            re_data = None
        # nationality
        elif len(str(nationality)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء تحديد تاريخ الجنسية'
            else:
                re_message = 'Please select the date of nationality'
            re_data = None
        elif len(str(total_qualification)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء ادخال مجموع الطالب'
            else:
                re_message = 'Please enter the student\'s total'
            re_data = None
        elif len(str(total_qualification)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء ادخال مجموع الطالب'
            else:
                re_message = 'Please enter the student\'s total'
            re_data = None
        elif recording_type == '1' and len(str(transfer_destination)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء ادخال جهة التحويل'
            else:
                re_message = 'Please enter the transfer destination'
            re_data = None
        elif len(str(system)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء تحديد نظام الالتحاق'
            else:
                re_message = 'Please select enrollment system'
            re_data = None
        elif len(str(team)) == 0:
            re_status = 103
            if ln == 'ar':
                re_message = 'الرجاء تحديد الفرقة الدراسية'
            else:
                re_message = 'Please select enrollment team'
            re_data = None
        else:
            username = ''
            password = ''.join(random.sample(string.ascii_lowercase, 12))
            get_username = True
            while get_username:
                new_username = ''.join(random.sample(string.ascii_lowercase, 8))
                try:
                    get_user = UserProfile.objects.get(username=new_username.lower())
                except:
                    username = new_username.lower()
                    break
            create_user = UserProfile.objects.create_user(
                first_name=name,
                username=username,
                password=password.lower(),
                new_pass=password.lower(),
                is_student=True,
                new_pass_as=True,
                address=address,
                email=email,
                phone=phone,
                national_id=national_id,
                pending=True,
                created_by=request.user,
            )
            create_user.save()
            create_student = Student.objects.create(
                user=create_user,
                religion=religion,
                social_status=social_status,
                date_birth=date_birth,
                nationality=nationality,
                educational_qualification=educational_qualification,
                total_qualification=total_qualification,
                recording_type=recording_type,
                transfer_destination=transfer_destination,
                student_type=student_type,
                army_status=army_status,
                system=system,
                team=team,
                created_at=request.user
            )
            create_student.save()
            re_status = 201
            re_message = 'تم اضافة الطالب بنجاح'
            re_data = None
    else:
        re_status = 104
        re_message = None
        re_data = None
    send_object = {
        're_status': re_status,
        're_message': re_message,
        're_data': re_data,
    }
    return JsonResponse(send_object)


@csrf_exempt
def edit_fun(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser:
        id = request.POST.get('id')
        ln = request.user.ln
        try:
            item = Teams.objects.get(id=id)
        except:
            item = None
        if item:
            try:
                name_ar = request.POST.get('name_ar').strip()
            except:
                name_ar = ''
            try:
                name_en = request.POST.get('name_en').strip()
            except:
                name_en = ''
            status = request.POST.get('status')
            type_ = request.POST.get('type')
            try:
                get_sys = Systems.objects.get(id=type_)
            except:
                get_sys = None
            if get_sys:
                if status == 'on':
                    status = True
                else:
                    status = False
                # name_ar
                if len(str(name_ar)) == 0:
                    re_status = 103
                    if ln == 'ar':
                        re_message = 'برجاء ادخال اسم النظام باللغة العربية'
                    else:
                        re_message = 'Please enter the name of the systems in Arabic'
                    re_data = None
                elif len(str(name_ar)) < 2:
                    re_status = 103
                    if ln == 'ar':
                        re_message = 'اسم النظام باللغة العربية قصير جدا'
                    else:
                        re_message = 'The name of the systems in Arabic is too short'
                    re_data = None
                elif len(str(name_ar)) > 48:
                    re_status = 103
                    if ln == 'ar':
                        re_message = 'اسم النظام باللغة العربية كبير جدا'
                    else:
                        re_message = 'The name of the systems in Arabic is too big'
                    re_data = None
                # name_en
                elif len(str(name_en)) == 0:
                    re_status = 103
                    if ln == 'ar':
                        re_message = 'برجاء ادخال اسم النظام الإنجليزية العربية'
                    else:
                        re_message = 'Please enter the name of the systems in English'
                    re_data = None
                elif len(str(name_en)) < 2:
                    re_status = 103
                    if ln == 'ar':
                        re_message = 'اسم النظام باللغة الإنجليزية قصير جدا'
                    else:
                        re_message = 'The name of the systems in English is too short'
                    re_data = None
                elif len(str(name_en)) > 48:
                    re_status = 103
                    if ln == 'ar':
                        re_message = 'اسم النظام باللغة الإنجليزية كبير جدا'
                    else:
                        re_message = 'The name of the systems in English is too big'
                    re_data = None
                else:
                    item.name_ar = name_ar
                    item.name_en = name_en
                    item.system = get_sys
                    item.status = status
                    item.updated_by = request.user
                    item.save()
                    re_status = 201
                    if ln == 'ar':
                        re_message = 'تم التحديث بنجاح'
                    else:
                        re_message = 'Updated successfully'
                    re_data = None
            else:
                re_status = 103
                if ln == 'ar':
                    re_message = 'لم يتم العثور علي النظام !'
                else:
                    re_message = 'Systems is not found !'
                re_data = None
        else:
            re_status = 103
            if ln == 'ar':
                re_message = 'لم يتم العثور علي هذا العنصر ! '
            else:
                re_message = 'This item was not found!'
            re_data = None
    else:
        re_status = 104
        re_message = None
        re_data = None
    send_object = {
        're_status': re_status,
        're_message': re_message,
        're_data': re_data,
    }
    return JsonResponse(send_object)


@csrf_exempt
def get_team_fun(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser:
        id = request.POST.get('id')
        ln = request.user.ln
        get_teams = Teams.objects.filter(system__id=id, status=True)
        all_teams = []
        for team in get_teams:
            if ln == 'en':
                name = team.name_en
            else:
                name = team.name_ar
            send_team = {
                'id': team.id,
                'name': name,
            }
            all_teams.append(send_team)
        re_status = 201
        re_message = None
        re_data = all_teams
    else:
        re_status = 104
        re_message = None
        re_data = None
    send_object = {
        're_status': re_status,
        're_message': re_message,
        're_data': re_data,
    }
    return JsonResponse(send_object)
