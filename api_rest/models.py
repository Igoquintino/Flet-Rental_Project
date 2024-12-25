from django.db import models

# Create your models here.
# Classe do Carrinho
class Carrinho(models.Model):
    CATEGORIA_CHOICES = [
        ('elétrico', 'Elétrico'),
        ('manual', 'Manual'),
    ]
    ESTADO_CHOICES = [
        ('disponível', 'Disponível'),
        ('alugado', 'Alugado'),
        ('manutenção', 'Em Manutenção'),
    ]
    
    nome = models.CharField(max_length=100, default='')
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    data_aquisicao = models.DateField(auto_now_add=True) #verificar isso
    preco_aluguel = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    
    def __str__(self):
        return self.nome

# Classe do Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    telefone = models.CharField(max_length=20, default='')
    endereco = models.TextField(default='')
    
    def __str__(self):
        return self.nome

# Classe do Aluguel
class Aluguel(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(default=None) #verificar isso
    data_fim = models.DateTimeField(default=None)# verificar isso
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('finalizado', 'Finalizado')])
    
    def __str__(self):
        return f'Aluguel de {self.carrinho} para {self.cliente}'
