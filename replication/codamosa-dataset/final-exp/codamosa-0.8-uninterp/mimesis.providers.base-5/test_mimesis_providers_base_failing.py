# Automatically generated by Pynguin.
import mimesis.providers.base as module_0
import builtins as module_1

def test_case_0():
    try:
        bytes_0 = b''
        base_provider_0 = module_0.BaseProvider(bytes_0)
        str_0 = '=4qp$LK/g\tZGz'
        list_0 = [base_provider_0, bytes_0, bytes_0, str_0]
        base_data_provider_0 = module_0.BaseDataProvider()
        str_1 = base_data_provider_0.get_current_locale()
        bytearray_0 = module_1.bytearray(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 348
        base_provider_0 = module_0.BaseProvider()
        base_provider_0.reseed()
        base_data_provider_0 = module_0.BaseDataProvider(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '%_2@T)1?HH(tlT`='
        base_data_provider_0 = module_0.BaseDataProvider()
        generator_0 = base_data_provider_0.override_locale()
        str_1 = base_data_provider_0.__str__()
        str_2 = base_data_provider_0.get_current_locale()
        base_data_provider_1 = module_0.BaseDataProvider(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        base_data_provider_0 = module_0.BaseDataProvider()
        str_0 = base_data_provider_0.__str__()
        str_1 = base_data_provider_0.get_current_locale()
        base_provider_0 = module_0.BaseProvider()
        base_provider_0.reseed()
        base_provider_0.reseed()
        float_0 = -1994.096
        base_data_provider_1 = module_0.BaseDataProvider(float_0)
    except BaseException:
        pass