# Automatically generated by Pynguin.
import mimesis.enums as module_0
import mimesis.providers.cryptographic as module_1

def test_case_0():
    try:
        algorithm_0 = module_0.Algorithm.SHA512
        list_0 = [algorithm_0]
        cryptographic_0 = module_1.Cryptographic(*list_0)
        str_0 = cryptographic_0.hash()
        cryptographic_1 = module_1.Cryptographic()
        var_0 = cryptographic_1.token_urlsafe()
        int_0 = -3119
        cryptographic_2 = module_1.Cryptographic()
        bytes_0 = cryptographic_2.token_bytes(int_0)
    except BaseException:
        pass