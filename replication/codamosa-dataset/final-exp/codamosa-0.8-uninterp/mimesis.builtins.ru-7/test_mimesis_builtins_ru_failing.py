# Automatically generated by Pynguin.
import mimesis.builtins.ru as module_0

def test_case_0():
    try:
        bytes_0 = b'\x0ct\x8d\xd9Z\xbd\xbf\x08.\xb8\x8f\xf9\x901?\r\x80n'
        russia_spec_provider_0 = module_0.RussiaSpecProvider()
        str_0 = russia_spec_provider_0.passport_series()
        russia_spec_provider_1 = module_0.RussiaSpecProvider(bytes_0)
        str_1 = russia_spec_provider_1.snils()
        russia_spec_provider_2 = module_0.RussiaSpecProvider()
        int_0 = russia_spec_provider_1.passport_number()
        russia_spec_provider_3 = module_0.RussiaSpecProvider(bytes_0)
        str_2 = russia_spec_provider_1.ogrn()
        str_3 = russia_spec_provider_3.passport_series()
        str_4 = russia_spec_provider_2.inn()
        str_5 = 'palaeocrinoidea'
        str_6 = russia_spec_provider_0.snils()
        str_7 = russia_spec_provider_1.ogrn()
        str_8 = russia_spec_provider_3.kpp()
        russia_spec_provider_4 = module_0.RussiaSpecProvider()
        int_1 = russia_spec_provider_2.passport_number()
        str_9 = russia_spec_provider_1.generate_sentence()
        str_10 = russia_spec_provider_2.series_and_number()
        str_11 = russia_spec_provider_2.snils()
        russia_spec_provider_5 = module_0.RussiaSpecProvider()
        str_12 = russia_spec_provider_3.bic()
        str_13 = russia_spec_provider_1.patronymic(str_5)
    except BaseException:
        pass