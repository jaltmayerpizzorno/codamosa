# Automatically generated by Pynguin.
import mimesis.providers.payment as module_0

def test_case_0():
    payment_0 = module_0.Payment()
    int_0 = payment_0.cvv()

def test_case_1():
    payment_0 = module_0.Payment()
    str_0 = payment_0.paypal()

def test_case_2():
    payment_0 = module_0.Payment()
    str_0 = payment_0.credit_card_number()
    str_1 = payment_0.bitcoin_address()
    payment_1 = module_0.Payment()
    str_2 = payment_0.bitcoin_address()
    int_0 = payment_0.cvv()

def test_case_3():
    payment_0 = module_0.Payment()
    str_0 = payment_0.credit_card_number()
    dict_0 = payment_0.credit_card_owner()
    str_1 = payment_0.ethereum_address()
    str_2 = payment_0.paypal()

def test_case_4():
    payment_0 = module_0.Payment()
    str_0 = payment_0.credit_card_number()
    dict_0 = payment_0.credit_card_owner()
    str_1 = payment_0.ethereum_address()
    str_2 = payment_0.credit_card_network()
    str_3 = payment_0.paypal()

def test_case_5():
    payment_0 = module_0.Payment()
    dict_0 = payment_0.credit_card_owner()

def test_case_6():
    payment_0 = module_0.Payment()
    dict_0 = payment_0.credit_card_owner()