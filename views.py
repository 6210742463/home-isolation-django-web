from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, get_user_model
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# automail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')
        repassword = data.get('repassword')
        status = data.get('status')
        if password == repassword:
            user = User.objects.create_user(username = username, password = password)
            s = Status(user = user, status = status)
            s.save()
            return redirect('/success')
        else:
            return redirect('/')
    return render(request, 'member/register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            status = Status.objects.get(user = user)
            if str(status.status) == 'petient':
                login(request, user)
                return redirect('/petient')
            elif str(status.status) == 'doctor':
                login(request, user)
                return redirect('/doctor')
    else:
        form = AuthenticationForm()
    return render(request, 'member/login.html', {
        'form':form,
    })

def success(request):
    return render(request, 'member/success.html')

@login_required(login_url='/login')
def petient(request):
    return render(request, 'member/petient.html')

@login_required(login_url='/login')
def doctor(request):
    return render(request, 'member/doctor.html')

@login_required(login_url='/login')
def history(request,id):
    getData = PulseDairy.objects.get(pk=id)
    return render(request, 'pulse/history.html',{'data': getData})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def dairy_pulse(request):
    if request.method == 'POST':
        username = request.user
        data = request.POST.copy()
        spo2 = data.get("spo2")
        temp = data.get("temp")
        beat = data.get("beat")
        gs1 = data.get("gs1")
        gs2 = data.get("gs2")
        gs3 = data.get("gs3")
        gs4 = data.get("gs4")
        gs5 = data.get("gs5")
        ys1 = data.get("ys1")
        ys2 = data.get("ys2")
        ys3 = data.get("ys3")
        ys4 = data.get("ys4")
        rs1 = data.get("rs1")
        rs2 = data.get("rs2")
        rs3 = data.get("rs3")

        new_dairy_pulse = PulseDairy(user = username,
                        spo2 = spo2,
                        temp = temp,
                        beat = beat,
                        gs1 = gs1,
                        gs2 = gs2,
                        gs3 = gs3,
                        gs4 = gs4,
                        gs5 = gs5,
                        ys1 = ys1,
                        ys2 = ys2,
                        ys3 = ys3,
                        ys4 = ys4,
                        rs1 = rs1,
                        rs2 = rs2,
                        rs3 = rs3)
        new_dairy_pulse.save()

        gs_list = [gs1,gs2,gs3,gs4,gs5]
        ys_list = [ys1,ys2,ys3,ys4]
        rs_list = [rs1,rs2,rs3]

        return sendpulse(request, gs_list, ys_list, rs_list, username)
    return render(request, 'pulse/dairypulse.html')

@login_required(login_url='/login')
def sendpulse(request, gs, ys, rs, username):
    if rs != [None, None, None]:
        color = 'danger'
        sendmail(username, 'สีแดง')
        return render(request, 'pulse/sendpulse.html', {'color': color})
    elif ys != [None, None, None, None]:
        color = 'warning'
        sendmail(username, 'สีเหลือง')
        return render(request, 'pulse/sendpulse.html', {'color': color})
    else:
        color = 'success'
        return render(request, 'pulse/sendpulse.html', {'color': color})

def sendmail(username, color):
    MY_EMAIL = 'yout_mail'
    MY_PASSWORD = 'yout_password'
    emailTo = ''
    
    msg = MIMEMultipart ()
    msg.attach(MIMEText ('<html> <body> <p> ผู้ป่วย ' + str(username) +  ' อยู่ในระดับ ' + str(color) +  '</p> </body> </html>', 'html', 'utf-8'))

    msg['Subject'] = "แจ้งเตือนความอันตรายของอาการผู้ป่วย"
    msg['From'] = 'Home Isolation application'
    msg['To'] = emailTo

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()

    s.login(MY_EMAIL, MY_PASSWORD)
    s.sendmail(MY_EMAIL, emailTo.split(','), msg.as_string())
    s.quit()


def reserve(request):
    if request.method == 'POST':
        return redirect('/success-reserve') 
    return render(request, 'reserve/reserve.html', {})

def s_reserve(request):
    return render(request, 'reserve/success-reserve.html')

def petient_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'member/petientlist.html',{'user':users})
