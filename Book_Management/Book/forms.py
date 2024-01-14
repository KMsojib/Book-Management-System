from django import forms
from Book.models import BookStoreModel
# form app_name.models import modele_name

class BookStoreForm(forms.ModelForm):
    
    class Meta:
        model = BookStoreModel
        exclude = ['First_publication','Last_publication']