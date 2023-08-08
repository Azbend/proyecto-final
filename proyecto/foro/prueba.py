from models import Consola

consolas = Consola.objects.all()
for consola in consolas:
    print(consola)