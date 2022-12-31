from django import forms
from .models import ValoracionProducto

class ValoracionForm(forms.ModelForm):
    class Meta:
        model = ValoracionProducto
        fields = ['valoracion', 'resenia']