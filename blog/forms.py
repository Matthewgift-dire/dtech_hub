# blog/forms.py

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
    
    
class ContactForm(forms.Form):
	Name = forms.CharField(
		label="",
		max_length=30,
		widget=forms.TextInput(attrs={"class": "email_text",
		"name":"Name",
		"placeholder":"Name",
		}
	  )
	)
	Email = forms.CharField(
		label="",
		widget=forms.TextInput(attrs={"class": "email_text",
		"name":"Email",
		"placeholder":"Email",
		}
	  )
	)
	Subject = forms.CharField(
		label="",
		max_length=30,
		widget=forms.TextInput(attrs={"class": "email_text",
		"name":"Subject",
		"placeholder":"Subject",
		}
	  )
	)
	Message = forms.CharField(
		max_length=500,
		label="",
		widget=forms.Textarea(attrs={
		"class": "email_text",
		"name":"Message",
		"placeholder":"Message",
		"id":"comment",
		"rows":5
		}
	  )
	)
	
class SearchForm(forms.Form):
	query = forms.CharField(
		label="",
		widget=forms.TextInput(attrs={
			"class": "email_text",
			"placeholder": "search",
		})
	)
	#Phone = forms.IntegerField()
#	Email = forms.EmailField()
#	Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    