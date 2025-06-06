from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from .views import editar_categoria, excluir_categoria

from .views import listar_categorias
from .views import editar_produto, excluir_produto
from .views import listar_empresas # já está importado, só confirmando


urlpatterns = [
    path('', listar_empresas, name='BASE_URL'),
    path('contato/', views.contato, name='CONTATO_URL'),
    path('console/', views.CONSOLE, name='CONSOLE_URL'),
    path('games-ps4/', views.GAMES, name = 'GAMES_URL'),
    path('listagem/', views.LISTAGEM, name='LISTAGEM_URL'),
    path('listagem-prod/', views.LISTAGEM_PROD, name= 'LISTAGEM-PROD_URL'),
    path('login_admin/', views.login_admin, name='LOGIN_ADMIN_URL'),
    path('dashboard/', views.admin_dashboard, name='ADMIN_DASHBOARD_URL'),
    path('administrador/', views.ADMIN_SITE, name='ADMIN_URL'),
    path('cadastro_prod/', views.CADASTRO_PROD, name= 'CADPRODUTO_URL'),
    path('logout_admin/', LogoutView.as_view(next_page='BASE_URL'), name='LOGOUT_ADMIN_URL'),
    path('categorias/', listar_categorias, name='LISTAR_CATEGORIAS_URL'),
    path('categorias/editar/<int:id>/', editar_categoria, name='EDITAR_CATEGORIA_URL'),
    path('produtos/editar/<int:id>/', editar_produto, name='EDITAR_PRODUTO_URL'),
    path('produtos/excluir/<int:id>/', excluir_produto, name='EXCLUIR_PRODUTO_URL'),
    path('categorias/excluir/<int:id>/', excluir_categoria, name='EXCLUIR_CATEGORIA_URL'),
    path('cadastro-empresa/', views.cadastro_empresa, name='CADASTRO_URL'),
    path('meus-dados/', views.meus_dados_empresa, name='EMPRESA_DADOS_URL'),
    path('empresa/editar/', views.editar_empresa, name='editar_empresa'),
    path('empresa/<int:empresa_id>/avaliar/', views.avaliar_empresa, name='avaliar_empresa'),
    path('avaliacoes/', views.visualizar_avaliacoes, name='AVALIACOES_EMPRESA_URL'),
    path('empresa/<int:empresa_id>/produtos/', views.produtos_por_empresa, name='PRODUTOS_EMPRESA_URL')


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)