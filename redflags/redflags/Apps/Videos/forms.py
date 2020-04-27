from django import forms
from .models import Ubicacion
class FormularioForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'latitud',
            'longitud',
            'foto_casa', # el archivo de subida no se declara dentro de los widgets, únicamente como un campo
            'tipo_apoyo',
            'nro_personas',
            'comentario',
        ]
        labels = {
            'nombre': 'Nombre ',
            'direccion': 'Dirección',
            'telefono':'Telefono',
            'latitud':'Latitud',
            'longitud':'Longitud',
            'foto_casa':'Foto del domicilio',
            'tipo_apoyo':'Tipo de apoyo',
            'nro_personas':'Número de personas',
            'comentario':'Comentarios adicionales',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de contacto'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección del domicilio'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','type':'text',
            'placeholder':'Por ejemplo, 09XXXXXXXX','minlength':'7','maxlength':'10',
            'title':'Ingresa correctamente el número telefónico (entre 7 y 10 dígitos)', 'required pattern':'[0-9]{7,10}'}),
            'latitud': forms.TextInput(attrs={'id':'lat','class': 'form-control','type':'number','step':'any',
            'placeholder':'Por ejemplo, -4.45654','min':'-90', 'max':'90'}),
            'longitud': forms.TextInput(attrs={'id':'long','class': 'form-control','type':'number','step':'any',
            'placeholder':'Por ejemplo, -78.45654','min':'-90', 'max':'90'}),           
            'tipo_apoyo': forms.Select(attrs={'class':'form-control'}),
            'nro_personas': forms.TextInput(attrs={'class': 'form-control','type':'number','min':'1', 'max':'20',
            'placeholder':'Número de personas del domicilio'}),
            'comentario': forms.Textarea(attrs={'class':'form-control','placeholder':'Comentarios adicionales'}),
        }
