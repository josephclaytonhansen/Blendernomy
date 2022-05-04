from django import forms
from django.conf import settings
from django.core.mail import send_mail
import environ, re
from .models import ProductKey
from captcha.fields import CaptchaField

def frog(b):
    env = environ.Env()
    environ.Env.read_env()
    c = env('FROG').split(".")
    a = re.sub("[^a-zA-Z0-9]", "", b).lower().strip()[:48]
    r = a
    a_s = []
    for s in a:
        if s in c:
            a_s.append(c.index(s))
        else:
            a_s.append(int(s))
    a = a_s  
    if len(a) % 2 != 0:
        a.pop()
    g = "e"
    d = []
    for i in range(0, len(a)-2):
        if i % 3 != 0:
            if g == "e":
                d.append(a[i] + a[i + 2])
                g = "f"
            if g == "f":
                d.append(abs(a[i] - a[i + 2]))
                g = "e"
        else:
            if g == "e":
                d.insert(0, a[i] + a[i + 2])
                g = "f"
            if g == "f":
                d.insert(0, abs(a[i] - a[i + 2]))
                g = "e"
    a_s = ""
    for s in d:
        a_s += str(s)
    j = a_s[0:7]
    k = a_s[len(a_s)-25:len(a_s)-11]
    o = a_s[12:15]
    p = a_s[8:11]
    m = ""
    for l in range(0, len(k)-1):
                m+= c[int(k[l])]
    q=r[0]+j+m+o+str(int(o)+int(p))+p+r[10]
    return q

class KeyValidator(forms.Form):
    email = forms.EmailField()
   
class ContactForm(forms.Form):
    captcha = CaptchaField()
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')
        
        spam_names = ["HenryjiP"]
        spam = False
        for n in spam_names:
            if n in name:
                spam = True
        if not spam:
            return subject, msg
        else:
            return 0,0

    def send(self):

        subject, msg = self.get_info()
        #b = super().clean().get('email')
        #q = frog(b) 
        #key,created = ProductKey.objects.get_or_create( email=b, key=q)
        #msg = msg + q

        if subject != 0 and msg != 0:
            send_mail(
                subject=subject,
                message=msg,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.RECIPIENT_ADDRESS]
            )
        
        