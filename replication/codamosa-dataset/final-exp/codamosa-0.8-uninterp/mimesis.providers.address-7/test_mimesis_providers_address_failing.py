# Automatically generated by Pynguin.
import mimesis.providers.address as module_0

def test_case_0():
    try:
        str_0 = '4vTV\nt;qqO0V3A)8\nd'
        str_1 = 'application/urc-uisocketdesc+xml'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_0: str_1}
        bool_0 = False
        address_0 = module_0.Address()
        str_2 = address_0.postal_code()
        str_3 = address_0.continent(bool_0)
        address_1 = module_0.Address()
        str_4 = address_1.federal_subject(**dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        address_0 = module_0.Address()
        list_0 = [address_0, address_0, address_0]
        str_0 = address_0.prefecture(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        address_0 = module_0.Address()
        str_0 = address_0.province()
        str_1 = address_0.street_name()
        str_2 = address_0.address()
        str_3 = address_0.state()
        str_4 = address_0.address()
        str_5 = address_0.region()
        float_0 = 815.7
        bool_0 = True
        str_6 = address_0.street_name()
        str_7 = address_0.state()
        dict_0 = address_0.coordinates(bool_0)
        list_0 = [float_0, float_0, float_0]
        str_8 = address_0.calling_code()
        str_9 = address_0.state(bool_0)
        address_1 = module_0.Address()
        str_10 = address_1.federal_subject()
        str_11 = address_1.calling_code()
        address_2 = module_0.Address(*list_0)
    except BaseException:
        pass