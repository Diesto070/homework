from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(str_number_card_or_account: str, number_account: list, number_card: list) -> str:
    if "Счет" in str_number_card_or_account or "счет" in str_number_card_or_account:
        number_account = list(str_number_card_or_account[-20:])
        get_mask_account(number_account)
        number_account_mask = get_mask_account(number_account)
        text = str(f"{list(str_number_card_or_account[:-21])} {number_account_mask}")

    else:
        number_card = list(str_number_card_or_account[-16:])
        get_mask_card_number(number_card)
        number_card_mask = get_mask_card_number(number_card)
        text = str(f"{list(str_number_card_or_account[:-17])} {number_card_mask}")

    return text


from datetime import datetime

def get_date(date_inp: str) -> str:
    date = datetime.strptime(date_inp[:10], '%Y-%m-%d')
    return f"{date.day:02}.{date.month:02}.{date.year}"


print(get_date("2024-03-11T02:26:18.671407"))