import math

import pandas as pd
from context import get_context
from utils import in_range
from 所得税及び復興特別所得税の申告内容確認表 import 所得金額等
from 納税者 import 納税者


class 国民健康保険:
    """
    国民健康保険
    """
    def __init__(self, 所得金額等: 所得金額等, 納税者: 納税者):
        self.所得金額等 = 所得金額等
        self.納税者 = 納税者

    @property
    def 保険料(self) -> int:
        """
        保険料
        TODO: 2人以上の世帯
        """
        return sum(self.区分別保険料.values())

    @property
    def 区分別保険料(self) -> dict[str,int]:
        """
        区分別保険料
        TODO: 2人以上の世帯

        参考：
            令和６年度の国民健康保険料の簡易計算方法
            https://www.city.suginami.tokyo.jp/_res/projects/default_project/_page_/001/004/555/keisanhouhou6.pdf
        """
        impl = get_context().国民健康保険
        if impl is None:
            raise NotImplementedError('Context.国民健康保険')

        # 軽減割合
        割合 = 1.0 - impl.低所得世帯軽減割合(self.所得金額等.総所得金額)

        # 区分別保険料
        result = {}
        for 保険料率区分 in impl.国民健康保険料率区分一覧(self.納税者.国民健康保険_加入地域):
            value = 0
            if in_range(保険料率区分.対象年齢, self.納税者.納税者本人.年齢):
                value = 保険料率区分.均等割 + self.賦課標準額 * 保険料率区分.所得割

                # 軽減割合適用
                value = math.floor(value * 割合)

                # 最高限度額適用
                value = min(value, 保険料率区分.最高限度額)

            result[保険料率区分.区分] = value

        return result

    @property
    def 賦課標準額(self) -> int:
        """
        総所得金額等から住民税の基礎控除（合計所得金額が2,400万円以下の場合は43万円）を差し引いた金額
        TODO: 2人以上の世帯

        参考：
            川崎市 : 国民健康保険料の所得割額の算定に用いる「賦課基準額」について知りたい。
            https://www.city.kawasaki.jp/templates/faq/350/0000029672.html
        """
        impl = get_context().住民税_基礎控除
        if impl is None:
            raise NotImplementedError('Context.住民税_基礎控除')

        return self.所得金額等.総所得金額等 - impl.住民税_基礎控除(self.所得金額等.合計所得金額)

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        dic = list(self.区分別保険料.items())
        dic.append(['合計', self.保険料])
        return pd.DataFrame(dic)
