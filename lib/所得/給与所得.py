"""
給与所得
"""

import pandas as pd
from context import get_context

"""
給与
"""

class 給与:
    def __init__(self, 給与等の収入金額: int = 0):
        self.給与等の収入金額 = 給与等の収入金額

    @property
    def 給与所得控除後の金額(self) -> int:
        impl = get_context().給与所得控除
        if impl is None:
            raise NotImplementedError('Context.給与所得控除')

        return impl.給与所得控除後の金額(self.給与等の収入金額)

    @property
    def 給与所得控除額(self) -> int:
        return self.給与等の収入金額 - self.給与所得控除後の金額


"""
TODO: 所得金額調整控除

所得税及び復興特別所得税の確定申告の手引き P10
https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2023/pdf/001.pdf
"""

"""
給与所得者の特定支出に関する明細書
"""

class 特定支出:
    """
    給与所得者の特定支出に関する明細書 -> 1 特定支出の金額 -> 各特定支出
    """
    def __init__(self, 区分: int):
        self.区分 = 区分
        self.支出金額 = 0

        # (注)「Ⓑ補塡される金額のうち非課税部分等」とは、特定支出について、
        # 給与等の支払者により補塡される部分のうち非課税部分及び雇用保険法に基づく教育訓練給付金、
        # 母子及び父子並びに寡婦福祉法に基づく母子家庭自立支援教育訓練給付金、
        # 同法に基づく父子家庭自立支援教育訓練給付金が支給される部分をいいます。
        self.補塡される金額のうち非課税部分等 = 0

    @property
    def 差引金額(self) -> int:
        return self.支出金額 - self.補塡される金額のうち非課税部分等

class 特定支出の金額:
    """
    給与所得者の特定支出に関する明細書 -> 1 特定支出の金額
    """
    def __init__(self):
        # 1. 通勤費【区分1】
        self.通勤費 = 特定支出(1)

        # 2. 職務上の旅費【区分256】
        self.職務上の旅費 = 特定支出(256)

        # 3. 転居費〔転任に伴うもの〕【区分2】
        self.転居費 = 特定支出(2)

        # 4. 研修費【区分4】
        self.研修費 = 特定支出(4)

        # 5. 資格取得費〔人の資格を取得するための費用〕【区分8】
        self.資格取得費 = 特定支出(8)

        # 6. 帰宅旅費〔単身赴任に伴うもの〕【区分16】
        self.帰宅旅費 = 特定支出(16)

        # 7. 勤務必要経費 -> 図書費【区分32】
        self.勤務必要経費_図書費 = 特定支出(32)

        # 8. 勤務必要経費 -> 衣服費【区分64】
        self.勤務必要経費_衣服費 = 特定支出(64)

        # 9. 勤務必要経費 -> 交際費等【区分128】
        self.勤務必要経費_交際費等 = 特定支出(128)

    @property
    def 勤務必要経費_小計(self) -> int:
        """
        10. 勤務必要経費 -> 小計
        (最高65万円)
        """
        total = 0
        total += self.勤務必要経費_図書費.差引金額
        total += self.勤務必要経費_衣服費.差引金額
        total += self.勤務必要経費_交際費等.差引金額
        return min(total, 650_000)

    @property
    def 特定支出の合計額(self) -> int:
        """
        11. 特定支出の合計額
        """
        total = 0
        total += self.通勤費.差引金額
        total += self.職務上の旅費.差引金額
        total += self.転居費.差引金額
        total += self.研修費.差引金額
        total += self.資格取得費.差引金額
        total += self.帰宅旅費.差引金額
        total += self.勤務必要経費_小計
        return total

    @property
    def 適用を受ける特定支出の区分の合計(self) -> int:
        """
        12. 適用を受ける特定支出の区分の合計
        （適用を受ける特定支出の各区分の【番号】を合計します。）
        """
        total = 0
        for var in vars(self).values():
            if isinstance(var, 特定支出):
                if var.差引金額>0:
                    total |= var.区分
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        特定支出詳細部分をDataFrameに変換
        """
        def to_row(特定支出: 特定支出):
            return [特定支出.区分, 特定支出.支出金額, 特定支出.補塡される金額のうち非課税部分等, 特定支出.差引金額]

        return pd.DataFrame([
            ['1', '通勤費', None] + to_row(self.通勤費),
            ['2', '職務上の旅費', None] + to_row(self.職務上の旅費),
            ['3', '転居費', None] + to_row(self.転居費),
            ['4', '研修費', None] + to_row(self.研修費),
            ['5', '資格取得費', None] + to_row(self.資格取得費),
            ['6', '帰宅旅費', None] + to_row(self.帰宅旅費),
            ['7', '勤務必要経費', '図書費'] + to_row(self.勤務必要経費_図書費),
            ['8', '勤務必要経費', '衣服費'] + to_row(self.勤務必要経費_衣服費),
            ['9', '勤務必要経費', '交際費等'] + to_row(self.勤務必要経費_交際費等),
        ], columns=['key', 'label1', 'label2', '区分', '支出金額', '補塡される金額のうち非課税部分等', '差引金額'])

    def to_agg_dataframe(self) -> pd.DataFrame:
        """
        特定支出集計部分をDataFrameに変換
        """
        return pd.DataFrame([
            ['10', '勤務必要経費', '小計', self.勤務必要経費_小計],
            ['11', '特定支出の合計額', None, self.特定支出の合計額],
            ['12', '適用を受ける特定支出の区分の合計', None, self.適用を受ける特定支出の区分の合計],
        ], columns=['key', 'label1', 'label2', 'value'])

class 給与所得者の特定支出に関する明細書:
    """
    給与所得者の特定支出に関する明細書
    https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/pdf/6-006.pdf
    """
    def __init__(self, x給与: 給与|None = None):
        self.給与 = x給与 or 給与()

        # 1 特定支出の金額
        self.特定支出の金額 = 特定支出の金額()

    @property
    def 給与等の収入金額の合計額(self) -> int:
        """
        2 特定支出控除適用後の給与所得金額 -> 13. 給与等の収入金額の合計額
        """
        return self.給与.給与等の収入金額

    @property
    def 特定支出控除適用前の給与所得金額(self) -> int:
        """
        2 特定支出控除適用後の給与所得金額 -> 14. 特定支出控除適用前の給与所得金額
        """
        return self.給与.給与所得控除後の金額

    @property
    def 給与所得控除額(self) -> int:
        """
        2 特定支出控除適用後の給与所得金額 -> 15. 給与所得控除額
        """
        return self.給与.給与所得控除額

    @property
    def _16(self) -> int:
        """
        2 特定支出控除適用後の給与所得金額 -> 16. 15×１／２
        """
        return int(self.給与所得控除額 / 2)

    @property
    def 特定支出控除の金額(self) -> int:
        """
        2 特定支出控除適用後の給与所得金額 -> 17. 特定支出控除の金額
        (赤字の場合は０)
        """
        return max(self.特定支出の金額.特定支出の合計額 - self._16, 0)

    @property
    def 特定支出控除適用後の給与所得金額(self) -> int:
        """
        2 特定支出控除適用後の給与所得金額 -> 18. 特定支出控除適用後の給与所得金額
        """
        return self.給与等の収入金額の合計額 - self.給与所得控除額 - self.特定支出控除の金額

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        # 1 特定支出の金額 詳細部分
        df = self.特定支出の金額.to_dataframe()
        df = df[['key', 'label1', 'label2', '差引金額']].rename(columns={'差引金額': 'value'})

        # 1 特定支出の金額 集計部分
        df2 = self.特定支出の金額.to_agg_dataframe()
        df = pd.concat([df, df2], ignore_index=True)

        # 2 特定支出控除適用後の給与所得金額
        df2 = pd.DataFrame([
            ['13', '給与等の収入金額の合計額', None, self.給与等の収入金額の合計額],
            ['14', '特定支出控除適用前の給与所得金額', None, self.特定支出控除適用前の給与所得金額],
            ['15', '給与所得控除額', None, self.給与所得控除額],
            ['16', '16', None, self._16],
            ['17', '特定支出控除の金額', None, self.特定支出控除の金額],
            ['18', '特定支出控除適用後の給与所得金額', None, self.特定支出控除適用後の給与所得金額],
        ], columns=['key', 'label1', 'label2', 'value'])
        df = pd.concat([df, df2], ignore_index=True)

        return df
