# Automatically generated by Pynguin.
import mimesis.builtins.pl as module_0
import mimesis.enums as module_1
import mimesis.providers.date as module_2

def test_case_0():
    poland_spec_provider_0 = module_0.PolandSpecProvider()

def test_case_1():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()

def test_case_2():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.pesel()

def test_case_3():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.pesel()

def test_case_4():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.regon()

def test_case_5():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.regon()

def test_case_6():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()
    str_1 = poland_spec_provider_0.pesel()
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_2 = poland_spec_provider_1.nip()
    datetime_0 = None
    str_3 = poland_spec_provider_1.pesel(datetime_0)
    str_4 = poland_spec_provider_0.pesel()
    str_5 = poland_spec_provider_1.regon()
    str_6 = poland_spec_provider_0.pesel(datetime_0)
    str_7 = poland_spec_provider_1.nip()
    str_8 = poland_spec_provider_1.nip()
    str_9 = poland_spec_provider_0.nip()
    gender_0 = module_1.Gender.MALE
    str_10 = poland_spec_provider_0.pesel(datetime_0, gender_0)
    str_11 = poland_spec_provider_0.pesel()

def test_case_7():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()
    str_1 = poland_spec_provider_0.nip()
    none_type_0 = None
    gender_0 = module_1.Gender.FEMALE
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_2 = poland_spec_provider_1.pesel(none_type_0, gender_0)

def test_case_8():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_1.regon()
    datetime_0 = None
    str_1 = poland_spec_provider_1.pesel(datetime_0)
    str_2 = poland_spec_provider_0.pesel()
    str_3 = poland_spec_provider_0.regon()
    str_4 = poland_spec_provider_1.regon()
    datetime_1 = module_2.Datetime()
    int_0 = 3488
    datetime_2 = datetime_1.datetime(int_0, int_0)
    str_5 = poland_spec_provider_0.regon()
    gender_0 = module_1.Gender.FEMALE
    str_6 = poland_spec_provider_0.pesel(datetime_0, gender_0)
    str_7 = poland_spec_provider_0.pesel(datetime_2)
    str_8 = poland_spec_provider_0.pesel()
    str_9 = poland_spec_provider_1.regon()
    str_10 = poland_spec_provider_1.regon()
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_11 = poland_spec_provider_2.nip()
    datetime_3 = module_2.Datetime()
    int_1 = 1386
    datetime_4 = datetime_3.datetime(int_1)
    str_12 = poland_spec_provider_1.nip()
    str_13 = poland_spec_provider_2.pesel(datetime_4)
    poland_spec_provider_3 = module_0.PolandSpecProvider(str_4)
    str_14 = poland_spec_provider_1.pesel()

def test_case_9():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.pesel()
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_1 = poland_spec_provider_1.regon()
    str_2 = poland_spec_provider_0.pesel()
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_3 = poland_spec_provider_0.regon()
    str_4 = poland_spec_provider_1.nip()
    datetime_0 = module_2.Datetime()
    int_0 = 4000
    datetime_1 = datetime_0.datetime(int_0, int_0)
    str_5 = poland_spec_provider_2.nip()
    str_6 = poland_spec_provider_2.pesel(datetime_1)
    str_7 = poland_spec_provider_1.nip()
    poland_spec_provider_3 = module_0.PolandSpecProvider()
    str_8 = poland_spec_provider_3.nip()