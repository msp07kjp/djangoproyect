from django import forms

class CreateNewTask(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200)
    descripcion = forms.CharField(label="Descripcion", max_length=200, required=False)
    fecha_creacion = forms.DateField(label="Fecha de Creacion")
    fecha_entrega = forms.DateField(label="Fecha de Entrega")
    estado = forms.CharField(label="Estado", max_length=20)
    hecho = forms.BooleanField(label="Hecho", required=False)
class CreateNewProyect(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200)
    descripcion = forms.CharField(label="Descripcion", max_length=200, required=False)
    fecha_creacion = forms.DateField(label="Fecha de Creacion")
    fecha_entrega = forms.DateField(label="Fecha de Entrega")
    estado = forms.CharField(label="Estado", max_length=20)