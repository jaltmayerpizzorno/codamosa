# Automatically generated by Pynguin.
import pypara.commons.zeitgeist as module_0
import pypara.accounting.journaling as module_1

def test_case_0():
    try:
        date_0 = None
        date_range_0 = module_0.DateRange(date_0, date_0)
        account_0 = None
        set_0 = {date_range_0, account_0}
        str_0 = 'T*g?V^)\x0bp`6_?9>;6T'
        str_1 = "'=fp\n$bl`p5+Xa1VJ:4Y"
        journal_entry_0 = module_1.JournalEntry(date_0, str_0, str_1)
        var_0 = journal_entry_0.post(date_0, account_0, set_0)
    except BaseException:
        pass