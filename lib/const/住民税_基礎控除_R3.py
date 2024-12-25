"""
定数定義 住民税 基礎控除
"""
import sys

from meta.住民税 import I住民税_基礎控除
from utils import get_range_dict_value


class 住民税_基礎控除_R3(I住民税_基礎控除):
    """
    住民税 基礎控除 令和3年度(令和2年に得た所得)以降の定義

    参考:
        杉並区 令和6年度 わたしたちの区税 P15
        https://www.city.suginami.tokyo.jp/_res/projects/default_project/_page_/001/014/046/r6kuzei.pdf.pdf
    """
    __住民税_基礎控除の定義: dict[range,int] = {
        # 2,400万円以下
        range(-sys.maxsize,  24_000_001): 430_000,
        # 2,400万円超2,450万円以下
        range(  24_000_001,  24_500_001): 290_000,
        # 2,450万円超2,500万円以下
        range(  24_500_001,  25_000_001): 150_000,
        # 2,500万円超
        range(  25_000_001, sys.maxsize): 0,
    }

    def 住民税_基礎控除(self, 合計所得金額: int) -> int:
        return get_range_dict_value(self.__住民税_基礎控除の定義, 合計所得金額)
