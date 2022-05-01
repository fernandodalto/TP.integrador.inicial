import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("Cotizacion.csv",header=0)


def promedio_precios():
    df = pd.DataFrame(datos)
    promedio_1 = df['googl'].mean().round(2)
    promedio_2 = df['aapl'].mean().round(2)
    print('El precio promedio de la acción de Google fue',promedio_1,'u$s')
    print('El precio promedio de la acción de Aapl fue',promedio_2,'u$s')
    print('''
********************************************************************
    ''')

def moda_precios():
    df = pd.DataFrame(datos)
    moda_1 = df['googl'].round(0).mode()
    moda_2 = df['aapl'].round(0).mode()
    print('''La moda es el valor, que dentro de un conjunto de datos, se repite
el mayor numero de veces. En este caso:''')
    print('Googl tiene 2 valores que se repiten con la misma frecuencia:\n',moda_1)
    print('Aapl por el otro lado tiene una sola moda y es:\n',moda_2)
    print('''
********************************************************************
    ''')



def detalle_cotizaciones():
    pri_pr_googl = datos.at[251,"googl"]
    ult_pr_googl = datos.at[0,"googl"]
    print('Googl arrancó el año cotizando a:',pri_pr_googl,'usd')
    print('Googl terminó el año cotizando a:',ult_pr_googl,'usd')
    pri_pr_aapl = datos.at[251,"aapl"]
    ult_pr_aapl = datos.at[0,"aapl"]
    print('Aapl arrancó el año cotizando a:',pri_pr_aapl,'usd')
    print('Aapl terminó el año cotizando a:',ult_pr_aapl,'usd')
    print('''
********************************************************************
    ''')



def variacion_porcentual():
    pri_pr_googl = datos.at[251,"googl"]
    ult_pr_googl = datos.at[0,"googl"]
    pri_pr_aapl = datos.at[251,"aapl"]
    ult_pr_aapl = datos.at[0,"aapl"]
    var_porc_googl = (((ult_pr_googl/pri_pr_googl)-1)*100).round(2)
    var_porc_aapl = (((ult_pr_aapl/pri_pr_aapl)-1)*100).round(2)
    print('La variación porcentual anual del precio de las acciones de googl fue de un',var_porc_googl,'%')
    print('La variación porcentual anual del precio de las acciones de aapl fue de un',var_porc_aapl,'%')
    print()
    if var_porc_googl > var_porc_aapl:
        print('La mejor inversión hubiese sido comprar acciones de Googl')
    elif var_porc_googl < var_porc_aapl:
        print('La mejor inversión hubiese sido comprar acciones de Aapl')
    else:
        print('Invertir en cualquiera de los activos hubiera arrojado el mismo retorno')
    print('''
********************************************************************
    ''')


def mov_precios():
    df = pd.DataFrame(datos)
    promedio_1 = df['googl'].mean().round(2)
    promedio_2 = df['aapl'].mean().round(2)
    dias_cot_1 = (df['googl']).count()
    dias_cot_2 = (df['aapl']).count()
    count_1 = (df['googl']>promedio_1).sum()
    count_2 = (df['aapl']>promedio_2).sum()
    print('De los',dias_cot_1,'días de cotización,',count_1,'días Googl cotizó por encima del precio promedio anual')
    print('De los',dias_cot_2,'días de cotización,',count_2,'días Aapl cotizó por encima del precio promedio anual')
    print('''
********************************************************************
    ''')


def graficos_acciones():

    data = pd.read_csv("Cotizacion_mensual.csv",header=0)

    x = data['date']
    y = data['googl']

    plt.title('Gráfico Mensual cotización Googl', fontdict = {'fontweight':'bold'})
    plt.xlabel('date', fontsize = 15, fontdict = {'fontweight':'bold'})
    plt.ylabel('U$S', fontsize = 13, fontdict = {'fontweight':'bold'})
    plt.plot(x,y)
    plt.show()

    x = data['date']
    y = data['aapl']

    plt.title('Gráfico Mensual cotización Aapl', fontdict = {'fontweight':'bold'})
    plt.xlabel('date', fontsize = 15, fontdict = {'fontweight':'bold'})
    plt.ylabel('U$S', fontsize = 13, fontdict = {'fontweight':'bold'})
    plt.plot(x,y)
    plt.show()

def grafico_comparativo():
    data = pd.read_csv("Cotizacion_mensual.csv",header=0)
    plt.xlabel('date', fontsize = 15, fontdict = {'fontweight':'bold'})
    plt.ylabel('U$S', fontsize = 13, fontdict = {'fontweight':'bold'})
    plt.title('Gráfico comparativo', fontdict = {'fontweight':'bold'})
    plt.plot(data.date, data.googl,'b.-', label="Googl")
    plt.plot(data.date, data.aapl,'r.-', label = "Aapl")
    plt.legend()
    plt.show()   

def analisis_volatilidad():
    data = pd.read_csv("Cotizacion.csv",header=0)
    calc_1= np.log(data['googl']/data['googl'].shift())
    calc_2 = np.log(data['aapl']/data['aapl'].shift())
    volatilidad_googl = ((calc_1.std()*252**.5).round(2))*100
    volatilidad_aapl = ((calc_2.std()*252**.5).round(2))*100
    print('La volatilidad de las acciones de Googl es de un',volatilidad_googl,'%','anual')
    print('La volatilidad de las acciones de Aapl es de un',volatilidad_aapl,'%','anual')

    if abs((volatilidad_aapl - volatilidad_googl)) < 10:
        print('La diferencia entre volatilidades no es representativa')
    else:
        print('La diferencia entre volatilidades es representativa')
        print('''
********************************************************************
    ''')


if __name__ == '__main__':

    print('Análisis comparativo del precio de las acciones de Googl y Aapl durante el 2021')
    print()
    
    detalle_cotizaciones()
    promedio_precios()
    mov_precios()
    moda_precios()
    analisis_volatilidad()
    variacion_porcentual()
    graficos_acciones()
    grafico_comparativo()
