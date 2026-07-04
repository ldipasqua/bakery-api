from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produto, Cliente, Pedidos
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger")
produto_tag = Tag(name="Produto", description="Visualização de produtos à base")
cliente_tag = Tag(name="Cliente", description="Adição de clientes à base")
pedido_tag = Tag(name="Pedidos", description="Adição e visualização de pedidos à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Requisição POST para adicionar um novo cliente

@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cliente(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados.    
    """
    cliente = Cliente(
        nome=form.nome,
        cpf=form.cpf,
        celular=form.celular,
        endereco=form.endereco,
        email=form.email)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando cliente
        session.add(cliente)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        session.rollback() 
        error_msg = "Cliente de mesmo nome já salvo na base :/"
        
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        session.rollback() 
        error_msg = "Não foi possível salvar novo item :/"
        
        return {"mesage": error_msg}, 400

# Requisição GET para buscar todos os produtos na base de dados.

@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os produtos cadastrados na base.

    Retorna uma representação da listagem de produtos.
    """    
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).all()

    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:        
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200



@app.post('/pedido', tags=[pedido_tag],
          responses={"200": PedidoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pedido(form: PedidoSchema):
    """Adiciona um novo Pedido com o preço total à base."""
    
    # criando conexão com a base
    session = Session()
    
    try:
        # Buscar o cliente usando o cpf como busca.
        cliente = session.query(Cliente).filter(Cliente.cpf == form.cpf_cliente).first()
        
        # Valida se o cliente realmente existe
        if not cliente:
            return {"mesage": "Cliente com o CPF informado não foi encontrado :/"}, 404
        
        # Criando o objeto Pedido        
        pedido = Pedidos(            
            cpf_cliente=cliente.cpf,
            preco_final=form.preco_final,
            data_insercao=form.data_insercao
        )
        
        # Adicionando e efetivando o pedido
        session.add(pedido)
        session.commit()
        
        return apresenta_pedido(pedido), 200

    except IntegrityError as e:
        # Desfaz a operação no banco em caso de erro de integridade
        session.rollback()
        error_msg = "Pedido duplicado ou erro de integridade na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # Importante: Desfaz a operação em qualquer outro erro inesperado
        session.rollback()
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400
        
    finally:        
        session.close()


# Requisição GET para buscar os pedidos na base de dados.

@app.get('/pedidos', tags=[pedido_tag],
         responses={"200": ListagemPedidosSchema, "404": ErrorSchema})
def get_pedidos(query: PedidoBuscaSchema):
    """Faz a busca por todos os Pedidos cadastrados

    Retorna uma representação da listagem de pedidos.
    """    
    cpf_busca = query.cpf_cliente
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo cpf do cliente
    pedidos = session.query(Pedidos).filter(Pedidos.cpf_cliente == cpf_busca).all()

    if not pedidos:       
        return {"mesagem": "Nenhum pedido encontrado para o CPF fornecido."}, 404
    else:        
        # retorna a representação dos pedidos encontrados
        print(pedidos)
        return apresenta_pedidos(pedidos), 200

   