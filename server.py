from doctest import debug
from usuarios import app
from usuarios.controllers import controlador
if __name__=='__main__':
    app.run(debug=True)