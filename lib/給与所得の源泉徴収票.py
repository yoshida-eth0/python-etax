"""
給与所得の源泉徴収票
"""

import pandas as pd
from 所得税及び復興特別所得税の申告内容確認表_第一表 import 所得税及び復興特別所得税の申告内容確認表_第一表


class 給与所得の源泉徴収票:
    """
    給与所得の源泉徴収票
    """
    def __init__(self, x所得税及び復興特別所得税の申告内容確認表_第一表: 所得税及び復興特別所得税の申告内容確認表_第一表):
        self.所得税及び復興特別所得税の申告内容確認表_第一表 = x所得税及び復興特別所得税の申告内容確認表_第一表

    @property
    def 支払金額(self) -> int:
        """
        支払金額
        """
        return self.所得税及び復興特別所得税の申告内容確認表_第一表.所得金額等.収入金額等_給与

    @property
    def 給与所得控除後の金額(self) -> int:
        """
        給与所得控除後の金額
        """
        return self.所得税及び復興特別所得税の申告内容確認表_第一表.所得金額等.所得金額等_給与

    @property
    def 所得控除の額の合計額(self) -> int:
        """
        所得控除の額の合計額
        """
        return self.所得税及び復興特別所得税の申告内容確認表_第一表.所得税_所得控除.所得控除合計

    @property
    def 源泉徴収税額(self) -> int:
        """
        源泉徴収税額
        TODO

        令和5年分　源泉徴収税額表｜国税庁
        https://www.nta.go.jp/publication/pamph/gensen/zeigakuhyo2022/02.htm
        """
        return 0

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['支払金額', self.支払金額],
            ['給与所得控除後の金額', self.給与所得控除後の金額],
            ['所得控除の額の合計額', self.所得控除の額の合計額],
            ['源泉徴収税額', self.源泉徴収税額],
        ], columns=['label', 'value'])
