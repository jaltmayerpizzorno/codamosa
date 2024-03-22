from unittest import TestCase

from string_utils import is_credit_card


class IsCreditCardTestCase(TestCase):
    # numbers generated by: http://www.getcreditcardnumbers.com
    sample_cards = {
        'VISA': [
            '4929108461099666',
            '4485341431836919',
            '4929383875909178',
            '4024007178235312',
            '4929943872251997'
        ],
        'MASTERCARD': [
            '5593685744413543',
            '5299068126557657',
            '5519706741220334',
            '5349375673926726',
            '5536077751185034'
        ],
        'DISCOVER': [
            '6011738421556670',
            '6011902207467698',
            '6011066039342048',
            '6011084365330958',
            '6011417613048024'
        ],
        'AMERICAN_EXPRESS': [
            '378255041294558',
            '344411347420469',
            '376197548847524',
            '348870102379192',
            '340073988128712'
        ],
        'JCB': [
            '3528968052436214',
            '213140714369305',
            '180095242210070',
            '213122809097983',
            '213181044765010'
        ],
        'DINERS_CLUB': [
            '30161673137117',
            '38476920787395',
            '38652978387607',
            '36802519893181',
            '30347192978103'
        ]
    }

    def test_should_return_false_for_non_string_objects(self):
        # noinspection PyTypeChecker
        self.assertFalse(is_credit_card(None))

        # noinspection PyTypeChecker
        self.assertFalse(is_credit_card(False))

        # noinspection PyTypeChecker
        self.assertFalse(is_credit_card(0))

        # noinspection PyTypeChecker
        self.assertFalse(is_credit_card([]))

        # noinspection PyTypeChecker
        self.assertFalse(is_credit_card({'a': 1}))

    def test_string_cannot_be_empty(self):
        self.assertFalse(is_credit_card(''))
        self.assertFalse(is_credit_card(' '))

    def test_string_cannot_contain_letters(self):
        self.assertFalse(is_credit_card('not a credit card for sure'))

    def test_numbers_in_string_should_be_15_at_least(self):
        self.assertFalse(is_credit_card('1' * 14))

    def test_should_accept_any_valid_card_number_if_type_is_not_specified(self):
        for card_type in self.sample_cards:
            for card_number in self.sample_cards[card_type]:
                self.assertTrue(is_credit_card(card_number), 'Invalid card: %s (%s)' % (card_number, card_type))

    def test_should_validate_only_specific_card_type_if_specified(self):
        for card_type in self.sample_cards:
            for card_number in self.sample_cards[card_type]:
                self.assertTrue(
                    is_credit_card(card_number, card_type=card_type),
                    'Invalid card: %s (%s)' % (card_number, card_type)
                )
                other_cards = self.sample_cards.copy()
                del other_cards[card_type]
                for other_card in other_cards:
                    self.assertFalse(
                        is_credit_card(card_number, card_type=other_card),
                        'Card %s should not be a valid %s' % (card_number, other_card)
                    )

    def test_cannot_provide_unsupported_card_type(self):
        self.assertRaises(KeyError, lambda: is_credit_card(self.sample_cards['VISA'][0], card_type='FOO_CARD'))
