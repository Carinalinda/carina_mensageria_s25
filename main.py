from consumidor import Consumidor
from produtor import Produtor

Consumidor = Consumidor()
Produtor = Produtor()

Produtor.register_observer(Consumidor)