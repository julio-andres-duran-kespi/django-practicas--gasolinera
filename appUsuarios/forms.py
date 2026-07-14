from django.contrib.auth.forms import UserCreationForm
from  appUsuarios.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
        