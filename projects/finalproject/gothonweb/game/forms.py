from django import forms

class RoomForm(forms.Form):
	answer = forms.CharField(label="answer", max_length=250)