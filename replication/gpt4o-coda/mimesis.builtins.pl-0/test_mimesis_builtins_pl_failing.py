# Automatically generated by Pynguin.
import mimesis.builtins.pl as module_0
import mimesis.enums as module_1
import datetime as module_2

def test_case_0():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.pesel()
        str_1 = poland_spec_provider_0.nip()
        str_2 = poland_spec_provider_0.regon()
        str_3 = poland_spec_provider_0.pesel()
        datetime_0 = None
        str_4 = poland_spec_provider_0.pesel(datetime_0)
        gender_0 = module_1.Gender.FEMALE
        str_5 = poland_spec_provider_0.pesel(gender_0)
    except BaseException:
        pass

def test_case_1():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.pesel()
        str_1 = poland_spec_provider_0.nip()
        str_2 = poland_spec_provider_0.regon()
        str_3 = poland_spec_provider_0.pesel()
        datetime_0 = None
        str_4 = poland_spec_provider_0.pesel(datetime_0)
        gender_0 = module_1.Gender.MALE
        str_5 = poland_spec_provider_0.pesel(gender_0)
    except BaseException:
        pass

def test_case_2():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        optional_0 = None
        gender_0 = module_1.Gender.MALE
        str_0 = poland_spec_provider_0.nip()
        str_1 = poland_spec_provider_0.nip()
        str_2 = poland_spec_provider_0.pesel(optional_0, gender_0)
        poland_spec_provider_1 = module_0.PolandSpecProvider()
        str_3 = poland_spec_provider_1.pesel()
        poland_spec_provider_2 = module_0.PolandSpecProvider()
        datetime_0 = module_2.datetime()
    except BaseException:
        pass

def test_case_3():
    try:
        none_type_0 = None
        gender_0 = module_1.Gender.FEMALE
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.pesel(none_type_0, gender_0)
        poland_spec_provider_1 = module_0.PolandSpecProvider()
        str_1 = poland_spec_provider_1.pesel()
        str_2 = poland_spec_provider_1.pesel(gender_0)
    except BaseException:
        pass