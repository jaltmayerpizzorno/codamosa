# Automatically generated by Pynguin.
import mimesis.builtins.ru as module_0
import mimesis.enums as module_1

def test_case_0():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()

def test_case_1():
    str_0 = 'hU5EENs\x0bo6/\\){\\ (#'
    russia_spec_provider_0 = module_0.RussiaSpecProvider(str_0)
    str_1 = russia_spec_provider_0.series_and_number()
    str_2 = russia_spec_provider_0.series_and_number()
    str_3 = russia_spec_provider_0.series_and_number()
    str_4 = russia_spec_provider_0.generate_sentence()
    str_5 = russia_spec_provider_0.bic()
    str_6 = russia_spec_provider_0.snils()
    str_7 = russia_spec_provider_0.snils()

def test_case_2():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()
    int_0 = russia_spec_provider_0.passport_number()
    str_1 = russia_spec_provider_0.patronymic()

def test_case_3():
    bytes_0 = b'dga\x9e'
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    int_0 = russia_spec_provider_0.passport_number()
    str_0 = russia_spec_provider_0.bic()
    str_1 = russia_spec_provider_0.ogrn()
    str_2 = russia_spec_provider_0.passport_series()

def test_case_4():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    optional_0 = None
    str_0 = russia_spec_provider_0.patronymic(optional_0)
    str_1 = russia_spec_provider_0.series_and_number()
    str_2 = russia_spec_provider_0.inn()
    str_3 = russia_spec_provider_0.ogrn()

def test_case_5():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.ogrn()
    str_1 = russia_spec_provider_0.bic()
    int_0 = russia_spec_provider_0.passport_number()
    str_2 = russia_spec_provider_0.snils()
    str_3 = russia_spec_provider_0.patronymic()
    int_1 = -2195
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_4 = russia_spec_provider_1.generate_sentence()
    str_5 = russia_spec_provider_0.bic()
    str_6 = russia_spec_provider_0.ogrn()
    str_7 = russia_spec_provider_0.ogrn()
    str_8 = russia_spec_provider_0.bic()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_9 = russia_spec_provider_0.ogrn()
    str_10 = russia_spec_provider_0.kpp()
    str_11 = russia_spec_provider_2.bic()
    russia_spec_provider_3 = module_0.RussiaSpecProvider()
    russia_spec_provider_4 = module_0.RussiaSpecProvider()
    str_12 = russia_spec_provider_4.series_and_number()
    russia_spec_provider_5 = module_0.RussiaSpecProvider(int_1)
    str_13 = russia_spec_provider_1.snils()
    str_14 = russia_spec_provider_5.kpp()
    russia_spec_provider_6 = module_0.RussiaSpecProvider()
    str_15 = russia_spec_provider_1.generate_sentence()
    gender_0 = module_1.Gender.FEMALE
    str_16 = russia_spec_provider_5.patronymic(gender_0)
    str_17 = russia_spec_provider_6.kpp()
    str_18 = russia_spec_provider_5.kpp()

def test_case_6():
    bytes_0 = b''
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    bytes_1 = b'*\x8as\x98{o\xe7\x8e'
    str_0 = russia_spec_provider_0.bic()
    russia_spec_provider_1 = module_0.RussiaSpecProvider(bytes_1)
    russia_spec_provider_2 = module_0.RussiaSpecProvider(bytes_1)
    str_1 = russia_spec_provider_2.snils()
    str_2 = russia_spec_provider_1.kpp()

def test_case_7():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.ogrn()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.bic()

def test_case_8():
    int_0 = 424
    russia_spec_provider_0 = module_0.RussiaSpecProvider(int_0)
    str_0 = russia_spec_provider_0.patronymic()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.kpp()

def test_case_9():
    bytes_0 = b'$9\xc6\xfez\xbe\xbd\x13.+\x10o'
    int_0 = -1414
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    str_0 = russia_spec_provider_0.passport_series(int_0)
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.bic()
    russia_spec_provider_2 = module_0.RussiaSpecProvider(bytes_0)
    str_2 = russia_spec_provider_2.bic()

def test_case_10():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    none_type_0 = None
    str_0 = russia_spec_provider_0.kpp()
    str_1 = russia_spec_provider_0.patronymic(none_type_0)
    str_2 = russia_spec_provider_0.patronymic()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_3 = russia_spec_provider_0.generate_sentence()
    str_4 = russia_spec_provider_0.patronymic()
    str_5 = russia_spec_provider_0.inn()
    str_6 = russia_spec_provider_0.patronymic()
    str_7 = russia_spec_provider_1.snils()
    int_0 = russia_spec_provider_1.passport_number()
    str_8 = russia_spec_provider_0.snils()
    str_9 = russia_spec_provider_1.inn()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_10 = russia_spec_provider_2.patronymic()
    str_11 = russia_spec_provider_0.snils()
    str_12 = russia_spec_provider_2.bic()
    str_13 = russia_spec_provider_0.snils()
    str_14 = russia_spec_provider_2.ogrn()
    russia_spec_provider_3 = module_0.RussiaSpecProvider()
    str_15 = russia_spec_provider_3.passport_series()
    str_16 = russia_spec_provider_0.snils()
    str_17 = russia_spec_provider_1.bic()
    russia_spec_provider_4 = module_0.RussiaSpecProvider()
    russia_spec_provider_5 = module_0.RussiaSpecProvider()
    str_18 = russia_spec_provider_4.snils()
    str_19 = russia_spec_provider_0.generate_sentence()
    str_20 = russia_spec_provider_3.series_and_number()
    russia_spec_provider_6 = module_0.RussiaSpecProvider()
    str_21 = russia_spec_provider_4.kpp()
    russia_spec_provider_7 = module_0.RussiaSpecProvider()
    russia_spec_provider_8 = module_0.RussiaSpecProvider(str_1)
    str_22 = russia_spec_provider_8.generate_sentence()
    russia_spec_provider_9 = module_0.RussiaSpecProvider()
    str_23 = russia_spec_provider_9.snils()