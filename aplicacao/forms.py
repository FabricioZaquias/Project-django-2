from django import forms
from .models import Produto
from .models import Form_Contato

class ProdutoForm(forms.ModelForm):
    imagemProd = forms.ImageField(
        label='Imagem',
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    nova_categoria = forms.CharField(required=False, label="Nova Categoria")

    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'valor', 'observacao', 'categoria', 'imagemProd')
        widgets = {
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
            'cnpj': forms.TextInput(attrs={'class': 'form-control cnpj-mask'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'data_abertura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'uridica': forms.TextInput(attrs={'class': 'form-control'}),
            'atividade_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control phone-mask'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'socio_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'socio_cpf': forms.TextInput(attrs={'class': 'form-control cpf-mask'}),
            'socio_data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'socio_cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'socio_telefone': forms.TextInput(attrs={'class': 'form-control phone-mask'}),
            'socio_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        widgets = {
            'nota': forms.RadioSelect(choices=[(i, f'{i} estrela{"s" if i > 1 else ""}') for i in range(1, 6)]),
            'comentario': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
