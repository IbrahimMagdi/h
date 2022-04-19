"""
    Create by Ahmad Ibrahim 
    at ١٢‏/٣‏/٢٠٢٢ - ١٢:٣١ ص
"""
from main_site.models import Teams, Systems
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def add_fun(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser:
        ln = request.user.ln
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
                Teams.objects.create(
                    name_ar=name_ar,
                    name_en=name_en,
                    system=get_sys,
                    status=status,
                    created_by=request.user,
                ).save()
                re_status = 201
                if ln == 'ar':
                    re_message = 'تمت الاضافة بنجاح'
                else:
                    re_message = 'Added successfully'
                re_data = None
        else:
            re_status = 103
            if ln == 'ar':
                re_message = 'لم يتم العثور علي النظام !'
            else:
                re_message = 'Systems is not found !'
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
