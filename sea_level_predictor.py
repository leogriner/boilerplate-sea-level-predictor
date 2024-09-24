import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Ler os dados do arquivo
    df = pd.read_csv('boilerplate-sea-level-predictor/epa-sea-level.csv')

    # Criar gráfico de dispersão
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])  # Gráfico de dispersão

    # Criar a primeira linha de melhor ajuste
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_level_pred = res.intercept + res.slope * years_extended
    ax.plot(years_extended, sea_level_pred, 'r', label='Best fit line (1880-2050)')

    # Criar a segunda linha de melhor ajuste (a partir do ano 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    recent_years_extended = pd.Series([i for i in range(2000, 2051)])
    recent_sea_level_pred = res_recent.intercept + res_recent.slope * recent_years_extended
    ax.plot(recent_years_extended, recent_sea_level_pred, 'g', label='Best fit line (2000-2050)')

    # Adicionar rótulos e título
    ax.set_title('Rise in Sea Level')  # Título do gráfico
    ax.set_xlabel('Year')  # Rótulo do eixo X
    ax.set_ylabel('Sea Level (inches)')  # Rótulo do eixo Y

    # Salvar o gráfico e retornar os dados para teste 
    plt.savefig('sea_level_plot.png')
    return plt.gca()
