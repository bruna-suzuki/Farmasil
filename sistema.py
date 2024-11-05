from sqlalchemy import Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import relatioship

Base = declarative_base ()



class Loja(Base):
    __tablename__ = 'Loja'
    
    loja_id = Column (Integer, primary_key = True)
    endereco = Column(String)
    telefone = Column(String)
    horario_func = Column(String)

    funcionario = relationship("Funcionario", backref="loja") #relacionando entre Loja e Funcionario

    def adicionar(self, session): #session pra acessar sqlalchemy 
        session.add(self)
        session.commit()
    
    def remover(self, session):
        session.delete(self)
        session.commit()

    def consultar(self, session, id = None): # id para cultar a Loja id
        if id: 
            return
            session.query(Loja).filter_by(id = id).first() #query = consulta. consulta da classe LOja filtrano pelo id
        else:
            return
            session.query(Loja).all()  # Se id for None, pode querer retornar todas as lojas.

    def atualizar(self, session, endereco = None, telefone = None, horario_func = None):
        if endereco:
            self.endereco = endereco
        if telefone:
            self.telefone = telefone
        if horario_func:
            self.horario_func = horario_func
        
        session.commit()

    def __str__(self):
        return f'Loja {self.endereco} , {self.telefone} , {self.horario_func}' 


class Funcionario(Base): 
    loja_id = Column(Integer, ForeignKey('Loja.id'))
    id_func = Column(Integer, primary_key = True)
    nome = Column(String)
    cargo = Column(String)
    salario = Column(Float)
    turno = Column(String)
    data_admissao = Column(String)
    horas_trab = Column(Float)

    def __init__(self, loja_id, id_func, nome, cargo, salario, turno, data_admissao, horas_trab):
        self.loja_id = loja_id
        self.id_func = id_func
        self.nome = nome
        self.cargo = cargo 
        self.salario = salario
        self.turno = turno
        self.data_admissao = data_admissao
        self.horas_trab = horas_trab

    
    def adicionar_func(self, session):
        session.add(self)
        session.commit()

    def remover_func(self, session):
        session.delete(self)
        session.commit()

    def atualizar(self, session, nome = None, cargo = None, salario = None, turno = None, data_admissao = None, horas_trab = None):
        if nome:
            self.nome = nome 
        if cargo:
            self.cargo = cargo
        if salario:
            self.salario = salario
        if turno:
            self.turno = turno
        if data_admissao:
            self.data_admissao = data_admissao
        if horas_trab:
            self.horas_trab = horas_trab
        
        session.commit()


    def calcular_func(self):
        if self.horas_trab > 0:
            valor_hora = self.salario / self.horas_trab
            salario_total = valor_hora * self.horas_trab
            return salario_total
        return 0


    def listar_func(self, session):
        return session.query(Funcionario).all()

        
    def __str__(self):
            return f'Funcionario {self.nome} , {self.cargo} , {self.salario} , {self.turno} , {self.data_admissao} , {self.horas_trab}' 
        




   
class Gerente(Funcionario):

    __tablename__ = 'Gerente'
    lojas_gerenciadas = relationship("Loja", back_populates = "Gerente")
    loja_id = Column(Integer, ForeignKey ('Loja.id'))
    id_func = Column(Integer, ForeignKey('Func.id'))
    id_gerente = Column(Integer, primary_key=True)

    def __init__(self, lojas_gerenciadas, loja_id, id_func, id_gerente):
        self.lojas_gerenciadas = lojas_gerenciadas
        self.loja_id = loja_id
        self.id_func = id_func
        self.id_gerente = id_gerente

    def gerenciar_lojas(self):
        if not self.lojas_gerenciadas:
            print("Nenhuma loja atribuída ao gerente")
        else:
            for Loja in self.lojas_gerenciadas:
                print(f"Loja id: {Loja.loja_id}, endereco: {Loja.endereco}, telefone:{Loja.telefone}")



    def monitorar_vendas(self, session):
        vendas = 

    
    def avaliar_funcionario(self, session):



class Cliente:
    __tablename__ = 'Cliente'
    cliente_id = Column(Integer, primary_key=True)
    nivel_fid = Column(Integer)
    nome = Column(String)
    cpf = Column(Integer)
    telefone = Column(Integer)
    email = Column(String)
    endereco = Column(String)
    historico_compra = Column(String)


    def __init__(self, id, nivel_fid, nome, cpf, telefone, email, endereco, historico_compra):
        self.id = id
        self.nivel_fid = nivel_fid
        self.nome = nome
        self.cpf = cpf
        self.tel = telefone
        self.email = email
        self.endereco = endereco
        self.historico_compra = historico_compra


    def add(self):
        print(self.id, self.nivel_fid, self.nome, self.cpf, self.tel, self.email, self.cartao_fid, self.endereco, self.historico_compra)




class Cartao_Fidelidade:
    def __init__(self, id_cli, id_cartao, nivel_fedelidade, pontos_acumulados, beneficios, desconto_atual):
        
        self.id_cli = id_cli
        self.id_cartao = id_cartao
        self.nivel_fedelidade = nivel_fedelidade
        self.pontos_acumulados = pontos_acumulados
        self.beneficios = beneficios
        self.desconto_atual = desconto_atual
    
    def exibir(self):
        print(self.id_cli, self.id_cartao, self.nivel_fedelidade, self.pontos_acumulados, self.beneficios, self.desconto_atual)



from sqlalchemy import create_engine
engine = create_engine('sqlite:///farmasil.db')

Session = sessionmaker(bind = engine)




class Pedido:
    __tablename__ = 'Pedido'
    id_pedidos = Column(Integer, primary_key= True)
    cliente_id = Column(Integer, ForeignKey('cliente_id'))
    func_id = Column(Integer, ForeignKey)
    itens = Column(String)
    total = Column(float)
    metodo_pag = Column(String)
    data = Column(String)
    status = Column(String)

    def __init__ (self, id_pedidos, clientes_id, func_id, itens, total, metodo_pag, data, status):
        self.id_pedidos = id_pedidos
        self.cliente_id =clientes_id
        self.func_id = func_id
        self.itens = itens
        self.total = total
        self.metodo_pag = metodo_pag
        self.data = data
        self.status = status

    def adicionar_item(self, id_pro, quantidade, session):
        item = ItemPedido(id_pro.id, id_pedidos = self.id, quantidade = quantidade, preco_unitario = Produto.preco)
        session.add(item)
        session.commit()
        self.valor_total += Produto.preco * quantidade
        session.commit()
        print(f'Item {Produto.nome} adicionado ao pedido. Quantidade: {quantidade}')
        
    def remover_item(self, id_pro, session):
        item = session.query(ItemPedido).filter_by(id_pedidos = self.id_pedidos id_pro = id_pro).first()
        if item:
            self.valor_total -= item.preco_unitario * item.quantidade
            session.delete(item)
            session.commit()
            print(f'item removido com sucesso')
        else:
            print('item não encontrado no pedido')

    def calcular_total(self, session):
        total = sum(item.preco_unitario * item.quantidade for item in self.itens)
        self.valor_total = total
        session.commit()
        print(f'Valor total do pedido: R$ {self.valor_total}')
        return self.valor_total

    def finalizar_pedido(self, session):
        if self.status != "Em andamento":
            print("O pedido já foi finalizado ou cancelado")
            return
        self.status = "Finalizado"
        self.data =  datatime.utcnow() 
        session.commit()
        print('Pedido finalizado com sucesso')
        

class Produto:
    __tablename__ =  'Produto'
    id_pro = Column(Integer, primary_key=True)
    nome = Column(String)
    categoria = Column(String)
    preco = Column(float)
    estoque = Column(Integer)
    fornecedor = Column(String)
    loja_id = Column(Integer, ForeignKey('Loja.loja_id'))
    loja = relationship("Loja", back_populates = "Produto")


    def adicionar_produto(self, session):
        session.add(self)
        session.commit()
        print(f'Produto {Produto.nome} adiocionado com sucesso')

    def remover_produto(self, id_pro, session):
        produto = session.query(Produto).filter_by(id = id_pro).first()
        if produto:
            session.delete(produto)
            session.commit()
            print(f"Produto {Produto.nome} removido com sucesso")
        else:
            print('Produto não encontrado')

    def atualizar_estoque(self, id_pro, quantidade, session):
        produto = session.query(Produto).filter_by(id = id_pro).first()
        if produto:
            produto.estoque += quantidade
            session.commit()
            print('Produto atualizado com sucesso')
        else:
            print('Produto não encontrado')

    def consultar_produto(self, id_pro, session):
        produto = session.query(Produto).filter_by(id = id_pro).first()
        if produto:
            return(f'id: {Produto.id_pro}, nome {Produto.nome}, categoria {Produto.categoria}, preco {Produto.preco}, estoque {Produto.estoque}, Fornecedor {Produto.fornecedor}')




class Remedio:
    __tablename__ = 'Remedio'
    id_remdedio = Column(Integer, primary_key= True)
    nome_re = Column(String)
    categoria = Column(String)
    tarja = Column(String)
    necessita_rec = Column(bool, default=False)
#############
    def verificar_validade(self)






class Caixa:









class Faturamento:


# f1 = Funcionario(1111, 2024, "Cindy", "24/10/2024", 15000, "caixa", "manha")
# f1.exibir()
