import os
import matplotlib.pyplot as plt

for filename in os.listdir('./fitness'):
    if filename.endswith('.txt'):
        file_path = os.path.join('./fitness', filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            historico = [int(linha.strip()) for linha in file if linha.strip()]
            
        plt.figure(figsize=(6, 4))
        plt.boxplot(historico, tick_labels=[filename])
        plt.title(f'Boxplot do Histórico de Fitness - {filename}')
        plt.ylabel('Fitness')

        os.makedirs('./boxplots', exist_ok=True)

        plt.savefig(f'./boxplots/boxplot_{filename}.png')
        plt.close()
