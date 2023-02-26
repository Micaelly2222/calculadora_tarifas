## Calculadora de Tarifas

## Linguagens e Ferramentas Utilizadas

* [Python](https://docs.python.org/pt-br/3/tutorial/), linguagem de programação de alto nível
* [Pandas](https://pypi.org/project/pandas/), biblioteca para análise e manipulação de dados
* [FastAPI](https://fastapi.tiangolo.com/), framework Python focado no desenvolvimento de API's
* [Pydantic](https://docs.pydantic.dev/), biblioteca Python útil para validar e analisar dados de entrada em uma aplicação
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/) , linguagem de marcação usada para criar páginas da web
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/), linguagem usada para criar interatividade em páginas da web
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/), biblioteca Python de template que torna mais fácil criar templates dinâmicos para gerar conteúdo HTML
* [Unittest](https://docs.python.org/3/library/unittest.html/), framework de testes unitários em Python 

## Objetivo do Projeto

* O objetivo desse projeto foi de servir uma página da web para calcular a tarifa de ligações usando diferentes planos. 
A página web contém uma tabela onde o usuário seleciona os códigos DDD de origem e destino e o tempo da chamada. Depois de clicar no botão "Enviar", o código JavaScript recupera os dados da tabela, envia-os ao servidor usando um XMLHttpRequest e exibe os resultados na página da web. Aqui está um detalhamento dos arquivos:

* main.py: este arquivo define uma aplicacao FastAPI, para isso usa dois endpoints:
o endpoint “/” retorna a página inicial da aplicação e o endpoint “/tarifas” calcula a tarifa para diferentes planos com base nos dados digitado pelo usuário na tabela. 

* Requirements.txt: este arquivo contém as bibliotecas e versoes utilizadas na aplicação

* index.html: este arquivo contém o código HTML e JavaScript da página web que exibe a tabela

* Tarifas.py : este arquivo contem uma classe que representa as tarifas para diferentes planos. Essa classe é útil para armazenar as tarifas, permitindo que outras partes do código possam acessar esses valores.

* DDEnum.py : este arquivo contem uma classe que representa os DDD permitidos na aplicação. O uso de um Enum ajuda a evitar erros de digitação ou uso indevido de valores não permitidos

* tarifas.py : este arquivo contem uma série de funções para calcular as tarifas de uma ligação . O cálculo das tarifas é feito a partir de um arquivo CSV de planos que contém as informações de origem, destino e preço da ligação

* tests.py  O arquivo contém uma classe de teste que utiliza a biblioteca unittest para verificar se as funções do arquivo tarifas.py estão retornando os valores corretos. O objetivo desses testes é garantir que as funções estão funcionando corretamente e retornando os valores esperados. 

* Em resumo, o código fornece uma pagina da web que permite aos usuários calcular tarifas de ligaçoes com base em diferentes planos. 
