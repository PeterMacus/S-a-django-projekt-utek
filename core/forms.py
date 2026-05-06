from django import forms
from .models import Student, Team, Competition

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['meno', 'priezvisko', 'trieda', 'email']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['nazov_timu', 'popis', 'veduci_timu']

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['nazov_sutaze', 'miesto', 'datum', 'typ']