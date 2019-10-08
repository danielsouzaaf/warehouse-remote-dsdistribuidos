# This is the code that runs this example.
from pessoa import Pessoa
import Pyro4

uri = input("Enter the uri of the warehouse: ").strip()
armazem = Pyro4.Proxy(uri)
gracon = Pessoa("Gracon")
daniel = Pessoa("daniel")
gracon.visitar(armazem)
daniel.visitar(armazem)