# Automatically generated by Pynguin.
import mimesis.builtins.pl as module_0
import mimesis.enums as module_1
import mimesis.providers.date as module_2

def test_case_0():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.regon()
        str_1 = poland_spec_provider_0.nip()
        gender_0 = module_1.Gender.MALE
        poland_spec_provider_1 = module_0.PolandSpecProvider()
        str_2 = poland_spec_provider_1.nip()
        str_3 = poland_spec_provider_1.pesel(gender_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'dotson'
        gender_0 = module_1.Gender.FEMALE
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_1 = poland_spec_provider_0.pesel(str_0, gender_0)
    except BaseException:
        pass

def test_case_2():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.nip()
        int_0 = -6684
        poland_spec_provider_1 = module_0.PolandSpecProvider(int_0)
        str_1 = poland_spec_provider_1.nip()
        str_2 = poland_spec_provider_0.pesel()
        str_3 = poland_spec_provider_0.nip()
        str_4 = poland_spec_provider_0.regon()
        gender_0 = module_1.Gender.MALE
        int_1 = 305
        datetime_0 = module_2.Datetime()
        datetime_1 = datetime_0.datetime(int_1)
        str_5 = poland_spec_provider_1.pesel(datetime_1, gender_0)
        str_6 = poland_spec_provider_1.regon()
        str_7 = poland_spec_provider_1.pesel(datetime_1)
        poland_spec_provider_2 = module_0.PolandSpecProvider()
        str_8 = poland_spec_provider_2.pesel()
        poland_spec_provider_3 = module_0.PolandSpecProvider()
        poland_spec_provider_4 = module_0.PolandSpecProvider()
        str_9 = poland_spec_provider_0.pesel(gender_0)
    except BaseException:
        pass

def test_case_3():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.nip()
        int_0 = -6684
        poland_spec_provider_1 = module_0.PolandSpecProvider(int_0)
        bool_0 = False
        str_1 = poland_spec_provider_1.nip()
        str_2 = poland_spec_provider_1.pesel(bool_0)
        str_3 = poland_spec_provider_1.nip()
        str_4 = poland_spec_provider_1.regon()
        none_type_0 = None
        gender_0 = module_1.Gender.MALE
        str_5 = poland_spec_provider_0.pesel(none_type_0, gender_0)
        str_6 = poland_spec_provider_0.pesel()
        str_7 = poland_spec_provider_1.pesel()
        poland_spec_provider_2 = module_0.PolandSpecProvider()
        optional_0 = None
        str_8 = poland_spec_provider_2.pesel(optional_0)
        poland_spec_provider_3 = module_0.PolandSpecProvider()
        datetime_0 = module_2.Datetime()
        int_1 = -4139
        datetime_1 = datetime_0.datetime(int_1)
        poland_spec_provider_4 = module_0.PolandSpecProvider()
        str_9 = datetime_0.gmt_offset()
        str_10 = poland_spec_provider_4.pesel(datetime_1)
        poland_spec_provider_5 = module_0.PolandSpecProvider(str_8)
        str_11 = poland_spec_provider_0.pesel(gender_0)
    except BaseException:
        pass

def test_case_4():
    try:
        poland_spec_provider_0 = module_0.PolandSpecProvider()
        poland_spec_provider_1 = module_0.PolandSpecProvider()
        str_0 = poland_spec_provider_0.nip()
        gender_0 = module_1.Gender.MALE
        str_1 = poland_spec_provider_0.pesel()
        datetime_0 = module_2.Datetime()
        int_0 = 2193
        datetime_1 = datetime_0.datetime(int_0, int_0)
        str_2 = poland_spec_provider_0.pesel()
        poland_spec_provider_2 = module_0.PolandSpecProvider()
        str_3 = poland_spec_provider_1.pesel(datetime_1, gender_0)
        str_4 = poland_spec_provider_2.regon()
        str_5 = poland_spec_provider_2.regon()
        str_6 = poland_spec_provider_2.pesel(datetime_1, gender_0)
        str_7 = poland_spec_provider_0.pesel()
        gender_1 = module_1.Gender.FEMALE
        str_8 = poland_spec_provider_1.pesel()
        poland_spec_provider_3 = module_0.PolandSpecProvider()
        str_9 = poland_spec_provider_1.pesel(datetime_1, gender_1)
        gender_2 = module_1.Gender.MALE
        poland_spec_provider_4 = module_0.PolandSpecProvider(str_1)
        str_10 = poland_spec_provider_3.pesel(gender_2)
    except BaseException:
        pass