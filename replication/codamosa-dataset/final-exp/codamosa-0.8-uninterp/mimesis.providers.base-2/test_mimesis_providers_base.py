# Automatically generated by Pynguin.
import mimesis.providers.base as module_0

def test_case_0():
    pass

def test_case_1():
    base_data_provider_0 = module_0.BaseDataProvider()

def test_case_2():
    int_0 = 4939
    base_provider_0 = module_0.BaseProvider(int_0)
    str_0 = base_provider_0.__str__()

def test_case_3():
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.__str__()
    base_provider_0 = module_0.BaseProvider()
    base_provider_0.reseed()

def test_case_4():
    base_provider_0 = module_0.BaseProvider()
    base_provider_0.reseed()
    int_0 = 40
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.__str__()
    base_provider_1 = module_0.BaseProvider()
    str_1 = base_provider_0.__str__()
    base_provider_1.reseed()
    generator_0 = base_data_provider_0.override_locale()
    base_provider_1.reseed(int_0)