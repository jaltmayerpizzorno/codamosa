# Automatically generated by Pynguin.
import mimesis.builtins.ru as module_0
import builtins as module_1
import mimesis.enums as module_2

def test_case_0():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()

def test_case_1():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.kpp()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.inn()
    optional_0 = None
    str_2 = russia_spec_provider_1.patronymic(optional_0)
    str_3 = russia_spec_provider_1.snils()
    str_4 = russia_spec_provider_1.generate_sentence()
    str_5 = russia_spec_provider_1.kpp()

def test_case_2():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.kpp()
    str_1 = russia_spec_provider_0.ogrn()
    bytes_0 = b'\xa5\xb7/^\xa5|\xbd5\xf0\x02\x96b\xf3'
    russia_spec_provider_1 = module_0.RussiaSpecProvider(bytes_0)
    str_2 = russia_spec_provider_1.patronymic()

def test_case_3():
    bytearray_0 = module_1.bytearray()
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytearray_0)
    str_0 = russia_spec_provider_0.passport_series()

def test_case_4():
    bytes_0 = b''
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    int_0 = russia_spec_provider_0.passport_number()

def test_case_5():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.patronymic()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.bic()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_2 = russia_spec_provider_2.bic()
    str_3 = russia_spec_provider_2.series_and_number()
    str_4 = russia_spec_provider_2.patronymic()
    str_5 = russia_spec_provider_2.passport_series()
    str_6 = russia_spec_provider_2.snils()
    str_7 = russia_spec_provider_2.passport_series()

def test_case_6():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()
    str_1 = russia_spec_provider_0.snils()
    str_2 = russia_spec_provider_0.inn()

def test_case_7():
    bytes_0 = b'\xc7\x1fjt\x0e\xbf\xa5\xa9\x08\x05'
    russia_spec_provider_0 = module_0.RussiaSpecProvider(bytes_0)
    str_0 = russia_spec_provider_0.kpp()

def test_case_8():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = 'Q\ro|R8f &"w\x0bi'
    int_0 = russia_spec_provider_0.passport_number()
    str_1 = russia_spec_provider_0.snils()
    str_2 = russia_spec_provider_0.passport_series(str_0)
    str_3 = russia_spec_provider_0.snils()
    int_1 = russia_spec_provider_0.passport_number()
    str_4 = russia_spec_provider_0.snils()
    str_5 = russia_spec_provider_0.passport_series()
    str_6 = russia_spec_provider_0.ogrn()

def test_case_9():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()
    str_1 = russia_spec_provider_0.snils()
    str_2 = russia_spec_provider_0.series_and_number()
    str_3 = russia_spec_provider_0.snils()
    str_4 = russia_spec_provider_0.series_and_number()
    str_5 = russia_spec_provider_0.kpp()
    str_6 = russia_spec_provider_0.passport_series()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_7 = russia_spec_provider_0.generate_sentence()
    str_8 = russia_spec_provider_1.passport_series()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_9 = russia_spec_provider_2.passport_series()
    str_10 = russia_spec_provider_2.kpp()
    str_11 = russia_spec_provider_2.generate_sentence()
    str_12 = russia_spec_provider_1.patronymic()
    str_13 = russia_spec_provider_0.generate_sentence()
    russia_spec_provider_3 = module_0.RussiaSpecProvider()
    russia_spec_provider_4 = module_0.RussiaSpecProvider()
    str_14 = russia_spec_provider_4.bic()
    str_15 = russia_spec_provider_2.generate_sentence()
    str_16 = russia_spec_provider_2.series_and_number()
    gender_0 = module_2.Gender.FEMALE
    russia_spec_provider_5 = module_0.RussiaSpecProvider(str_10)
    str_17 = russia_spec_provider_4.passport_series()
    str_18 = russia_spec_provider_1.patronymic(gender_0)
    str_19 = russia_spec_provider_1.generate_sentence()
    russia_spec_provider_6 = module_0.RussiaSpecProvider(str_10)
    str_20 = russia_spec_provider_4.kpp()
    str_21 = russia_spec_provider_6.snils()
    str_22 = russia_spec_provider_4.generate_sentence()
    str_23 = russia_spec_provider_0.inn()
    str_24 = russia_spec_provider_6.ogrn()
    russia_spec_provider_7 = module_0.RussiaSpecProvider()

def test_case_10():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()
    str_1 = russia_spec_provider_0.series_and_number()
    str_2 = russia_spec_provider_0.kpp()
    int_0 = 127
    str_3 = russia_spec_provider_0.inn()
    str_4 = russia_spec_provider_0.ogrn()
    str_5 = russia_spec_provider_0.bic()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_6 = russia_spec_provider_0.bic()
    str_7 = russia_spec_provider_0.bic()
    str_8 = russia_spec_provider_0.snils()
    str_9 = russia_spec_provider_0.bic()
    str_10 = russia_spec_provider_0.inn()
    str_11 = russia_spec_provider_0.passport_series(int_0)
    str_12 = russia_spec_provider_0.inn()
    str_13 = russia_spec_provider_0.inn()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_14 = russia_spec_provider_0.snils()
    str_15 = russia_spec_provider_1.series_and_number()
    russia_spec_provider_3 = module_0.RussiaSpecProvider(str_0)
    str_16 = russia_spec_provider_1.generate_sentence()
    str_17 = russia_spec_provider_3.ogrn()
    str_18 = russia_spec_provider_1.ogrn()
    str_19 = russia_spec_provider_1.ogrn()
    str_20 = russia_spec_provider_2.patronymic()
    str_21 = russia_spec_provider_3.passport_series()
    str_22 = russia_spec_provider_2.snils()
    str_23 = russia_spec_provider_0.snils()
    str_24 = russia_spec_provider_0.passport_series()
    str_25 = russia_spec_provider_2.passport_series()
    str_26 = russia_spec_provider_2.passport_series()
    str_27 = russia_spec_provider_0.series_and_number()
    russia_spec_provider_4 = module_0.RussiaSpecProvider(str_9)

def test_case_11():
    str_0 = ';}6vg@ZUz3J\r'
    russia_spec_provider_0 = module_0.RussiaSpecProvider(str_0)
    str_1 = russia_spec_provider_0.patronymic()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_2 = russia_spec_provider_2.generate_sentence()
    str_3 = russia_spec_provider_1.snils()
    str_4 = russia_spec_provider_1.bic()
    russia_spec_provider_3 = module_0.RussiaSpecProvider()
    gender_0 = module_2.Gender.FEMALE
    russia_spec_provider_4 = module_0.RussiaSpecProvider()
    str_5 = russia_spec_provider_4.patronymic(gender_0)
    str_6 = russia_spec_provider_1.ogrn()
    str_7 = russia_spec_provider_1.bic()
    str_8 = russia_spec_provider_3.ogrn()
    int_0 = russia_spec_provider_1.passport_number()
    int_1 = russia_spec_provider_3.passport_number()
    russia_spec_provider_5 = module_0.RussiaSpecProvider()
    none_type_0 = None
    str_9 = russia_spec_provider_2.inn()
    str_10 = russia_spec_provider_0.patronymic(none_type_0)
    str_11 = russia_spec_provider_3.series_and_number()
    str_12 = russia_spec_provider_1.series_and_number()
    str_13 = russia_spec_provider_2.passport_series()
    str_14 = russia_spec_provider_2.inn()