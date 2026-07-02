from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "Jõao Simas"
    cpf: str = "123.4567.890"
    celular: str = "(11)99999-9999"
    endereco: str = "Rua das Flores, 123"
    email: str = "joao.simas@gmail.com"


class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no nome, cpf do cliente e no celular.
    """
    nome: str = "Jõao Simas"
    cpf: str = "12345678900"
    celular: str = "(11)99999-9999"


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    clientes:List[ClienteSchema]


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado
    """
    id: int = 1
    nome: str = "Jõao Simas"
    cpf: str = "12345678900"
    celular: str = "(11)99999-9999"
    endereco: str = "Rua das Flores, 123"
    email: str = "[EMAIL_ADDRESS]"
    

def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "celular": cliente.celular,
            "endereco": cliente.endereco,
            "email": cliente.email
        })

    return {"clientes": result}


class ClienteDelSchema(BaseModel):  
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "cpf": cliente.cpf,
        "celular": cliente.celular,
        "endereco": cliente.endereco,
        "email": cliente.email
    }