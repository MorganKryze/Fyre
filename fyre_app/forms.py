from django import forms

class PlotForm(forms.Form):
    title = forms.CharField(label='Plot title', max_length=100)