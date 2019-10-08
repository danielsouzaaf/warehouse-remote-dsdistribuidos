from __future__ import print_function


class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

    def visitar(self, armazem):
        print("Olá {0}.".format(self.nome))
        self.depositar(armazem)
        self.retirar(armazem)
        print("Obrigado, volte sempre!")

    def depositar(self, armazem):
        print("O armazém contém:", armazem.listar_itens())
        item = input("Digite o que você deseja guardar (ou vazio): ").strip()
        if item:
            armazem.guardar(self.nome, item)

    def retirar(self, armazem):
        print("O armazém contém:", armazem.listar_itens())
        item = input("Digite o que você deseja remover (ou vazio): ").strip()
        if item:
            armazem.retirar(self.nome, item)
