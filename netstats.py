from collections import deque
from grafo import Grafo
import sys
import csv

class Net:
	def __init__(self):
		self.ops = ['listar_operaciones',
		'camino',
		'rango',
		'navegacion',
		'clustering']
		self.map = {'camino': self.camino_check,
		'rango': self.rango_check,
		'navegacion': self.navegacion_check,
		'clustering': self.clustering_check
		}

		self.f = {'navegacion': nav_primer_link,
		'clustering': coef_clustering

		}


	def validate(self, op):
		cmd = op.split(" ", 1)
		ok = False
		if(cmd[0] in self.ops):
			ok = True
			p = self.map[cmd[0]](op)
			if p:
				return cmd[0], p
		if not ok:
			print("No se identificó ningún comando")

	def error_n(self, params, n):
		cmd = params.split(" ", 1)
		if(len(cmd) < n):
			print("Parámetros no especificados.")
			return False
		p = cmd[1].split(",")
		if(len(p) > n or len(p) < n):
			print("Cantidad de parámetros incorrecta.")
			return False
		return p


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


def grafo_init():
	grafo = Grafo(True)
	file  = open(sys.argv[1])
	src = csv.reader(file, delimiter = '\t')
	rows = [row for row in src]
	for row in rows:
		grafo.agregar_vertice(row[0])
	for row in rows:
		for i in range(1, len(row)):
			grafo.agregar_arista(row[0], row[i])
	file.close()
	return grafo

# def lectura_2_am(grafo, params):
# 	camino = []
# 	visitados  = set()
# 	for v in params:
# 		if not grafo.pertenece_vertice(v):
# 			raise ValueError("El vertice "{0}" no pertenece al grafo" .format(v))
# 			continue
# 		visitados.add(v)
# 		camino.append(v)
# 		for w in grafo.adyacentes(v):
# 			if w in params and not in visitados:
# 				camino.append(w)

def todos_en_rango(grafo, params):
	vertice = params[0]
	if not grafo.pertenece_vertice(vertice):
		print("ERROR. El articulo no pertenece a la red")
		print("None")
	n = int(params[1])
	cant = 0
	largo = bfs_var(grafo, vertice, cant, n)
	print(largo)

def bfs_var(grafo, inicio, cant, n):
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
		page = params[0]
		result = clustering_page(grafo, page)
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
		net.f[cmd](grafo, params)






def main():
	net = Net()
	grafo = grafo_init()
	input(net, grafo)

	

main()