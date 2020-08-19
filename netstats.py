#!/usr/bin/python3.

from collections import deque
from grafo import Grafo
from libgraph import * 
import sys
import csv
import heapq as hp
sys.setrecursionlimit(75000)


class Net:
	def __init__(self):
		self.ops = ['listar_operaciones',
		'camino',
		'ciclo',
		'rango',
		'navegacion',
		'clustering',
		'mas_importantes',
		'comunidad',
		'conectados',
		'lectura']

		self.map = {'listar_operaciones': self.listar_check,
		'camino': self.camino_check,
		'rango': self.rango_check,
		'navegacion': self.navegacion_check,
		'clustering': self.clustering_check,
		'conectados': self.conectividad_check,
		'ciclo': self.ciclo_check,
		'mas_importantes': self.importantes_check,
		'comunidad': self.comunidad_check,
		'lectura': self.lectura_check
		}

		self.f = {'listar_operaciones': self.listar_operaciones,
		'navegacion': nav_primer_link,
		'clustering': coef_clustering,
		'camino': camino_mas_corto,
		'mas_importantes': art_mas_importantes, 
		'ciclo': ciclo_n_articulos,
		'conectados': conectividad,
		'lectura': lectura_2_am,
		'rango': todos_en_rango,
		'comunidad': comunidades
		}


	def validate(self, op):
		if not op:
			print("No se recibió ninguna instrucción.")
			return None, None
		cmd = op.split(" ", 1)
		if(cmd[0] in self.ops):
			p = self.map[cmd[0]](op)
			if p:
				return cmd[0], p
			else:
				return None, None
		else:
			print("El comando '{0}' no es válido." .format(cmd[0]))
			return None, None

	def error_n(self, params, n):
		cmd = params.split(" ", 1)
		if len(cmd) > 2 and n == 0:
			print("Esta operación no requiere parámetros.")
		if n == 0:
			return True
		if(len(cmd) < 2):
			print("Parámetros no especificados.")
			return False
		p = cmd[1].split(",")
		if(len(p) > n or len(p) < n):
			print("Cantidad de parámetros incorrecta.")
			return False
		return p

	def listar_operaciones(self, grafo, params):
		for op in self.ops:
			if op == 'listar_operaciones':
				continue
			print(">" + op)

	def camino_check(self, params):
		return self.error_n(params, 2)
	
	def rango_check(self, params):
		return self.error_n(params, 2)

	def navegacion_check(self, params):
		return self.error_n(params, 1)

	def clustering_check(self, params):
		cmd = params.split(" ", 1)
		if(len(cmd) > 2):
			print("Cantidad de parámetros incorrecta.")
			return False
		if(len(cmd) == 2):
			p = cmd[1]
			return [p]
		return []

	def conectividad_check(self, params):
		return self.error_n(params, 1)

	def ciclo_check(self, params):
		return self.error_n(params, 2)

	def importantes_check(self, params):
		return self.error_n(params, 1)

	def lectura_check(self, params):
		cmd = params.split(" ", 1)
		if len(cmd) == 2:
			p = cmd[1].split(",")
		return self.error_n(params, len(p))

	def listar_check(self, params):
		return self.error_n(params, 0)

	def comunidad_check(self, params):
		return self.error_n(params, 1)

def grafo_init():
	grafo = Grafo(True)
	file  = open(sys.argv[1])
	src = csv.reader(file, delimiter = '\t')
	rows = [row for row in src]
	for row in rows:
		row[0].strip()
		grafo.agregar_vertice(row[0])
	for row in rows:
		for i in range(1, len(row)):
			row[i].strip()
			grafo.agregar_arista(row[0], row[i])
	file.close()
	return grafo

def lectura_2_am(grafo, params):
	camino = []
	grados = {}
	for v in params:
		grados[v] = 0
	for v in params:
		for w in grafo.adyacentes(v):
			if w in params:
				grados[w] += 1
	q = deque()
	for v in params:
		if grados[v] == 0:
			q.append(v)
	while q:
		v = q.popleft()
		camino.append(v)
		for w in grafo.adyacentes(v):
			if w in params:
				grados[w] -= 1
				if grados[w] == 0:
					q.append(w)
	if len(camino) == len(params):
		return camino
	else:
		print("No existe formada de leer las paginas en orden")

def todos_en_rango(grafo, params):
	vertice = params[0]
	if not grafo.pertenece_vertice(vertice):
		print("ERROR. El articulo no pertenece a la red")
		print("None")
	n = int(params[1])
	cant = 0
	largo = largo_bfs_var(grafo, vertice, cant, n)
	print(largo)

def largo_bfs_var(grafo, inicio, cant, n):
	visitados = set()
	costo = {}
	visitados.add(inicio)
	costo[inicio] = 0
	cola = deque()
	cola.append(inicio)
	while(cola):
		vertice = cola.popleft()
		for adyac in grafo.adyacentes(vertice):
			if adyac in visitados:
				continue
			visitados.add(adyac)
			costo[adyac] = costo[vertice] + 1
			if(costo[adyac] == n):
				cant +=1
			cola.append(adyac)
	return cant

def nav_primer_link(grafo, params):
	origen = params[0]
	cant = 0
	camino = []
	nav(grafo, origen, cant, camino)
	print(" -> ".join(camino))

def nav(grafo, origen, cant, camino):
	camino.append(origen)
	if cant == 20 or origen == 'Filosofía':
		return None
	if not grafo.adyacentes(origen):
		return None
	cant += 1
	nav(grafo, grafo.adyacentes(origen)[0], cant, camino)

def coef_clustering(grafo, params):
	if not params:
		result = clustering_overall(grafo)
	else:
		result = clustering_page(grafo, params[0])
	print("{:.3f}" .format(result))

def clustering_overall(grafo):
	suma = 0
	cant = 0
	for v in grafo.obtener_vertices():
		suma += clustering_page(grafo, v)
		cant += 1
	return suma/cant


def clustering_page(grafo, page):
	cant = 0;
	if len(grafo.adyacentes(page)) < 2:
		return 0
	for w in grafo.adyacentes(page):
		for v in grafo.adyacentes(page):
			if grafo.vertices_unidos(v, w):
				cant += 1
	lenght = len(grafo.adyacentes(page))
	div = lenght*(lenght-1)
	return cant/div

def input(net, grafo):
	for x in sys.stdin:
		line = x.strip()
		cmd, params = net.validate(line)
		if not cmd or not params:
			continue
		net.f[cmd](grafo, params)


def art_mas_importantes(grafo, params):
	top_k = int(params[0])
	mas_importantes = []
	cal_pagerank = pagerank(grafo)
	
	rank_values = [valor for valor in cal_pagerank.values()]
	heap = [rank_values[x] for x in range(top_k)]
	hp.heapify(heap)

	#algoritmo top-k
	for rango in rank_values[top_k+1:]:
		if heap[0] < rango:
			hp.heappop(heap)
			hp.heappush(heap, rango)

	dict_rango_pagina = dict([(rank, page) for page, rank in cal_pagerank.items()])
	while heap:
		rango = hp.heappop(heap)
		mas_importantes.append(dict_rango_pagina[rango])
	print(",".join(mas_importantes[::-1]))


def ciclo_n_articulos(grafo, params):
	inicio = params[0]
	n = int(params[1])
	ciclo_articulos = ciclo_de_largo_n(grafo, inicio, n)
	
	if len(ciclo_articulos) == 0:
		print("No se encontro recorrido")
	else:
		print("->".join(ciclo_articulos))


def camino_mas_corto(grafo, params):
	origen = params[0]
	destino = params[1]
	camino_min , costo = camino_minimo(grafo, origen, destino)
	print("->".join(camino_min))
	print(costo)


def conectividad(grafo, params):
	pagina = params[0]
	index_comp = {}
	comp_conex = []
	if len(index_comp) == 0:
		comp_conex = cfc(grafo)
		for num_componente in range(len(comp_conex)):	
			for indice in range(len(comp_conex[num_componente])):
				index_comp[comp_conex[num_componente][indice]] = num_componente
	print(",".join(comp_conex[index_comp[pagina]]))


def comunidades(grafo, params):
	pagina = params[0]
	comunidad_pagina = []

	todas_comunidades = label_propagation(grafo)
	label_pagina = todas_comunidades[pagina]
	for pagina, label in todas_comunidades.items():
		if label == label_pagina:
			comunidad_pagina.append(pagina)

	print(",".join(comunidad_pagina))



def main():
	net = Net()
	grafo = grafo_init()
	input(net, grafo)

	

main()