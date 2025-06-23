from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected",
                         [
                             ("7000792289606361", "7000 79** **** 6361"),
                             ("1234567890123456", "1234 56** **** 3456"),
                             ("11111111111111111", "Неверный формат входных данных"),
                             ("3333", "Неверный формат входных данных"),
                             ("", "Неверный формат входных данных"),
                             ("Invalid_data", "Неверный формат входных данных")
                         ])
def test_get_mask_card_number(card_number: Union[str, None], expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected",
                         [
                             ("73654108430135874305", "**4305"),
                             ("98765432198765432198", "**2198"),
                             ("111111111111111111111", "Неверный формат входных данных"),
                             ("1234", "Неверный формат входных данных"),
                             ("", "Неверный формат входных данных"),
                             ("Invalid_data", "Неверный формат входных данных")
                         ])
def test_get_mask_account(account_number: Union[str, None], expected: str) -> None:
    assert get_mask_account(account_number) == expected
