# Automatically generated by Pynguin.
import pypara.accounting.ledger as module_0
import datetime as module_1
import pypara.commons.zeitgeist as module_2
import pypara.accounting.generic as module_3

def test_case_0():
    try:
        read_initial_balances_0 = None
        str_0 = 'Xf\\C@>'
        var_0 = module_0.compile_general_ledger_program(read_initial_balances_0, str_0)
        date_0 = module_1.date()
    except BaseException:
        pass

def test_case_1():
    try:
        date_range_0 = None
        str_0 = '`3{:7L 2s"\x0byyns'
        dict_0 = {}
        var_0 = module_0.build_general_ledger(date_range_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        date_0 = None
        date_range_0 = module_2.DateRange(date_0, date_0)
        iterable_0 = None
        account_0 = None
        bool_0 = False
        balance_0 = module_3.Balance(date_0, bool_0)
        dict_0 = {account_0: balance_0, account_0: balance_0, account_0: balance_0}
        var_0 = module_0.build_general_ledger(date_range_0, iterable_0, dict_0)
    except BaseException:
        pass