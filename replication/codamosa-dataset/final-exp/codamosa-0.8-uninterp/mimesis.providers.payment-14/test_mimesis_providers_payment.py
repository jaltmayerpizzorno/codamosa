# Automatically generated by Pynguin.
import mimesis.providers.payment as module_0
import mimesis.enums as module_1

def test_case_0():
    payment_0 = module_0.Payment()
    dict_0 = payment_0.credit_card_owner()

def test_case_1():
    payment_0 = module_0.Payment()
    str_0 = payment_0.paypal()
    str_1 = payment_0.credit_card_network()
    payment_1 = module_0.Payment()
    int_0 = payment_1.cvv()
    dict_0 = payment_1.credit_card_owner()
    str_2 = payment_0.bitcoin_address()

def test_case_2():
    payment_0 = module_0.Payment()
    str_0 = payment_0.credit_card_number()
    payment_1 = module_0.Payment()
    int_0 = payment_1.cvv()
    payment_2 = module_0.Payment()
    payment_3 = module_0.Payment()
    str_1 = payment_3.ethereum_address()
    str_2 = payment_3.credit_card_network()

def test_case_3():
    payment_0 = module_0.Payment()
    dict_0 = payment_0.credit_card_owner()
    str_0 = payment_0.credit_card_network()

def test_case_4():
    payment_0 = module_0.Payment()
    dict_0 = payment_0.credit_card_owner()

def test_case_5():
    payment_0 = module_0.Payment()
    str_0 = payment_0.credit_card_number()
    str_1 = payment_0.credit_card_number()
    dict_0 = payment_0.credit_card_owner()
    int_0 = -1229
    card_type_0 = module_1.CardType.AMERICAN_EXPRESS
    str_2 = payment_0.credit_card_number(card_type_0)
    str_3 = payment_0.bitcoin_address()
    str_4 = payment_0.credit_card_network()
    int_1 = payment_0.cid()
    str_5 = payment_0.credit_card_number()
    int_2 = payment_0.cvv()
    str_6 = payment_0.bitcoin_address()
    str_7 = payment_0.ethereum_address()
    payment_1 = module_0.Payment()
    str_8 = payment_1.credit_card_expiration_date(int_0)