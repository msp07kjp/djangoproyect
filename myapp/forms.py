from django import forms
# quiero mandar en widget atributos para que se aplique bs5 y se vea muy bien el formulario
class CreateNewTask(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label="Descripcion", max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #para elegir las fechas quiero que salga un calendario
    fecha_creacion = forms.DateField(label="Fecha de Creacion", widget=forms.TextInput(attrs={'class': 'form-control','type': 'date'}))
    fecha_entrega = forms.DateField(label="Fecha de Entrega", widget=forms.TextInput(attrs={'class': 'form-control','type': 'date'}))
    estado = forms.CharField(label="Estado", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hecho = forms.BooleanField(label="Hecho", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
class CreateNewProyect(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    descripcion = forms.CharField(label="Descripcion", max_length=200, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    #para elegir las fechas quiero que salga un calendario
    fecha_creacion = forms.DateField(label="Fecha de Creacion", widget=forms.DateInput(attrs={"class": "form-control", 'type': 'date'}))
    fecha_entrega = forms.DateField(label="Fecha de Entrega", widget=forms.DateInput(attrs={"class": "form-control", 'type': 'date'}))
    estado = forms.CharField(label="Estado", max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))