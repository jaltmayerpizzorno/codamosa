# Automatically generated by Pynguin.
import mimesis.providers.address as module_0

def test_case_0():
    try:
        str_0 = '~eP:pw/Mv.nx*./9^)l'
        address_0 = module_0.Address()
        var_0 = address_0.latitude()
        str_1 = address_0.calling_code()
        bytes_0 = b'\xaa\xf8\x9f\xc2\x9e\xb2\x91\x9bd\xb9\xd4\x1a\xb9\x8f|\xff\xfc6\x1e\xc4'
        dict_0 = {}
        var_1 = address_0.latitude()
        address_1 = module_0.Address()
        bool_0 = False
        dict_1 = address_1.coordinates(bool_0)
        str_2 = address_1.province(**dict_0)
        dict_2 = {bytes_0: bytes_0, bytes_0: bytes_0, str_0: str_0}
        dict_3 = {str_0: dict_2, str_0: str_0}
        str_3 = address_0.postal_code()
        bool_1 = True
        str_4 = address_1.country(bool_1)
        address_2 = module_0.Address(**dict_3)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'r'
        str_1 = '-_I9VKxM Sp'
        dict_0 = {str_0: str_0, str_1: str_1}
        list_0 = []
        address_0 = module_0.Address(*list_0)
        str_2 = address_0.continent()
        address_1 = module_0.Address(**dict_0)
    except BaseException:
        pass