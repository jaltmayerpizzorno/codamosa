# Automatically generated by Pynguin.
import mimesis.builtins.pt_br as module_0

def test_case_0():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cnpj()

def test_case_1():
    str_0 = None
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_1 = brazil_spec_provider_0.cnpj()
    brazil_spec_provider_1 = module_0.BrazilSpecProvider(str_0)
    bool_0 = False
    str_2 = brazil_spec_provider_1.cpf(bool_0)

def test_case_2():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cpf()

def test_case_3():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cpf()
    str_1 = brazil_spec_provider_0.cpf()

def test_case_4():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    bool_0 = False
    brazil_spec_provider_1 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_1.cnpj(bool_0)
    brazil_spec_provider_2 = module_0.BrazilSpecProvider(str_0)
    str_1 = brazil_spec_provider_1.cnpj()

def test_case_5():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    brazil_spec_provider_1 = module_0.BrazilSpecProvider(brazil_spec_provider_0)
    str_0 = brazil_spec_provider_1.cpf()
    brazil_spec_provider_2 = module_0.BrazilSpecProvider()
    str_1 = brazil_spec_provider_2.cpf()
    str_2 = brazil_spec_provider_2.cpf()