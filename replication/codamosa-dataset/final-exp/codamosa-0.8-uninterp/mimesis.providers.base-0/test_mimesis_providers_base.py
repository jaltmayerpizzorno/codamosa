# Automatically generated by Pynguin.
import mimesis.providers.base as module_0

def test_case_0():
    pass

def test_case_1():
    base_provider_0 = module_0.BaseProvider()
    base_provider_0.reseed()

def test_case_2():
    base_provider_0 = module_0.BaseProvider()
    str_0 = base_provider_0.__str__()
    base_provider_1 = module_0.BaseProvider()
    bytes_0 = b''
    base_data_provider_0 = module_0.BaseDataProvider(bytes_0)
    base_provider_1.reseed()
    str_1 = base_provider_1.__str__()
    base_provider_1.reseed()
    base_provider_1.reseed()

def test_case_3():
    base_data_provider_0 = module_0.BaseDataProvider()
    generator_0 = base_data_provider_0.override_locale()
    base_data_provider_1 = module_0.BaseDataProvider()
    bytes_0 = b'p\x0e'
    str_0 = '.bb'
    base_provider_0 = module_0.BaseProvider(str_0)
    base_provider_0.reseed(bytes_0)
    str_1 = base_data_provider_1.get_current_locale()
    str_2 = '\n&$}bL\x0bwQgfY\r\x0cFG\rA<1'
    generator_1 = base_data_provider_1.override_locale(str_2)
    str_3 = base_data_provider_1.__str__()
    base_provider_1 = module_0.BaseProvider(str_3)
    base_provider_1.reseed()