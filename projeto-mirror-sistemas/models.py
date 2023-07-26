from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Produto(db.Model):
    __tablename__ = "produtos"
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    description: str = db.Column(db.Text, nullable=False)
    date_created: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    update_date: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id: int = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pedido_id: int = db.Column(db.Integer, db.ForeignKey('pedidos.id'))

    def __repr__(self):
        return f'<Produto {self.id}>'
    
@dataclass
class User(db.Model):
    __tablename__ = "users"
    id: int = db.Column(db.Integer, primary_key=True)
    date_created: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    name: str = db.Column(db.String(100))
    email: str = db.Column(db.String(100), unique=True)
    password: str = db.Column(db.String(100))
    produtos = db.relationship('Produto', backref='user', lazy=True)
    pedidos = db.relationship('Pedido', backref='user', lazy=True)

    def __str__(self):
        return self.name
    
@dataclass
class Pedido(db.Model):
    __tablename__ = "pedidos"
    id: int = db.Column(db.Integer, primary_key=True)
    status: str = db.Column(db.String, nullable=False)
    date_created: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    update_date: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id: int = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    produtos = db.relationship('Produto', backref='pedido', lazy=True)

    def __repr__(self):
        return f'<Pedido {self.id}>'
