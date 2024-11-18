import numpy as np

Mean_VarianceStandard_Deviation_Calculator = {

    }

def media(matriz):
    Mean_VarianceStandard_Deviation_Calculator['mean'] = [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), matriz.mean()]


def variancia(matriz):
    Mean_VarianceStandard_Deviation_Calculator['variance'] = [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), matriz.var()]


def desvio_padrao(matriz):
    Mean_VarianceStandard_Deviation_Calculator['standard deviation'] = [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), matriz.std()]


def maximo(matriz):
    Mean_VarianceStandard_Deviation_Calculator['max'] = [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), matriz.max()]


def minimo(matriz):
    Mean_VarianceStandard_Deviation_Calculator['min'] = [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), matriz.min()]

def soma(matriz):
    Mean_VarianceStandard_Deviation_Calculator['sum'] = [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), matriz.sum()]


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matriz = np.array(list).reshape(3, 3)
    
    media(matriz)
    variancia(matriz)
    desvio_padrao(matriz)
    maximo(matriz)
    minimo(matriz)
    soma(matriz)
    
    return Mean_VarianceStandard_Deviation_Calculator
