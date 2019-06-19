"""
Desafio 107

Problema: Crie um módulo chamado moedas.py que tenha as funções incorporadas
          aumentar(), diminuir(), dobro() e metade().

          Faça também um programa que importe esse módulo e use algumas dessas
          funçóes.

Resolução do problema:
"""


def moeda(valor):
    """
    -> Realiza formatação do valor passado para dinheiro
    :param valor: Valor do dinheiro
    :return: Retorna o parâmetro passado em formato de reais (R$)
    """
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, bonus, view=True):
    """
    -> Realiza o calculo de aumento sálarial e retorna seu valor
    :param valor: Valor do dinheiro
    :param bonus: Porcentagem do bônus
    :param view: Visualizar ou não retorno formatado
    :return: Retorna valor com aumento sálarial
    """
    if not view:
        return moeda(valor + (valor * bonus / 100))
    else:
        return valor + (valor * bonus / 100)


def diminuir(valor, onus, view=True):
    """
    -> Realiza o calculo de redução salárial e retorna seu valor
    :param valor: Valor do dinheiro
    :param onus: Porcentagem do ônus
    :param view: Visualizar ou não retorno formatado
    :return: Retorna o valor da redução salárial
    """
    if not view:
        return moeda(valor - (valor * onus / 100))
    else:
        return valor - (valor * onus / 100)


def dobro(valor, view=True):
    """
    -> Realiza o calculo de dobro salárial
    :param valor: Valor do dinheiro
    :param view: Visualizar ou não retorno formatado
    :return: Retorna o valor dobrado
    """
    if not view:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor, view=True):
    """
    -> Realiza o calculo de metade salárial
    :param valor: Valor do dinheiro
    :param view: Visualizar ou não retorno formatado
    :return: Retorna a metade do valor
    """
    if not view:
        return moeda(valor / 2)
    else:
        return valor / 2
