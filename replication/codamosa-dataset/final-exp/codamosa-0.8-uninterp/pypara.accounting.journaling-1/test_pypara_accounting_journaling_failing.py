# Automatically generated by Pynguin.
import pypara.accounting.journaling as module_0
import pypara.commons.zeitgeist as module_1

def test_case_0():
    try:
        date_0 = None
        str_0 = None
        journal_entry_0 = module_0.JournalEntry(date_0, str_0, str_0)
        journal_entry_0.validate()
        account_0 = None
        complex_0 = None
        date_range_0 = module_1.DateRange(date_0, date_0)
        list_0 = [date_0, journal_entry_0, complex_0, account_0]
        var_0 = journal_entry_0.post(date_0, account_0, list_0)
    except BaseException:
        pass