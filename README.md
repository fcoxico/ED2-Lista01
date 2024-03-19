# Atividade Complementar 01

---

## Parte I: Árvores AVL e SPLAY (Rotações)

1. Mostre e descreva
   1. Qual a definição de uma árvore AVL?
   2. Qual a definição de uma árvore SPLAY?
   3. Como é o funcionamento das rotações da AVL e Splay?
   4. Quando se usa as rotações Splay, qual o seu objetivo e que configuração se espera sobre os elementos da árvore?
   5. Quais as complexidades da AVL e Splay (Inserção, busca e deleção)?
   6. Mostre porque são necessárias as rotações, e a quê objetivo se prestam.
2. Implemente computacionalmente:
   1. A classe AVL considerando os métodos: InicializaAVL, InserirAVL, BuscaAVL, RemoveAVL, MostraAVL, RotacaoSimples, RotacaoDupla, FinalizaAVL;
   2. A classe SPLAY considerando os métodos: InicializaSPLAY, InserirSPLAY, BuscaSPLAY, RemoveSPLAY, MostraSPLAY, RotacaoZig, RotacaoZag, RotacaoZigZig, RotacaoZagZag, RotacaoZigZag, RotacaoZagZig, FinalizaSPLAY;
   3. A classe árvore ótima, considerando que as frequências de busca são dadas aos elementos internos dados e externos.
3. Mostre como ficam as árvores AVL e Splay depois de acontecer os seguintes movimentos nessa ordem:
   1. Inserção de S = (26, 22, 32, 38, 81, 16, 94, 19, 21, 98, 49, 74, 13, 81, 11, 64, 36, 33, 19)
   2. Busca B = (81, 11, 32, 94, 11, 16, 94, 19)
   3. Deleção de D = (22, 13, 32, 11, 19)
   4. Mostre na árvore final da AVL e da SPLAY a altura de cada nó e o número de níveis da estrutura;
   5. Em qual nível está o nó 74 na AVL e na SPLAY?
   6. Mostre a árvore ótima de S considerando a busca B e compare-a à solução obtida na árvore SPLAY após a busca.
4. Nos quadros de aula, foram apresentados resultados de desempenho de três árvores (Binária, AVL e Splay) considerando o processo de Busca, a partir de 10 experimentos com os mesmos conjuntos de dados e as mesmas árvores após uma inserção de 500mil índices de valores numéricos entre 0-1milhão. Responda:
   1. Qual das árvores apresenta o melhor desempenho?
   2. Por quê num processo de busca com dados em uma distribuição de Poisson a SPLAY tem melhor desempenho que a AVL?
   3. Por que o mesmo não acontece na distribuição normal?
   4. Quando os gráficos mostram o domínio da AVL? E da Splay?
   5. Você confia nos gráficos apresentados? Por quê?

---

## (Parte II – Árvores Ótimas)

5. Calcule o custo total da árvore abaixo, e mostre se a árvore binária apresentada é ótima.

6. Sejam dados S={15, 29, 35, 44}, f=(-,3,4,12,18) e f´=(8, 2, 11, 5, 19). Encontre o custo e apresente a árvore ótima.
