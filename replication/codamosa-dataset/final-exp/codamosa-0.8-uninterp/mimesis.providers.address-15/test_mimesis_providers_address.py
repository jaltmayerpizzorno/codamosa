# Automatically generated by Pynguin.
import mimesis.providers.address as module_0

def test_case_0():
    pass

def test_case_1():
    address_0 = module_0.Address()

def test_case_2():
    bool_0 = True
    address_0 = module_0.Address()
    dict_0 = address_0.coordinates(bool_0)

def test_case_3():
    address_0 = module_0.Address()
    str_0 = address_0.address()

def test_case_4():
    bool_0 = False
    address_0 = module_0.Address()
    str_0 = address_0.state()
    str_1 = address_0.street_name()
    str_2 = address_0.prefecture()
    dict_0 = address_0.coordinates(bool_0)

def test_case_5():
    address_0 = module_0.Address()
    str_0 = address_0.region()
    bool_0 = True
    var_0 = address_0.longitude(bool_0)
    str_1 = address_0.address()
    str_2 = address_0.city()

def test_case_6():
    address_0 = module_0.Address()
    str_0 = address_0.region()
    bool_0 = True
    str_1 = address_0.province()
    var_0 = address_0.longitude(bool_0)
    str_2 = address_0.address()
    dict_0 = {}
    address_1 = module_0.Address(**dict_0)
    var_1 = address_1.latitude(bool_0)

def test_case_7():
    address_0 = module_0.Address()
    str_0 = address_0.continent()
    dict_0 = {}
    address_1 = module_0.Address(**dict_0)
    str_1 = address_1.postal_code()
    str_2 = address_0.federal_subject()
    address_2 = module_0.Address()

def test_case_8():
    dict_0 = {}
    address_0 = module_0.Address(**dict_0)
    str_0 = address_0.zip_code()

def test_case_9():
    none_type_0 = None
    address_0 = module_0.Address()
    str_0 = address_0.country_code(none_type_0)
    dict_0 = {}
    address_1 = module_0.Address(**dict_0)
    str_1 = address_1.street_suffix()

def test_case_10():
    address_0 = module_0.Address()
    str_0 = address_0.zip_code()
    var_0 = address_0.longitude()
    str_1 = address_0.city()
    str_2 = address_0.continent()
    str_3 = address_0.address()

def test_case_11():
    bool_0 = True
    dict_0 = {}
    address_0 = module_0.Address(**dict_0)
    var_0 = address_0.latitude(bool_0)

def test_case_12():
    bool_0 = True
    address_0 = module_0.Address()
    str_0 = address_0.calling_code()
    str_1 = address_0.region()
    var_0 = address_0.latitude(bool_0)
    str_2 = address_0.address()
    str_3 = address_0.country()
    var_1 = address_0.longitude()
    str_4 = address_0.address()
    str_5 = address_0.continent(bool_0)

def test_case_13():
    address_0 = module_0.Address()
    str_0 = address_0.region()
    bool_0 = True
    var_0 = address_0.longitude(bool_0)
    str_1 = address_0.address()
    str_2 = address_0.city()
    address_1 = module_0.Address()
    str_3 = address_1.continent(bool_0)
    str_4 = address_0.address()

def test_case_14():
    bool_0 = True
    address_0 = module_0.Address()
    dict_0 = address_0.coordinates(bool_0)

def test_case_15():
    bool_0 = True
    address_0 = module_0.Address()
    dict_0 = address_0.coordinates(bool_0)

def test_case_16():
    bool_0 = True
    address_0 = module_0.Address()
    var_0 = address_0.longitude()
    address_1 = module_0.Address()
    str_0 = address_1.address()
    var_1 = address_1.longitude()
    str_1 = address_0.city()
    str_2 = address_0.continent()
    str_3 = address_0.address()
    str_4 = address_0.country(bool_0)