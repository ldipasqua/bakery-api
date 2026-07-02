from datetime import datetime  
from pydantic import BaseModel, Field
from typing import Optional, List
from model.pedidos import Pedidos


class PedidoSchema(BaseModel):
    """ Define como um novo pedido a ser inserido deve ser representado
    """
    cpf_cliente: str = '123.4567.890'
    preco_final: float = 300.0
    data_insercao: datetime = Field(default_factory=datetime.now)
    


class PedidoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no cpf do cliente.
    """
    cpf_cliente: str = '123.4567.890'


class PedidoViewSchema(BaseModel):
    """ Define como um pedido será retornado: pedido + cliente + produto.
    """
    id: int = 1
    cpf_cliente: str = '000.000.000-00'
    preco_final: float = 0.0
    data_insercao: datetime = Field(default_factory=datetime.now)
    endereco_entrega: str = 'Rua Maravilha 123'

class ListagemPedidosSchema(BaseModel):
    """ Define como uma listagem de pedidos será retornada.
    """
    pedidos: List[PedidoViewSchema]    


def apresenta_pedidos(pedidos: List[Pedidos]):
    """ Retorna uma representação do pedido seguindo o schema definido em
        PedidoViewSchema.
    """
    result = []
    for pedido in pedidos:
        result.append({
            "id": pedido.id,
            "cpf_cliente": pedido.cpf_cliente,
            "preco_final": pedido.preco_final,         
            "data_insercao": pedido.data_insercao.strftime("%Y-%m-%d"),
            "endereco_entrega": pedido.cliente.endereco if pedido.cliente else "Não informado"
        })
    return {"pedidos": result}


def apresenta_pedido(pedido: Pedidos):
    """ Retorna uma representação do pedido seguindo o schema definido em
        PedidoViewSchema.
    """
    return {
        "id": pedido.id,
        "cpf_cliente": pedido.cpf_cliente,
        "preco_final": pedido.preco_final,
        "endereco_entrega": pedido.cliente.endereco if pedido.cliente else "Não informado",
        "data_insercao": pedido.data_insercao.strftime("%Y-%m-%d")
    }


class PedidoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    id: int