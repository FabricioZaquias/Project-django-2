from django.shortcuts import render, redirect
from .models import Form_Contato
from .models import Produto
from .models import Categoria
from .forms import ContatoForm
from django.contrib import messages
from django.utils import timezone
from .models import Login_Admin
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def BASE(request):
    return render(request, 'index.html')

def CONTATO(request):
    return render(request, 'contato.html')

def CONSOLE(request):
    return render(request, 'console.html')  

def GAMES(request):
    produtos = Produto.objects.all()
    produtos = Produto.objects.filter(categoria__nome='Jogos PS4')
    return render(request, 'games_ps4.html', {'produtos': produtos})

def ADMIN_SITE(request):
    return render(request,'admin_site.html')

def CADASTRO_PROD(request):
    return render(request, 'cadastro_prod.html')

def LISTAGEM(request):
    data = {}
    data["contatos"] = Form_Contato.objects.all()
    return render(request, "listagem.html", data)

def LISTAGEM_PROD(request):
    data = {}
    data["produtos"] = Produto.objects.all()
    if request.method == 'POST':
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        produto = Produto(nome='Produto 1', descricao='Descrição do produto 1', valor=10.0, categoria=categoria, created_by=request.user)
        produto.save()
        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('LISTAGEM-PROD_URL')
    return render(request,"listagem-prod.html" ,data)



def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.data = timezone.now()
            contato.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('CONTATO_URL')
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})



#Login do admin ------------------------------------
from .models import Login_Admin, Empresa

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        empresa_login = Login_Admin.objects.filter(usuario=username, senha=password).first()

        if empresa_login:
            # Busca a empresa correspondente ao login
            empresa = Empresa.objects.filter(username=username).first()
            if empresa:
                request.session['empresa_id'] = empresa.id  # <-- ESSENCIAL
                return redirect('ADMIN_DASHBOARD_URL')
            else:
                messages.error(request, 'Empresa não encontrada.')
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')

    return render(request, 'admin_site.html')


#logout do admin -----------------------------
from django.contrib.auth import logout as django_logout

def logout_admin(request):
    django_logout(request)
    return redirect('LOGIN_ADMIN_URL')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

from django.shortcuts import render, redirect
from .forms import ProdutoForm

from .models import Categoria

def CADASTRO_PROD(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            nova_categoria_nome = form.cleaned_data.get('nova_categoria')
            if nova_categoria_nome:
                categoria, created = Categoria.objects.get_or_create(nome=nova_categoria_nome)
                produto = form.save(commit=False)
                produto.categoria = categoria
                produto.save()
            else:
                form.save()
            return redirect('LISTAGEM-PROD_URL')
    else:
        form = ProdutoForm()
        return render(request, 'cadastro_prod.html', {'form': form})


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
        return redirect('LISTAGEM-PROD_URL')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('LISTAGEM-PROD_URL')
    return render(request, 'excluir_produto.html', {'produto': produto})

from .models import Categoria
from django.contrib.auth.decorators import login_required

@login_required
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categorias.html', {'categorias': categorias})
from django.shortcuts import get_object_or_404, redirect
from .forms import CategoriaForm

@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('LISTAR_CATEGORIAS_URL')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form})

@login_required
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('LISTAR_CATEGORIAS_URL')

from .models import Empresa, Login_Admin
from .forms import EmpresaForm

def cadastro_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            empresa = form.save()

            # Cria o login com os dados da empresa
            Login_Admin.objects.create(
                usuario=empresa.username,
                senha=empresa.password  # ⚠️ Idealmente, use hash de senha
            )

            return redirect('LOGIN_ADMIN_URL')  # Redireciona para o login
    else:
        form = EmpresaForm()
    return render(request, 'cadastro_empresa.html', {'form': form})
def meus_dados_empresa(request):
    empresa_id = request.session.get('empresa_id')
    if not empresa_id:
        return redirect('LOGIN_ADMIN_URL')

    empresa = Empresa.objects.get(id=empresa_id)
    return render(request, 'empresa_dashboard.html', {'empresa': empresa})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa
from .forms import EmpresaForm

def editar_empresa(request):
    empresa_id = request.session.get('empresa_id')
    if not empresa_id:
        return redirect('LOGIN_ADMIN_URL')

    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('meus_dados_empresa')  # Redireciona para a visualização dos dados
    else:
        form = EmpresaForm(instance=empresa)

    return render(request, 'editar_empresa.html', {'form': form})
