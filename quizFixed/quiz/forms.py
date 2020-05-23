from django import forms
from django.contrib.auth.models import User
from quiz.models import UserProfileInfo, Answer

class AnswerForm(forms.ModelForm):

    round_number = forms.IntegerField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput(),max_length=50)

    class Meta():
        model = Answer
        fields = ('__all__')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('screen_name', 'profile_pic')
