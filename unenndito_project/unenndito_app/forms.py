from django import forms
from django.forms import ModelForm
from .models import UserRegistration

    

CATEGORIES_CHOICES = [
    ('', ''),
    ('Abak', 'Abak'),
    ('Eastern Obolo', 'Eastern Obolo'),
    ('Eket', 'Eket'),
    ('Esit Eket', 'Esit Eket'),
    ('Essien Udim', 'Essien Udim'),
    ('Etim Ekpo', 'Etim Ekpo'),
    ('Etinan', 'Etinan'),
    ('Ibeno', 'Ibeno'),
    ('Ibesikpo Asutan', 'Ibesikpo Asutan'),
    ('Ibiono Ibom', 'Ibiono Ibom'),
    ('Ika', 'Ika'),
    ('Ikono', 'Ikono'),
    ('Ikot Abasi', 'Ikot Abasi'),
    ('Ikot Ekpene', 'Ikot Ekpene'),
    ('Ini', 'Ini'),

    ('Itu', 'Itu'),
    ('Mbo', 'Mbo'),
    ('Mkpat Enin', 'Mkpat Enin'),
    ('Nsit Atai', 'Nsit Atai'),
    ('Nsit Ibom', 'Nsit Ibom'),
    ('Nsit Ubium', 'Nsit Ubium'),
    ('Obot Akara', 'Obot Akara'),
    ('Okobo', 'Okobo'),
    ('Onna', 'Onna'),
    ('Oron', 'Oron'),
    ('Oruk Anam', 'Oruk Anam'),
    ('Udung Uko', 'Udung Uko'),
    ('Ukanafun', 'Ukanafun'),
    ('Uruan', 'Uruan'),
    ('Urue-Offong/Oruko', 'Urue-Offong/Oruko'),
    ('Uyo', 'Uyo')
]



# class CategoriesForm(forms.Form):
#     categories = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CATEGORIES_CHOICES)
#     lat = forms.CharField()
#     lng = forms.CharField()





class UserRegistrationForm(ModelForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
    # username = forms.CharField(label='Username', widget=forms.TextInput, max_length=20
    # 0)
    username = forms.CharField(label='Username', widget=forms.TextInput, max_length=200)
    lga = forms.CharField(label='Lga', required=True, widget=forms.Select(choices=CATEGORIES_CHOICES))
    class Meta:
        model = UserRegistration
        fields = ['useremail', 'username', 'firstname', 'middlename', 'lastname', 'address', 'phone', 'age', 'lga']