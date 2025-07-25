"""
定数定義 住民税 税率一覧
"""
from meta.住民税 import I住民税_税率一覧, 住民税の税率


class 住民税_税率一覧_R7(I住民税_税率一覧):
    """
    住民税 税率一覧(定額減税なし)

    参考:
        杉並区 令和7年度 わたしたちの区税 P15
        https://www.city.suginami.tokyo.jp/documents/7168/r7kuzei.pdf
    """
    __住民税の税率一覧 = [
        住民税の税率(区分='特別区民税', 所得割=0.06, 均等割=3_000),
        住民税の税率(区分='都民税', 所得割=0.04, 均等割=1_000),
    ]

    def 住民税の税率一覧(self) -> list[住民税の税率]:
        return self.__住民税の税率一覧

    def 住民税_定額減税対象可否(self, 合計所得金額: int) -> bool:
        return False
