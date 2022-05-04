from django.forms import ModelForm
from.models import matchs

class matchform(ModelForm):
    class Meta:
        model=matchs
        fields="__all__"

        