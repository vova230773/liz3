from django import forms
from pytils.translit import slugify


from core.models import Counterparts, Resume
from .models import News


class KontrForm(forms.ModelForm):

    class Meta:
        model = Counterparts
        fields = [
            "name",
            "full_name",
            "slug",
            "adres",
            "country",
            "city",
            "street",
            "number",
            "letter",
            "okpo_cod",
            "inn",
            "director",
            "phone",
            "group",
            "guid",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "adres": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "street": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "letter": forms.TextInput(attrs={"class": "form-control"}),
            "okpo_cod": forms.TextInput(attrs={"class": "form-control"}),
            "inn": forms.TextInput(attrs={"class": "form-control"}),
            "director": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "group": forms.Select(attrs={"class": "form-control"}),
            "guid": forms.TextInput(attrs={"class": "form-control"}),
        }


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ["name", "file"]


class EmpForm(forms.ModelForm):

    class Meta:
        model = Counterparts
        fields = [
            "name",
            "full_name",
            "slug",
            "adres",
            "country",
            "city",
            "street",
            "number",
            "letter",
            "okpo_cod",
            "inn",
            "director",
            "phone",
            "group",
            "guid",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "adres": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "street": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "letter": forms.TextInput(attrs={"class": "form-control"}),
            "okpo_cod": forms.TextInput(attrs={"class": "form-control"}),
            "inn": forms.TextInput(attrs={"class": "form-control"}),
            "director": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "group": forms.Select(attrs={"class": "form-control"}),
            "guid": forms.TextInput(attrs={"class": "form-control"}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "image", "file"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug:
            instance.slug = slugify(instance.title)

            if commit:
                instance.save()
        return instance
