from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def listas_dcicionarios():
    usuarios = [
        {'Id': 1, 'Titulo': "|Guerra |", "Conteudo": "|Conteudo da primeira postagem|"},
        {'Id': 2, 'Titulo': "|Guerras|", "Conteudo": "|Conteudo da segunda postagem|"},
        {'Id': 3, 'Titulo': "|Guerras|", "Conteudo": "|Conteudo da terceira postagem|"},
        {'Id': 4, 'Titulo': "|Guerras|", "Conteudo": "|Conteudo da quarta postagem|"},
  
    ]
        
    return render_template('Blog.html', usuarios=usuarios)


if __name__ == '__main__':
    app.run(debug=True)
    

