#!/usr/bin/python3.

from random import choice


class Grafo:
	''' Grafo dirigido'''

	def __init__(self):
		self.vertices = {}
		#self.cant_vertices = 0


	def __iter__(self):
		return iter(self.vertices)

	
	def agregar_vertice(self, vertice):
		if vertice in self.vertices:
			return False 
		self.vertices[vertice] = {}
		#self.cant_vertices += 1
		return True

	def agregar_arista(self, vert_inicio, vertice_fin, peso = 1):
		if vert_inicio not in self.vertices or vertice_fin not in self.vertices:
			raise ValueError("No se puede agregar la arista") 
			return False
	
		adya_inicio = self.vertices.get(vert_inicio, {})
		adya_inicio[vertice_fin] = peso
		self.vertices[vert_inicio] = adya_inicio
		
		return True

	def sacar_arista(self, desde, hasta):
		if desde not in self.vertices or hasta not in self.vertices:
			raise ValueError("No se puede sacar una arista")
		dict_adyacente = self.vertices.get(desde, {})
		dict_adyacente.pop(hasta)
		self.vertices[desde] = dict_adyacente


	def sacar_vertice(self, vertice):
		if vertice not in self.vertices:
			raise ValueError("El vertice no se encuentra en el grafo")
			return False
		
		del self.vertices[vertice]		
		
		for vertices in self.vertices.values():
			vertices.pop(vertice, None)
		return True


	def vertice_random(self):
		return choice(list(self.vertices.keys()))


	def adyacentes(self, vertice):
		if vertice not in self.vertices:
			raise ValueError("El vertice no se encuentra en el grafo")
			return False
		return list(self.vertices[vertice])

	def obtener_vertices(self):
		return list(self.vertices)


	def pertenece_vertice(self, vertice):
		return vertice in self.vertices


	def peso(self, vertice1, vertice2):
		dic_aux = self.vertices[vertice1]
		peso = dic_aux.get(vertice2) # dic_aux[vertice2]
		return peso


	def vertices_unidos(self, vertice1, vertice2):
		dic_aux = self.vertices[vertice1]
		if vertice2 in dic_aux:
			return vertice1, vertice2, self.peso(vertice1, vertice2)
		return False

