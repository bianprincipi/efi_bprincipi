from app import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('marca.id'))
    costo = db.Column(db.Float, nullable=False)

    modelo = db.relationship('Modelo', backref='equipos')
    categoria = db.relationship('Marca', backref='equipos')
    stock = db.relationship('Stock', backref='equipo', uselist=False)
    caracteristicas = db.relationship('Caracteristica', backref='equipo')
    accesorios = db.relationship('Accesorio', backref='equipo')

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'))

    fabricante = db.relationship('Fabricante', backref='modelos')

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    pais_origen = db.Column(db.String(64), nullable=False)

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(64), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'))

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(128), nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'))

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), nullable=False)
    contacto = db.Column(db.String(64), nullable=False)

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(64), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'))
