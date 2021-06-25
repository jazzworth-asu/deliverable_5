from logging import disable, error
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


STATE_CHOICES = [
    ('', 'Choose one'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]

GENDER_CHOICES = [
    ('', 'Choose one'),
    ('F', 'Female'),
    ('M', 'Male'),
]


class SignInForm(forms.Form):
    username = forms.CharField(max_length=8)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=8)


class SignUpForm(forms.Form):

    username = forms.CharField(
        max_length=8,
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Username field is required!',
            'max_length': 'Max length is 8 characters!',
        }
    )

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Email field is required!',
            'invalid': 'Email format is invalid!',
        })

    password = forms.CharField(
        max_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Password field is required!',
            'max_length': 'Max length is 8 characters!',
        })

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not any(char.isupper() for char in password):
            raise ValidationError("Uppercase needed!")

        if not any(char.islower() for char in password):
            raise ValidationError("Lowercase needed!")

        if not any(char.isdigit() for char in password):
            raise ValidationError("Digit needed!")

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Firstname field is required!',
            'max_length': 'Max length is 8 characters!',
        })

    middle_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
        })

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Lastname field is required!',
        })

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={
        'class': 'form-control'
    }), error_messages={
        'required': 'Gender field is required!',
    })

    street_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Street address field is required!',
        })

    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'City field is required!',
        })

    state = forms.CharField(widget=forms.Select(choices=STATE_CHOICES, attrs={
        'class': 'form-control'
    }), error_messages={
        'required': 'State field is required!',
    })

    zipcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Zipcode field is required!',
        })

    cell = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tell', 'class': 'form-control'}), error_messages={
            'required': 'Cell field is required!',
        })

    country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Country field is required!',
        })

    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), error_messages={
        'required': 'DoB field is required!',
    })

    member_organization = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
        })


class UserUpdateForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Firstname field is required!',
            'max_length': 'Max length is 8 characters!',
        })

    middle_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
        })

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Lastname field is required!',
        })

    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES, attrs={
        'class': 'form-control'
    }), error_messages={
        'required': 'Gender field is required!',
    })

    street_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Street address field is required!',
        })

    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'City field is required!',
        })

    state = forms.CharField(widget=forms.Select(choices=STATE_CHOICES, attrs={
        'class': 'form-control'
    }), error_messages={
        'required': 'State field is required!',
    })

    zipcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Zipcode field is required!',
        })

    cell = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tell', 'class': 'form-control'}), error_messages={
            'required': 'Cell field is required!',
        })

    country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'required': 'Country field is required!',
        })

    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), error_messages={
        'required': 'DoB field is required!',
    })

    member_organization = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
        })
