from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import UserAddress, UserBillingAddress
from django.core.exceptions import ValidationError


class UserAddressForm(forms.ModelForm):
    default = forms.BooleanField(required=False, label='Set as default')
    class Meta:
        model = UserAddress
        fields = ['first_name', 'last_name', 'address', 'address2', 'city', 'state', 'zipcode']
    def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'first_name',
            'placeholder': 'First name',
            'type': 'text'})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'last_name',
            'placeholder': 'Last name',
            'type': 'text'})
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'name': 'address',
            'placeholder': 'Address line 1',
            'type': 'text'})
        self.fields['address2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'address',
            'placeholder': 'Address line 2',
            'type': 'text'})
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'name': 'city',
            'placeholder': 'City',
            'type': 'text'})
        self.fields['state'].widget.attrs.update({
            'class': 'form-control',
            'name': 'state',
            'placeholder': 'State',
            'type': 'text'})
        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-control',
            'name': 'zipcode',
            'placeholder': 'ZIP',
            'type': 'text'})


class UserBillingAddressForm(forms.ModelForm):
    default = forms.BooleanField(required=False, label='Set as default')
    class Meta:
        model = UserBillingAddress
        fields = ['first_name', 'last_name', 'address', 'address2', 'city', 'state', 'zipcode']
    def __init__(self, *args, **kwargs):
        super(UserBillingAddressForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'first_name',
            'placeholder': 'First name',
            'type': 'text'})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'last_name',
            'placeholder': 'Last name',
            'type': 'text'})
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'name': 'address',
            'placeholder': 'Address line 1',
            'type': 'text'})
        self.fields['address2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'address',
            'placeholder': 'Address line 2',
            'type': 'text'})
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'name': 'city',
            'placeholder': 'City',
            'type': 'text'})
        self.fields['state'].widget.attrs.update({
            'class': 'form-control',
            'name': 'state',
            'placeholder': 'State',
            'type': 'text'})
        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-control',
            'name': 'zipcode',
            'placeholder': 'ZIP',
            'type': 'text'})


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Username',
            'type': 'text'})
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'first_name',
            'placeholder': 'Your first name',
            'type': 'text'})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'last_name',
            'placeholder': 'Your last name',
            'type': 'text'})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'email@example.com',
            'type': 'text'})
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Enter password',
            'type': 'password'})
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Confirm password',
            'type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self, *args, **keyargs):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError('This email has already been registered')
        return email


class UsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Username',
            'type': 'text'})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password',
            'type': 'password'})
    
    def clean_username(self, *args, **keyargs):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('This user does not exists')
        return username

    def clean_password(self, *args, **keyargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        
        if user is not None and not user.check_password(password):
            raise forms.ValidationError('Invalid Password')
        elif user is None:
            pass
        else:
            return password

class UserPasswordResetForm(forms.Form):
    MIN_LENGTH = 8
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Username',
            'type': 'text'})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'email@example.com',
            'type': 'email'})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'New password',
            'type': 'password'})
        self.fields['confirm_password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'confirm_password',
            'placeholder': 'Confirm new password',
            'type': 'password'})

    def clean(self):
        cleaned_data = super(UserPasswordResetForm, self).clean()
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        # Check if a user has that email and password
        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            self.add_error('username', "This user does not exist")

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        # Run Djangos built in password validators
        try:
            password_validation.validate_password(password)
        except ValidationError as e:
            self.add_error('password', e)

        # Check if both passwords match
        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data


