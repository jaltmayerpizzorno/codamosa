# Automatically generated by Pynguin.
import mimesis.builtins.pt_br as module_0

def test_case_0():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()

def test_case_1():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cnpj()
    bool_0 = False
    str_1 = brazil_spec_provider_0.cpf(bool_0)
    brazil_spec_provider_1 = module_0.BrazilSpecProvider()
    str_2 = brazil_spec_provider_0.cnpj()
    bool_1 = False
    str_3 = brazil_spec_provider_0.cpf()
    str_4 = brazil_spec_provider_1.cnpj()
    brazil_spec_provider_2 = module_0.BrazilSpecProvider()
    str_5 = brazil_spec_provider_1.cpf(bool_1)
    str_6 = brazil_spec_provider_0.cnpj()

def test_case_2():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cpf()

def test_case_3():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cpf()

def test_case_4():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    bool_0 = False
    str_0 = brazil_spec_provider_0.cnpj(bool_0)
    str_1 = brazil_spec_provider_0.cnpj()
    str_2 = brazil_spec_provider_0.cpf()

def test_case_5():
    brazil_spec_provider_0 = module_0.BrazilSpecProvider()
    str_0 = brazil_spec_provider_0.cnpj()

def test_case_6():
    str_0 = '/ly1'
    brazil_spec_provider_0 = module_0.BrazilSpecProvider(str_0)
    str_1 = brazil_spec_provider_0.cpf()
    str_2 = brazil_spec_provider_0.cpf()