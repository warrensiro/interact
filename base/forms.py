from django.forms import ModelForm
from .models import Room, User, Message
from django.contrib.auth.forms import UserCreationForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avatar', 'bio']


class NewUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
