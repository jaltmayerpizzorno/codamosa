# Automatically generated by Pynguin.
import mimesis.builtins.pl as module_0
import builtins as module_1
import mimesis.enums as module_2
import mimesis.providers.date as module_3

def test_case_0():
    poland_spec_provider_0 = module_0.PolandSpecProvider()

def test_case_1():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.pesel()

def test_case_2():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.regon()
    str_1 = poland_spec_provider_0.pesel()

def test_case_3():
    bytearray_0 = module_1.bytearray()
    poland_spec_provider_0 = module_0.PolandSpecProvider(bytearray_0)
    str_0 = poland_spec_provider_0.regon()

def test_case_4():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_1.regon()

def test_case_5():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()
    str_1 = poland_spec_provider_0.nip()
    none_type_0 = None
    gender_0 = module_2.Gender.MALE
    str_2 = poland_spec_provider_0.nip()
    str_3 = poland_spec_provider_0.pesel(none_type_0, gender_0)
    str_4 = poland_spec_provider_0.pesel()
    poland_spec_provider_1 = module_0.PolandSpecProvider(str_3)

def test_case_6():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    none_type_0 = None
    gender_0 = module_2.Gender.FEMALE
    str_0 = poland_spec_provider_0.pesel(none_type_0, gender_0)
    str_1 = poland_spec_provider_0.regon()
    datetime_0 = None
    str_2 = poland_spec_provider_0.pesel(datetime_0)
    poland_spec_provider_1 = module_0.PolandSpecProvider(str_1)
    datetime_1 = module_3.Datetime()
    int_0 = 2369
    datetime_2 = datetime_1.datetime(int_0, int_0)
    str_3 = poland_spec_provider_0.pesel()
    str_4 = poland_spec_provider_1.pesel(datetime_2)
    str_5 = poland_spec_provider_1.nip()

def test_case_7():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.regon()
    str_1 = poland_spec_provider_0.pesel()
    datetime_0 = None
    str_2 = poland_spec_provider_0.pesel(datetime_0)
    poland_spec_provider_1 = module_0.PolandSpecProvider(str_1)
    datetime_1 = module_3.Datetime()
    int_0 = 2369
    datetime_2 = datetime_1.datetime(int_0, int_0)
    str_3 = poland_spec_provider_0.pesel()
    str_4 = poland_spec_provider_1.pesel(datetime_2)
    str_5 = poland_spec_provider_1.nip()

def test_case_8():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()
    str_1 = poland_spec_provider_0.regon()
    gender_0 = module_2.Gender.FEMALE
    str_2 = poland_spec_provider_0.pesel()
    datetime_0 = None
    str_3 = poland_spec_provider_0.pesel(datetime_0)
    datetime_1 = module_3.Datetime()
    int_0 = 2277
    datetime_2 = datetime_1.datetime(int_0, int_0)
    str_4 = poland_spec_provider_0.pesel()
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_5 = poland_spec_provider_2.pesel(datetime_2, gender_0)
    poland_spec_provider_3 = module_0.PolandSpecProvider()
    str_6 = poland_spec_provider_2.pesel()
    poland_spec_provider_4 = module_0.PolandSpecProvider()
    str_7 = poland_spec_provider_4.regon()