# Automatically generated by Pynguin.
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

def test_case_0():
    price_0 = module_0.Price()

def test_case_1():
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.negative()

def test_case_2():
    decimal_0 = None
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.scalar_add(none_money_0)
    none_money_1 = module_0.NoneMoney()
    bool_0 = none_money_1.gt(money_0)
    var_0 = None
    list_0 = [var_0, var_0, var_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_1 = some_money_0.lt(money_0)
    money_1 = none_money_1.with_qty(decimal_0)
    bool_2 = some_money_0.lt(money_1)
    money_2 = some_money_0.subtract(money_1)
    bool_3 = money_2.__le__(money_0)
    bool_4 = some_money_0.gte(money_0)
    money_3 = some_money_0.add(money_0)
    money_4 = money_1.__add__(money_0)

def test_case_3():
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.abs()
    price_1 = none_price_0.positive()

def test_case_4():
    set_0 = set()
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.floor_divide(set_0)
    price_1 = price_0.__neg__()

def test_case_5():
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.negative()
    price_1 = none_price_0.positive()

def test_case_6():
    none_price_0 = module_0.NonePrice()
    var_0 = None
    list_0 = [var_0, var_0, var_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.as_boolean()
    currency_0 = None
    price_0 = none_price_0.with_ccy(currency_0)
    price_1 = price_0.scalar_subtract(var_0)
    decimal_0 = module_1.Decimal()
    some_price_0 = module_0.SomePrice(*list_0)
    price_2 = some_price_0.with_qty(decimal_0)
    price_3 = price_2.negative()
    bool_1 = price_3.__le__(price_3)

def test_case_7():
    money_0 = module_0.Money()
    list_0 = [money_0, money_0, money_0]
    some_price_0 = module_0.SomePrice(*list_0)
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.negative()
    price_1 = price_0.negative()
    bool_0 = some_price_0.lt(price_1)
    price_2 = price_0.subtract(price_0)

def test_case_8():
    money_0 = module_0.Money()
    str_0 = '_T'
    int_0 = 29
    currency_type_0 = module_2.CurrencyType.CRYPTO
    decimal_0 = module_1.Decimal()
    currency_0 = module_2.Currency(str_0, str_0, int_0, currency_type_0, decimal_0, int_0)
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.with_ccy(currency_0)
    money_1 = money_0.with_qty(decimal_0)

def test_case_9():
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.positive()
    bool_0 = none_price_0.is_equal(price_0)

def test_case_10():
    money_0 = module_0.Money()
    list_0 = [money_0, money_0, money_0]
    some_price_0 = module_0.SomePrice(*list_0)
    var_0 = None
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.divide(var_0)
    bool_0 = some_price_0.gt(price_0)
    price_1 = price_0.subtract(price_0)

def test_case_11():
    bytes_0 = b'\x85\xa8\xa4\x1c\xa2\xaf\xf3\xe4\xd2\xdc\xdf\xf1\x01'
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.floor_divide(bytes_0)
    bool_0 = money_0.__bool__()

def test_case_12():
    none_price_0 = module_0.NonePrice()
    none_money_0 = module_0.NoneMoney()
    money_0 = None
    bool_0 = none_money_0.gt(money_0)
    var_0 = None
    list_0 = [var_0, var_0, var_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_1 = some_money_0.as_boolean()
    money_1 = none_money_0.multiply(var_0)
    some_price_0 = module_0.SomePrice(*list_0)
    bool_2 = some_price_0.is_equal(bool_0)
    money_2 = money_1.__add__(money_0)

def test_case_13():
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.scalar_add(none_money_0)
    none_money_1 = module_0.NoneMoney()
    bool_0 = none_money_1.gt(money_0)
    var_0 = None
    list_0 = [var_0, var_0, var_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_1 = some_money_0.lt(money_0)
    money_1 = none_money_0.multiply(var_0)
    bool_2 = some_money_0.lt(money_1)
    money_2 = some_money_0.subtract(money_1)
    bool_3 = money_2.__le__(money_0)
    bool_4 = some_money_0.gte(money_0)
    money_3 = some_money_0.add(money_0)
    money_4 = money_1.__add__(money_0)

def test_case_14():
    date_0 = None
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.abs()
    price_1 = none_price_0.with_dov(date_0)
    dict_0 = {}
    price_2 = module_0.Price(**dict_0)
    bool_0 = price_2.gte(price_1)

def test_case_15():
    none_price_0 = module_0.NonePrice()
    var_0 = None
    list_0 = [var_0, var_0, var_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.as_boolean()
    decimal_0 = module_1.Decimal()
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.with_qty(decimal_0)
    price_1 = price_0.negative()
    bool_1 = price_1.__le__(price_1)

def test_case_16():
    price_0 = module_0.Price()
    bool_0 = price_0.__ge__(price_0)
    bool_1 = price_0.__bool__()

def test_case_17():
    price_0 = module_0.Price()
    int_0 = price_0.__int__()

def test_case_18():
    price_0 = module_0.Price()
    price_1 = price_0.__pos__()

def test_case_19():
    money_0 = module_0.Money()
    money_1 = money_0.__pos__()

def test_case_20():
    money_0 = module_0.Money()
    money_1 = money_0.__abs__()

def test_case_21():
    money_0 = module_0.Money()
    bool_0 = money_0.__eq__(money_0)

def test_case_22():
    money_0 = module_0.Money()
    float_0 = -530.2095
    list_0 = [money_0, money_0, money_0, float_0]
    money_1 = money_0.__truediv__(list_0)
    bool_0 = money_0.lte(money_0)

def test_case_23():
    money_0 = module_0.Money()
    bool_0 = money_0.__bool__()

def test_case_24():
    money_0 = module_0.Money()
    list_0 = [money_0, money_0, money_0]
    some_price_0 = module_0.SomePrice(*list_0)
    var_0 = None
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.divide(var_0)
    bool_0 = some_price_0.gt(price_0)
    currency_0 = None
    price_1 = some_price_0.with_ccy(currency_0)
    price_2 = price_1.subtract(price_0)

def test_case_25():
    price_0 = module_0.Price()
    date_0 = None
    price_1 = price_0.with_dov(date_0)

def test_case_26():
    price_0 = module_0.Price()
    float_0 = price_0.__float__()

def test_case_27():
    money_0 = module_0.Money()
    none_price_0 = module_0.NonePrice()
    str_0 = 'XMR'
    price_0 = module_0.Price()
    price_1 = price_0.__floordiv__(str_0)

def test_case_28():
    money_0 = module_0.Money()
    list_0 = [money_0, money_0, money_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.positive()
    str_0 = 'DZD'
    some_money_0 = module_0.SomeMoney(*list_0)
    money_1 = some_money_0.floor_divide(str_0)