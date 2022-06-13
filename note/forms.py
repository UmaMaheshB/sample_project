from django.forms import ModelForm
from .models import *

class NoteModelForm(ModelForm):
	class Meta:
		model = Note
		fields = "__all__"