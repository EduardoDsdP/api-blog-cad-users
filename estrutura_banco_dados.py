from flask import Flask
from flask_sqlalchemy import SQLAlchemy   

# criar uma API flask
app = Flask(__name__)

# criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'Hardflip@2626' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  

db = SQLAlchemy(app)
db:SQLAlchemy 


# definir a estrutura da tabela postagem
class Postagem(db.Model):  
    __tablename__ = 'postagem'  
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))  



# definir a estrutura da tabela Autor
#id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')  

# Executar o comando para criar o bando de dados:
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()   

        # Criar usuarios administradores:
        autor = Autor(nome = 'Eduardo', email='eduardo@gmail.com', senha='123456', admin=True)
        db.session.add(autor) # aqui é para de fato adicionar esse autor admin ao banco de dados. 
        db.session.commit()  # esse comando é para realmente salvar tudo que você criou. 
if __name__ == '__main__':
    inicializar_banco()