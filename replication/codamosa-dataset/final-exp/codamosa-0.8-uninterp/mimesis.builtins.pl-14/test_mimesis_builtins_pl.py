# Automatically generated by Pynguin.
import mimesis.builtins.pl as module_0
import builtins as module_1
import mimesis.providers.date as module_2
import mimesis.enums as module_3

def test_case_0():
    pass

def test_case_1():
    poland_spec_provider_0 = module_0.PolandSpecProvider()

def test_case_2():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()

def test_case_3():
    var_0 = None
    poland_spec_provider_0 = module_0.PolandSpecProvider(var_0)
    str_0 = poland_spec_provider_0.regon()
    str_1 = poland_spec_provider_0.pesel()
    str_2 = poland_spec_provider_0.nip()
    str_3 = poland_spec_provider_0.regon()
    str_4 = poland_spec_provider_0.pesel()
    str_5 = poland_spec_provider_0.regon()
    str_6 = poland_spec_provider_0.nip()

def test_case_4():
    optional_0 = None
    bytearray_0 = module_1.bytearray()
    poland_spec_provider_0 = module_0.PolandSpecProvider(bytearray_0)
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_1.pesel(optional_0)

def test_case_5():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.pesel()

def test_case_6():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.regon()
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_1 = poland_spec_provider_1.nip()

def test_case_7():
    var_0 = None
    poland_spec_provider_0 = module_0.PolandSpecProvider(var_0)
    str_0 = poland_spec_provider_0.pesel()
    str_1 = poland_spec_provider_0.nip()
    str_2 = poland_spec_provider_0.regon()
    str_3 = poland_spec_provider_0.pesel()
    str_4 = poland_spec_provider_0.regon()
    str_5 = poland_spec_provider_0.nip()

def test_case_8():
    int_0 = 2266
    datetime_0 = module_2.Datetime()
    datetime_1 = datetime_0.datetime(int_0, int_0)
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    gender_0 = module_3.Gender.MALE
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_1.pesel(datetime_1, gender_0)
    str_1 = poland_spec_provider_0.regon()
    str_2 = poland_spec_provider_1.regon()
    str_3 = poland_spec_provider_0.nip()
    str_4 = poland_spec_provider_1.pesel()
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_5 = poland_spec_provider_0.pesel()
    poland_spec_provider_3 = module_0.PolandSpecProvider()
    str_6 = poland_spec_provider_3.nip()
    str_7 = poland_spec_provider_2.regon()

def test_case_9():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()
    str_1 = poland_spec_provider_0.regon()
    str_2 = poland_spec_provider_0.nip()
    str_3 = poland_spec_provider_0.regon()
    str_4 = poland_spec_provider_0.nip()
    poland_spec_provider_1 = module_0.PolandSpecProvider(str_0)
    str_5 = poland_spec_provider_1.nip()
    datetime_0 = None
    str_6 = poland_spec_provider_1.pesel()
    str_7 = poland_spec_provider_1.regon()
    str_8 = poland_spec_provider_1.nip()
    str_9 = poland_spec_provider_0.pesel(datetime_0)
    str_10 = poland_spec_provider_0.pesel(datetime_0)
    str_11 = poland_spec_provider_0.pesel()
    str_12 = poland_spec_provider_1.pesel()
    gender_0 = module_3.Gender.FEMALE
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_13 = poland_spec_provider_2.pesel(datetime_0, gender_0)
    str_14 = poland_spec_provider_0.nip()
    str_15 = poland_spec_provider_0.regon()
    poland_spec_provider_3 = module_0.PolandSpecProvider()
    str_16 = poland_spec_provider_3.pesel(datetime_0)

def test_case_10():
    none_type_0 = None
    bytearray_0 = module_1.bytearray()
    poland_spec_provider_0 = module_0.PolandSpecProvider(bytearray_0)
    str_0 = poland_spec_provider_0.regon()
    poland_spec_provider_1 = module_0.PolandSpecProvider()
    str_1 = poland_spec_provider_1.pesel()
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_2 = poland_spec_provider_2.pesel(none_type_0)
    poland_spec_provider_3 = module_0.PolandSpecProvider()
    optional_0 = None
    str_3 = poland_spec_provider_2.pesel(optional_0)
    str_4 = poland_spec_provider_3.pesel()
    str_5 = poland_spec_provider_2.regon()
    str_6 = poland_spec_provider_3.nip()
    str_7 = poland_spec_provider_2.pesel()
    str_8 = poland_spec_provider_3.pesel()
    str_9 = poland_spec_provider_3.regon()
    str_10 = poland_spec_provider_3.regon()
    poland_spec_provider_4 = module_0.PolandSpecProvider()
    str_11 = poland_spec_provider_4.regon()
    str_12 = poland_spec_provider_3.pesel()
    str_13 = poland_spec_provider_4.regon()
    str_14 = poland_spec_provider_4.pesel()
    str_15 = poland_spec_provider_4.nip()
    int_0 = 269
    datetime_0 = module_2.Datetime()
    datetime_1 = datetime_0.datetime(int_0)
    str_16 = poland_spec_provider_3.pesel(datetime_1)
    str_17 = poland_spec_provider_4.regon()

def test_case_11():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.pesel()
    str_1 = poland_spec_provider_0.nip()
    str_2 = poland_spec_provider_0.pesel()
    int_0 = 2320
    datetime_0 = module_2.Datetime()
    str_3 = poland_spec_provider_0.pesel()
    datetime_1 = datetime_0.datetime(int_0, int_0)
    poland_spec_provider_1 = module_0.PolandSpecProvider(int_0)
    str_4 = poland_spec_provider_0.nip()
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_5 = poland_spec_provider_2.pesel()
    poland_spec_provider_3 = module_0.PolandSpecProvider()
    str_6 = poland_spec_provider_1.pesel()
    str_7 = poland_spec_provider_0.regon()
    str_8 = poland_spec_provider_0.regon()
    poland_spec_provider_4 = module_0.PolandSpecProvider()
    str_9 = poland_spec_provider_0.regon()
    str_10 = poland_spec_provider_3.pesel()
    str_11 = poland_spec_provider_1.pesel(datetime_1)
    gender_0 = module_3.Gender.FEMALE
    poland_spec_provider_5 = module_0.PolandSpecProvider()
    str_12 = poland_spec_provider_3.pesel(datetime_1, gender_0)
    str_13 = poland_spec_provider_2.nip()
    str_14 = poland_spec_provider_4.regon()
    str_15 = poland_spec_provider_3.pesel(datetime_1)

def test_case_12():
    poland_spec_provider_0 = module_0.PolandSpecProvider()
    str_0 = poland_spec_provider_0.nip()
    str_1 = poland_spec_provider_0.nip()
    str_2 = poland_spec_provider_0.pesel()
    int_0 = 2192
    str_3 = poland_spec_provider_0.nip()
    datetime_0 = module_2.Datetime()
    str_4 = poland_spec_provider_0.pesel()
    datetime_1 = datetime_0.datetime(int_0, int_0)
    poland_spec_provider_1 = module_0.PolandSpecProvider(int_0)
    str_5 = poland_spec_provider_0.regon()
    str_6 = poland_spec_provider_1.pesel(datetime_1)
    str_7 = poland_spec_provider_0.regon()
    str_8 = poland_spec_provider_0.nip()
    str_9 = poland_spec_provider_1.pesel()
    str_10 = poland_spec_provider_0.nip()
    str_11 = poland_spec_provider_1.pesel()
    str_12 = poland_spec_provider_0.regon()
    gender_0 = module_3.Gender.FEMALE
    poland_spec_provider_2 = module_0.PolandSpecProvider()
    str_13 = poland_spec_provider_2.pesel(datetime_1, gender_0)
    str_14 = poland_spec_provider_0.nip()
    str_15 = poland_spec_provider_1.regon()
    str_16 = poland_spec_provider_2.regon()
    poland_spec_provider_3 = module_0.PolandSpecProvider()
    str_17 = poland_spec_provider_3.regon()
    poland_spec_provider_4 = module_0.PolandSpecProvider()
    str_18 = poland_spec_provider_2.pesel(datetime_1)
    poland_spec_provider_5 = module_0.PolandSpecProvider(str_11)
    poland_spec_provider_6 = module_0.PolandSpecProvider()
    str_19 = poland_spec_provider_1.pesel(datetime_1)
    poland_spec_provider_7 = module_0.PolandSpecProvider()
    poland_spec_provider_8 = module_0.PolandSpecProvider()
    str_20 = poland_spec_provider_7.nip()
    str_21 = poland_spec_provider_1.regon()
    poland_spec_provider_9 = module_0.PolandSpecProvider()
    str_22 = poland_spec_provider_8.pesel()