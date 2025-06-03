from flask import Flask, request, redirect, jsonify
import string, random, json, os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Liberar CORS para todas as rotas e origens

ARQUIVO_URLS = 'urls.json'

# Função para ler URLs do arquivo JSON
def ler_urls():
    if not os.path.exists(ARQUIVO_URLS):
        return []
    with open(ARQUIVO_URLS, 'r') as f:
        return json.load(f)

# Função para salvar URLs no arquivo JSON
def salvar_urls(urls):
    with open(ARQUIVO_URLS, 'w') as f:
        json.dump(urls, f, indent=4)

def gerar_id(tamanho=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

@app.route('/api/shorten', methods=['POST'])
def encurtar():
    dados = request.get_json()
    url_longa = dados.get('longUrl')
    if not url_longa:
        return jsonify({'error': 'longUrl é obrigatório'}), 400

    short_id = gerar_id()

    urls = ler_urls()

    # Evitar duplicação de short_id (pode gerar repetido)
    while any(u['short_id'] == short_id for u in urls):
        short_id = gerar_id()

    urls.append({'short_id': short_id, 'long_url': url_longa})
    salvar_urls(urls)

    return jsonify({'shortUrl': f'http://localhost:5000/{short_id}'})

@app.route('/<short_id>')
def redirecionar(short_id):
    urls = ler_urls()
    resultado = next((u for u in urls if u['short_id'] == short_id), None)
    if resultado:
        return redirect(resultado['long_url'])
    return 'URL não encontrada', 404

if __name__ == '__main__':
    app.run(debug=True)
