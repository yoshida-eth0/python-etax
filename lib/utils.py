import math
from functools import wraps
from typing import TypeVar

T = TypeVar('T')


def intfloor(value: int|float, n: int) -> int:
    """
    整数に変換しn桁まで切り捨てる
    """
    roundvalue = 10 ** n
    return math.floor(value / roundvalue) * roundvalue


def ゼロ以上(func) -> int:
    """
    戻り値をゼロを下限とするデコレータ
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        retval = func(*args, **kwargs)
        return max(retval, 0)
    return wrapper


def get_range_dict_value(dic: dict[range,T], key: int) -> T:
    """
    rangeをキーに持つ辞書からrangeに含まれるkeyの要素を返す

    args:
        dic (dict[range,T]): 検索対象の辞書
        key (int): 検索値
    return:
        obj (T): 一致する要素
    """
    for key_range, obj in dic.items():
        start, stop = sorted([key_range.start, key_range.stop])
        if start<=key and key<stop:
            return obj
    raise ValueError(f'no match key value in range key: {key}')
