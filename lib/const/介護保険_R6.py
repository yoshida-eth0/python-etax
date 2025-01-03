"""
定数定義 社会保険 -> 介護保険
"""
import sys

from meta.介護保険 import I介護保険
from meta.社会保険 import 標準額区分
from utils import get_range_dict_value


class 介護保険_R6(I介護保険):
    """
    介護保険 令和6年3月分（4月納付分）から

    参考：
        都道府県毎の保険料額表 | 協会けんぽ | 全国健康保険協会
        https://www.kyoukaikenpo.or.jp/g7/cat330/sb3150/

        令和６年度 介護保険料率について
        https://www.kyoukaikenpo.or.jp/file/20240109_shiryou2-3.pdf
    """
    __標準報酬額区分の定義: dict[range,標準額区分] = {
        range(-sys.maxsize,      93_000): 標準額区分(等級= 1, 月額= 88_000),
        range(      93_000,     101_000): 標準額区分(等級= 2, 月額= 98_000),
        range(     101_000,     107_000): 標準額区分(等級= 3, 月額=104_000),
        range(     107_000,     114_000): 標準額区分(等級= 4, 月額=110_000),
        range(     114_000,     122_000): 標準額区分(等級= 5, 月額=118_000),
        range(     122_000,     130_000): 標準額区分(等級= 6, 月額=126_000),
        range(     130_000,     138_000): 標準額区分(等級= 7, 月額=134_000),
        range(     138_000,     146_000): 標準額区分(等級= 8, 月額=142_000),
        range(     146_000,     155_000): 標準額区分(等級= 9, 月額=150_000),
        range(     155_000,     165_000): 標準額区分(等級=10, 月額=160_000),
        range(     165_000,     175_000): 標準額区分(等級=11, 月額=170_000),
        range(     175_000,     185_000): 標準額区分(等級=12, 月額=180_000),
        range(     185_000,     195_000): 標準額区分(等級=13, 月額=190_000),
        range(     195_000,     210_000): 標準額区分(等級=14, 月額=200_000),
        range(     210_000,     230_000): 標準額区分(等級=15, 月額=220_000),
        range(     230_000,     250_000): 標準額区分(等級=16, 月額=240_000),
        range(     250_000,     270_000): 標準額区分(等級=17, 月額=260_000),
        range(     270_000,     290_000): 標準額区分(等級=18, 月額=280_000),
        range(     290_000,     310_000): 標準額区分(等級=19, 月額=300_000),
        range(     310_000,     330_000): 標準額区分(等級=20, 月額=320_000),
        range(     330_000,     350_000): 標準額区分(等級=21, 月額=340_000),
        range(     350_000,     370_000): 標準額区分(等級=22, 月額=360_000),
        range(     370_000,     395_000): 標準額区分(等級=23, 月額=380_000),
        range(     395_000,     425_000): 標準額区分(等級=24, 月額=410_000),
        range(     425_000,     455_000): 標準額区分(等級=25, 月額=440_000),
        range(     455_000,     485_000): 標準額区分(等級=26, 月額=470_000),
        range(     485_000,     515_000): 標準額区分(等級=27, 月額=500_000),
        range(     515_000,     545_000): 標準額区分(等級=28, 月額=530_000),
        range(     545_000,     575_000): 標準額区分(等級=29, 月額=560_000),
        range(     575_000,     605_000): 標準額区分(等級=30, 月額=590_000),
        range(     605_000,     635_000): 標準額区分(等級=31, 月額=620_000),
        range(     635_000, sys.maxsize): 標準額区分(等級=32, 月額=650_000),
    }

    __介護保険料率の定義: dict[range,float] = {
        range(-sys.maxsize,          40): 0.0,
        # 40歳から64歳までの介護保険第2号被保険者
        range(          40,          65): 0.016,
        # 65歳以上の介護保険第1号被保険者
        range(          65, sys.maxsize): 0.0,
    }

    def 標準報酬額区分(self, 報酬月額: int) -> int:
        return get_range_dict_value(self.__標準報酬額区分の定義, 報酬月額)

    def 保険料率(self, 年齢: int) -> float:
        """
        介護保険料率
        40歳から64歳までの方（介護保険第2号被保険者）は、これに全国一律の介護保険料率（1.60％）が加わります。
        """
        return get_range_dict_value(self.__介護保険料率の定義, 年齢)
