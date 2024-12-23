from django import forms


class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
            }
        ),
    )


class SetNewPasswordForm(forms.Form):
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "New password"}
        ),
        
    )
    confirm_password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        if len(password) < 5:
            raise forms.ValidationError("Password must be at least 5 characters long.")
        return cleaned_data
