#API = É um lugar para disponibilizar recursos e/ou funcionalidades

#objetivo desta API de teste:
#API para disponibilizar consulta, criação, edição e exclusão de livros.

#URL base:
#localhost

#Endpoints:
#localhost/livros (GET) #Consulta todos os livros.
#localhost/livros (POST) #Inclui novo livro.
#localhost/livros/*id (GET) #Consulta livro pelo ID.
#localhost/livro/*id (PUT) #Atualiza livro pelo ID.
#localhost/livro/*id (DELETE) #Exclui livro pelo ID.

#Quais recursos:
#Livros

from flask import Flask, jsonify, request

app = Flask(__name__)


livros = [
    {
        'id':1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
    },
    {
        'id':2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Howling',
    },
    {
        'id':3,
        'titulo': 'James Clear',
        'autor': 'Habitos Atômicos',
    }
]


#Consultar (TODOS)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar (ID)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#Criar
@app.route('/livros',methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Editar (ID)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
    return jsonify(livros)

#Excluir (ID)
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)


app.run(host='localhost',port=5000,debug=True)