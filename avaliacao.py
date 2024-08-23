class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    # Método para converter o objeto Avaliacao em um dicionário para salvar em JSON
    def __dict__(self):
        return {
            'cliente': self._cliente,
            'nota': self._nota
        }