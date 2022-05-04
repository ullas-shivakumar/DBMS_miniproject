from django.forms import ModelForm
from .models import tournament 

class tournamentform(ModelForm):
    class Meta:
        model=tournament
        fields=['tournament_name','game','winner_prize','runner_prize','entry_fee']

        