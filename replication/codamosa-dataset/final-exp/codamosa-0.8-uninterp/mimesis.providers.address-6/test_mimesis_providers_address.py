# Automatically generated by Pynguin.
import mimesis.providers.address as module_0
import mimesis.enums as module_1

def test_case_0():
    pass

def test_case_1():
    address_0 = module_0.Address()

def test_case_2():
    list_0 = []
    address_0 = module_0.Address(*list_0)
    str_0 = address_0.street_name()
    bool_0 = True
    var_0 = address_0.longitude(bool_0)

def test_case_3():
    bool_0 = True
    address_0 = module_0.Address()
    var_0 = address_0.latitude(bool_0)

def test_case_4():
    address_0 = module_0.Address()
    str_0 = address_0.address()

def test_case_5():
    address_0 = module_0.Address()
    str_0 = address_0.street_suffix()

def test_case_6():
    dict_0 = {}
    list_0 = []
    address_0 = module_0.Address(*list_0)
    str_0 = address_0.federal_subject(**dict_0)
    address_1 = module_0.Address()
    str_1 = address_1.street_name()

def test_case_7():
    address_0 = module_0.Address()
    var_0 = address_0.longitude()
    str_0 = address_0.address()
    str_1 = address_0.zip_code()

def test_case_8():
    address_0 = module_0.Address()
    country_code_0 = module_1.CountryCode.A3
    str_0 = address_0.country_code(country_code_0)
    var_0 = address_0.longitude()
    str_1 = address_0.address()
    str_2 = address_0.federal_subject()
    str_3 = address_0.street_name()
    str_4 = address_0.country()

def test_case_9():
    list_0 = []
    address_0 = module_0.Address(*list_0)
    str_0 = address_0.street_name()
    str_1 = address_0.country()
    bool_0 = True
    var_0 = address_0.longitude(bool_0)

def test_case_10():
    bool_0 = True
    address_0 = module_0.Address()
    str_0 = address_0.street_number()
    str_1 = address_0.street_suffix()
    str_2 = address_0.country(bool_0)
    dict_0 = address_0.coordinates(bool_0)

def test_case_11():
    list_0 = []
    address_0 = module_0.Address(*list_0)
    str_0 = address_0.street_name()
    str_1 = address_0.country()
    bool_0 = True
    dict_0 = address_0.coordinates(bool_0)
    address_1 = module_0.Address()
    str_2 = address_1.region()
    str_3 = address_1.postal_code()
    str_4 = address_0.continent()
    dict_1 = {}
    address_2 = module_0.Address(**dict_1)
    str_5 = address_2.continent()
    var_0 = address_2.longitude()
    str_6 = address_1.city()

def test_case_12():
    address_0 = module_0.Address()
    var_0 = address_0.longitude()
    str_0 = address_0.address()

def test_case_13():
    bool_0 = True
    address_0 = module_0.Address()
    str_0 = address_0.street_number()
    str_1 = address_0.continent(bool_0)
    str_2 = address_0.street_suffix()
    str_3 = address_0.country(bool_0)
    dict_0 = address_0.coordinates(bool_0)

def test_case_14():
    list_0 = []
    address_0 = module_0.Address(*list_0)
    str_0 = address_0.street_name()
    str_1 = address_0.country()
    bool_0 = True
    dict_0 = address_0.coordinates(bool_0)
    address_1 = module_0.Address()
    str_2 = address_1.region()
    address_2 = module_0.Address(*list_0)
    str_3 = address_2.address()
    str_4 = address_1.zip_code()

def test_case_15():
    address_0 = module_0.Address()
    address_1 = module_0.Address()
    bool_0 = True
    str_0 = address_0.calling_code()
    str_1 = address_0.street_suffix()
    str_2 = address_0.calling_code()
    str_3 = address_0.state(bool_0)
    str_4 = address_0.country()
    var_0 = address_0.latitude(bool_0)
    str_5 = address_0.continent()
    str_6 = address_1.street_suffix()
    address_2 = module_0.Address()
    str_7 = address_2.country()
    dict_0 = address_0.coordinates()

def test_case_16():
    address_0 = module_0.Address()
    str_0 = address_0.street_suffix()
    var_0 = address_0.longitude()
    address_1 = module_0.Address()
    bool_0 = False
    str_1 = address_1.continent(bool_0)
    str_2 = address_1.zip_code()
    str_3 = address_1.zip_code()

def test_case_17():
    address_0 = module_0.Address()
    address_1 = module_0.Address()
    bool_0 = True
    str_0 = address_0.calling_code()
    str_1 = address_0.street_suffix()
    str_2 = address_0.calling_code()
    str_3 = address_0.state(bool_0)
    str_4 = address_0.country()
    var_0 = address_1.longitude()
    str_5 = 'ja'
    list_0 = [str_5]
    address_2 = module_0.Address(*list_0)
    str_6 = address_2.address()
    str_7 = address_0.city()
    address_3 = module_0.Address()
    str_8 = address_3.state(bool_0)
    str_9 = address_0.zip_code()
    str_10 = address_3.street_number()
    str_11 = address_3.country_code()
    str_12 = address_2.prefecture()