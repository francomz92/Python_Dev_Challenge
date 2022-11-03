import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    'product_name': ['Chocolate', 'Granizado', 'Limon', 'Dulce de Leche'],
    'quantity': [3, 10, 0, 5],
})


def is_product_avaiable(product_name: str, quantity: int) -> bool:
    _product = _PRODUCT_DF.product_name == product_name
    _quantity = _PRODUCT_DF.quantity >= quantity
    df = _PRODUCT_DF[_product & _quantity]
    return len(df) > 0
