import math
from functools import wraps


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
