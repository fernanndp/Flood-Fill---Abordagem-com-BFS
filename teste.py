from collections import deque, defaultdict
import networkx as nx

# 8 direções
direcoes = [
    (0, 1), (1, 1), (1, 0), (1, -1),
    (0, -1), (-1, -1), (-1, 0), (-1, 1)
]

def construir_grafo_completo(matriz):
    grafo = defaultdict(list)
    linhas, colunas = len(matriz), len(matriz[0])
    for x in range(linhas):
        for y in range(colunas):
            for dx, dy in direcoes:
                nx_, ny_ = x + dx, y + dy
                if 0 <= nx_ < linhas and 0 <= ny_ < colunas:
                    grafo[(x, y)].append((nx_, ny_))
    return grafo

def bfs_valor_igual(grafo, matriz, x_inicial, y_inicial):
    valor_original = matriz[x_inicial][y_inicial]
    visitados = set()
    fila = deque([(x_inicial, y_inicial)])

    while fila:
        x, y = fila.popleft()
        if (x, y) in visitados or matriz[x][y] != valor_original:
            continue
        visitados.add((x, y))
        for vizinho in grafo[(x, y)]:
            vx, vy = vizinho
            if vizinho not in visitados and matriz[vx][vy] == valor_original:
                fila.append(vizinho)
    return visitados

def aplicar_floodfill(matriz, visitados, novo_valor):
    for x, y in visitados:
        matriz[x][y] = novo_valor
    return matriz

def exportar_grafo_para_arquivo(visitados, matriz, caminho_arquivo):
    G = nx.Graph()
    for x, y in visitados:
        G.add_node((x, y), valor=matriz[x][y])
    for x, y in visitados:
        for dx, dy in direcoes:
            nx_, ny_ = x + dx, y + dy
            if (nx_, ny_) in visitados:
                G.add_edge((x, y), (nx_, ny_))
    nx.write_graphml(G, caminho_arquivo)
    print(f"Grafo exportado: {caminho_arquivo} ({len(G.nodes)} nós, {len(G.edges)} arestas)")

def ler_matriz_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def escrever_matriz_em_arquivo(caminho_arquivo, matriz):
    with open(caminho_arquivo, 'w') as file:
        for row in matriz:
            file.write(" ".join(map(str, row)) + "\n")

def main():
    caminho_input = "input.txt"
    caminho_output_matriz = "matriz_modificada.txt"
    caminho_graphml_antes = "grafo_antes.graphml"
    caminho_graphml_depois = "grafo_depois.graphml"

    matriz = ler_matriz_do_arquivo(caminho_input)

    x_inicial, y_inicial = 27, 479
    novo_valor = 72

    grafo_completo = construir_grafo_completo(matriz)
    visitados = bfs_valor_igual(grafo_completo, matriz, x_inicial, y_inicial)
    print(f"Total de nós visitados: {len(visitados)}")

    exportar_grafo_para_arquivo(visitados, matriz, caminho_graphml_antes)

    matriz_modificada = aplicar_floodfill(matriz, visitados, novo_valor)

    exportar_grafo_para_arquivo(visitados, matriz_modificada, caminho_graphml_depois)

    escrever_matriz_em_arquivo(caminho_output_matriz, matriz_modificada)
    print(f"Matriz modificada salva em {caminho_output_matriz}")

if __name__ == "__main__":
    main()
