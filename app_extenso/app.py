import os
import argparse
import sys
from flask import Flask, jsonify, request, send_from_directory

# Cria app com Flask
app = Flask(__name__)

# Função da tradução dos números inteiros para escrita por extenso
def traduz_inteiro(valor_int):
    # Listas de números por extenso
        unidades = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", 
                    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
        dezenas = ["zero", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        centenas = ["cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

        # Inicio resposta por extenso e string do sinal negativo
        extenso, menos = "", ""

        # Converte entrada para uma lista de caracteres
        digitos = [str(n) for n in valor_int]
        
        # Caso possuo sinal de - adiciona palavra e remove da lista
        if digitos[0] == "-":
            menos = "menos "
            digitos.pop(0)
        
        # Verifica se os caracteres são números de 0 a 9
        for i in digitos:
            if ord(i) < 48 or ord(i) > 57:
                print("\nNúmero especificado incorreto! \nDigite algum número inteiro de -99999 à 99999 no endereço da URL.")
                return jsonify({"extenso":extenso})
                
        # Verifica se o valor de entrada está dentro dos parâmetros exigidos
        if int(valor_int) > 99999 or int(valor_int)<-99999:
            print("\nNúmero especificado incorreto! \nDigite algum número inteiro de -99999 à 99999 no endereço da URL.")
            return jsonify({"extenso":extenso})   
        
        # Função para retornar o valor a cada três digitos por extenso
        def converte_extenso(tres_digitos):

            # Inicia a variável string vazia
            traducao = ""
            # Cria lista de digitos inteiros 
            list_digitos = [int(dig) for dig in tres_digitos]
            # Converte o valor de três digitos recebido para inteiro
            tres_digitos = int(tres_digitos)

            # Caso o valor seja igual a 0
            if tres_digitos == 0:
                traducao = unidades[0]

            # Caso o valor seja igual a 100
            elif tres_digitos == 100:
                traducao = centenas[0]            
            
            # Caso o valor seja de 1 a 99
            elif tres_digitos < 100:
                if tres_digitos % 100 == 0:
                    traducao += ""
                elif tres_digitos % 100 < 20:
                    traducao += unidades[tres_digitos % 100]
                else:
                    if tres_digitos % 10 == 0:
                        traducao += dezenas[list_digitos[1]]
                    else:
                        traducao += dezenas[list_digitos[1]] + " e " + unidades[list_digitos[2]]

            # Caso o valor se de 101 a 999
            elif tres_digitos > 100:
                traducao = centenas[list_digitos[0]]
                if tres_digitos % 100 == 0:
                    traducao += ""
                elif tres_digitos % 100 < 20:
                    traducao += " e " + unidades[tres_digitos % 100]
                else:
                    if tres_digitos % 10 == 0:
                        traducao += " e " + dezenas[list_digitos[1]]
                    else:
                        traducao += " e " + dezenas[list_digitos[1]] + " e " + unidades[list_digitos[2]]

            # Retorna o resultado da tradução
            return traducao

        # Cria e completa uma lista para conter 6 digitos
        digitos_completos = ["0"] * (6-len(digitos))
        digitos_completos.extend(digitos)

        # Inicia variável string para comparação
        compara_txt = ""
        
        # Faz a comparação dos três primeiros digitos e configura escrita
        compara_txt = converte_extenso(digitos_completos[0]+digitos_completos[1]+digitos_completos[2])
        if compara_txt != "zero":
            extenso = compara_txt + " mil"
        
        # Faz a compatação dos três ultimos digitos e configura escrita
        compara_txt = converte_extenso(digitos_completos[3]+digitos_completos[4]+digitos_completos[5]) 
        if extenso == "":
            extenso = compara_txt
        elif extenso != "" and compara_txt != "zero":
            extenso += " e " + compara_txt

        # Adiciona a escrita por extenso do sinal de menos caso exista
        extenso = menos + extenso

        # Exibe e retorna o resultado por extenso
        print("\nResposta: ", extenso)
        return extenso

# Rota para prevenir GET request favicon.ico
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico",
            mimetype="image/vnd.microsoft.icon")

# Rota da lógica principal 
@app.route("/<string:valor_int>", methods = ["GET"])
def traducao_int(valor_int):
    
    try:
        # Apenas em request GET
        if request.method == "GET":
            return jsonify({"extenso":traduz_inteiro(valor_int)}) 
        
    # Exibe o erro caso ocorra
    except Exception as e:
        print("\nProblema detectado:", e)


# Rota da página principal
@app.route('/')
def index():
    # Informação para a página principal
    return "\nDigite algum número inteiro de -99999 à 99999 no endereço da URL."

# Execução principal
if __name__ == '__main__':

    # Recebe o argumento para a porta do servidor local
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default='5000' , help = 'Numeração da porta para gerar servidor')
    args = parser.parse_args()

    # Exibe argumento
    if len(sys.argv) != None:
        print('-->Porta do servidor:', args.port)
    
    print(' * AJUDA PARA ALTERAR ARGUMENTOS DE ENTRADA: python nome_do_script.py -h\n')

    # Roda a aplicação Flask
    app.run(debug=False, host='0.0.0.0', threaded=True, port=args.port)
