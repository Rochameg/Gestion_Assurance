from . import db
from flask_login import UserMixin
from datetime import datetime
from enum import Enum


class StatusEnum(Enum):
    CLIENT = "client"
    ADMIN = "admin"
    
class Client(db.Model):
    __tablename__ = 'clients'
    id_client = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    date_naissance = db.Column(db.Date)
    adresse = db.Column(db.String(255))
    telephone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    date_inscription = db.Column(db.Date, default=datetime.utcnow)

    contrats = db.relationship('Contrat', backref='client', lazy=True)
    users = db.relationship('User', backref='client', lazy=True)


class Contrat(db.Model):
    __tablename__ = 'contrats'
    id_contrat = db.Column(db.Integer, primary_key=True)
    numero_contrat = db.Column(db.String(50), unique=True, nullable=False)
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id_client'), nullable=False)
    date_debut = db.Column(db.Date)
    date_fin = db.Column(db.Date)
    montant = db.Column(db.Numeric(10, 2))
    statut = db.Column(db.String(20), default='actif')

    paiements = db.relationship('Paiement', backref='contrat', lazy=True)


class Paiement(db.Model):
    __tablename__ = 'paiements'
    id_paiement = db.Column(db.Integer, primary_key=True)
    id_contrat = db.Column(db.Integer, db.ForeignKey('contrats.id_contrat'), nullable=False)
    date_paiement = db.Column(db.Date)
    montant = db.Column(db.Numeric(10, 2))
    mode_paiement = db.Column(db.String(50))
    statut = db.Column(db.String(20), default='validé')


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))
    role = db.Column(db.Enum(StatusEnum), default=StatusEnum.CLIENT)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
