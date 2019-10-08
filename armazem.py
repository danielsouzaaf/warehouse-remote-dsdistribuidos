from __future__ import print_function


class Armazem(object):
    def __init__(self):
        self.itens = ["cadeira", "bicicleta", "lanterna", "laptop", "almofada"]

    def listar_itens(self):
        return self.itens

    def retirar(self, nome, item):
        self.itens.remove(item)
        print("{0} pegou a(o) {1}.".format(nome, item))

    def guardar(self, nome, item):
        self.itens.append(item)
        print("{0} guardou a(o) {1}.".format(nome, item))
