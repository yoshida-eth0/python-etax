"""
定数定義 給与所得控除
"""
import sys

from meta.給与所得控除 import I給与所得控除, 給与所得控除後の金額Protocol
from utils import get_range_dict_value, intfloor


class 給与所得控除_R2(I給与所得控除):
    """
    給与所得控除 令和2年分以降の定義

    参考:
        No.1410 給与所得控除｜国税庁
        https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm

        手順2　収入金額等、所得金額を計算する｜国税庁
        https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2023/03/order2/3-2_06.htm
    """
    __給与所得控除の定義: dict[range,給与所得控除後の金額Protocol] = {
        # ～550,999円
        range(-sys.maxsize,     551_000): lambda a: 0,
        # 551,000円～1,618,999円
        range(     551_000,   1_619_000): lambda a: a - 550_000,
        # 1,619,000円～1,619,999円
        range(   1_619_000,   1_620_000): lambda a: 1_069_000,
        # 1,620,000円～1,621,999円
        range(   1_620_000,   1_622_000): lambda a: 1_070_000,
        # 1,622,000円～1,623,999円
        range(   1_622_000,   1_624_000): lambda a: 1_072_000,
        # 1,624,000円～1,627,999円
        range(   1_624_000,   1_628_000): lambda a: 1_074_000,
        # 1,628,000円～1,799,999円
        range(   1_628_000,   1_800_000): lambda a: round(intfloor(a/4, 3) * 2.4 + 100_000),
        # 1,800,000円～3,599,999円
        range(   1_800_000,   3_600_000): lambda a: round(intfloor(a/4, 3) * 2.8 - 80_000),
        # 3,600,000円～6,599,999円
        range(   3_600_000,   6_600_000): lambda a: round(intfloor(a/4, 3) * 3.2 - 440_000),
        # 6,600,000円～8,499,999円
        range(   6_600_000,   8_500_000): lambda a: round(a * 0.9 - 1_100_000),
        # 8,500,000円～
        range(   8_500_000, sys.maxsize): lambda a: a - 1_950_000,
    }

    def 給与所得控除後の金額の式(self, 給与等の収入金額: int) -> 給与所得控除後の金額Protocol:
        return get_range_dict_value(self.__給与所得控除の定義, 給与等の収入金額)

