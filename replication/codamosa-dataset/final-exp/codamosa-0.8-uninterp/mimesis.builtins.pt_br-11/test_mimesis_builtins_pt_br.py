# Automatically generated by Pynguin.
import mimesis.builtins.pt_br as module_0
import builtins as module_1

def test_case_0():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cnpj()

def test_case_1():
    bool_0 = False
    bytearray_0 = module_1.bytearray()
    brazil_spec_provider_0 = module_0.BrazilSpecProvider(bytearray_0)
    str_0 = brazil_spec_provider_0.cpf(bool_0)

def test_case_2():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cpf()

def test_case_3():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cpf()

def test_case_4():
    str_0 = '0q_inrdo{'
    bool_0 = False
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    bool_1 = False
    str_1 = brazil_spec_provider_0.cpf(bool_1)
    bool_2 = True
    brazil_spec_provider_1 = module_0.BrazilSpecProvider()
    str_2 = brazil_spec_provider_1.cpf(bool_2)
    str_3 = brazil_spec_provider_0.cnpj(bool_0)
    bool_3 = True
    brazil_spec_provider_2 = module_0.BrazilSpecProvider()
    str_4 = brazil_spec_provider_2.cpf(bool_3)
    brazil_spec_provider_3 = module_0.BrazilSpecProvider(str_0)

def test_case_5():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cpf()
    bool_0 = True
    str_1 = brazil_spec_provider_0.cpf(bool_0)
    str_2 = brazil_spec_provider_0.cpf()