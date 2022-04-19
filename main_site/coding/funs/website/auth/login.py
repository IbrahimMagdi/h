from main_site.models import *
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



@csrf_exempt
def login_fun(request):
    if not request.user.is_authenticated:
        try:
            username = request.POST.get('username').strip()
        except:
            username = ''
        print(int(username))
        password = str(request.POST.get('password').strip().lower())
        try:
            get_user = UserProfile.objects.get(username=username.lower())
        except:
            try:
                get_user = UserProfile.objects.get(email=username.lower())
            except:
                try:
                    get_user = UserProfile.objects.get(phone=int(username))
                except:
                    get_user = None
        if len(str(username).strip()) == 0:
            re_status = 103
            re_message = 'الرجاء ادخال البريد الإلكتروني او الكود او رقم الموبايل'
            re_data = None
        elif len(str(password).strip()) == 0:
            re_status = 103
            re_message = 'الرجاء ادخال كلمة السر'
            re_data = None
        elif get_user is None:
            re_status = 103
            re_message = 'لم يتم العثور علي حسابك !'
            re_data = None
        else:
            user = authenticate(username=get_user.username, password=password, backend='django.contrib.auth.backends.ModelBackend')
            if user:
                if get_user.is_active:
                    auth_login(request, get_user, backend='django.contrib.auth.backends.ModelBackend')
                    re_status = 201
                    re_message = 'تم تسجيل الدخول بنجاح'
                    if get_user.is_staff or get_user.is_superuser:
                        re_data = '/dashboard/'
                    elif get_user.is_student:
                        re_data = '/my-profile/'
                    else:
                        re_data = '/'
                else:
                    re_status = 103
                    re_message = 'حسابك ممنوع من تسجيل الدخول'
                    re_data = True
            else:
                re_status = 103
                re_message = 'كلمة السر غير صحيحة'
                re_data = True
    else:
        re_status = 103
        re_message = 'انت قيد تسجيل الدخول بالفعل'
        re_data = None
    send_object = {
        're_status': re_status,
        're_message': re_message,
        're_data': re_data,
    }
    return JsonResponse(send_object)
