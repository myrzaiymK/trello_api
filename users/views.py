from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from .utils import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, "users/dashboard.html")


# def login(request):
#     return render(request, 'registration/login.html')


@login_required
def home(request):
    return render(request, 'users/dashboard.html')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('dashboard')
    else:
        messages.error(request, "Activation link is invalid.")
    return redirect('dashboard')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("registration/confirm/activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on\
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed correctly.')


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = CustomUserCreationForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={'form': form}
    )
