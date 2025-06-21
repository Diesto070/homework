from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(str_number_card_or_account: str) -> str:
    """ Функция принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""
    if "Счет" in str_number_card_or_account or "счет" in str_number_card_or_account:
        number_account = (str_number_card_or_account[-20:])
        get_mask_account(number_account)
        number_account_mask = get_mask_account(number_account)
        text = str(f"{(str_number_card_or_account[:-21])} {number_account_mask}")

    else:
        number_card = (str_number_card_or_account[-16:])
        get_mask_card_number(number_card)
        number_card_mask = get_mask_card_number(number_card)
        text = str(f"{(str_number_card_or_account[:-17])} {number_card_mask}")

    return text


def get_date(date_inp: str) -> str:
    """Функция, которая принимает на вход строку и возвращает строку с датой."""
    if not date_inp or len(date_inp) > 26 or '-' not in date_inp:
        return "Неверный формат входных данных"

    date = datetime.strptime(date_inp[:10], '%Y-%m-%d')
    return f"{date.day:02}.{date.month:02}.{date.year}"
