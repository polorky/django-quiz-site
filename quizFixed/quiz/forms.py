from django import forms
from django.contrib.auth.models import User
from quiz.models import UserProfileInfo, Answer, Round

class AnswerForm(forms.ModelForm):

    round_number = forms.IntegerField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput(),max_length=50)
    quiz_number = forms.IntegerField(widget=forms.HiddenInput())

    correct1 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct2 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct3 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct4 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct5 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct6 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct7 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct8 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct9 = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    correct10 = forms.BooleanField(widget=forms.HiddenInput(), required=False)

    class Meta():
        model = Answer
        fields = ('__all__')

class AdminRoundForm(forms.ModelForm):

    round_number = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta():
        model = Round
        fields = ('round_status','round_number')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('screen_name', 'profile_pic')
