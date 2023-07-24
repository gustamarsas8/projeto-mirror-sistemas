from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Produto, User, Pedido
from flask_login import LoginManager, login_required

app = Flask(__name__) 
app.config["SECRET_KEY"] = 'secret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#---------------------------------------------------------- ROTAS DO PROJETO


@app.route("/register", methods= ["POST"]) 

def register():
        data = request.get_json()
        user = User()
        user.name = data["name"]
        user.email = data["email"]
        user.password = generate_password_hash(data["password"])

        db.session.add(user)
        db.session.commit()
        return ("Usuário criado, verifique a lista de usuários.")



# Aba de login do usuário
@app.route("/login", methods=["POST"]) 
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return("Credênciais incorretas")
    
    if not check_password_hash(user.password, password):

        return("Credênciais incorretas")

    return ("Usuário acaba de ser logado!")

# Aba de atualizar senha
@app.route('/update_password', methods=["GET"])
def show_update_password_form():
    return ('Senha')

@app.route('/update_password', methods=["POST"])
def update_password():
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    return 'Senha atualizada com sucesso'


#---------------------------------------------------------- USUÁRIO


# Aba de listar Usuário
@app.route('/listar_usuarios', methods=["GET"])
def list_users():

    users = User.query.all()

    return jsonify(users)

# Aba de atualizar Usuário
@app.route('/atualizar_usuario/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'Usuário não encontrado'}), 404

        data = request.get_json()
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']

        db.session.commit()

        return jsonify({'message': 'Usuário atualizado com sucesso'}), 200



# Aba de deletar Usuário
@app.route('/deletar_usuario/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'Usuário deletado com sucesso'}), 200


#---------------------------------------------------------- PRODUTO

# Aba de criar produto
@app.route('/criar_produto', methods=['POST'])
def criar_produto():
    data = request.get_json()

    nome = data['name']
    descricao = data['description']
    preco = float(data['price'])
    user_id = data['user_id']
    novo_produto = Produto(name=nome, description=descricao, price=preco, user_id=user_id)
    db.session.add(novo_produto)
    db.session.commit()

    return jsonify({'message': 'Produto criado com sucesso!'}), 201

# Aba de atualizar produto
@app.route('/atualizar_produto/<int:produto_id>', methods=["PUT"])
def atualizar_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404

    data = request.get_json()
    if 'name' in data:
        produto.name = data['name']
    if 'price' in data:
        produto.price = data['price']
    if 'description' in data:
        produto.description = data['description']

    db.session.commit()

    return jsonify({'message': 'Produto atualizado com sucesso'}), 200

# Aba de deletar produto
@app.route('/deletar_produto/<int:produto_id>', methods=['DELETE'])
def deletar_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404

    db.session.delete(produto)
    db.session.commit()

    return jsonify({'message': 'Produto deletado com sucesso'}), 200

# Aba de listar produtos
@app.route('/listar_produtos', methods=["GET"])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify(produtos)


# Aba de listar produto (:ID)
@app.route('/listar_produto/<int:id>', methods=["GET"])
def listar_produto(id):
    produto = Produto.query.get(id)

    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404

    return jsonify(produto), 200

#---------------------------------------------------------- PEDIDO

# Aba de criar pedido
@app.route('/criar_pedido', methods=["POST"])
def criar_pedido():
    data = request.get_json()
    status = data['status']
    user_id = data['user_id']
    produto_id = data['produto_id']

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    novo_pedido = Pedido(status=status, user_id=user_id, produto_id=produto_id)
    db.session.add(novo_pedido)
    db.session.commit()

    return jsonify({'message': 'Pedido criado com sucesso!'}), 201

# Aba de atualizar produto
@app.route('/atualizar_pedido/<int:pedido_id>', methods=["PUT"])
def atualizar_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404

    data = request.get_json()
    if 'status' in data:
        pedido.status = data['status']

    db.session.commit()

    return jsonify({'message': 'Pedido atualizado com sucesso'}), 200

# Aba de deletar pedidos
@app.route('/deletar_pedidos/<int:pedido_id>', methods=["DELETE"])
def deletar_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404

    db.session.delete(pedido)
    db.session.commit()

    return jsonify({'message': 'Pedido deletado com sucesso'}), 200

# Aba de listar pedidos
@app.route('/listar_pedidos', methods=["GET"])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify(pedidos), 200

# Aba de listar pedidos (:ID)
@app.route('/listar_pedido/<int:id>', methods=["GET"])
def listar_pedido(id):
    pedido = Pedido.query.get(id)

    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404

    return jsonify(pedido), 200
