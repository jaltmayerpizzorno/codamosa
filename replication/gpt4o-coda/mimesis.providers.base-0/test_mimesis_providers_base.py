# Automatically generated by Pynguin.
import mimesis.providers.base as module_0
import builtins as module_1

def test_case_0():
    base_data_provider_0 = module_0.BaseDataProvider()

def test_case_1():
    list_0 = []
    bytearray_0 = module_1.bytearray(*list_0)
    base_provider_0 = module_0.BaseProvider(bytearray_0)

def test_case_2():
    base_provider_0 = module_0.BaseProvider()
    str_0 = None
    base_provider_1 = module_0.BaseProvider()
    str_1 = base_provider_1.__str__()
    base_provider_2 = module_0.BaseProvider(str_0)

def test_case_3():
    bytearray_0 = module_1.bytearray()
    base_data_provider_0 = module_0.BaseDataProvider(bytearray_0)

def test_case_4():
    base_data_provider_0 = module_0.BaseDataProvider()
    generator_0 = base_data_provider_0.override_locale()
    base_data_provider_1 = module_0.BaseDataProvider()
    str_0 = base_data_provider_1.get_current_locale()

def test_case_5():
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.__str__()

def test_case_6():
    base_provider_0 = module_0.BaseProvider()
    base_provider_0.reseed()
    base_provider_0.reseed()
    str_0 = base_provider_0.__str__()
    base_provider_1 = module_0.BaseProvider()
    base_provider_2 = module_0.BaseProvider()
    base_provider_1.reseed()
    base_data_provider_0 = module_0.BaseDataProvider()
    base_provider_1.reseed()
    str_1 = base_provider_1.__str__()
    generator_0 = base_data_provider_0.override_locale()
    str_2 = base_data_provider_0.__str__()
    base_provider_3 = module_0.BaseProvider()
    str_3 = base_provider_3.__str__()
    base_provider_3.reseed()