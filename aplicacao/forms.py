from django import forms
from .models import Produto
from .models import Form_Contato

class ProdutoForm(forms.ModelForm):
    imagem = forms.ImageField(label='Imagem', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    nova_categoria = forms.CharField(required=False, label="Nova Categoria")
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'valor', 'observacao', 'categoria', 'imagem')
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Form_Contato
        fields = ['nome_contato', 'email', 'assunto', 'mensagem', 'data']
        widgets = {
                'data': forms.DateInput(attrs={'type': 'date'})
}

from .models import Categoria

class CategoriaForm(forms.ModelForm):
     class Meta:
        model = Categoria
        fields = ['nome']

from .models import Empresa

from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    imagem = forms.ImageField(
        label='Imagem', 
        required=False, 
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Empresa
        fields = (
            'imagem', 'nome', 'username', 'password', 'cnpj', 'inscricao_estadual',
            'tipo_empresa', 'data_abertura', 'natureza_juridica', 'atividade_principal',
            'endereco', 'telefone', 'email',
            'socio_nome', 'socio_cpf', 'socio_data_nascimento', 'socio_cargo',
            'socio_telefone', 'socio_email'
        )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_empresa': forms.Select(attrs={'class': 'form-control'}),
            'data_abertura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'uridica': forms.TextInput(attrs={'class': 'form-control'}),
            'atividade_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'socio_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'socio_cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'socio_data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'socio_cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'socio_telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'socio_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
