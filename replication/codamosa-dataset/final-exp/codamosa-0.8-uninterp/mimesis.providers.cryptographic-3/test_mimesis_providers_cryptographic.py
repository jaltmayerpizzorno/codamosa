# Automatically generated by Pynguin.
import mimesis.providers.cryptographic as module_0
import mimesis.enums as module_1

def test_case_0():
    cryptographic_0 = module_0.Cryptographic()
    bytes_0 = cryptographic_0.token_bytes()

def test_case_1():
    cryptographic_0 = module_0.Cryptographic()
    str_0 = cryptographic_0.hash()

def test_case_2():
    cryptographic_0 = module_0.Cryptographic()
    algorithm_0 = module_1.Algorithm.SHA512
    int_0 = None
    str_0 = cryptographic_0.token_hex(int_0)
    str_1 = cryptographic_0.hash(algorithm_0)
    var_0 = cryptographic_0.token_urlsafe()
    str_2 = cryptographic_0.hash()
    str_3 = cryptographic_0.mnemonic_phrase()

def test_case_3():
    int_0 = 2526
    cryptographic_0 = module_0.Cryptographic()
    var_0 = cryptographic_0.uuid()
    str_0 = 'dabblingly'
    cryptographic_1 = module_0.Cryptographic()
    str_1 = cryptographic_1.mnemonic_phrase(int_0, str_0)
    bytes_0 = cryptographic_1.token_bytes()
    str_2 = cryptographic_1.hash()
    str_3 = cryptographic_1.mnemonic_phrase()
    str_4 = cryptographic_1.token_hex()
    str_5 = cryptographic_0.hash()
    var_1 = cryptographic_0.token_urlsafe()
    algorithm_0 = module_1.Algorithm.MD5
    str_6 = cryptographic_1.hash(algorithm_0)
    str_7 = cryptographic_0.mnemonic_phrase()