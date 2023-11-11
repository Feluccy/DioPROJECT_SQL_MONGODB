import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, inspect, select, func, Numeric

Base = declarative_base()


class Cliente(Base):
    """
    Classe de Cliente a ser utilizada na aplicação

    """
    __tablename__ = "cliente"
    # atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    cpf = Column(String(9), unique=True)
    address = Column(String(30), unique=True)

    conta = relationship(
        "Conta", back_populates="cliente", cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}, cpf={self.cpf})"


class Conta(Base):
    """ Classe de Conta bancária a ser utilizada na aplicação

    """
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_account = (Column(String))
    agencia = (Column(String))
    numero = Column(Integer, unique=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    saldo = Column(Integer)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta (id={self.id}, Tipo_conta={self.type_account}, agencia={self.agencia}, numero={self.numero}) "


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

insp = inspect(engine)
