from flask import Flask, jsonify, request # --\\-- jsonify é utilizado para interagir com dados http

app = Flask(__name__) # a utilizaçao do _name_, ajuda o flask a achar o local da aplicacao

usuariosData = []

@app.route('/api/acesso', methods=['GET']) # api irá responder requests posts quando essa rota for acessada
def verificarAcesso():
    rfid = request.args.get('rfid')
    if not rfid: 
        return jsonify({'error': 'RFID não fornecido'}), 400 # se nao for fornecido um rfid, ele entrara nessa logica entregando um erro

    usuario = next((u for u in usuariosData if u['rfid'] == rfid), None) # ele verifica se usuariosData esta o rfid fornecido
    
    if usuario:
        return jsonify({'mensagem': 'Acesso permitido', 'usuario': usuario['nome']}), 200 # se for encontrado, ele acessará normalmente
    else:
        return jsonify({'mensagem': 'Acesso negado'}), 403 # se nao for encontrado, ele retornara erro 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # inicia o servidor