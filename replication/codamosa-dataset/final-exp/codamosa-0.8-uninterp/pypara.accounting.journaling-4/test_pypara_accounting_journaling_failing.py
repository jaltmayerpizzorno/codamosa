# Automatically generated by Pynguin.
import pypara.accounting.journaling as module_0

def test_case_0():
    try:
        str_0 = 'date'
        str_1 = 'description'
        str_2 = 'source'
        journal_entry_0 = module_0.JournalEntry(str_0, str_1, str_2)
        int_0 = 0
        int_1 = 1
        int_2 = 2
        var_0 = journal_entry_0.post(int_0, int_1, int_2)
    except BaseException:
        pass