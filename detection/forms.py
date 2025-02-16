from django import forms


class EmailForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": 40}))
