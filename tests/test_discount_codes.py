from core.dicount_codes import _AVAIABLE_DISCOUNT_CODES, validate_discount_code


class TestDiscountCodes:

    def __init__(self) -> None:
        self.test_valid_code()
        self.test_invalid_code()

    def test_valid_code(self):
        f"""
            Se ingresa un código con menos de 3 caracteres diferentes a los cargados en{_AVAIABLE_DISCOUNT_CODES}
            retorna True
        """
        assert validate_discount_code('primavera2021') == True, 'Error'
        print('Success')

    def test_invalid_code(self):
        f"""
            Se ingresa un código con 3 o más caracteres diferentes a los cargados en{_AVAIABLE_DISCOUNT_CODES}
            retorna False
        """
        assert validate_discount_code('strangeCode35') == False, 'Error'
        print('Success')
