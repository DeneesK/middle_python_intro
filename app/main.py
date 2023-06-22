"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    separated_name = name.split(' ')
    cap_name = ' '.join([name.capitalize() for name in separated_name])
    return 'Привет, {0}'.format(cap_name)
