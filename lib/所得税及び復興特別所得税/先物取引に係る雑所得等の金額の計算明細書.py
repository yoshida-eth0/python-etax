"""
所得税及び復興特別所得税
先物取引に係る雑所得等の金額の計算明細書
"""

from datetime import date
from functools import reduce

import pandas as pd


class 先物取引に係る雑所得等の金額の計算明細書_詳細:
    """
    先物取引に係る雑所得等の金額の計算明細書
    1列
    """
    def __init__(self, label: str):
        self.label = label

        # 取引の内容 -> 種類
        self.取引の内容_種類: str|None = None

        # 取引の内容 -> 決済年月日
        self.取引の内容_決済年月日: date|None = None

        # 取引の内容 -> 数量
        self.取引の内容_数量: int|None = None

        # 取引の内容 -> 決済の方法
        self.取引の内容_決済の方法: str|None = None

        # 1. 総収入金額 -> 差金等決済に係る利益又は損失の額
        self.総収入金額_差金等決済に係る利益又は損失の額: int = 0

        # 2. 総収入金額 -> 譲渡による収入金額
        self.総収入金額_譲渡による収入金額: int = 0

        # 3. 総収入金額 -> その他の収入
        self.総収入金額_その他の収入: int = 0

        # 5. 必要経費等 -> 手数料等
        self.必要経費等_手数料等: int = 0

        # 6. 必要経費等 -> 2に係る取得費
        self.必要経費等_2に係る取得費: int = 0

        # 7. 必要経費等 -> その他の経費 -> 1
        self.必要経費等_その他の経費_value1: int = 0

        # 8. 必要経費等 -> その他の経費 -> 2
        self.必要経費等_その他の経費_value2: int = 0

        # 9. 必要経費等 -> その他の経費 -> 3
        self.必要経費等_その他の経費_value3: int = 0

    @property
    def 総収入金額_計(self) -> int:
        """
        4. 総収入金額 -> 計
        """
        return sum([
            self.総収入金額_差金等決済に係る利益又は損失の額,
            self.総収入金額_譲渡による収入金額,
            self.総収入金額_その他の収入,
        ])

    @property
    def 必要経費等_その他の経費_小計(self) -> int:
        """
        10. 必要経費等 -> その他の経費 -> 小計
        """
        return sum([
            self.必要経費等_その他の経費_value1,
            self.必要経費等_その他の経費_value2,
            self.必要経費等_その他の経費_value3,
        ])

    @property
    def 必要経費等_計(self) -> int:
        """
        11. 必要経費等 -> 計
        """
        return sum([
            self.必要経費等_手数料等,
            self.必要経費等_2に係る取得費,
            self.必要経費等_その他の経費_小計,
        ])

    @property
    def 所得金額(self) -> int:
        """
        12. 所得金額
        """
        return self.総収入金額_計 - self.必要経費等_計

    def to_dataframe(self, 必要経費等_その他の経費_label1: str, 必要経費等_その他の経費_label2: str, 必要経費等_その他の経費_label3: str) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['', '取引の内容', '種類', None, self.取引の内容_種類],
            ['', '取引の内容', '決済年月日', None, self.取引の内容_決済年月日],
            ['', '取引の内容', '数量', None, self.取引の内容_数量],
            ['', '取引の内容', '決済の方法', None, self.取引の内容_決済の方法],
            ['1', '総収入金額', '差金等決済に係る利益又は損失の額', None, self.総収入金額_差金等決済に係る利益又は損失の額],
            ['2', '総収入金額', '譲渡による収入金額', None, self.総収入金額_譲渡による収入金額],
            ['3', '総収入金額', 'その他の収入', None, self.総収入金額_その他の収入],
            ['4', '総収入金額', '計', None, self.総収入金額_計],
            ['5', '必要経費等', '手数料等', None, self.必要経費等_手数料等],
            ['6', '必要経費等', '2に係る取得費', None, self.必要経費等_2に係る取得費],
            ['7', '必要経費等', 'その他の経費', 必要経費等_その他の経費_label1, self.必要経費等_その他の経費_value1],
            ['8', '必要経費等', 'その他の経費', 必要経費等_その他の経費_label2, self.必要経費等_その他の経費_value2],
            ['9', '必要経費等', 'その他の経費', 必要経費等_その他の経費_label3, self.必要経費等_その他の経費_value3],
            ['10', '必要経費等', 'その他の経費', '小計', self.必要経費等_その他の経費_小計],
            ['11', '必要経費等', '計', None, self.必要経費等_計],
            ['12', '所得金額', None, None, self.所得金額],
        ], columns=['key', 'label1', 'label2', 'label3', self.label])


class 先物取引に係る雑所得等の金額の計算明細書_合計:
    """
    先物取引に係る雑所得等の金額の計算明細書
    合計
    """
    def __init__(self, 詳細一覧: list[先物取引に係る雑所得等の金額の計算明細書_詳細]):
        self.詳細一覧 = 詳細一覧
        self.label = '合計'

    @property
    def 総収入金額_差金等決済に係る利益又は損失の額(self) -> int:
        """
        1. 総収入金額 -> 差金等決済に係る利益又は損失の額
        """
        return sum([v.総収入金額_差金等決済に係る利益又は損失の額 for v in self.詳細一覧])

    @property
    def 総収入金額_譲渡による収入金額(self) -> int:
        """
        2. 総収入金額 -> 譲渡による収入金額
        """
        return sum([v.総収入金額_譲渡による収入金額 for v in self.詳細一覧])

    @property
    def 総収入金額_その他の収入(self) -> int:
        """
        3. 総収入金額 -> その他の収入
        """
        return sum([v.総収入金額_その他の収入 for v in self.詳細一覧])

    @property
    def 総収入金額_計(self) -> int:
        """
        4. 総収入金額 -> 計
        """
        return sum([v.総収入金額_計 for v in self.詳細一覧])

    @property
    def 必要経費等_手数料等(self) -> int:
        """
        5. 必要経費等 -> 手数料等
        """
        return sum([v.必要経費等_手数料等 for v in self.詳細一覧])

    @property
    def 必要経費等_2に係る取得費(self) -> int:
        """
        6. 必要経費等 -> 2に係る取得費
        """
        return sum([v.必要経費等_2に係る取得費 for v in self.詳細一覧])

    @property
    def 必要経費等_その他の経費_value1(self) -> int:
        """
        7. 必要経費等 -> その他の経費 -> 1
        """
        return sum([v.必要経費等_その他の経費_value1 for v in self.詳細一覧])

    @property
    def 必要経費等_その他の経費_value2(self) -> int:
        """
        8. 必要経費等 -> その他の経費 -> 2
        """
        return sum([v.必要経費等_その他の経費_value2 for v in self.詳細一覧])

    @property
    def 必要経費等_その他の経費_value3(self) -> int:
        """
        9. 必要経費等 -> その他の経費 -> 3
        """
        return sum([v.必要経費等_その他の経費_value3 for v in self.詳細一覧])

    @property
    def 必要経費等_その他の経費_小計(self) -> int:
        """
        10. 必要経費等 -> その他の経費 -> 小計
        """
        return sum([v.必要経費等_その他の経費_小計 for v in self.詳細一覧])

    @property
    def 必要経費等_計(self) -> int:
        """
        11. 必要経費等 -> 計
        """
        return sum([v.必要経費等_計 for v in self.詳細一覧])

    @property
    def 所得金額(self) -> int:
        """
        12. 所得金額
        """
        return sum([v.所得金額 for v in self.詳細一覧])

    def to_dataframe(self, 必要経費等_その他の経費_label1: str, 必要経費等_その他の経費_label2: str, 必要経費等_その他の経費_label3: str) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['1', '総収入金額', '差金等決済に係る利益又は損失の額', None, self.総収入金額_差金等決済に係る利益又は損失の額],
            ['2', '総収入金額', '譲渡による収入金額', None, self.総収入金額_譲渡による収入金額],
            ['3', '総収入金額', 'その他の収入', None, self.総収入金額_その他の収入],
            ['4', '総収入金額', '計', None, self.総収入金額_計],
            ['5', '必要経費等', '手数料等', None, self.必要経費等_手数料等],
            ['6', '必要経費等', '2に係る取得費', None, self.必要経費等_2に係る取得費],
            ['7', '必要経費等', 'その他の経費', 必要経費等_その他の経費_label1, self.必要経費等_その他の経費_value1],
            ['8', '必要経費等', 'その他の経費', 必要経費等_その他の経費_label2, self.必要経費等_その他の経費_value2],
            ['9', '必要経費等', 'その他の経費', 必要経費等_その他の経費_label3, self.必要経費等_その他の経費_value3],
            ['10', '必要経費等', 'その他の経費', '小計', self.必要経費等_その他の経費_小計],
            ['11', '必要経費等', '計', None, self.必要経費等_計],
            ['12', '所得金額', None, None, self.所得金額],
        ], columns=['key', 'label1', 'label2', 'label3', self.label])


class 先物取引に係る雑所得等の金額の計算明細書:
    """
    先物取引に係る雑所得等の金額の計算明細書
    """
    def __init__(self):
        self.必要経費等_その他の経費_label1: str = ''
        self.必要経費等_その他の経費_label2: str = ''
        self.必要経費等_その他の経費_label3: str = ''

        self.a = 先物取引に係る雑所得等の金額の計算明細書_詳細('A')
        self.b = 先物取引に係る雑所得等の金額の計算明細書_詳細('B')
        self.c = 先物取引に係る雑所得等の金額の計算明細書_詳細('C')
        self.合計 = 先物取引に係る雑所得等の金額の計算明細書_合計([self.a, self.b, self.c])

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        def to_dataframe(v: 先物取引に係る雑所得等の金額の計算明細書_詳細|先物取引に係る雑所得等の金額の計算明細書_合計) -> tuple[pd.DataFrame,str]:
            # 詳細または合計をDataFrameに変換し、マージ用のキーを設定する
            df = v.to_dataframe(
                self.必要経費等_その他の経費_label1,
                self.必要経費等_その他の経費_label2,
                self.必要経費等_その他の経費_label3
            )
            df['tmp_key'] = df['key'] + df['label2'].fillna('')
            df = df.set_index('tmp_key')
            return df, v.label

        def concat_df(a: tuple[pd.DataFrame,str], b: tuple[pd.DataFrame,str]) -> tuple[pd.DataFrame,str]:
            # DataFrameに明細の値列を追加する
            a_df = a[0]
            b_df = b[0]
            label = b[1]

            a_df[label] = b_df[label]
            return a_df, label

        dfs = [to_dataframe(v) for v in [self.a, self.b, self.c, self.合計]]
        df, _ = reduce(concat_df, dfs)

        return df.reset_index(drop=True)
