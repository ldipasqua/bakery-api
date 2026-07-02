from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Bolo de chocolate"
    sabor: str = "Chocolate"
    tamanho: str = "Pequeno"
    fatias: int = 8
    valor: float = 12.50


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no nome do produto e no tamanho.
    """
    nome: str = "Chocolate"
    tamanho: str = "Pequeno"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Bolo de chocolate"
    sabor: str = "Chocolate"
    tamanho: str = "Pequeno"
    fatias: int = 8
    valor: float = 12.50

def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "sabor": produto.sabor,
            "tamanho": produto.tamanho,
            "fatias": produto.fatias,
            "valor": produto.valor
        })

    return {"produtos": result}


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "sabor": produto.sabor,
        "tamanho": produto.tamanho,
        "fatias": produto.fatias,
        "valor": produto.valor
    }
