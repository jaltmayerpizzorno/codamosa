# Automatically generated by Pynguin.
import mimesis.providers.base as module_0

def test_case_0():
    pass

def test_case_1():
    base_data_provider_0 = module_0.BaseDataProvider()

def test_case_2():
    base_data_provider_0 = module_0.BaseDataProvider()
    base_provider_0 = module_0.BaseProvider(base_data_provider_0)
    str_0 = base_provider_0.__str__()
    generator_0 = base_data_provider_0.override_locale()

def test_case_3():
    str_0 = ''
    base_data_provider_0 = module_0.BaseDataProvider(str_0)
    str_1 = base_data_provider_0.__str__()
    base_provider_0 = module_0.BaseProvider()
    str_2 = base_data_provider_0.get_current_locale()
    base_provider_1 = module_0.BaseProvider(str_0)
    base_provider_1.reseed()
    str_3 = base_data_provider_0.__str__()
    base_provider_0.reseed()
    str_4 = base_provider_1.__str__()
    base_provider_2 = module_0.BaseProvider()
    base_data_provider_1 = module_0.BaseDataProvider()

def test_case_4():
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.get_current_locale()

def test_case_5():
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.__str__()

def test_case_6():
    base_data_provider_0 = module_0.BaseDataProvider()
    str_0 = base_data_provider_0.__str__()
    base_provider_0 = module_0.BaseProvider()
    str_1 = base_data_provider_0.get_current_locale()
    base_provider_0.reseed()
    base_provider_0.reseed()
    str_2 = base_provider_0.__str__()