from core.products import is_product_avaiable


class TestIsProductAvaiable:

    def __init__(self) -> None:
        self.test_quantity_et_avaiable()
        self.test_quantity_gt_avaiable()
        self.test_quantity_lt_avaiable()

    def test_quantity_lt_avaiable(self):
        assert is_product_avaiable('Chocolate', 1) == True, 'Error'
        print('Success')

    def test_quantity_gt_avaiable(self):
        assert is_product_avaiable('Granizado', 20) == False, 'Error'
        print('Success')

    def test_quantity_et_avaiable(self):
        assert is_product_avaiable('Dulce de Leche', 5) == True, 'Error'
        print('Success')
