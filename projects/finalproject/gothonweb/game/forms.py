from django import forms

class RoomForm(forms.Form):
	room = forms.CharField(label="answer", max_length=250)