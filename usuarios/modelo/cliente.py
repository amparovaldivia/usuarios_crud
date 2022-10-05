from usuarios.configuracion.mysqlconnection import BaseDeDatos
class Cliente:
    def __init__(self,data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.creado_en=data['creado_en']
        self.actualizado_en=data['actualizado_en']
    @classmethod
    def create(cls,data):
        query='INSERT INTO usuario(nombre,apellido,email)values(%(nombre)s,%(apellido)s,%(email)s);'
        resultado = BaseDeDatos('datos_clientes').query_db(query, data)
        return resultado

    @classmethod
    def read_clientes(cls):
        query = 'SELECT * FROM usuario;'
        resultados = BaseDeDatos('datos_clientes').query_db(query)
        clientes = []
        for resultado in resultados:
            clientes.append(cls(resultado))
        return clientes

    @classmethod
    def read_cliente(cls, data):
        query = 'SELECT * FROM usuario WHERE id=%(id)s;'
        resultados = BaseDeDatos('datos_clientes').query_db(query, data)
        cliente = cls(resultados[0])
        return cliente

    @classmethod
    def update(cls, data):
        query = 'UPDATE usuario SET nombre=%(nombre)s, apellido=%(apellido)s,email=%(email)s WHERE id=%(id)s ;'
        resultado = BaseDeDatos('datos_clientes').query_db(query, data)
        return resultado

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM usuario WHERE id=%(id)s;'
        resultado = BaseDeDatos('datos_clientes').query_db(query, data)
        return resultado
