from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from models import db, Llave, Texto

def operacion(texto, llave_list, operacion, max_text_length, max_key_length):
    resultado = []
    text_length = longitud(texto)
    key_length = longitud(llave_list)
    if text_length == 0 and key_length == 0:
        return "Ambos la entrada de texto y la llave estan vacias"
    if text_length == 0:
        return "La entrada de texto no tiene contenido"
    if key_length == 0:
        return "La llave esta vacia"
    if text_length > max_text_length and key_length > max_key_length:
        return "Ambos textos en la entrada de texto y en la llave son muy largos"
    if text_length > max_text_length:
        return "El texto en la entrada de texto es muy largo"
    if key_length > max_key_length:
        return "El texto en la llave es muy largo"
    salir = 0
    i = 0
    lims_llave = len(llave_list) - 1
    lim_llave = limite(0, lims_llave)
    for caracter in texto:
        caracter_num = ord(caracter)
        i = i_plus(i, lims_llave, lim_llave)
        llave = num_llave(llave_list, i)
        if operacion == 1:
            llave = -llave
        for lista in listas:
            salir = l_op(resultado, caracter_num, lista, llave)
            if salir == 1:
                i = i + 1
                break
        else:
            resultado.append(caracter)
    resultado = "".join(resultado)
    save_key(llave_list)
    save_text(texto, resultado, llave_list)
    return resultado

def l_op(resultado, caracter_num, lista, llave):
    lim_inferior = limite_inferior(lista)
    lim_superior = limite_superior(lista)
    if (caracter_num >= lim_inferior and caracter_num <= lim_superior):
        caracter_num = caracter_num + llave
        caracter_num = verificar(caracter_num, lim_inferior, lim_superior)
        resultado.append(caracter_num)
        return 1
    return 0

def num_llave(llave_list, i):
    return ord(llave_list[i])

def i_plus(i, lims_llave, lim_llave):
    if i >= lims_llave:
        return i - lim_llave
    return i

def verificar(caracter, limete_inferior, limite_superior):
    lim = limite(limete_inferior, limite_superior)
    while (caracter < limete_inferior or caracter > limite_superior):
        if caracter < limete_inferior:
            caracter = caracter + lim
        elif caracter > limite_superior:
            caracter = caracter - lim
    return chr(caracter)

def limite_inferior(lista):
    return ord(lista[0])

def limite_superior(lista):
    return ord(lista[(len(lista)-1)])

def limite(limite_inferior, limite_superior):
    return (limite_superior - limite_inferior + 1)

def longitud(text):
    return len(text)

def generar_lista(limite_inferior, limite_superior):
    lista = []
    limite_superior += 1
    for i in range(limite_superior):
        if i < limite_inferior:
            pass
        else:
            character = chr(i)
            lista.append(character)
    return lista

def on_init():
    ctr = generar_lista(32, 47)
    num = generar_lista(48, 57)
    op = generar_lista(58, 64)
    abecedario_mayus = generar_lista(65, 90)
    abecedario = generar_lista(97, 122)
    ls = generar_lista(123, 126)
    return [ctr, num, op, abecedario_mayus, abecedario, ls]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

def save_key(llave):
    with app.app_context():
        existe = Llave.query.filter_by(key=llave).count()
        if existe > 0:
            return
        new_key = Llave(key=llave)
        db.session.add(new_key)
        db.session.commit()

def save_text(text_e, text_r, llave):
    key_found = Llave.query.filter_by(key=llave).first()
    existe = Texto.query.filter_by(texto_inicial=text_e, texto_resultante=text_r, key_id=key_found.id).count()
    if existe > 0:
        return
    new_text = Texto(texto_inicial=text_e, texto_resultante=text_r, key_id=key_found.id)
    db.session.add(new_text)
    db.session.commit()

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def h_operation():
    if request.method == 'POST':
        entry_text = request.form['entry_text']
        key = request.form['key']
        oper = int(request.form['operacion'])
        result = operacion(texto=entry_text, llave_list=key, operacion=oper, max_text_length=250, max_key_length=50)
        return render_template('result.html', text=entry_text, key=key, result=result)
    return render_template('index.html')

if __name__ == "__main__":
    listas = on_init()
    app.run(debug=True)