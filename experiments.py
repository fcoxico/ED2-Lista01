class ExperimentoAVL:
    def __init__(self, tamanho_experimento, max_valor):
        self.tamanho_experimento = tamanho_experimento
        self.max_valor = max_valor
        self.avl = AVL()
        self.tempos_insercao = []
        self.tempos_busca = []
        self.cpu_insercao = []
        self.cpu_busca = []

    def executar_experimentos(self):
        for _ in range(10):
            # Criação de dados fictícios para o experimento
            dados = random.sample(range(self.max_valor), self.tamanho_experimento)

            # Inserção na árvore AVL e registro do tempo e CPU
            inicio_tempo = time.time()
            inicio_cpu = psutil.cpu_percent(interval=1)
            for dado in dados:
                self.avl.InserirAVL(dado)
            fim_cpu = psutil.cpu_percent(interval=1)
            fim_tempo = time.time()

            self.tempos_insercao.append(fim_tempo - inicio_tempo)
            self.cpu_insercao.append((inicio_cpu + fim_cpu) / 2)

            # Busca na árvore AVL e registro do tempo e CPU
            inicio_tempo = time.time()
            inicio_cpu = psutil.cpu_percent(interval=1)
            for dado in dados:
                self.avl.BuscaAVL(dado)
            fim_cpu = psutil.cpu_percent(interval=1)
            fim_tempo = time.time()

            self.tempos_busca.append(fim_tempo - inicio_tempo)
            self.cpu_busca.append((inicio_cpu + fim_cpu) / 2)

    def projetar_desempenho(self):
        # Projeção baseada em dados menores
        fator = 500000 / self.tamanho_experimento
        tempo_medio_insercao = sum(self.tempos_insercao) / len(self.tempos_insercao)
        tempo_medio_busca = sum(self.tempos_busca) / len(self.tempos_busca)
        cpu_medio_insercao = sum(self.cpu_insercao) / len(self.cpu_insercao)
        cpu_medio_busca = sum(self.cpu_busca) / len(self.cpu_busca)

        # As projeções são escaladas de acordo com o fator
        tempo_projetado_insercao = tempo_medio_insercao * fator
        tempo_projetado_busca = tempo_medio_busca * fator
        cpu_projetado_insercao = cpu_medio_insercao * fator
        cpu_projetado_busca = cpu_medio_busca * fator

        print(f"Projeção para 500 mil inserções: {tempo_projetado_insercao:.2f} segundos e CPU {cpu_projetado_insercao:.2f}%")
        print(f"Projeção para 500 mil buscas: {tempo_projetado_busca:.2f} segundos e CPU {cpu_projetado_busca:.2f}%")


    def plotar_graficos(self):
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.plot(self.tempos_insercao, label='Inserção')
        plt.plot(self.tempos_busca, label='Busca')
        plt.title('Tempo de operações')
        plt.xlabel('Experimento')
        plt.ylabel('Tempo (s)')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(self.cpu_insercao, label='Inserção')
        plt.plot(self.cpu_busca, label='Busca')
        plt.title('Uso de CPU')
        plt.xlabel('Experimento')
        plt.ylabel('CPU (%)')
        plt.legend()

        plt.tight_layout()
        plt.show()

# Exemplo de uso
experimento = ExperimentoAVL(tamanho_experimento=1000, max_valor=1000000)
experimento.executar_experimentos()
experimento.projetar_desempenho()
experimento.plotar_graficos()
