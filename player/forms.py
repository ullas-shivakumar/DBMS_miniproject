from django.forms import ModelForm
from .models import team,player,invitation

class teamform(ModelForm):
    class Meta:
        model=team
        fields= ['team_id','team_name','game','no_players','tournament_id']

class playerform(ModelForm):
    class Meta:
        model=player
        fields="__all__"

class invitationform(ModelForm):
    class Meta:
        model=player
        fields="__all__"
        