# Automatically generated by Pynguin.
import pypara.accounting.ledger as module_0
import pypara.accounting.accounts as module_1
import pypara.commons.zeitgeist as module_2
import pypara.accounting.generic as module_3

def test_case_0():
    try:
        read_initial_balances_0 = None
        date_range_0 = None
        dict_0 = None
        general_ledger_0 = module_0.GeneralLedger(date_range_0, dict_0)
        var_0 = module_0.compile_general_ledger_program(read_initial_balances_0, general_ledger_0)
        account_0 = module_1.Account()
    except BaseException:
        pass

def test_case_1():
    try:
        date_0 = None
        date_range_0 = module_2.DateRange(date_0, date_0)
        iterable_0 = None
        dict_0 = {}
        var_0 = module_0.build_general_ledger(date_range_0, iterable_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        date_0 = None
        account_0 = None
        var_0 = None
        balance_0 = module_3.Balance(date_0, account_0)
        ledger_0 = module_0.Ledger(account_0, balance_0)
        var_1 = ledger_0.add(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        date_0 = None
        date_range_0 = module_2.DateRange(date_0, date_0)
        str_0 = 'WONgHV'
        dict_0 = {}
        var_0 = module_0.build_general_ledger(date_range_0, str_0, dict_0)
    except BaseException:
        pass