# Conversão de numero inteiro para escrita por extenso

Aplicação para conversão de números inteiros, fornecidos em uma requisição GET de um servidor HTTP, para escrita por extenso em um JSON. 

## Estrutura do projeto

app/	

	'-|app.py
	
	'-|README.md
	
	'-|requirements.txt
	
	'-|teste_app.py

## Pré-requisitos

Seguem abaixo os requisitos para rodar a aplicação e junto os comandos sugeridos para instalação, caso esteja usando Ubuntu.

* Python 3: 		sudo apt-get install python3
* Pip3:			sudo apt-get install python3-pip 
* Flask:		pip3 install Flask
* Pytest		pip3 install pytest

## Argumentos de entrada

É possível alterar a porta onde será gerado o servidor local (padrão:8000).

* -h				--Ajuda
* -p 5000			--Numeração da porta para gerar servidor

## Instruções de uso

* A aplicação pode ser aberta no navegador a partir do servidor local e porta ativa (ex.:http://localhost:5000).
* Na sequência é possível fornecer os números inteiros de -99999 à 99999 para efetuar a conversão dos digitos para escrita por extenso (ex.:http://localhost:5000/256).
* Na página aparecerá o resultado da chave em JSON (ex.: {"extenso":"duzentos e cinquenta e seis"}).
* Para executar os testes pré-definidos e avaliar a consistência do programa conforme alguns resultados esperados pode-se executar o pytest com o comando "py.test .\testes\teste_extenso.py".

## Autor

* **Augusto Abling** - *Janeiro 2020*
