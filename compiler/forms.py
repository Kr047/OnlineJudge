from django import forms
from compiler.models import CodeSubmission

language_choices = [
    ("py","Python"),
    ("c","C"),
    ("cpp","C++")
]

class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=language_choices)

    class Meta:
        model = CodeSubmission
        fields = ["language","code","input_data"]