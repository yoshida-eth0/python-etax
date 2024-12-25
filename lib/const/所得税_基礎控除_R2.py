"""
定数定義 所得税 基礎控除
"""
import sys

from meta.所得税 import I所得税_基礎控除
from utils import get_range_dict_value


class 所得税_基礎控除_R2(I所得税_基礎控除):
    """
    所得税 基礎控除 令和2年分以降の定義

    参考:
        No.1199 基礎控除｜国税庁
        https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm
    """
    __所得税_基礎控除の定義: dict[range,int] = {
        # 2,400万円以下
        range(-sys.maxsize,  24_000_001): 480_000,
        # 2,400万円超2,450万円以下
        range(  24_000_001,  24_500_001): 320_000,
        # 2,450万円超2,500万円以下
        range(  24_500_001,  25_000_001): 160_000,
        # 2,500万円超
        range(  25_000_001, sys.maxsize): 0,
    }

    def 所得税_基礎控除(self, 所得金額等_合計: int) -> int:
        return get_range_dict_value(self.__所得税_基礎控除の定義, 所得金額等_合計)
