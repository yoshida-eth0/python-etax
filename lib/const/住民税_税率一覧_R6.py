"""
定数定義 住民税 税率一覧
"""
import sys

from meta.住民税 import I住民税_税率一覧, 住民税の税率
from utils import get_range_dict_value


class 住民税_税率一覧_R6(I住民税_税率一覧):
    """
    住民税 税率一覧 令和6年度(定額減税あり)

    参考:
        杉並区 令和6年度 わたしたちの区税 P15
        https://www.city.suginami.tokyo.jp/_res/projects/default_project/_page_/001/014/046/r6kuzei.pdf.pdf
    """
    __住民税の税率一覧 = [
        住民税の税率(区分='特別区民税', 所得割=0.06, 均等割=3_000, 復興特別所得税率=0.021, 定額減税=6_000),
        住民税の税率(区分='都民税', 所得割=0.04, 均等割=1_000, 復興特別所得税率=0.021, 定額減税=4_000),
    ]

    def 住民税の税率一覧(self) -> list[住民税の税率]:
        return self.__住民税の税率一覧

    __住民税_定額減税対象可否の定義: dict[range,bool] = {
        # 1805万円以下
        range(-sys.maxsize,  18_050_001): True,
        # 1805万円を超える
        range(  18_050_001, sys.maxsize): False,
    }

    def 住民税_定額減税対象可否(self, 合計所得金額: int) -> bool:
        return get_range_dict_value(self.__住民税_定額減税対象可否の定義, 合計所得金額)
