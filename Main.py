import os
from flask import Flask, jsonify
from flask_cors import CORS
from math import sqrt

app = Flask(__name__)

CORS(app)

# ----------------------------------------------------------------------------------------------------------------------


@app.route('/')
def root():
    return 'Digite qual operação gostaria de fazer entre as opções <br> <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/sum/primeiro valor/segundo valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/subtraction/primeiro valor/segundo valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/division/primeiro valor/segundo valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/multiplication/primeiro valor/segundo valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/squareroot/valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/power/base/expoente <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/arithmeticaverage/primeiro valor/segundo valor/terceiro valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/harmonicmean/primeiro valor/segundo valor/terceiro valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/mod/primeiro valor/segundo valor/terceiro valor <br>'


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/sum/<value1>/<value2>', methods=['GET'])
def somar(value1, value2):

    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    ret = { "Resultado" : valor1 + valor2 }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/subtraction/<value1>/<value2>', methods=['GET'])
def subtraction(value1,value2):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    ret = { "Resultado" : valor1 - valor2 }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/division/<value1>/<value2>', methods=['GET'])
def division(value1,value2):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    ret = { "Resultado" : valor1 / valor2 }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/multiplication/<value1>/<value2>', methods=['GET'])
def multiplication(value1,value2):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    ret = { "Resultado" : valor1 * valor2 }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/squareroot/<value>', methods=['GET'])
def squareroot(value):
    try:
        valor1 = int(value)
    except:
        return 'Valor inválido.'

    ret = { "Resultado" : sqrt(valor1) }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/power/<base>/<exponent>', methods=['GET'])
def power(base,exponent):
    try:
        li_base = int(base)
    except:
        return 'Base Inválida.'

    try:
        li_exponent = int(exponent)
    except:
        return 'Expoente inválido.'

    ret = { "Resultado" : li_base ** li_exponent }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/arithmeticaverage/<value1>/<value2>/<value3>', methods=['GET'])
def arithmeticaverage(value1,value2,value3):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    try:
        valor3 = int(value3)
    except:
        return 'Terceiro valor inválido.'

    ret = { "Resultado" : (valor1 + valor2 + valor3) / 3 }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/harmonicmean/<value1>/<value2>/<value3>', methods=['GET'])
def harmonicmean(value1,value2,value3):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    try:
        valor3 = int(value3)
    except:
        return 'Terceiro valor inválido.'

    ret = { "Resultado" : 3 / ((1 / valor1) + (1 / valor2) + (1 / valor3)) }

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/mod/<value1>/<value2>/<value3>', methods=['GET'])
def mod(value1,value2,value3):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    try:
        valor3 = int(value3)
    except:
        return 'Terceiro valor inválido.'

    dicionario = {}
    array = [valor1, valor2, valor3]

    for numeros in array:
        try:
            dicionario[str(numeros)] = dicionario[str(numeros)] + 1
        except:
            dicionario[str(numeros)] = 1

    if dicionario[max(dicionario, key=dicionario.get)] == 1:
        ret = { "Resultado" : str(dicionario.keys()) }
    else:
        ret = { "Resultado" : (max(dicionario, key=dicionario.get)) }

    return jsonify(ret)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
