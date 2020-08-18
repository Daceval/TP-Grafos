from grafo import * 
from collections import deque
import heapq as hp 

def bfs(grafo, inicio):
	visitados = set()
	costo = {}
	padre = {}
	
	visitados.add(inicio)
	padre[inicio] = None
	costo[inicio] = 0
	cola = deque()
	cola.append(inicio)
	while(cola):
		vertice = cola.popleft()
		for adyac in grafo.adyacentes(vertice):
			if adyac in visitados:
				continue
			visitados.add(adyac)
			padre[adyac] = vertice
			costo[adyac] = costo[vertice] + 1
			cola.append(adyac)

	return padre, costo


def camino_minimo(grafo, inicio, fin):
	camino = []
	costo = 0
	padres, distancia = bfs(grafo, inicio)
	if fin not in padres:
		return False

	camino.append(fin)
	seguir = padres.get(fin)
	while True:
		if seguir != None: 
			camino.append(seguir)
			seguir = padres.get(seguir)
		else:
			break
	costo = distancia[fin]

	return camino[::-1], costo


def diametro_grafo(grafo):
	max_min_dist = 0
	for vertice in grafo:
		caminos, distancias = bfs(grafo, vertice)
		for w in distancias:
			if distancias[w] > max_min_dist:
				max_min_dist = distancias[w]
	
	return max_min_dist


def ciclo(grafo, vertice, n, inicio, camino):
	print(camino)
	if vertice == inicio and len(camino) == n:
		camino.append(inicio)
		print("entre")
		return True

	if len(camino) >= n:
		return False
	camino.append(vertice)

	for w in grafo.adyacentes(vertice):
		print("adyacente de {} es {} ".format(vertice, w))
		if ciclo(grafo, w, n, inicio, camino):
			return True
	
	camino.pop()
	return False


def ciclo_de_largo_n(grafo, v, n):
	list_ciclo = []
	inicio = v
	ciclo(grafo, v, n, inicio, list_ciclo)
	return list_ciclo


def info_links(grafo):
	links_entrantes = {}
	cant_links = {} 
	for pagina in grafo:
		links = grafo.adyacentes(pagina)
		if len(links) == 0:
			cant_links[pagina] = 0
		for link in links:
			if link not in links_entrantes:
				links_entrantes[link] = set()

			links_entrantes[link].add(pagina)
			cant_links[pagina] = len(links)
			
	for pagina in grafo:
		if pagina not in links_entrantes:
			links_entrantes[pagina] = {} 
	
	return links_entrantes, cant_links 


def pagerank(web, coef_amortiguacion = 0.85, iteraciones = 100):  

	links_entrantes, cant_links = info_links(web)
	rank = {}
	for pagina in web:
		rank[pagina] = 1 / float(len(web))

	for _ in range(iteraciones):
		new_rank = {}
		for pagina in web:
			sum_rank = 0
			inlinks = links_entrantes[pagina]
			for link in inlinks:
				sum_rank += coef_amortiguacion * (float(rank.get(link)) / float(cant_links.get(link)))
	
			total_rango = ((1 - coef_amortiguacion) / float(len(web))) + sum_rank
			new_rank[pagina] = total_rango
		rank = new_rank


	return rank

def cfc(grafo):
	todas_cfc = []
	visitados = set()
	for vertice_inicial in grafo:
		if vertice_inicial not in visitados:
			pila = deque()
			apilados = set()
			orden = {}
			mas_bajo = {}
			mas_bajo[vertice_inicial] = 0
			orden[vertice_inicial] = 0
			componentes_fuertemente_conexas(grafo, vertice_inicial, visitados, pila, apilados, orden, mas_bajo, todas_cfc)
	return todas_cfc


def componentes_fuertemente_conexas(grafo, v, visitados, pila, apilados, orden, mas_bajo, todas_cfc):
	visitados.add(v)
	mas_bajo[v] = orden[v]
	pila.appendleft(v)
	apilados.add(v)
	
	for w in grafo.adyacentes(v):
		if w not in visitados:
			orden[w] = orden[v] + 1
			componentes_fuertemente_conexas(grafo, w, visitados, pila, apilados, orden, mas_bajo, todas_cfc)

		if w in apilados:
			mas_bajo[v] = min(mas_bajo[v], mas_bajo[w])
    
	if orden[v] == mas_bajo[v] and len(pila) > 0:
		nueva_cfc = []
		while True:
			w = pila.popleft()
			apilados.remove(w)
			nueva_cfc.append(w)
			if w == v:
				break
		todas_cfc.append(nueva_cfc)
  

if __name__ == "__main__":

	grafo = Grafo(True)
	grafo.agregar_vertice("a")
	grafo.agregar_vertice("e")
	grafo.agregar_vertice("q")
	grafo.agregar_vertice("d")
	grafo.agregar_vertice("z")
	grafo.agregar_vertice("p")
	grafo.agregar_vertice("w")
	grafo.agregar_vertice("v")
	grafo.agregar_vertice("t")


	grafo.agregar_arista("d", "e")
	grafo.agregar_arista("e", "q")
	grafo.agregar_arista("e", "p")
	grafo.agregar_arista("e", "z")
	grafo.agregar_arista("q", "p")
	grafo.agregar_arista("v", "p")
	grafo.agregar_arista("p", "t")
	grafo.agregar_arista("z", "w")
	grafo.agregar_arista("w", "a")
	grafo.agregar_arista("a", "d")
	grafo.agregar_arista("a", "e")

	# rank = pagerank(grafo)
	# print("rank: ", rank)
	# array = [valor for valor in rank.values()]
	
	# #print("invertido", dic)

	# heap = [array[x] for x in range(4)]
	# print("heap al principio", heap, end = "\n")
	# hp.heapify(heap)
	# print("heap despues de heapify", heap, end = "\n")
	# for i in array[4:]:
	# 	if i > heap[0]:
	# 		hp.heappop(heap)
	# 		hp.heappush(heap, i)

	# print("mas grandes", heap[::-1], end = "\n")
	# print("array original", array)
	# print("\n")
	# dic = dict([(v, c) for c, v in rank.items()])

	# for r, p in enumerate(heap[::-1]):
	# 	print(f'Puesto{r + 1}°', dic[p])
	#print("page rank: ", rank)
	# comp_conex = []
	# comp_conex = cfc(grafo)
	# pagina = "a"
	# print("componentes conexas : ", comp_conex)
	# dicci = {}
	# for i in range(len(comp_conex)):
	# 	for j in range(len(comp_conex[i])):
	# 		dicci[comp_conex[i][j]] = i
	# print(comp_conex[dicci[pagina]])

	
				








