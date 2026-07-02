from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Pedidos(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True)

    cpf_cliente = Column(String, ForeignKey("cliente.cpf"), nullable=False)
    preco_final = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now)

    cliente = relationship("Cliente", back_populates="pedido")

    def __init__(self, cpf_cliente:str, preco_final:float, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Pedido

        Arguments:
            cpf_cliente: cpf do cliente.
            produto_id: id do produto.
            preco_final: preco final do pedido.            
            data_insercao: data de inserção do pedido.            
        """
        self.cpf_cliente = cpf_cliente
        self.preco_final = preco_final        
        
        if data_insercao:
            self.data_insercao = data_insercao
