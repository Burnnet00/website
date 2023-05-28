from django import forms

class OrdersForm(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))#добавимо необовязкове поле, виджет створеного цсс
    phone = forms.CharField(max_length=200)

