# Automatically generated by Pynguin.
import mimesis.providers.payment as module_0

def test_case_0():
    try:
        payment_0 = module_0.Payment()
        int_0 = payment_0.cvv()
        int_1 = payment_0.cvv()
        none_type_0 = None
        str_0 = payment_0.credit_card_number(none_type_0)
        dict_0 = payment_0.credit_card_owner()
        str_1 = payment_0.ethereum_address()
        str_2 = payment_0.credit_card_number(payment_0)
    except BaseException:
        pass