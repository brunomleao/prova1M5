from sqlalchemy import create_engine, Integer, String, Column, Float
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

class Base(DeclarativeBase):
    pass

class Jogos(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primarykey = True)
    nome_jogo = Column(String)
    plataforma_jogo = Column(String)
    preco_jogo = Column(Float)
    qtd_jogo = Column(Integer)

engine = create_engine('sqlite:///banco.db', echo = True)

session = sessionmaker(bind = engine)

session = Session()

Base.metadata.create_all(engine)

jogo = Jogos(nome_jogo="DEAD SPACE REMAKE", plataforma_jogo="PS5", preco_jogo = 350.00, qtd_jogo = 10)

session.add(jogo)
session.commit()

jogo = Jogos(nome_jogo="FORSPOKEN", plataforma_jogo="PC", preco_jogo = 299.00, qtd_jogo = 8)

session.add(jogo)
session.commit()

jogo = Jogos(nome_jogo="DEAD ISLAND 2", plataforma_jogo="PS5", preco_jogo = 350.00, qtd_jogo = 10)

session.add(jogo)
session.commit()

jogo = Jogos(nome_jogo="HOGWARTS LEGACY", plataforma_jogo="PC", preco_jogo = 219.00, qtd_jogo = 7)

session.add(jogo)
session.commit()

jogo = Jogos(nome_jogo="WILD HEARTS", plataforma_jogo="XBox Series", preco_jogo = 350.00, qtd_jogo = 7)

session.add(jogo)
session.commit()

jogo = Jogos(nome_jogo="RESIDENT EVIL 4", plataforma_jogo="PS5", preco_jogo = 289.00, qtd_jogo = 10)

session.add(jogo)
session.commit()

jogo = Jogos(nome_jogo="THE LEGEND OF ZELDA: TEARS OF THE KINGDOM", plataforma_jogo="Switch", preco_jogo = 350.00, qtd_jogo = 10)

session.add(jogo)
session.commit()