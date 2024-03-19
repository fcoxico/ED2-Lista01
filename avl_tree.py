import matplotlib.pyplot as plt
import networkx as nx
import os

class NodoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.altura = 1
        self.esquerda = None
        self.direita = None
        self.fator_balanceamento = 0

class AVL:
    def __init__(self):
        self.InicializaAVL()
        self.image_counter = 0  # Inicializa o contador de imagens
        self.operacoes_por_nivel = {}  # Inicializa o dicionário de operações por nível

    def InicializaAVL(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return -1  # A altura de uma subárvore vazia é -1
        else:
            return no.altura

    def atualizar_altura(self, no):
        if no is not None:
            no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def atualizar_operacoes_por_nivel(self, nivel, operacao, numero):
        if nivel not in self.operacoes_por_nivel:
            self.operacoes_por_nivel[nivel] = []
        self.operacoes_por_nivel[nivel].append(f"{operacao} {numero}")

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.direita) - self.altura(no.esquerda)

    def balancear(self, no):
        if no is None:
            return no

        # Atualizar a altura do nó
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

        # Calcular o fator de balanceamento
        fator_balanceamento = self.altura(no.direita) - self.altura(no.esquerda)

        # Caso desbalanceado à direita
        if fator_balanceamento > 1:
            if self.altura(no.direita.direita) >= self.altura(no.direita.esquerda):
                return self.rotacao_esquerda(no)
            else:
                no.direita = self.rotacao_direita(no.direita)
                return self.rotacao_esquerda(no)

        # Caso desbalanceado à esquerda
        if fator_balanceamento < -1:
            if self.altura(no.esquerda.esquerda) >= self.altura(no.esquerda.direita):
                return self.rotacao_direita(no)
            else:
                no.esquerda = self.rotacao_esquerda(no.esquerda)
                return self.rotacao_direita(no)

        return no

    def rotacao_direita(self, no):
        filho_esquerdo = no.esquerda
        no.esquerda = filho_esquerdo.direita
        filho_esquerdo.direita = no
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        filho_esquerdo.altura = 1 + max(self.altura(filho_esquerdo.esquerda), self.altura(filho_esquerdo.direita))
        return filho_esquerdo

    def rotacao_esquerda(self, no):
        filho_direito = no.direita
        no.direita = filho_direito.esquerda
        filho_direito.esquerda = no
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        filho_direito.altura = 1 + max(self.altura(filho_direito.esquerda), self.altura(filho_direito.direita))
        return filho_direito

    def inserir_no(self, no, chave, nivel=0):
        # Se o nó for None, insere um novo NodoAVL com a chave dada
        if no is None:
            if nivel == 0:
                print(f"Inserindo chave {chave} na raiz da árvore.")
            else:
                print(f"Inserindo chave {chave} no nível {nivel}.")
            return NodoAVL(chave)

        # Se a chave for menor, insere na subárvore esquerda
        if chave < no.chave:
            print(f"Inserindo chave {chave} à esquerda de {no.chave} no nível {nivel + 1}.")
            no.esquerda = self.inserir_no(no.esquerda, chave, nivel + 1)
        # Se a chave for maior, insere na subárvore direita
        elif chave > no.chave:
            print(f"Inserindo chave {chave} à direita de {no.chave} no nível {nivel + 1}.")
            no.direita = self.inserir_no(no.direita, chave, nivel + 1)
        # Se a chave já existir, retorna o nó sem alterar a árvore
        else:
            return no

        # Atualiza a altura do nó atual
        self.atualizar_altura(no)

        # Balanceia a árvore e retorna o nó
        return self.balancear(no)

    def InserirAVL(self, chave):
        self.raiz = self.inserir_no(self.raiz, chave)

    def rotacaoDuplaDireita(self, no):
        no.esquerda = self.rotacao_esquerda(no.esquerda)
        return self.rotacao_direita(no)

    def rotacaoDuplaEsquerda(self, no):
        no.direita = self.rotacao_direita(no.direita)
        return self.rotacao_esquerda(no)

    def BuscaAVL(self, chave):
        return self.buscaAVLRec(self.raiz, chave)

    def buscaAVLRec(self, no, chave, nivel=0):
        if no is None:
            print(f"Chave {chave} não encontrada na árvore.")
            return None
        elif no.chave == chave:
            print(f"Chave {chave} encontrada no nível {nivel}.")
            return no
        elif chave < no.chave:
            print(f"Buscando chave {chave} à esquerda de {no.chave} no nível {nivel + 1}.")
            return self.buscaAVLRec(no.esquerda, chave, nivel + 1)
        else:
            print(f"Buscando chave {chave} à direita de {no.chave} no nível {nivel + 1}.")
            return self.buscaAVLRec(no.direita, chave, nivel + 1)

    def RemoveAVL(self, chave):
        self.raiz = self.remover_no(self.raiz, chave)

    def remover_no(self, no, chave, nivel=0):
        if no is None:
            print(f"Chave {chave} não encontrada para remoção.")
            return no

        if chave < no.chave:
            print(f"Removendo chave {chave} à esquerda de {no.chave} no nível {nivel + 1}.")
            no.esquerda = self.remover_no(no.esquerda, chave, nivel + 1)
        elif chave > no.chave:
            print(f"Removendo chave {chave} à direita de {no.chave} no nível {nivel + 1}.")
            no.direita = self.remover_no(no.direita, chave, nivel + 1)
        else:
            print(f"Removendo chave {chave} que está no nível {nivel}.")
            if no.esquerda is None or no.direita is None:
                temp = no.esquerda if no.esquerda else no.direita
                if temp is None:
                    temp = no
                    no = None
                else:
                    no = temp
            else:
                temp = self.minValueNode(no.direita)
                no.chave = temp.chave
                no.direita = self.remover_no(no.direita, temp.chave, nivel + 1)
        if no is None:
            return no

        self.atualizar_altura(no)
        return self.balancear(no)

    def MostraAVL(self):
        self.mostraAVLRec(self.raiz)

    def mostraAVLRec(self, no):
        if no != None:
            self.mostraAVLRec(no.esquerda)
            print("%d" % no.chave)
            self.mostraAVLRec(no.direita)

    def minValueNode(self, no):
        current = no
        while (current.esquerda is not None):
            current = current.esquerda
        return current

    def plotar_nodos(self, nodo, G, posicoes_nodos, nivel, pos_x, largura, ax):
        if nodo is not None:
            G.add_node(nodo.chave)
            posicoes_nodos[nodo.chave] = (pos_x, -nivel)
            self.operacoes_por_nivel[nivel] = self.operacoes_por_nivel.get(nivel, []) + [
                nodo.chave]  # Adiciona o nó ao nível correspondente
            fator_balanceamento = self.fator_balanceamento(nodo)

            ax.text(pos_x + 0.1, -nivel, f"{fator_balanceamento}", color='red', fontsize=8, ha='left', va='center',
                    fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle,pad=0.2'))
            espaco = largura / (2 ** (nivel + 1))
            if nodo.esquerda:
                if nodo.esquerda.chave != nodo.chave:
                    G.add_edge(nodo.chave, nodo.esquerda.chave)
                    self.plotar_nodos(nodo.esquerda, G, posicoes_nodos, nivel + 1, pos_x - espaco, largura, ax)

            if nodo.direita:
                if nodo.direita.chave != nodo.chave:
                    G.add_edge(nodo.chave, nodo.direita.chave)
                    self.plotar_nodos(nodo.direita, G, posicoes_nodos, nivel + 1, pos_x + espaco, largura, ax)

    def mostrar_arvore(self, operacao_linha):
        fig, ax = plt.subplots(figsize=(12, 8))
        G = nx.DiGraph()
        posicoes_nodos = {}
        largura_inicial = 3  # Ajuste a largura inicial conforme necessário

        if self.raiz is not None:
            self.plotar_nodos(self.raiz, G, posicoes_nodos, 0, 0, largura_inicial, ax)
        nx.draw(G, pos=posicoes_nodos, ax=ax, with_labels=True, arrows=False)

        # Adiciona linhas horizontais para mostrar a altura da árvore
        for nivel in range(self.altura_da_arvore()):
            ax.axhline(y=-nivel, color='blue', linewidth=1)

        return fig, ax

    def mostrar_e_salvar_arvore(self, nome_arquivo, operacao_linha):
        fig, ax = self.mostrar_arvore(operacao_linha)
        if fig:  # Verifica se a figura foi criada com sucesso
            caminho_completo = os.path.join('arvore_avl', nome_arquivo)
            plt.savefig(caminho_completo)
            plt.close(fig)  # Fecha a figura para liberar memória
            self.image_counter += 1  # Incrementa o contador de imagens

    def altura_da_arvore(self):
        return self.altura(self.raiz)

    def atualizar_altura_apos_operacao(self):
        self._atualizar_altura_recursivo(self.raiz)

    def _atualizar_altura_recursivo(self, no):
        if no is not None:
            no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
            self._atualizar_altura_recursivo(no.esquerda)
            self._atualizar_altura_recursivo(no.direita)

    def operar_conjuntos(self, conjunto_S, conjunto_B, conjunto_D):
        if not os.path.exists('arvore_avl'):
            os.makedirs('arvore_avl')

        for numero in conjunto_S:
            self.InserirAVL(numero)
            self.operacao_e_salvar('S', numero)

        for numero in conjunto_B:
            self.BuscaAVL(numero)
            self.operacao_e_salvar('B', numero)

        for numero in conjunto_D:
            self.RemoveAVL(numero)
            self.operacao_e_salvar('D', numero)

        # Atualiza a altura da árvore após todas as operações
        self.atualizar_altura_apos_operacao()
        self.mostrar_e_salvar_arvore(f"arvore_final.png", operacao_linha='Final')
        print(f'Altura final da árvore: {self.altura_da_arvore()}')

    def operacao_e_salvar(self, operacao, numero):
        self.atualizar_altura_apos_operacao()
        nome_arquivo = f"{str(self.image_counter).zfill(3)} - arvore_avl - {operacao} - {numero}.png"
        self.mostrar_e_salvar_arvore(nome_arquivo, operacao_linha=self.image_counter)
        self.operacoes_por_nivel.clear()
        print(f'Altura após operações: {self.altura_da_arvore()}')

    def FinalizaAVL(self):
        self.raiz = None


if __name__ == "__main__":
    avl = AVL()

    # Conjuntos de dados
    conjunto_S = (12, 19, 91, 76, 74, 36, 10, 11, 38, 81, 16, 94, 54, 19, 81, 91, 64, 1, 33, 4, 17, 43, 29)
    conjunto_B = (94, 11, 38, 74, 11, 16, 1, 19)
    conjunto_D = (11, 54, 10, 81, 19, 43)

    avl.operar_conjuntos(conjunto_S, conjunto_B, conjunto_D)
