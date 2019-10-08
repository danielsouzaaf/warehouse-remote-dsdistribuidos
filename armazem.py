from __future__ import print_function
import Pyro4


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
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


def main():
    Pyro4.Daemon.serveSimple(
        {
            Armazem: "example.armazem"
        },
        ns=False)


if __name__ == "__main__":
    main()
