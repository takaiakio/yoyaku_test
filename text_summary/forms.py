from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='入力テキスト')
