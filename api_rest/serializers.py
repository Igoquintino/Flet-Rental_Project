from rest_framework import serializers
from api_rest.models import Carrinho, Aluguel, Cliente

# lembrando que esse serializer serve para serializar os dados ou seja, tranformar em JSON ou XML, no caso JSON
# informção serializada para front end e back end do carrinho 
class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = '__all__'

# informção serializada para front end e back end do cliente        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# informção serializada para front end e back end do aluguel
class AluguelSerializer(serializers.ModelSerializer):
    
    carrinho_nome = serializers.CharField(source='carrinho.nome', read_only=True)
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    class Meta:
        model = Aluguel
        fields = '__all__'
        