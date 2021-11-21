from django import forms


class SelectIdeaForm(forms.Form):
    id = forms.IntegerField()
