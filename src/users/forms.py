from django import forms


class UpdateAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    institution = forms.CharField(max_length=100, required=False)

    def clean_institution(self):
        institution_value = self.cleaned_data["institution"].strip()
        if not institution_value:
            return None
        return institution_value


class UpdateModelForm(forms.Form):
    # TODO: Should the user be able of changing the Model's Author?
    # model_author = forms.ModelChoiceField(queryset=Author.objects.all())
    model_id = forms.IntegerField()
    model_name = forms.CharField(max_length=100)
    model_description = forms.CharField(max_length=500)
    model_repository = forms.CharField(max_length=200)
    model_language = forms.CharField(max_length=100)
    model_type = forms.CharField(max_length=100)

    # def clean_model_author(self):
    #     author = self.cleaned_data["model_author"]
    #     if not Author.objects.filter(user__username=author.user.username).exists():
    #         raise forms.ValidationError("Author not found")
    #     return author


class DeleteModelForm(forms.Form):
    model_id = forms.IntegerField()
