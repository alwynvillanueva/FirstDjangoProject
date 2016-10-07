from django.forms import ModelForm
from django import forms
from .models import Tips
class newguide(ModelForm):
	class Meta:
		model = Tips
		fields=['title',
				'author',
			    'desc',
			    'imgdesc',	
			   ]

class contactus(forms.Form):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
	