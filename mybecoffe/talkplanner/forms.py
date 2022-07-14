from django import forms
from .models import Talks

class TalkForm(forms.ModelForm):
	class Meta:
		model = Talks
		fields="__all__"