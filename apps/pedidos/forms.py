from django import forms

from .models import Pedido, Item

class PedidoForm(forms.ModelForm):

	class Meta:
		model = Pedido
		fields = [
			'cliente',
			'data',
			'total',
		]
  
class ItemForm(forms.ModelForm):
    
	class Meta:
		model = Item
		fields = [
			'produto',
			'quantidade',
		]