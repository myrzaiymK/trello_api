# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)
from django import forms



from django.contrib.auth.forms import UserCreationForm


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ("email", )


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = [
            "username",
            "email",
        ]
