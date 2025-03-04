"""
雑所得
収支内訳書
"""

import pandas as pd


class 収入金額:
    """
    収支内訳書
    1~4. 収入金額
    """
    def __init__(self, 売上金額: int = 0, 家事消費: int = 0, その他の収入: int = 0):
        # 1. 売上(収入)金額
        self.売上金額 = 売上金額

        # 2. 家事消費
        self.家事消費 = 家事消費

        # 3. その他の収入
        self.その他の収入 = その他の収入

    @property
    def 計(self) -> int:
        """
        4. 計
        """
        return self.売上金額 + self.家事消費 + self.その他の収入

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['1', '売上(収入)金額', self.売上金額],
            ['2', '家事消費', self.家事消費],
            ['3', 'その他の収入', self.その他の収入],
            ['4', '計', self.計],
        ], columns=['key', 'label', 'value'])


class 売上原価:
    """
    収支内訳書
    5~9. 売上原価
    """
    def __init__(self):
        # 5. 期首商品(製品) 棚卸高
        self.期首商品_棚卸高: int = 0

        # 6. 仕入金額(製品製造原価)
        self.仕入金額: int = 0

        # 8. 期末商品 (製品) 棚卸高
        self.期末商品_棚卸高: int = 0

    @property
    def 小計(self) -> int:
        """
        7. 小計
        """
        return self.期首商品_棚卸高 + self.仕入金額

    @property
    def 差引原価(self) -> int:
        """
        9. 差引原価
        """
        return self.小計 - self.期末商品_棚卸高

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['5', '期首商品(製品) 棚卸高', self.期首商品_棚卸高],
            ['6', '仕入金額(製品製造原価)', self.仕入金額],
            ['7', '小計', self.小計],
            ['8', '期末商品 (製品) 棚卸高', self.期末商品_棚卸高],
            ['9', '差引原価', self.差引原価],
        ], columns=['key', 'label', 'value'])


class その他の経費:
    """
    収支内訳書
    イ~レ. 経費 -> その他の経費
    """
    def __init__(self):
        # イ. 租税公課
        self.租税公課: int = 0

        # ロ. 荷造運賃
        self.荷造運賃: int = 0

        # ハ. 水道光熱費
        self.水道光熱費: int = 0

        # ニ. 旅費交通費
        self.旅費交通費: int = 0

        # ホ. 通信費
        self.通信費: int = 0

        # ヘ. 広告宣伝費
        self.広告宣伝費: int = 0

        # ト. 接待交際費
        self.接待交際費: int = 0

        # チ. 損害保険料
        self.損害保険料: int = 0

        # リ. 修繕費
        self.修繕費: int = 0

        # ヌ. 消耗品費
        self.消耗品費: int = 0

        # ル. 福利厚生費
        self.福利厚生費: int = 0

        # ヲ.
        self.label_wo: str = ''
        self.value_wo: int = 0

        # ワ.
        self.label_wa: str = ''
        self.value_wa: int = 0

        # カ.
        self.label_ka: str = ''
        self.value_ka: int = 0

        # ヨ.
        self.label_yo: str = ''
        self.value_yo: int = 0

        # タ.
        self.label_ta: str = ''
        self.value_ta: int = 0

        # レ. 雑費
        self.雑費: int = 0

    @property
    def 小計(self):
        """
        17. 小計
        """
        total = 0
        total += self.租税公課
        total += self.荷造運賃
        total += self.水道光熱費
        total += self.旅費交通費
        total += self.通信費
        total += self.広告宣伝費
        total += self.接待交際費
        total += self.損害保険料
        total += self.修繕費
        total += self.消耗品費
        total += self.福利厚生費
        total += self.value_wo
        total += self.value_wa
        total += self.value_ka
        total += self.value_yo
        total += self.value_ta
        total += self.雑費
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['イ', '租税公課', self.租税公課],
            ['ロ', '荷造運賃', self.荷造運賃],
            ['ハ', '水道光熱費', self.水道光熱費],
            ['ニ', '旅費交通費', self.旅費交通費],
            ['ホ', '通信費', self.通信費],
            ['ヘ', '広告宣伝費', self.広告宣伝費],
            ['ト', '接待交際費', self.接待交際費],
            ['チ', '損害保険料', self.損害保険料],
            ['リ', '修繕費', self.修繕費],
            ['ヌ', '消耗品費', self.消耗品費],
            ['ル', '福利厚生費', self.福利厚生費],
            ['ヲ', self.label_wo, self.value_wo],
            ['ワ', self.label_wa, self.value_wa],
            ['カ', self.label_ka, self.value_ka],
            ['ヨ', self.label_yo, self.value_yo],
            ['タ', self.label_ta, self.value_ta],
            ['17', '小計', self.小計],
        ], columns=['key', 'label', 'value'])


class 経費:
    """
    収支内訳書
    11~18. 経費
    """
    def __init__(self):
        # 11. 給料賃金
        self.給料賃金: int = 0

        # 12. 外注工賃
        self.外注工賃: int = 0

        # 13. 減価償却費
        self.減価償却費: int = 0

        # 14. 貸倒金
        self.貸倒金: int = 0

        # 15. 地代家賃
        self.地代家賃: int = 0

        # 16. 利子割引料
        self.利子割引料: int = 0

        # イ~レ. その他の経費
        self.その他の経費 = その他の経費()

    @property
    def 経費計(self) -> int:
        """
        17. 経費計
        """
        total = 0
        total += self.給料賃金
        total += self.外注工賃
        total += self.減価償却費
        total += self.貸倒金
        total += self.地代家賃
        total += self.利子割引料
        total += self.その他の経費.小計
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        df = pd.DataFrame([
            ['11', '給料賃金', self.給料賃金],
            ['12', '外注工賃', self.外注工賃],
            ['13', '減価償却費', self.減価償却費],
            ['14', '貸倒金', self.貸倒金],
            ['15', '地代家賃', self.地代家賃],
            ['16', '利子割引料', self.利子割引料],
        ], columns=['key', 'label1', 'value'])

        # その他の経費
        df2 = self.その他の経費.to_dataframe()
        df2['label1'] = 'その他の経費'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        return df


class 収支内訳書:
    """
    収支内訳書
    """
    def __init__(self):
        # 1~4. 収入金額
        self.収入金額 = 収入金額()

        # 5~9. 売上原価
        self.売上原価 = 売上原価()

        # 11~18. 経費
        self.経費 = 経費()

        # 20. 専従者控除
        self.専従者控除: int = 0

    @property
    def 差引金額(self) -> int:
        """
        11. 差引金額
        """
        return self.収入金額.計 - self.売上原価.差引原価

    @property
    def 専従者控除前の所得金額(self) -> int:
        """
        19. 専従者控除前の所得金額
        """
        return self.差引金額 - self.経費.経費計

    @property
    def 所得金額(self) -> int:
        """
        21. 所得金額
        """
        return self.専従者控除前の所得金額 - self.専従者控除

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        # 収入金額
        df = self.収入金額.to_dataframe()
        df['label1'] = '収入金額'
        df.rename(columns={'label': 'label2'}, inplace=True)

        # 売上原価
        df2 = self.売上原価.to_dataframe()
        df2['label1'] = '売上原価'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        # 差引金額
        df2 = pd.DataFrame([
            ['10', '差引金額', self.差引金額],
        ], columns=['key', 'label1', 'value'])
        df = pd.concat([df, df2], ignore_index=True)

        # 経費
        df2 = self.経費.to_dataframe()
        df2.rename(columns={'label1': 'label2', 'label2': 'label3'}, inplace=True)
        df2['label1'] = '経費'
        df = pd.concat([df, df2], ignore_index=True)

        # 専従者控除
        df2 = pd.DataFrame([
            ['19', '専従者控除前の所得金額', self.専従者控除前の所得金額],
            ['20', '専従者控除', self.専従者控除],
            ['21', '所得金額', self.所得金額],
        ], columns=['key', 'label1', 'value'])
        df = pd.concat([df, df2], ignore_index=True)

        return df[['key', 'label1', 'label2', 'label3', 'value']]
