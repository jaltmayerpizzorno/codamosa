# Automatically generated by Pynguin.
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1
import builtins as module_2

def test_case_0():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.generate_sentence()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()

def test_case_1():
    bytes_0 = b"c\xf6\xb4\xea}\x9b-\xec\x94 'h'\x8eV\xba"
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    str_0 = russia_spec_provider_0.kpp()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    gender_0 = module_1.Gender.MALE
    str_1 = russia_spec_provider_1.patronymic(gender_0)
    str_2 = russia_spec_provider_1.series_and_number()
    str_3 = russia_spec_provider_1.kpp()

def test_case_2():
    bytes_0 = b'\xebM'
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    str_0 = russia_spec_provider_0.passport_series()
    str_1 = russia_spec_provider_0.kpp()
    str_2 = russia_spec_provider_0.generate_sentence()
    str_3 = russia_spec_provider_0.bic()
    str_4 = russia_spec_provider_0.generate_sentence()

def test_case_3():
    bytes_0 = b'u9\xa3\x81\x94\xc9"3A\x96'
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    str_0 = russia_spec_provider_0.series_and_number()
    str_1 = russia_spec_provider_0.ogrn()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_2 = russia_spec_provider_2.ogrn()
    int_0 = russia_spec_provider_2.passport_number()

def test_case_4():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    bytes_0 = b'\xe5:\xa9\xba\xd5$\x0c\xc7\x99\x06\xd6)\xe9'
    russia_spec_provider_1 = module_0.RussiaSpecProvider(bytes_0)
    int_0 = russia_spec_provider_1.passport_number()
    str_0 = russia_spec_provider_1.series_and_number()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    russia_spec_provider_3 = module_0.RussiaSpecProvider(bytes_0)
    str_1 = russia_spec_provider_3.snils()

def test_case_5():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.passport_series()
    str_1 = russia_spec_provider_0.bic()
    str_2 = russia_spec_provider_0.generate_sentence()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_3 = russia_spec_provider_1.inn()
    str_4 = russia_spec_provider_0.ogrn()
    int_0 = russia_spec_provider_0.passport_number()
    str_5 = russia_spec_provider_0.series_and_number()
    int_1 = russia_spec_provider_0.passport_number()
    complex_0 = None
    str_6 = russia_spec_provider_0.patronymic(complex_0)
    str_7 = russia_spec_provider_1.snils()
    str_8 = russia_spec_provider_0.series_and_number()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_9 = russia_spec_provider_1.snils()
    str_10 = russia_spec_provider_1.bic()
    russia_spec_provider_3 = module_0.RussiaSpecProvider()
    str_11 = russia_spec_provider_3.kpp()
    str_12 = russia_spec_provider_1.inn()
    int_2 = russia_spec_provider_2.passport_number()
    str_13 = russia_spec_provider_1.snils()
    str_14 = russia_spec_provider_2.kpp()
    str_15 = russia_spec_provider_2.patronymic()
    str_16 = russia_spec_provider_3.kpp()
    str_17 = russia_spec_provider_1.kpp()
    str_18 = russia_spec_provider_2.kpp()
    str_19 = russia_spec_provider_0.bic()

def test_case_6():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    int_0 = russia_spec_provider_0.passport_number()
    str_0 = russia_spec_provider_0.passport_series()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.ogrn()
    int_1 = russia_spec_provider_1.passport_number()
    str_2 = russia_spec_provider_1.inn()
    str_3 = russia_spec_provider_0.generate_sentence()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_4 = russia_spec_provider_1.bic()
    russia_spec_provider_3 = module_0.RussiaSpecProvider(str_2)
    str_5 = russia_spec_provider_3.passport_series()
    int_2 = russia_spec_provider_1.passport_number()
    str_6 = russia_spec_provider_2.inn()
    str_7 = russia_spec_provider_3.snils()
    str_8 = russia_spec_provider_3.series_and_number()

def test_case_7():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.inn()
    str_1 = russia_spec_provider_0.bic()
    str_2 = ')bW'
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_3 = russia_spec_provider_1.inn()
    str_4 = russia_spec_provider_0.inn()
    russia_spec_provider_2 = module_0.RussiaSpecProvider(str_2)
    str_5 = russia_spec_provider_2.patronymic()
    russia_spec_provider_3 = module_0.RussiaSpecProvider()

def test_case_8():
    str_0 = "K#lKl*C#1Wu'T"
    optional_0 = None
    russia_spec_provider_0 = module_0.RussiaSpecProvider(str_0)
    str_1 = russia_spec_provider_0.ogrn()
    str_2 = russia_spec_provider_0.passport_series(optional_0)
    russia_spec_provider_1 = module_0.RussiaSpecProvider(str_0)
    str_3 = russia_spec_provider_1.generate_sentence()

def test_case_9():
    int_0 = -818
    bytearray_0 = module_2.bytearray()
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytearray_0)
    str_0 = russia_spec_provider_0.passport_series(int_0)
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.ogrn()
    str_2 = 'O^}R77jZ|j/pB;|3%*2A'
    str_3 = russia_spec_provider_1.ogrn()
    list_0 = [str_2, str_2, str_2]
    russia_spec_provider_2 = module_0.RussiaSpecProvider(str_2)
    str_4 = russia_spec_provider_2.patronymic()
    str_5 = russia_spec_provider_2.passport_series(list_0)
    russia_spec_provider_3 = module_0.RussiaSpecProvider(str_2)
    russia_spec_provider_4 = module_0.RussiaSpecProvider()
    str_6 = russia_spec_provider_3.passport_series()

def test_case_10():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.inn()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_0.series_and_number()
    str_2 = russia_spec_provider_1.ogrn()
    russia_spec_provider_2 = module_0.RussiaSpecProvider(str_2)
    str_3 = russia_spec_provider_1.inn()
    gender_0 = module_1.Gender.FEMALE
    str_4 = russia_spec_provider_0.patronymic(gender_0)
    str_5 = russia_spec_provider_1.passport_series()
    russia_spec_provider_3 = module_0.RussiaSpecProvider()
    str_6 = russia_spec_provider_0.ogrn()
    str_7 = russia_spec_provider_1.kpp()
    russia_spec_provider_4 = module_0.RussiaSpecProvider(str_7)
    str_8 = russia_spec_provider_4.generate_sentence()
    str_9 = russia_spec_provider_0.generate_sentence()
    str_10 = russia_spec_provider_0.generate_sentence()
    str_11 = russia_spec_provider_2.kpp()
    str_12 = russia_spec_provider_2.inn()
    str_13 = russia_spec_provider_0.kpp()
    str_14 = russia_spec_provider_1.generate_sentence()
    str_15 = russia_spec_provider_2.patronymic()
    str_16 = russia_spec_provider_1.passport_series()
    str_17 = russia_spec_provider_3.ogrn()
    russia_spec_provider_5 = module_0.RussiaSpecProvider()
    str_18 = russia_spec_provider_2.snils()
    str_19 = russia_spec_provider_3.generate_sentence()
    str_20 = russia_spec_provider_1.bic()
    str_21 = russia_spec_provider_3.bic()