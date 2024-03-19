import matplotlib.pyplot as plt
import networkx as nx
import os

class No:
    def __init__(self, chave):
        self.chave = chave
        self.pai = None
        self.esquerda = None
        self.direita = None

class SPLAY:
    def __init__(self):
        self.raiz = None
        self.image_counter = 0  # Contador de imagens


    def InicializaSPLAY(self):
        self.raiz = None

    def InserirSPLAY(self, chave):
        # Verificar primeiro se a chave já existe e, em caso afirmativo, realizar um splay
        existente_no = self.BuscaSPLAY(chave)
        if existente_no:
            self.splay(existente_no)
            return  # Não insere uma chave duplicada

        # Inserir nova chave se não existir
        novo_no = No(chave)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._InserirSPLAY(self.raiz, novo_no)
        self.splay(novo_no)
        
      
    def _InserirSPLAY(self, current, new_node):
        if new_node.chave < current.chave:
            if current.esquerda is None:
                current.esquerda = new_node
                new_node.pai = current
            else:
                self._InserirSPLAY(current.esquerda, new_node)
        else: # new_node.chave > current.chave
            if current.direita is None:
                current.direita = new_node
                new_node.pai = current
            else:
                self._InserirSPLAY(current.direita, new_node)
                
                        
    def BuscaSPLAY(self, chave):
        no = self._BuscaSPLAY(chave, self.raiz)
        if no:
            self.splay(no)
        return no
        
                            
    def _BuscaSPLAY(self, chave, no_atual):
        if no_atual is None or chave == no_atual.chave:
            return no_atual
        elif chave < no_atual.chave and no_atual.esquerda is not None:
            return self._BuscaSPLAY(chave, no_atual.esquerda)
        elif no_atual.direita is not None:
            return self._BuscaSPLAY(chave, no_atual.direita)

    def RemoveSPLAY(self, chave):
        no = self.BuscaSPLAY(chave)
        if no:
            self.remove_no(no)

    def remove_no(self, no):
        self.splay(no)
        if no.esquerda is None or no.direita is None:
            self.substitui_no(no, no.esquerda if no.esquerda is not None else no.direita)
        else:
            sucessor = self.subarvore_minimo(no.direita)
            if sucessor.pai != no:
                self.substitui_no(sucessor, sucessor.direita)
                sucessor.direita = no.direita
                sucessor.direita.pai = sucessor
            self.substitui_no(no, sucessor)
            sucessor.esquerda = no.esquerda
            sucessor.esquerda.pai = sucessor
        del no

    def substitui_no(self, no, novo_filho):
        if no.pai is None:
            self.raiz = novo_filho
        elif no == no.pai.esquerda:
            no.pai.esquerda = novo_filho
        else:
            no.pai.direita = novo_filho
        if novo_filho is not None:
            novo_filho.pai = no.pai
            
    def subarvore_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
        
    def splay(self, no):
        while no != self.raiz:
            if no.pai == self.raiz:  # Zig Step
                if no == no.pai.esquerda:
                    self.RotacaoZig(no)
                else:
                    self.RotacaoZag(no)
            elif no.pai and no.pai.pai:  # Verifique se o pai e o avô existem
                pai = no.pai
                avo = pai.pai
                if avo.esquerda == pai:
                    if pai.esquerda == no:
                        self.RotacaoZigZig(no)  # ZigZig Step
                    else:
                        self.RotacaoZigZag(no)  # ZigZag Step
                else:
                    if pai.direita == no:
                        self.RotacaoZagZag(no)  # ZagZag Step
                    else:
                        self.RotacaoZagZig(no)  # ZagZig Step
            if self.raiz == no:
                break

         
                        
    def _RemoveSPLAY(self, no):
        if no.esquerda is None and no.direita is None:
            if no == self.raiz:
                self.raiz = None
            elif no.pai.esquerda == no:
                no.pai.esquerda = None
            else:
                no.pai.direita = None
            self.RotacaoZagZag(no.pai)
        elif no.esquerda is None:
            if no == self.raiz:
                self.raiz = no.direita
                no.direita.pai = None
            elif no.pai.esquerda == no:
                no.pai.esquerda = no.direita
                no.direita.pai = no.pai
            else:
                no.pai.direita = no.direita
                no.direita.pai = no.pai
            self.RotacaoZigZig(no.pai)
        elif no.direita is None:
            if no == self.raiz:
                self.raiz = no.esquerda
                no.esquerda.pai = None
            elif no.pai.esquerda == no:
                no.pai.esquerda = no.esquerda
                no.esquerda.pai = no.pai
            else:
                no.pai.direita = no.esquerda
                no.esquerda.pai = no.pai
            self.RotacaoZagZag(no.pai)
        else:
            sucessor = self.EncontrarSucessor(no)
            chave = sucessor.chave
            self._RemoveSPLAY(sucessor)
            no.chave = chave
        return no

    def EncontrarSucessor(self, no):
        if no.direita is not None:
            return self.EncontrarSucessorMinimo(no.direita)
        else:
            pai = no.pai
            while pai is not None and no == pai.direita:
                no = pai
                pai = no.pai
            return pai

    def EncontrarSucessorMinimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def MostraSPLAY(self):
        if self.raiz is not None:
            self._MostraSPLAY(self.raiz)

    def _MostraSPLAY(self, no_atual):
        if no_atual is not None:
            self._MostraSPLAY(no_atual.esquerda)
            print(no_atual.chave)
            self._MostraSPLAY(no_atual.direita)
            
    def RotacaoZig(self, no):
        pai = no.pai
        if pai.esquerda == no:
            pai.esquerda = no.direita
            if no.direita:
                no.direita.pai = pai
            no.direita = pai
            no.pai = pai.pai
            pai.pai = no
            if no.pai and no.pai.esquerda == pai:
                no.pai.esquerda = no
            elif no.pai and no.pai.direita == pai:
                no.pai.direita = no
        if pai == self.raiz:
            self.raiz = no


    def RotacaoZag(self, no):
        pai = no.pai
        if pai.direita == no:
            pai.direita = no.esquerda
            if no.esquerda:
                no.esquerda.pai = pai
            no.esquerda = pai
            no.pai = pai.pai
            pai.pai = no
            if no.pai and no.pai.direita == pai:
                no.pai.direita = no
            elif no.pai and no.pai.esquerda == pai:
                no.pai.esquerda = no
        if pai == self.raiz:
            self.raiz = no

    def RotacaoZigZig(self, no):
        if no.pai and no.pai.pai:
            self.RotacaoZig(no.pai)
            self.RotacaoZig(no)

    def RotacaoZagZag(self, no):
        if no.pai and no.pai.pai:
            self.RotacaoZag(no.pai)
            self.RotacaoZag(no)

    def RotacaoZigZag(self, no):
        if no.pai:
            self.RotacaoZag(no)
            self.RotacaoZig(no)

    def RotacaoZagZig(self, no):
        if no.pai:
            self.RotacaoZig(no)
            self.RotacaoZag(no)

    def FinalizaSPLAY(self):
        self.raiz = None
        
    def plotar_nodos(self, nodo, G, posicoes_nodos, nivel, pos_x, largura, ax):
        if nodo is not None:
            G.add_node(nodo.chave)
            posicoes_nodos[nodo.chave] = (pos_x, -nivel)
            espaco = largura / (2 ** (nivel + 1))
            if nodo.esquerda:
                G.add_edge(nodo.chave, nodo.esquerda.chave)
                self.plotar_nodos(nodo.esquerda, G, posicoes_nodos, nivel + 1, pos_x - espaco, largura, ax)
            if nodo.direita:
                G.add_edge(nodo.chave, nodo.direita.chave)
                self.plotar_nodos(nodo.direita, G, posicoes_nodos, nivel + 1, pos_x + espaco, largura, ax)

    def mostrar_arvore(self, operacao_linha):
        fig, ax = plt.subplots(figsize=(12, 8))
        G = nx.DiGraph()
        posicoes_nodos = {}
        largura_inicial = 3

        if self.raiz is not None:
            self.plotar_nodos(self.raiz, G, posicoes_nodos, 0, 0, largura_inicial, ax)
        nx.draw(G, pos=posicoes_nodos, ax=ax, with_labels=True, arrows=False)

        # Adiciona linhas horizontais para mostrar a altura da árvore
        for nivel in range(self.altura_da_arvore()):
            ax.axhline(y=-nivel, color='blue', linewidth=1)

        return fig, ax
        
    def mostrar_e_salvar_arvore(self, nome_arquivo):
        fig, ax = plt.subplots(figsize=(12, 8))
        G = nx.DiGraph()
        posicoes_nodos = {}
        self.plotar_nodos(self.raiz, G, posicoes_nodos, 0, 0, 3, ax)
        nx.draw(G, pos=posicoes_nodos, ax=ax, with_labels=True, arrows=False)
        ax.set_title(nome_arquivo.replace('.png', ''))  # Remove a extensão .png para o título
        
        # Cria o diretório se não existir
        if not os.path.exists('arvore_splay'):
            os.makedirs('arvore_splay')
        plt.savefig(f'arvore_splay/{nome_arquivo}')
        plt.close(fig)
        
    def altura_da_arvore(self):
        return self.altura(self.raiz)

    def altura(self, no):
        if no is None:
            return -1
        altura_esq = self.altura(no.esquerda)
        altura_dir = self.altura(no.direita)
        return 1 + max(altura_esq, altura_dir)
        
        
    def operar_conjuntos(self, conjunto_S, conjunto_B, conjunto_D):
        # Alterar as chamadas para 'self.operacao_e_salvar' passando o operador e o número
        for numero in conjunto_S:
            self.InserirSPLAY(numero)
            self.operacao_e_salvar('S', numero)

        for numero in conjunto_B:
            self.BuscaSPLAY(numero)
            self.operacao_e_salvar('B', numero)

        for numero in conjunto_D:
            self.RemoveSPLAY(numero)
            self.operacao_e_salvar('D', numero)

        self.operacao_e_salvar('Final', '')  # Passa uma string vazia para 'numero' na operação final

    def operacao_e_salvar(self, operacao, numero):
        nome_arquivo = f"{str(self.image_counter).zfill(3)} - arvore_splay - {operacao} - {numero}.png"
        self.mostrar_e_salvar_arvore(nome_arquivo)
        self.image_counter += 1  # Incrementa o contador após salvar a imagem
        print(f'Operação {operacao} com número {numero} concluída.')    
            

if __name__ == "__main__":
    splay = SPLAY()

    # Conjuntos de dados
    conjunto_S = (26, 22, 32, 38, 81, 16, 94, 19, 21, 98, 49, 74, 13, 81, 11, 64, 36, 33, 19)
    conjunto_B = (81, 11, 32, 94, 11, 16, 94, 19)
    conjunto_D = (22, 13, 32, 11, 19)

    splay.operar_conjuntos(conjunto_S, conjunto_B, conjunto_D)