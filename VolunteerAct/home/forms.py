from django import forms


class ContactUsForm(forms.Form):

    full_name = forms.CharField(
        required=True
    )

    subject = forms.CharField(
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    message = forms.CharField(
        widget=forms.Textarea,
        required=True
    )
