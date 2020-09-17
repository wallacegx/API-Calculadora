from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
from flask_cors import CORS
from math import sqrt

app = Flask(__name__)

CORS(app)
run_with_ngrok(app)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/')
def root():
    return 'Digite qual operação gostaria de fazer entre as opções <br>' + \
           '/sum <br>' + \
           '/Subtraction'

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/sum?value1=<value1>&value2=<value2>', methods=['GET'])
def sum(value1,value2):
    try:
        valor1 = int(value1);
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2);
    except:
        return 'Segundo valor inválido.'

    ret = { "message" : valor1 + valor2 }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/subtraction?value1=<value1>&value2=<value2>', methods=['GET'])
def subtraction(value1,value2):
    try:
        valor1 = int(value1);
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2);
    except:
        return 'Segundo valor inválido.'

    ret = { "message" : valor1 - valor2 }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/division?value1=<value1>&value2=<value2>', methods=['GET'])
def division(value1,value2):
    try:
        valor1 = int(value1);
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2);
    except:
        return 'Segundo valor inválido.'

    ret = { "message" : valor1 / valor2 }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/multiplication?value1=<value1>&value2=<value2>', methods=['GET'])
def multiplication(value1,value2):
    try:
        valor1 = int(value1);
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2);
    except:
        return 'Segundo valor inválido.'

    ret = { "message" : valor1 * valor2 }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/squareroot?value=<value>', methods=['GET'])
def squareroot(value):
    try:
        valor1 = int(value);
    except:
        return 'Valor inválido.'

    ret = { "message" : sqrt(valor1) }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/power?base=<base>&exponent=<exponent>', methods=['GET'])
def power(base,exponent):
    try:
        li_base = int(base);
    except:
        return 'Base Inválida.'

    try:
        li_exponent = int(exponent);
    except:
        return 'Expoente inválido.'

    ret = { "message" : li_base ** li_exponent }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/arithmeticaverage?value1=<value1>&value2=<value2>&value3=<value3>', methods=['GET'])
def arithmeticaverage(value1,value2,value3):
    try:
        valor1 = int(value1);
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2);
    except:
        return 'Segundo valor inválido.'

    try:
        valor3 = int(value3);
    except:
        return 'Terceiro valor inválido.'

    ret = { "message" : (valor1 + valor2 + valor3) / 3 }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/harmonicmean?value1=<value1>&value2=<value2>&value3=<value3>', methods=['GET'])
def harmonicmean(value1,value2,value3):
    try:
        valor1 = int(value1);
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2);
    except:
        return 'Segundo valor inválido.'

    try:
        valor3 = int(value3);
    except:
        return 'Terceiro valor inválido.'

    ret = { "message" : ((1 / valor1) + (1 / valor2) * (1 / valor3)) / 3 }

    return jsonify(ret)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/mod?value1=<value1>&value2=<value2>&value3=<value3>', methods=['GET'])
def mod(value1,value2,value3):
    try:
        valor1 = int(value1);
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2);
    except:
        return 'Segundo valor inválido.'

    try:
        valor3 = int(value3);
    except:
        return 'Terceiro valor inválido.'

    ret = { "message" : (valor1 * valor2 * valor3) / 3 }

    return jsonify(ret)

app.run()