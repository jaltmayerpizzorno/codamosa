# Automatically generated by Pynguin.
import pypara.accounting.ledger as module_0

def test_case_0():
    try:
        date_range_0 = None
        read_initial_balances_0 = None
        set_0 = {read_initial_balances_0, date_range_0, read_initial_balances_0}
        var_0 = module_0.compile_general_ledger_program(read_initial_balances_0, set_0)
        iterable_0 = None
        dict_0 = None
        var_1 = module_0.build_general_ledger(date_range_0, iterable_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        date_range_0 = None
        dict_0 = {}
        list_0 = [date_range_0]
        var_0 = module_0.build_general_ledger(date_range_0, dict_0, dict_0)
        var_1 = module_0.build_general_ledger(date_range_0, list_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        date_range_0 = None
        iterable_0 = None
        account_0 = None
        balance_0 = None
        dict_0 = {account_0: balance_0}
        var_0 = module_0.build_general_ledger(date_range_0, iterable_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        account_0 = None
        balance_0 = None
        var_0 = None
        ledger_0 = module_0.Ledger(account_0, balance_0)
        var_1 = ledger_0.add(var_0)
    except BaseException:
        pass