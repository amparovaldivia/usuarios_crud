from usuarios import app
from flask import render_template, redirect, request,session
from usuarios import modelo
from usuarios.modelo.cliente import Cliente


@app.route('/users')
def ver_clientes():
    clientes = Cliente.read_clientes()
    return render_template('leer.html', clientes=clientes)


@app.route('/users/new', methods=['POST'])
def agregar_clientes():
    print(request.form)
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        
    }
    id = Cliente.create(data)
    return redirect(f'/users/{id}')


@app.route('/users/new')
def traer():
    return render_template('crear.html')


@app.route('/users/<int:cliente_id>')
def ver_cliente(cliente_id):
    cliente = Cliente.read_cliente({'id':cliente_id})
    return render_template('html3.html',cliente=cliente)




@app.route('/users/<int:cliente_id>/edit')
def formulario_editar_cliente(cliente_id):
    cliente = Cliente.read_cliente({'id':cliente_id})
    return render_template('html4.html',cliente=cliente)


@app.route('/users/<int:cliente_id>/edit',methods=['POST'])
def editar_cliente(cliente_id):
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'id':cliente_id
    }
    Cliente.update(data=data)
    return redirect(f'/users/{cliente_id}')

@app.route('/users/<int:cliente_id>/destroy')
def destruir_cliente(cliente_id):
    Cliente.delete({'id':cliente_id})
    return redirect('/users')
    