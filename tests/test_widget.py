import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("number_card_or_account, expected",

                         [
                             ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                             ("Счет 73654108430135874305", "Счет **4305"),
                             ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                             ("", " Неверный формат входных данных"),
                             ("Invalid_data", " Неверный формат входных данных")
                         ])
def test_mask_account_card(number_card_or_account: str, expected: str) -> None:
    assert mask_account_card(number_card_or_account) == expected


@pytest.fixture
def correct_date() ->str:
    return "11.03.2024"


def test_get_date(correct_date):
    assert get_date("2024-03-11T02:26:18.671407") == correct_date


@pytest.mark.parametrize("date_inp, expected",
                         [
                             ("20240311T02:26:18.671407", "Неверный формат входных данных"),
                             ("20240311T02:26:18.6714076879875", "Неверный формат входных данных"),
                             ("", "Неверный формат входных данных")
                         ])
def test_get_date_incorrect(date_inp, expected) -> None:
    assert get_date(date_inp) == expected
