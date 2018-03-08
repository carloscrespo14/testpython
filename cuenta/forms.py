from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
        }