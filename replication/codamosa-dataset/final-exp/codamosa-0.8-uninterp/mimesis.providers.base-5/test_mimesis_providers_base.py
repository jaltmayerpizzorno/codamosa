# Automatically generated by Pynguin.
import mimesis.providers.base as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    base_data_provider_0 = module_0.BaseDataProvider()

def test_case_2():
    base_provider_0 = module_0.BaseProvider()
    str_0 = base_provider_0.__str__()

def test_case_3():
    bytearray_0 = module_1.bytearray()
    base_provider_0 = module_0.BaseProvider(bytearray_0)
    str_0 = base_provider_0.__str__()
    bytearray_1 = module_1.bytearray()
    base_data_provider_0 = module_0.BaseDataProvider()
    str_1 = base_data_provider_0.__str__()
    base_data_provider_1 = module_0.BaseDataProvider(bytearray_1)
    str_2 = base_data_provider_0.get_current_locale()
    base_provider_1 = module_0.BaseProvider()
    base_provider_1.reseed(str_2)
    str_3 = base_data_provider_1.get_current_locale()
    int_0 = 1267
    generator_0 = base_data_provider_0.override_locale(str_0)
    generator_1 = base_data_provider_1.override_locale(str_3)
    base_provider_2 = module_0.BaseProvider(int_0)
    str_4 = base_data_provider_0.__str__()
    str_5 = base_data_provider_0.get_current_locale()
    str_6 = base_provider_2.__str__()
    generator_2 = base_data_provider_1.override_locale()

def test_case_4():
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.get_current_locale()

def test_case_5():
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.__str__()