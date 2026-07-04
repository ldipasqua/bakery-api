from pydantic import BaseModel
from typing import List
from model.produto import Produto

class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Bolo de chocolate"
    sabor: str = "Chocolate"
    tamanho: str = "Pequeno"
    fatias: int = 8
    valor: float = 12.50


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos: List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ListagemProdutosSchema.
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
