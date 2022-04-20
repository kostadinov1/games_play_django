from django import forms

from web_basics_exam_retake.core.models import Profile, Game


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password',)
        widgets = {
            'password': forms.TextInput(
                attrs={'type': 'password'}
            )
        }



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameEditForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = '__all__'