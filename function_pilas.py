def inicializar_pila():
    """Inicializar pila. Crea una pila vacía."""
    pila = []
    return pila

def apilar(self,x):
    """Apila el elemnto X."""
    self.append(x)

def desapilar(self):
    """Desapila el elemento x. No lo devuelve.
    Si la pila esta vacia levanta una excepción."""
    if len(self)>0:
        self.pop()
    else:
        raise ValueError("Pila vacía")

def tope(self):
    """Devuelve el top de la pila. No desapila el elemnto x.
    Si la pila está vacía levanta una excepción."""
    if len(self)>0:
        return self[-1]
    else:
        raise ValueError("Pila Vacía.")

def esta_vacia(self):
    """Devuelve True si la lista está vacía, False si no."""
    return len(self) == 0






