# Automatically generated by Pynguin.
import mimesis.providers.cryptographic as module_0

def test_case_0():
    try:
        cryptographic_0 = module_0.Cryptographic()
        var_0 = cryptographic_0.uuid()
        bytes_0 = cryptographic_0.token_bytes()
        str_0 = cryptographic_0.hash()
        str_1 = cryptographic_0.mnemonic_phrase()
        bytes_1 = cryptographic_0.token_bytes()
        str_2 = cryptographic_0.token_hex()
        str_3 = cryptographic_0.hash()
        cryptographic_1 = module_0.Cryptographic()
        var_1 = cryptographic_1.uuid()
        bytes_2 = cryptographic_1.token_bytes()
        str_4 = cryptographic_0.token_hex()
        var_2 = cryptographic_1.token_urlsafe()
        str_5 = cryptographic_1.hash()
        bool_0 = True
        var_3 = cryptographic_1.uuid(bool_0)
        int_0 = -2759
        str_6 = cryptographic_1.token_hex(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        cryptographic_0 = module_0.Cryptographic()
        var_0 = cryptographic_0.token_urlsafe()
        str_0 = cryptographic_0.hash()
        str_1 = cryptographic_0.mnemonic_phrase(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        cryptographic_0 = module_0.Cryptographic()
        str_0 = cryptographic_0.mnemonic_phrase(int_0)
    except BaseException:
        pass