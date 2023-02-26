import pandas as pd
from models import Tarifas

planos = r'C:\Users\Pichau\Desktop\planos.csv'
df = pd.read_csv(planos, index_col=[0, 1], dtype={'Origem': str, 'Destino': str}).squeeze("columns")


def get_price(origem, destino):
    """Retorna o valor da tarifa para uma ligacao considerando uma origem e um destino."""
    return df.loc[(origem, destino)]


def sem_plano(tempo, preco):
    """Calcula o valor total de uma ligacao sem o uso de um plano"""
    valor = tempo * preco
    return valor


def com_plano(tempo, preco, minutos_plano):
    """Calcula o valor total de uma ligacao com o uso de um plano"""
    excedente = tempo - minutos_plano
    if excedente <= 0:
        return 0
    return sem_plano(excedente, preco * 1.1)


def calcula_tarifas(origem, destino, tempo):
    """Calcula as tarifas para uma ligacao, dada a origem, destino e tempo da chamada."""
    preco = get_price(origem, destino)
    preco_sem_plano = sem_plano(tempo, preco)
    tarifas = {"sem_plano": preco_sem_plano}
    for plano, minutos in [('FaleMais30', 30), ('FaleMais60', 60), ('FaleMais120', 120)]:
        preco_com_plano = com_plano(tempo, preco, minutos)
        tarifas[plano] = preco_com_plano

    return tarifas
