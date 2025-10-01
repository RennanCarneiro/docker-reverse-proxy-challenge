from flask import Flask, send_from_directory
import os

app = Flask(__name__) #cria uma instancia da aplicação flask
'''
@define a rota pra minha aplicação (decorator)
app.rout informa ao flask que a func abaixo deve ser executada quando um usuario acessar a URL associada
'/' rota para raiz
send_from_directory, envia um arqv ao diretorio especificado.
. diretorio atual no docker(/app) que foi definido no docker
Em resumo a func pega o index que está no mesmo dir e envia como resposta HTTP para o cliente
'''
@app.route('/') 
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5001)

