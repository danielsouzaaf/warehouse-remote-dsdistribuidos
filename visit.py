# This is the code that runs this example.
from armazem import Armazem
from pessoa import Pessoa

armazem = Armazem()
janet = Pessoa("Janet")
henry = Pessoa("Henry")
janet.visitar(armazem)
henry.visitar(armazem)