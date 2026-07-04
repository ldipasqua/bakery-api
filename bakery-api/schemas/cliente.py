from pydantic import BaseModel
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "Jõao Simas"
    cpf: str = "123.4567.890"
    celular: str = "(11)99999-9999"
    endereco: str = "Rua das Flores, 123"
    email: str = "joao.simas@gmail.com"


class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado
    """
    id: int = 1
    nome: str = "Jõao Simas"
    cpf: str = "12345678900"
    celular: str = "(11)99999-9999"
    endereco: str = "Rua das Flores, 123"
    email: str = "joao.simas@gmail.com"


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