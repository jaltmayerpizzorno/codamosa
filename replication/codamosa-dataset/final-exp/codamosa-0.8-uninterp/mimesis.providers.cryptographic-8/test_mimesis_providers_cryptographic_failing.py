# Automatically generated by Pynguin.
import mimesis.providers.cryptographic as module_0

def test_case_0():
    try:
        cryptographic_0 = module_0.Cryptographic()
        str_0 = cryptographic_0.token_hex()
        cryptographic_1 = module_0.Cryptographic()
        cryptographic_2 = module_0.Cryptographic()
        str_1 = cryptographic_1.token_hex()
        cryptographic_3 = module_0.Cryptographic()
        str_2 = cryptographic_3.mnemonic_phrase(cryptographic_1)
    except BaseException:
        pass