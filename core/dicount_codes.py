"""
    Ejercicio 3:
        Completar la función validate_discount_code con el siguiente objetivo:
        ● Dada la lista de códigos de descuento vigentes y un código de descuento mencionado
        por el cliente, devuelve True si la diferencia entre el código mencionado y los códigos
        vigentes es menor a tres caracteres, en al menos uno de los casos.
        Por diferencia se entiende: caracteres que están presentes en el código brindado, pero no en el
        código evaluado de la lista o viceversa
"""

_AVAIABLE_DISCOUNT_CODES = ['Primavera2021', 'Verano2021', 'Navidad2x1', 'heladoFrozen']


def validate_discount_code(discount_code: str) -> bool:
    for code in _AVAIABLE_DISCOUNT_CODES:
        result = set(discount_code) ^ set(code)
        if len(result) < 3:
            return True
    return False
