# Automatically generated by Pynguin.
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

def test_case_0():
    pass

def test_case_1():
    none_price_0 = module_0.NonePrice()
    bool_0 = none_price_0.as_boolean()

def test_case_2():
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.abs()

def test_case_3():
    bool_0 = True
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    currency_type_0 = module_2.CurrencyType.MONEY
    list_0 = []
    none_price_0 = module_0.NonePrice(*list_0)
    price_0 = none_price_0.scalar_subtract(currency_type_0)
    price_1 = price_0.__mul__(bool_0)
    monetary_operation_exception_0 = module_0.MonetaryOperationException(**dict_0)
    none_price_1 = module_0.NonePrice()
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.scalar_add(monetary_operation_exception_0)
    money_1 = money_0.__add__(money_0)

def test_case_4():
    currency_type_0 = module_2.CurrencyType.MONEY
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.negative()
    bool_0 = money_0.__eq__(currency_type_0)

def test_case_5():
    currency_type_0 = module_2.CurrencyType.MONEY
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.positive()
    bool_0 = money_0.__eq__(currency_type_0)

def test_case_6():
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.positive()

def test_case_7():
    bool_0 = False
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    var_0 = money_0.__round__()

def test_case_8():
    bool_0 = True
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    currency_type_0 = module_2.CurrencyType.MONEY
    list_0 = []
    none_price_0 = module_0.NonePrice(*list_0)
    price_0 = none_price_0.scalar_subtract(currency_type_0)
    int_0 = 460
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.floor_divide(int_0)
    money_1 = money_0.round()
    price_1 = price_0.__mul__(bool_0)
    monetary_operation_exception_0 = module_0.MonetaryOperationException(**dict_0)
    none_price_1 = module_0.NonePrice()
    none_money_1 = module_0.NoneMoney()
    money_2 = none_money_1.scalar_add(monetary_operation_exception_0)
    money_3 = money_2.__add__(money_2)

def test_case_9():
    bool_0 = False
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    list_0 = []
    none_price_0 = module_0.NonePrice(*list_0)
    price_0 = none_price_0.with_qty(decimal_0)
    price_1 = price_0.__mul__(bool_0)
    monetary_operation_exception_0 = module_0.MonetaryOperationException(**dict_0)
    none_price_1 = module_0.NonePrice()
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.scalar_add(monetary_operation_exception_0)
    money_1 = money_0.__sub__(money_0)

def test_case_10():
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    list_0 = []
    none_price_0 = module_0.NonePrice(*list_0)
    price_0 = none_price_0.abs()
    monetary_operation_exception_0 = module_0.MonetaryOperationException(*list_0)
    none_price_1 = module_0.NonePrice()
    none_money_0 = module_0.NoneMoney(*list_0, **dict_0)
    var_0 = None
    money_0 = none_money_0.scalar_add(var_0)
    money_1 = module_0.Money()
    money_2 = money_0.__sub__(money_1)

def test_case_11():
    bool_0 = False
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    var_0 = money_0.__round__()
    int_0 = -3102
    list_0 = [var_0, int_0, var_0]
    decimal_0 = module_1.Decimal()
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    price_1 = price_0.__add__(price_0)

def test_case_12():
    none_price_0 = module_0.NonePrice()
    int_0 = -3102
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    price_1 = price_0.__add__(price_0)
    currency_0 = None
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.with_ccy(currency_0)
    bool_0 = some_price_0.lt(price_0)
    money_1 = money_0.__sub__(money_0)
    money_2 = money_1.round(int_0)
    price_2 = none_price_0.positive()
    price_3 = price_1.__sub__(price_2)

def test_case_13():
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    currency_type_0 = module_2.CurrencyType.ALTERNATIVE
    list_0 = []
    none_price_0 = module_0.NonePrice(*list_0)
    price_0 = none_price_0.scalar_subtract(currency_type_0)
    price_1 = price_0.__sub__(price_0)
    monetary_operation_exception_0 = module_0.MonetaryOperationException(**dict_0)
    none_price_1 = module_0.NonePrice()
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.scalar_add(monetary_operation_exception_0)
    money_1 = money_0.negative()

def test_case_14():
    bool_0 = True
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    currency_type_0 = module_2.CurrencyType.MONEY
    list_0 = []
    none_price_0 = module_0.NonePrice(*list_0)
    price_0 = none_price_0.scalar_subtract(currency_type_0)
    int_0 = 460
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.floor_divide(int_0)
    money_1 = money_0.round()
    price_1 = price_0.__mul__(bool_0)
    monetary_operation_exception_0 = module_0.MonetaryOperationException(**dict_0)
    none_price_1 = module_0.NonePrice()
    none_money_1 = module_0.NoneMoney()
    money_2 = module_0.Money()
    money_3 = money_2.__add__(money_2)

def test_case_15():
    bool_0 = False
    str_0 = '8"Ah#"bh$D'
    str_1 = 'RQc&`0@tS\nGo8\r[3-'
    str_2 = 'SBD'
    dict_0 = {str_1: str_1, str_2: str_0, str_1: str_1, str_0: str_0}
    str_3 = 'us:Z-\\`O\x0ct.S|V=='
    int_0 = 0
    currency_type_0 = module_2.CurrencyType.CRYPTO
    decimal_0 = module_1.Decimal()
    currency_0 = module_2.Currency(str_0, str_3, int_0, currency_type_0, decimal_0, int_0)
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.convert(currency_0)
    price_1 = price_0.__pos__()
    money_0 = price_1.times(dict_0)
    money_1 = money_0.__neg__()
    dict_1 = {}
    decimal_1 = module_1.Decimal(**dict_1)
    list_0 = []
    none_price_1 = module_0.NonePrice(*list_0)
    price_2 = none_price_1.with_qty(decimal_1)
    price_3 = price_2.__mul__(bool_0)
    monetary_operation_exception_0 = module_0.MonetaryOperationException(**dict_1)
    none_price_2 = module_0.NonePrice()
    none_money_0 = module_0.NoneMoney()
    money_2 = none_money_0.scalar_add(monetary_operation_exception_0)
    money_3 = money_2.__sub__(money_2)

def test_case_16():
    bool_0 = False
    str_0 = '8"Ah#"bh$D'
    str_1 = 'RQc&`0@tS\nGo8\r[3-'
    str_2 = 'SBD'
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.positive()
    list_0 = [str_0, str_1, str_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_1 = some_price_0.add(price_0)
    dict_0 = {str_1: str_1, str_2: str_0, str_1: str_1, str_0: str_0}
    str_3 = 'us:Z-\\`O\x0ct.S|V=='
    int_0 = 0
    currency_type_0 = module_2.CurrencyType.CRYPTO
    decimal_0 = module_1.Decimal()
    currency_0 = module_2.Currency(str_0, str_3, int_0, currency_type_0, decimal_0, int_0)
    none_price_1 = module_0.NonePrice()
    price_2 = none_price_1.convert(currency_0)
    price_3 = price_2.__pos__()
    money_0 = price_3.times(dict_0)
    money_1 = money_0.__neg__()
    dict_1 = {}
    decimal_1 = module_1.Decimal(**dict_1)
    price_4 = none_price_1.with_qty(decimal_1)
    price_5 = price_4.__mul__(bool_0)
    monetary_operation_exception_0 = module_0.MonetaryOperationException(**dict_1)
    none_price_2 = module_0.NonePrice()
    none_money_0 = module_0.NoneMoney()
    money_2 = none_money_0.scalar_add(monetary_operation_exception_0)
    money_3 = money_2.__sub__(money_2)

def test_case_17():
    int_0 = -3072
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    price_1 = price_0.__add__(price_0)
    price_2 = price_1.__neg__()
    price_3 = price_0.subtract(price_2)
    price_4 = price_3.round(int_0)

def test_case_18():
    bool_0 = False
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    var_0 = money_0.__round__()
    int_0 = -3102
    list_0 = [var_0, int_0, var_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_1 = some_money_0.lt(money_0)
    int_1 = some_money_0.as_integer()
    currency_type_0 = module_2.CurrencyType.CRYPTO
    currency_0 = None
    none_money_0 = module_0.NoneMoney()
    money_1 = money_0.scalar_add(money_0)
    money_2 = none_money_0.with_ccy(currency_0)
    price_0 = none_price_0.abs()
    currency_1 = None
    none_money_1 = module_0.NoneMoney()
    money_3 = none_money_1.positive()
    money_4 = money_3.positive()
    int_2 = -342
    money_5 = money_4.round(int_2)
    money_6 = money_3.round()
    money_7 = money_3.subtract(money_3)
    list_1 = [money_3, currency_1, currency_type_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_1 = none_price_0.with_ccy(currency_0)

def test_case_19():
    none_money_0 = module_0.NoneMoney()
    bool_0 = none_money_0.as_boolean()

def test_case_20():
    currency_type_0 = None
    list_0 = [currency_type_0, currency_type_0, currency_type_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.as_boolean()

def test_case_21():
    bool_0 = False
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    int_0 = -3104
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_1 = some_money_0.gt(money_0)
    decimal_0 = module_1.Decimal()
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.positive()
    money_1 = money_0.subtract(money_0)
    price_1 = price_0.__add__(price_0)
    bool_2 = some_money_0.lt(money_0)
    bool_3 = some_price_0.gt(price_0)
    none_money_0 = module_0.NoneMoney()
    bool_4 = some_money_0.lte(money_1)
    none_money_1 = module_0.NoneMoney()
    price_2 = price_0.with_qty(decimal_0)
    price_3 = price_2.__neg__()
    bool_5 = money_1.gte(money_1)
    price_4 = price_3.__mul__(decimal_0)
    bool_6 = price_4.gte(price_2)
    money_2 = none_money_0.positive()
    money_3 = money_2.positive()
    money_4 = some_money_0.add(money_0)
    money_5 = none_money_1.add(money_3)
    money_6 = money_4.subtract(money_3)
    some_price_1 = module_0.SomePrice(*list_0)
    float_0 = some_price_0.as_float()

def test_case_22():
    int_0 = -3102
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    str_0 = '$m;Y\ngffL=HNd~K'
    int_1 = 2781
    currency_type_0 = None
    decimal_0 = module_1.Decimal()
    currency_0 = module_2.Currency(str_0, str_0, int_1, currency_type_0, decimal_0, int_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.positive()
    price_1 = price_0.__add__(price_0)
    int_2 = some_money_0.as_integer()
    price_2 = price_1.__neg__()
    none_money_0 = module_0.NoneMoney()
    some_price_1 = module_0.SomePrice(*list_0)
    float_0 = some_price_1.as_float()
    price_3 = price_0.round(int_2)

def test_case_23():
    int_0 = -3072
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    some_price_0 = module_0.SomePrice(*list_0)
    bool_0 = some_money_0.lte(money_0)

def test_case_24():
    bool_0 = True
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    int_0 = -3102
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_1 = some_money_0.lt(money_0)
    bool_2 = some_money_0.gte(money_0)
    bool_3 = some_money_0.lte(money_0)
    none_money_0 = module_0.NoneMoney()
    money_1 = some_money_0.add(money_0)
    money_2 = money_1.__abs__()
    money_3 = money_1.subtract(money_1)

def test_case_25():
    int_0 = -3072
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.negative()
    some_price_0 = module_0.SomePrice(*list_0)
    bool_0 = some_money_0.lte(money_0)

def test_case_26():
    money_0 = module_0.Money()
    bool_0 = money_0.gte(money_0)
    money_1 = money_0.__sub__(money_0)

def test_case_27():
    money_0 = module_0.Money()
    money_1 = money_0.__pos__()

def test_case_28():
    bool_0 = False
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    int_0 = -3102
    list_0 = [money_0, int_0, money_0]
    var_0 = None
    price_0 = module_0.Price()
    price_1 = price_0.__mul__(var_0)
    price_2 = none_price_0.round()
    bool_1 = price_2.__gt__(price_1)
    some_money_0 = module_0.SomeMoney(*list_0)
    decimal_0 = module_1.Decimal()
    bool_2 = some_money_0.lt(money_0)
    currency_0 = None
    none_money_0 = module_0.NoneMoney()
    money_1 = money_0.with_ccy(currency_0)
    none_money_1 = module_0.NoneMoney()
    money_2 = none_money_1.positive()
    var_1 = None
    money_3 = money_2.positive()
    money_4 = some_money_0.add(money_2)
    money_5 = none_money_1.add(money_2)
    money_6 = money_2.subtract(money_2)
    some_price_0 = module_0.SomePrice(*list_0)
    float_0 = some_price_0.as_float()
    money_7 = money_2.__truediv__(var_1)

def test_case_29():
    int_0 = -3072
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    some_price_0 = module_0.SomePrice(*list_0)
    bool_0 = some_money_0.lte(money_0)

def test_case_30():
    none_price_0 = module_0.NonePrice()
    int_0 = -3072
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    price_1 = price_0.__add__(price_0)
    bool_0 = some_price_0.gt(price_0)
    price_2 = price_1.__neg__()
    price_3 = price_0.subtract(price_2)
    price_4 = price_3.round(int_0)

def test_case_31():
    int_0 = -3102
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    price_1 = price_0.__add__(price_0)
    bool_0 = some_price_0.gte(price_0)
    bool_1 = price_1.gt(price_0)
    price_2 = price_1.__neg__()
    none_money_0 = module_0.NoneMoney()
    int_1 = price_2.as_integer()
    price_3 = price_2.round()

def test_case_32():
    bool_0 = False
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    int_0 = -3072
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    price_0 = none_price_0.positive()
    bool_1 = some_money_0.gt(money_0)
    money_1 = some_money_0.subtract(money_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_1 = some_price_0.abs()
    price_2 = price_1.__add__(price_1)
    bool_2 = some_money_0.lte(money_1)
    bool_3 = some_money_0.lt(money_0)
    bool_4 = some_price_0.gt(price_1)
    price_3 = price_2.__neg__()
    money_2 = money_1.__abs__()
    price_4 = price_1.subtract(price_3)
    price_5 = price_4.round(int_0)
    bool_5 = some_money_0.gte(money_1)

def test_case_33():
    bool_0 = False
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    int_0 = -1330
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_1 = some_money_0.lt(money_0)
    bool_2 = some_money_0.gte(money_0)
    bool_3 = some_money_0.lte(money_0)
    money_1 = some_money_0.add(money_0)
    money_2 = money_1.subtract(money_1)
    bool_4 = money_2.__gt__(money_2)
    decimal_0 = module_1.Decimal()
    price_0 = none_price_0.with_qty(decimal_0)

def test_case_34():
    none_price_0 = module_0.NonePrice()
    int_0 = -3102
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    bool_0 = some_money_0.lt(money_0)
    int_1 = some_money_0.as_integer()
    currency_0 = None
    none_money_0 = module_0.NoneMoney()
    money_1 = none_money_0.with_ccy(currency_0)
    none_money_1 = module_0.NoneMoney()
    money_2 = money_1.positive()
    money_3 = money_2.round(int_0)
    money_4 = money_2.subtract(money_2)
    bool_1 = money_4.gt(money_3)

def test_case_35():
    bool_0 = True
    none_price_0 = module_0.NonePrice()
    money_0 = none_price_0.times(bool_0)
    var_0 = money_0.__round__()
    int_0 = -3104
    list_0 = [var_0, int_0, var_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    str_0 = '$m;Y\ngffL=HNd~K'
    bool_1 = some_money_0.gt(money_0)
    decimal_0 = module_1.Decimal()
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.round(int_0)
    price_1 = price_0.__add__(price_0)
    bool_2 = some_money_0.lt(money_0)
    bool_3 = some_price_0.gt(price_0)
    none_money_0 = module_0.NoneMoney()
    bool_4 = price_0.__eq__(str_0)
    set_0 = None
    money_1 = none_money_0.scalar_add(set_0)
    float_0 = some_price_0.as_float()
    money_2 = some_money_0.subtract(money_0)
    price_2 = price_1.positive()
    bool_5 = money_2.__gt__(money_2)
    money_3 = none_money_0.positive()
    money_4 = some_money_0.add(money_1)
    money_5 = money_0.__abs__()
    money_6 = money_0.subtract(money_4)
    price_3 = price_0.subtract(price_2)
    int_1 = -1025
    price_4 = price_1.round()
    money_7 = money_1.__truediv__(int_1)
    str_1 = '"C%dt6\r@g4Z.lf&(FR 6'
    some_price_1 = module_0.SomePrice(*list_0)
    price_5 = some_price_1.floor_divide(str_1)

def test_case_36():
    money_0 = module_0.Money()
    int_0 = -5024
    money_1 = money_0.__mul__(int_0)

def test_case_37():
    money_0 = module_0.Money()
    bool_0 = money_0.gte(money_0)
    money_1 = money_0.__sub__(money_0)
    bool_1 = money_0.lt(money_1)