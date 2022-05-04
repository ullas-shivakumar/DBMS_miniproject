from django.forms import ModelForm
from.models import organiser

class organiserform(ModelForm):
    class Meta:
        model=organiser
        fields="__all__"

        