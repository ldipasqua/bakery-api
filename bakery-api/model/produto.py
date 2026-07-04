from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column("produto_id", Integer, primary_key=True)
    nome = Column(String(140), nullable=False)
    sabor = Column(String(140))
    tamanho = Column(String(140))
    fatias = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, sabor:str, tamanho:str, fatias:int, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            
            nome: nome do produto.
            sabor: sabor do produto.
            tamanho: tamanho do produto.
            fatias: quantidade de fatias do produto.
            valor: valor esperado para o produto
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.sabor = sabor
        self.tamanho = tamanho
        self.fatias = fatias
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

