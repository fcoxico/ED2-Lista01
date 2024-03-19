if __name__ == "__main__":
    # Inicializa a classe de experimentos com o tamanho do experimento e o valor máximo
    experimento_avl = ExperimentoAVL(tamanho_experimento=1000, max_valor=1000000)

    # Executa os experimentos de inserção e busca
    experimento_avl.executar_experimentos()

    # Projeta o desempenho para 500 mil inserções e buscas
    experimento_avl.projetar_desempenho()

    # Plota os gráficos de tempo e uso de CPU
    experimento_avl.plotar_graficos()