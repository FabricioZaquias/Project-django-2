from django.db import models
from django.utils import timezone


class Categoria(models.Model):

    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

from django.conf import settings  

class Produto(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacao = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    visao_geral = models.TextField(null=True, blank=True)
    imagemProd = models.ImageField(upload_to='produtos/', null=True, blank=True)

    # 🔥 Este campo é essencial para saber de qual empresa é o produto
    created_by = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.descricao

    
class Cad_Cliente(models.Model):
    data = models.DateField(auto_now_add=True)
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)

    class Meta():
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

class Form_Contato(models.Model):
    nome_contato = models.CharField(max_length =200)
    email = models.CharField(max_length=200)
    assunto = models.CharField(max_length =200)
    mensagem = models.TextField(null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name_plural = "Contatos"

    def __str__(self):
        return self.nome_contato
    
class Login_Admin(models.Model):
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=8)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario
from django.db import models

class Empresa(models.Model):
    imagem = models.ImageField(upload_to='empresas/', null=True, blank=True)
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    inscricao_estadual = models.CharField(max_length=50, blank=True)
    tipo_empresa = models.CharField(max_length=100, blank=True)
    data_abertura = models.DateField(null=True, blank=True)
    natureza_juridica = models.CharField(max_length=100, blank=True)
    atividade_principal = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()

    # Sócio
    socio_nome = models.CharField(max_length=100)
    socio_cpf = models.CharField(max_length=14)
    socio_data_nascimento = models.DateField()
    socio_cargo = models.CharField(max_length=100)
    socio_telefone = models.CharField(max_length=20)
    socio_email = models.EmailField()

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação {self.nota} para {self.empresa.nome}"
