from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Union

from model import Base
from model.pedidos import Pedidos

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column ("cliente_id", Integer, primary_key=True)
    nome = Column(String(140))
    cpf = Column(String, unique=True)
    celular = Column(String(15), unique=True)
    endereco = Column(String(140))
    email = Column(String(140))
    data_insercao = Column(DateTime, default=datetime.now)

    # Relacionamento um a muitos com Pedido: um cliente pode ter mais de um pedido, por exemplo
    # comprou 1 bolo de chocolate e 5 muffins de morango.
    pedido = relationship("Pedidos", back_populates="cliente")

    def __init__(self, nome:str, cpf:str, celular:str, endereco:str, 
                email:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            nome: nome do cliente.
            cpf: cpf do cliente.
            celular: celular do cliente.
            endereço: endereço do cliente.
            email: email do cliente
        """
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        self.endereco = endereco
        self.email = email

        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_pedido(self, pedido: Pedidos):
        """
        Adiciona um novo Pedido ao Cliente.

        Arguments:
            pedido: Pedido a ser adicionado ao cliente.
        """
        self.pedido.append(pedido)
