# Automatically generated by Pynguin.
import mimesis.builtins.pl as module_0
import mimesis.enums as module_1
import builtins as module_2
import mimesis.providers.date as module_3

def test_case_0():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.pesel()
        datetime_0 = None
        poland_spec_provider_1 = module_0.PolandSpecProvider()
        str_1 = poland_spec_provider_1.regon()
        gender_0 = module_1.Gender.MALE
        str_2 = poland_spec_provider_0.pesel(datetime_0, gender_0)
        bytearray_0 = module_2.bytearray()
        poland_spec_provider_2 = module_0.PolandSpecProvider(bytearray_0)
        str_3 = poland_spec_provider_2.pesel(gender_0)
    except BaseException:
        pass

def test_case_1():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.nip()
        str_1 = poland_spec_provider_0.regon()
        str_2 = poland_spec_provider_0.nip()
        str_3 = '}i1&blS'
        poland_spec_provider_1 = module_0.PolandSpecProvider(str_3)
        poland_spec_provider_2 = module_0.PolandSpecProvider(str_3)
        str_4 = poland_spec_provider_1.regon()
        str_5 = poland_spec_provider_2.regon()
        str_6 = poland_spec_provider_2.pesel()
        str_7 = poland_spec_provider_0.pesel()
        int_0 = 1694
        datetime_0 = module_3.Datetime()
        datetime_1 = datetime_0.datetime(int_0)
        str_8 = poland_spec_provider_2.pesel(datetime_1)
        str_9 = poland_spec_provider_2.nip()
        gender_0 = module_1.Gender.MALE
        poland_spec_provider_3 = module_0.PolandSpecProvider()
        str_10 = poland_spec_provider_3.nip()
        str_11 = poland_spec_provider_2.pesel()
        str_12 = poland_spec_provider_1.pesel(gender_0)
    except BaseException:
        pass