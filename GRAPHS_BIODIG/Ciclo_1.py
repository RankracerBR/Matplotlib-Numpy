import numpy as np
from scipy.interpolate import interp1d, lagrange
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

#1
dias = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
                 23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,
                 43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60], dtype = float)

temperatura_biodig = np.array([30.7, 40.6, 40.7, 41.2, 40.9, 40.8, 40.7, 40.6,
                               40.7, 40.5, 41.2, 40.5, 40.4, 40.8, 40.6, 40.5,
                               40.3, 40.6, 40.4, 40.5, 40.6, 40.6, 40.8, 40.5, 
                               40.7, 40.4, 40.8, 41.2, 41.3, 40.9, 40.3, 40.6, 
                               41.2, 40.7, 40.5, 40.6, 40.9, 40.7, 40.8, 40.6, 
                               39.2, 40.5, 40.9, 41.3, 40.9, 40.7, 40.6, 40.5, 
                               40.8, 40.5, 41.2, 40.9, 41.2, 40.4, 40.8, 40.8, 
                               40.7, 41.3, 41.2, 41.3, 41.2], dtype = float)

spline = interp1d(dias, temperatura_biodig, kind='cubic')

dias_novo = np.linspace(0, 60, 1000)
temperatura_biodig_novo = spline(dias_novo)

fig = plt.figure(figsize=(5, 6))  # Define o tamanho da figura

ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(dias, temperatura_biodig, c='red')
ax1.plot(dias_novo, temperatura_biodig_novo, c='green')
ax1.set_xlabel('Dias')
ax1.set_ylabel('Temperatura Biodigestor', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Criando um segundo eixo y
ax2 = ax1.twinx()
ax2.set_ylabel('Outro Eixo Y', color='blue')
ax2.plot([], [])  # Para criar uma linha vazia apenas para incluir no gráfico
ax2.tick_params(axis='y', labelcolor='blue')

# Define os limites do eixo y
ax1.set_ylim(0, 60)
ax2.set_ylim(0, 60)
ax1.grid(axis='both')

plt.grid(True)
plt.show()

#2
recirculacao = np.array([
    0, 1, 126, 158, 275, 231, 297, 240, 109, 271, 310, 198, 147, 287, 478,
    226, 396, 470, 542, 638, 578, 555, 515, 581, 517, 577, 514, 608, 594,
    567, 566, 623, 453, 474, 398, 506, 399, 339, 335, 366, 200, 78, 302, 205,
    87, 498, 507, 633, 551, 625, 10, 46, 39, 32, 33, 31, 35, 37, 44, 40, 17], dtype = float)

spline_2 = interp1d(dias,recirculacao, kind='cubic')

dias_novo_2 = np.linspace(0,60,1000)
recirculacao_novo = spline_2(dias_novo_2)

plt.scatter(dias,recirculacao)
plt.plot(dias_novo_2, recirculacao_novo, c = 'green' )
plt.xlabel('Dias')
plt.ylabel('Recirculação')
plt.grid()
plt.show()

#3
ph_inferior = np.array([3.80, 3.30, 3.40, 3.63, 3.21, 3.23, 3.77, 3.52, 3.52, 3.54, 3.82, 4.12, 4.10, 3.80,
                        4.29, 4.45, 4.85, 4.22, 4.33, 4.49, 4.01, 3.98, 4.40, 4.52, 4.48, 4.92, 4.97, 4.78,
                        5.06, 5.02, 4.95, 4.96, 4.96, 4.97, 4.76, 4.79, 4.97, 5.25, 5.35, 5.27, 5.33, 5.35,
                        4.95, 5.00, 4.95, 5.02, 4.97, 5.01, 5.03, 4.97, 4.91, 5.04, 4.94, 4.95, 4.92, 4.94,
                        4.97, 4.97, 5.01, 4.99, 4.98], dtype = float)

ph_superior = np.array([3.70, 3.51, 3.54, 3.65, 3.94, 4.47, 4.64, 4.31, 4.33, 4.43, 4.48, 4.83, 5.08, 4.87,
                        5.11, 5.29, 5.60, 5.27, 5.30, 5.43, 5.04, 4.95, 5.58, 5.44, 5.29, 5.46, 5.55, 5.49,
                        5.63, 5.56, 5.65, 5.64, 5.62, 5.58, 5.18, 5.22, 5.45, 5.56, 5.58, 5.57, 5.58, 5.56,
                        5.23, 5.21, 5.21, 5.23, 5.21, 5.19, 5.20, 5.17, 5.16, 5.16, 5.15, 5.16, 5.15, 5.16,
                        5.18, 5.20, 5.18, 5.20, 5.21], dtype = float)

f_inferior = interp1d(dias, ph_inferior, kind='cubic')
f_superior = interp1d(dias, ph_superior, kind='cubic')


dias_interp = np.linspace(0, 60, 1000)  
ph_inferior_interp = f_inferior(dias_interp)
ph_superior_interp = f_superior(dias_interp)

# Plot dos dados originais e das curvas interpoladas
plt.plot(dias, ph_inferior, 'ro', label='pH Inferior')
plt.plot(dias, ph_superior, 'bo', label='pH Superior')
plt.plot(dias_interp, ph_inferior_interp, 'r-', label='pH Inferior (Interpolado)')
plt.plot(dias_interp, ph_superior_interp, 'b-', label='pH Superior (Interpolado)')
plt.xlabel('Dias')
plt.ylabel('pH')
plt.legend()
plt.grid(True)
plt.show()

#4
producao_biogas = np.array([0, 486, 218, 825, 1335, 1328, 861, 743, 494, 561, 297, 
                            252, 321, 275, 205, 177, 84, 138, 281, 218, 149, 88, 
                            184, 228, 284, 198, 236, 189, 176, 162, 132, 193, 168, 
                            93, 322, 141, 199, 306, 288, 367, 249, 136, 102, 437, 
                            423, 50, 0, 0, 0, 0, 1, 0, 0, 2, 0, 3, 3, 1, 2, 3, 7], dtype = float)

spline_3 = interp1d(dias, producao_biogas, kind='cubic')

dias_novo_3 = np.linspace(0,60,1000)
producao_biogas_novo = spline_3(dias_novo_3)

plt.scatter(dias,producao_biogas)
plt.plot(dias_novo_3,producao_biogas_novo, c = 'orange' )
plt.xlabel('Dias')
plt.ylabel('Produção Biogás')
plt.grid()
plt.show()

#5
drenagem = np.array([0.000, 21.628, 18.169, 36.029, 65.759, 74.179, 42.418, 40.287, 27.513, 32.649, 
                     24.361, 19.244, 19.259, 23.515, 27.540, 16.250, 20.154, 25.386, 35.861, 31.684, 
                     31.404, 29.977, 29.432, 31.458, 34.927, 31.981, 32.632, 31.399, 30.924, 31.811, 
                     28.943, 30.353, 29.178, 25.256, 28.496, 26.921, 24.243, 27.862, 26.049, 28.102, 
                     15.465, 9.618, 21.604, 25.375, 23.182, 21.077, 21.400, 21.785, 20.764, 21.077, 
                     0.495, 1.246, 1.544, 1.365, 1.245, 1.456, 1.575, 1.424, 1.988, 1.782, 1.068], dtype = float)

spline_4 = interp1d(dias,drenagem, kind='cubic')

dias_novo_4 = np.linspace(0,60,1000)
drenagem_novo = spline_4(dias_novo_4)

plt.scatter(dias,drenagem)
plt.plot(dias_novo_4,drenagem_novo, c = 'purple' )
plt.xlabel('Dias')
plt.ylabel('Drenagem')
plt.grid()
plt.show()

#6




'''Comparação dos Dados'''

plt.figure(figsize=(10, 6))
plt.plot(dias, temperatura_biodig, label='Temperatura do Biodigestor')
plt.plot(dias, recirculacao, label='Recirculação')
plt.plot(dias, ph_inferior, label='pH Inferior')
plt.plot(dias, ph_superior, label='pH Superior')
plt.plot(dias, producao_biogas, label='Produção de Biogás')
plt.plot(dias, drenagem, label='Drenagem')

# Adicionar legendas e título
plt.xlabel('Dias')
plt.ylabel('Valores')
plt.title('Dados Biogás')

# Mostrar a legenda
plt.legend()
plt.grid()

# Exibir o gráfico
plt.show()


'''Correlação'''
correlation = np.corrcoef(temperatura_biodig, recirculacao)[0, 1]
print(f"Coeficiente de correlação: {correlation}")

# Definir os nomes das variáveis
nomes_variaveis = ['Temperatura do Biodigestor', 'Recirculação', 'pH Inferior', 'pH Superior', 'Produção de Biogás','Drenagem']

# Criar matriz de correlação
data = np.array([temperatura_biodig, recirculacao, ph_inferior, ph_superior, producao_biogas,drenagem])
correlation_matrix = np.corrcoef(data)

# Criar gráfico de matriz de correlação com mapa de calor
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True,
            yticklabels=nomes_variaveis)

# Adicionar título
plt.title('Matriz de Correlação')

# Exibir o gráfico
plt.show()

correlation1, p_value_1 = stats.pearsonr(temperatura_biodig, producao_biogas)
print("Coeficiente de correlação:", correlation1)
print("Valor-p:", p_value_1)

# Cria o gráfico de dispersão
sns.set(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.regplot(x=temperatura_biodig, y=producao_biogas, color='b')
plt.xlabel('Temperatura Biodigestor')
plt.ylabel('Produção Biogás')
plt.title('Gráfico de Dispersão e Regressão Linear')
plt.text(38, 1200, f"Coeficiente de correlação: {correlation1:.4f}", fontsize=9, color='r')
plt.show()

##
correlation2, p_value_2 = stats.pearsonr(temperatura_biodig, recirculacao)
print("Coeficiente de correlação:", correlation2)
print("Recirculação", p_value_2)

# Cria o gráfico de dispersão
sns.set(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.regplot(x=temperatura_biodig, y=recirculacao, color='b')
plt.xlabel('Temperatura Biodigestor')
plt.ylabel('Recirculação')
plt.title('Gráfico de Dispersão e Regressão Linear')
plt.text(38, 1200, f"Coeficiente de correlação: {correlation2:.4f}", fontsize=9, color='r')
plt.show()


##
correlation3, p_value_3 = stats.pearsonr(temperatura_biodig, ph_inferior)
print("Coeficiente de correlação:", correlation3)
print("Ph inferior", p_value_3)

# Cria o gráfico de dispersão
sns.set(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.regplot(x=temperatura_biodig, y=ph_inferior, color='b')
plt.xlabel('Temperatura Biodigestor')
plt.ylabel('Ph inferior')
plt.title('Gráfico de Dispersão e Regressão Linear')
plt.text(0.5, 0.9, f"Coeficiente de correlação: {correlation3:.4f}", fontsize=9, color='r', transform=plt.gca().transAxes)
plt.show()

##
correlation4, p_value_4 = stats.pearsonr(temperatura_biodig, ph_superior)
print("Coeficiente de correlação:", correlation4)
print("Ph superior", p_value_4)

# Cria o gráfico de dispersão
sns.set(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.regplot(x=temperatura_biodig, y=ph_superior, color='b')
plt.xlabel('Temperatura Biodigestor')
plt.ylabel('Ph superior')
plt.title('Gráfico de Dispersão e Regressão Linear')
plt.text(0.5, 0.9, f"Coeficiente de correlação: {correlation4:.4f}", fontsize=9, color='r', transform=plt.gca().transAxes)
plt.show()

correlation5, p_value_5 = stats.pearsonr(temperatura_biodig, drenagem)
print("Coeficiente de correlação:", correlation5)
print("Ph superior", p_value_5)

# Cria o gráfico de dispersão
sns.set(style="darkgrid")
plt.figure(figsize=(8, 6))
sns.regplot(x=temperatura_biodig, y=drenagem, color='b')
plt.xlabel('Temperatura Biodigestor')
plt.ylabel('Ph superior')
plt.title('Gráfico de Dispersão e Regressão Linear')
plt.text(0.5, 0.9, f"Coeficiente de correlação: {correlation5:.4f}", fontsize=9, color='r', transform=plt.gca().transAxes)
plt.show()