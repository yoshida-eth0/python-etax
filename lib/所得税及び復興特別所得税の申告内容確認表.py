import math

import pandas as pd
from context import get_context
from meta.所得税 import 所得税の税率
from utils import intfloor, ゼロ以上
from 所得.事業所得 import 損益計算書
from 所得.給与所得 import 給与所得者の特定支出に関する明細書
from 納税者 import 納税者


class 所得金額等:
    """
    所得金額

    所得税及び復興特別所得税の申告内容確認表 第一表
    ア~サ. 収入金額等
    1~12. 所得金額等

    対象:
        事業 営業等
        事業 農業
        不動産
        配当
        給与
        雑 公的年金等
        雑 業務
        雑 その他
        総合譲渡 短期
        総合譲渡 長期
        一時
    TODO:
        事業所得以外未実装
    """
    def __init__(self, 事業_営業等: 損益計算書|None = None, 給与: 給与所得者の特定支出に関する明細書|None = None):
        self.事業_営業等: 損益計算書 = 事業_営業等 or 損益計算書()
        self.給与 = 給与 or 給与所得者の特定支出に関する明細書()

    @property
    def 収入金額等_事業_営業等(self) -> int:
        """
        ア. 収入金額等 -> 事業 -> 営業等
        """
        return self.事業_営業等.売上_差引金額

    @property
    def 収入金額等_給与(self) -> int:
        """
        オ. 収入金額等 -> 給与
        """
        return self.給与.給与等の収入金額の合計額

    @property
    def 収入金額等_給与_区分(self) -> int:
        """
        オ. 収入金額等 -> 給与 -> 区分
        """
        return self.給与.特定支出の金額.適用を受ける特定支出の区分の合計

    @property
    def 所得金額等_事業_営業等(self) -> int:
        """
        1. 所得金額等 -> 事業 -> 営業等
        """
        return self.事業_営業等.所得金額

    @property
    def 所得金額等_給与(self) -> int:
        """
        6. 所得金額等 -> 給与
        """
        return self.給与.特定支出控除適用後の給与所得金額

    @property
    def 所得金額等_合計(self) -> int:
        """
        12. 所得金額等 -> 合計
        """
        return self.総所得金額等

    @property
    def 総所得金額(self) -> int:
        """
        総所得金額
        ・申告分離課税を加算しない
        ・繰越控除適用後の金額 (TODO)
        ・所得控除を差し引かない

        参考:
            合計所得金額、総所得金額、総所得金額等の違い／さつま町公式ホームページ
            https://www.satsuma-net.jp/soshiki/yakuba/1005/3/zeikin/chokenminzei_juminzei/6766.html
        """
        total = 0
        total += self.所得金額等_事業_営業等
        total += self.所得金額等_給与
        return total

    @property
    def 合計所得金額(self) -> int:
        """
        合計所得金額
        ・申告分離課税を加算する (TODO)
        ・繰越控除適用前の金額
        ・所得控除を差し引かない

        参考:
            合計所得金額、総所得金額、総所得金額等の違い／さつま町公式ホームページ
            https://www.satsuma-net.jp/soshiki/yakuba/1005/3/zeikin/chokenminzei_juminzei/6766.html

            専門用語集｜国税庁
            https://www.nta.go.jp/taxes/shiraberu/taxanswer/yogo/senmon.htm#word2
        """
        total = 0
        total += self.所得金額等_事業_営業等
        total += self.所得金額等_給与
        return total

    @property
    def 総所得金額等(self) -> int:
        """
        総所得金額等
        ・申告分離課税を加算する (TODO)
        ・繰越控除適用後の金額 (TODO)
        ・所得控除を差し引かない

        参考:
            専門用語集｜国税庁
            https://www.nta.go.jp/taxes/shiraberu/taxanswer/yogo/senmon.htm#word1
        """
        total = 0
        total += self.所得金額等_事業_営業等
        total += self.所得金額等_給与
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['ア', '収入金額等', '事業', '営業等', self.収入金額等_事業_営業等],
            ['イ', '収入金額等', '事業', '農業', 0],
            ['ウ', '収入金額等', '不動産', None, 0],
            ['エ', '収入金額等', '配当', None, 0],
            ['オ', '収入金額等', '給与', None, self.収入金額等_給与],
            ['カ', '収入金額等', '雑', '公的年金等', 0],
            ['キ', '収入金額等', '雑', '業務', 0],
            ['ク', '収入金額等', '雑', 'その他', 0],
            ['ケ', '収入金額等', '総合譲渡', '短期', 0],
            ['コ', '収入金額等', '総合譲渡', '長期', 0],
            ['サ', '収入金額等', '一時', None, 0],
            ['1', '所得金額等', '事業', '営業等', self.所得金額等_事業_営業等],
            ['2', '所得金額等', '事業', '農業', 0],
            ['3', '所得金額等', '不動産', None, 0],
            ['4', '所得金額等', '利子', None, 0],
            ['5', '所得金額等', '配当', None, 0],
            ['6', '所得金額等', '給与', None, self.所得金額等_給与],
            ['7', '所得金額等', '雑', '公的年金等', 0],
            ['8', '所得金額等', '雑', '業務', 0],
            ['9', '所得金額等', '雑', 'その他', 0],
            ['10', '所得金額等', '雑', '7から9までの計', 0],
            ['11', '所得金額等', '総合譲渡・一時', None, 0],
            ['12', '所得金額等', '合計', None, self.所得金額等_合計],
        ], columns=['key', 'label1', 'label2', 'label3', 'value'])


class 所得税_所得控除:
    """
    所得税の所得控除

    所得税及び復興特別所得税の申告内容確認表 第一表
    13~29. 所得から差し引かれる金額

    対象:
        社会保険料控除
        小規模企業共済等掛金控除
        生命保険料控除 (TODO)
        地震保険料控除 (TODO)
        寡婦、ひとり親控除 (TODO)
        勤労学生、障害者控除 (TODO)
        配偶者(特別)控除 (TODO)
        扶養控除 (TODO)
        基礎控除
        雑損控除 (TODO)
        医療費控除 (TODO)
        寄附金控除
    """
    def __init__(self, 所得金額等: 所得金額等, 納税者: 納税者):
        self.所得金額等 = 所得金額等
        self.納税者 = 納税者

    @property
    def 社会保険料控除(self) -> int:
        """
        13. 社会保険料控除
        """
        return self.納税者.社会保険料

    @property
    def 小規模企業共済等掛金控除(self) -> int:
        """
        14. 小規模企業共済等掛金控除
        """
        return self.納税者.小規模企業共済等掛金

    @property
    def 生命保険料控除(self) -> int:
        """
        15. 生命保険料控除
        """
        if self.納税者.生命保険料>0:
            raise NotImplementedError('生命保険料控除')
        return 0

    @property
    def 地震保険料控除(self) -> int:
        """
        16. 地震保険料控除
        """
        if self.納税者.地震保険料>0:
            raise NotImplementedError('地震保険料控除')
        return 0

    @property
    def 寡婦控除(self) -> int:
        """
        17~18. 寡婦控除
        """
        if self.納税者.is_寡婦:
            raise NotImplementedError('寡婦控除')
        return 0

    @property
    def ひとり親控除(self) -> int:
        """
        17~18. ひとり親控除
        """
        if self.納税者.is_ひとり親:
            raise NotImplementedError('ひとり親控除')
        return 0

    @property
    def 勤労学生控除(self) -> int:
        """
        19~20. 勤労学生控除
        """
        if self.納税者.納税者本人.is_勤労学生:
            raise NotImplementedError('勤労学生控除')
        return 0

    @property
    def 障害者控除(self) -> int:
        """
        19~20. 障害者控除
        """
        if len(self.納税者.障害者一覧)>0:
            raise NotImplementedError('障害者控除')
        return 0

    @property
    def 配偶者控除(self) -> int:
        """
        21~22. 配偶者控除
        """
        if self.納税者.配偶者 is not None:
            raise NotImplementedError('配偶者控除')
        return 0

    @property
    def 配偶者特別控除(self) -> int:
        """
        21~22. 配偶者特別控除
        """
        if self.納税者.配偶者 is not None:
            raise NotImplementedError('配偶者特別控除')
        return 0

    @property
    def 扶養控除(self) -> int:
        """
        23. 扶養控除
        """
        if len(self.納税者.扶養親族一覧)>0:
            raise NotImplementedError('扶養控除')
        return 0

    @property
    def 基礎控除(self) -> int:
        """
        24. 基礎控除
        """
        impl = get_context().所得税_基礎控除
        if impl is None:
            raise NotImplementedError(f'Context.所得税_基礎控除')

        return impl.所得税_基礎控除(self.所得金額等.所得金額等_合計)

    @property
    def _13から24までの計(self) -> int:
        """
        25. 13から24までの計
        """
        total = 0
        total += self.社会保険料控除
        total += self.小規模企業共済等掛金控除
        total += self.生命保険料控除
        total += self.地震保険料控除
        total += self.寡婦控除
        total += self.ひとり親控除
        total += self.勤労学生控除
        total += self.障害者控除
        total += self.配偶者控除
        total += self.配偶者特別控除
        total += self.扶養控除
        total += self.基礎控除
        return total

    @property
    def 雑損控除(self) -> int:
        """
        26. 雑損控除
        """
        if self.納税者.雑損.損失金額>0:
            raise NotImplementedError('雑損控除')
        return 0

    @property
    def 医療費控除(self) -> int:
        """
        27. 医療費控除
        """
        if self.納税者.医療費.医療費の実質負担額>0 or self.納税者.医療費.スイッチOTC医薬品の実質負担額>0:
            raise NotImplementedError('医療費控除')
        return 0

    @property
    def 特定寄附金額(self) -> int:
        """
        特定寄附金の額の合計額
        """
        total = 0
        total += self.納税者.ふるさと納税額
        return total

    @property
    @ゼロ以上
    def 寄附金控除(self) -> int:
        """
        28. 寄附金控除

        No.1150 一定の寄附金を支払ったとき(寄附金控除)｜国税庁
        https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1150.htm

        No.1155 ふるさと納税(寄附金控除)｜国税庁
        https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1155.htm

        総務省｜ふるさと納税のしくみ｜税金の控除について
        https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/furusato/mechanism/deduction.html
        """
        # （1） その年に支出した特定寄附金の額の合計額
        kihu = self.特定寄附金額

        # （2） その年の総所得金額等の40パーセント相当額
        shotoku40per = math.floor(self.所得金額等.総所得金額等 * 0.40)

        # （1）または（2）のいずれか低い金額 - 2000円 ＝ 寄附金控除額
        return min(kihu, shotoku40per) - 2000

    @property
    def 所得控除合計(self) -> int:
        """
        29. 合計
        """
        total = 0
        total += self._13から24までの計
        total += self.雑損控除
        total += self.医療費控除
        total += self.寄附金控除
        return total

    @property
    def 人的控除額(self) -> int:
        """
        人的控除額
        障害者控除、寡婦控除、ひとり親控除、勤労学生控除、配偶者控除、配偶者特別控除、扶養控除、基礎控除の合計
        """
        total = 0
        total += self.寡婦控除
        total += self.ひとり親控除
        total += self.勤労学生控除
        total += self.障害者控除
        total += self.配偶者控除
        total += self.配偶者特別控除
        total += self.扶養控除
        total += self.基礎控除
        return total

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['13', '社会保険料控除', self.社会保険料控除],
            ['14', '小規模企業共済等掛金控除', self.小規模企業共済等掛金控除],
            ['15', '生命保険料控除', self.生命保険料控除],
            ['16', '地震保険料控除', self.地震保険料控除],
            ['17', '寡婦控除', self.寡婦控除],
            ['18', 'ひとり親控除', self.ひとり親控除],
            ['19', '勤労学生控除', self.勤労学生控除],
            ['20', '障害者控除', self.障害者控除],
            ['21', '配偶者控除', self.配偶者控除],
            ['22', '配偶者特別控除', self.配偶者特別控除],
            ['23', '扶養控除', self.扶養控除],
            ['24', '基礎控除', self.基礎控除],
            ['25', '13から24までの計', self._13から24までの計],
            ['26', '雑損控除', self.雑損控除],
            ['27', '医療費控除', self.医療費控除],
            ['28', '寄附金控除', self.寄附金控除],
            ['29', '合計', self.所得控除合計],
        ], columns=['key', 'label', 'value'])


class 所得税_税額控除:
    """
    所得税の税額控除

    所得税及び復興特別所得税の申告内容確認表 第一表
    30~52. 税金の計算

    No.1200 税額控除｜国税庁
    https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1200.htm

    TODO
    """
    def __init__(self, 所得税_所得控除: 所得税_所得控除, 納税者: 納税者):
        self.所得金額等 = 所得税_所得控除.所得金額等
        self.所得税_所得控除 = 所得税_所得控除
        self.納税者 = 納税者

        # 42. 災害減免額
        self.災害減免額: int = 0

    @property
    @ゼロ以上
    def 課税される所得金額又は第三表(self) -> int:
        """
        30. 課税される所得金額又は第三表
        """
        return intfloor(self.所得金額等.所得金額等_合計 - self.所得税_所得控除.所得控除合計, 3)

    @property
    def 所得税の税率(self) -> 所得税の税率:
        """
        課税される所得金額に対応した所得税の計算式
        """
        impl = get_context().所得税_税率
        if impl is None:
            raise NotImplementedError(f'Context.所得税_税率')

        return impl.所得税の税率(self.課税される所得金額又は第三表)

    @property
    def 上の30に対する税額又は第三表の93(self) -> int:
        """
        31. 上の30に対する税額又は第三表の93
        """
        zeiritsu = self.所得税の税率
        return math.floor(self.課税される所得金額又は第三表 * zeiritsu.税率 - zeiritsu.控除額)

    @property
    def 差引所得税額(self) -> int:
        """
        41. 差引所得税額
        """
        total = self.上の30に対する税額又は第三表の93
        return total

    @property
    @ゼロ以上
    def 再差引所得税額(self) -> int:
        """
        43. 再差引所得税額(基準所得税額)
        """
        return self.差引所得税額 - self.災害減免額

    @property
    def 復興特別所得税(self) -> int:
        """
        44. 復興特別所得税
        """
        zeiritsu = self.所得税の税率
        return math.floor(self.再差引所得税額 * zeiritsu.復興特別所得税率)

    @property
    def 所得税及び復興特別所得税(self) -> int:
        """
        45. 所得税及び復興特別所得税
        """
        return self.再差引所得税額 + self.復興特別所得税

    @property
    def 申告納税額(self) -> int:
        """
        49. 申告納税額
        """
        return intfloor(self.所得税及び復興特別所得税, 2)

    @property
    def 予定納税額(self) -> int:
        """
        50. 予定納税額(第1期分・第2期分)
        """
        return self.納税者.予定納税額_第1期分 + self.納税者.予定納税額_第2期分

    @property
    def 第3期分の税額(self) -> int:
        """
        51. 第3期分の税額
        """
        return self.申告納税額 - self.予定納税額

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        return pd.DataFrame([
            ['30', '課税される所得金額又は第三表', None, self.課税される所得金額又は第三表],
            ['31', '上の30に対する税額又は第三表の93', None, self.上の30に対する税額又は第三表の93],
            ['32', '配当控除', None, 0],
            ['33', '', None, 0],
            ['34', '(特定増改築等)住宅借入金等特別控除', None, 0],
            ['35', '政党等寄附金等特別控除', None, 0],
            ['36', '政党等寄附金等特別控除', None, 0],
            ['37', '政党等寄附金等特別控除', None, 0],
            ['38', '住宅耐震改修特別控除', None, 0],
            ['39', '住宅特定改修特別税額控除', None, 0],
            ['40', '認定住宅等新築等特別税額控除', None, 0],
            ['41', '差引所得税額', None, self.差引所得税額],
            ['42', '災害減免額', None, self.災害減免額],
            ['43', '再差引所得税額(基準所得税額)', None, self.再差引所得税額],
            ['44', '復興特別所得税', None, self.復興特別所得税],
            ['45', '所得税及び復興特別所得税', None, self.所得税及び復興特別所得税],
            ['46', '外国税額控除', None, 0],
            ['47', '外国税額控除', None, 0],
            ['48', '源泉徴収税額', None, 0],
            ['49', '申告納税額', None, self.申告納税額],
            ['50', '予定納税額(第1期分・第2期分)', None, self.予定納税額],
            ['51', '第3期分の税額', '収める税金', max(0, self.第3期分の税額)],
            ['52', '第3期分の税額', '還付される税金', min(0, self.第3期分の税額)],
        ], columns=['key', 'label1', 'label2', 'value'])


class 所得税及び復興特別所得税の申告内容確認表_第一表:
    """
    所得税及び復興特別所得税の申告内容確認表 第一表
    """
    def __init__(self, 所得金額等: 所得金額等, 納税者: 納税者):
        # ア~サ. 収入金額等
        # 1~12. 所得金額等
        self.所得金額等 = 所得金額等

        # 13~29. 所得から差し引かれる金額
        self.所得税_所得控除 = 所得税_所得控除(所得金額等, 納税者)

        # 32~52. 税金の計算
        self.所得税_税額控除 = 所得税_税額控除(self.所得税_所得控除, 納税者)

    def to_dataframe(self) -> pd.DataFrame:
        """
        DataFrameに変換
        """
        # 収入金額等, 所得金額等
        df = self.所得金額等.to_dataframe()

        # 所得から差し引かれる金額
        df2 = self.所得税_所得控除.to_dataframe()
        df2['label1'] = '所得から差し引かれる金額'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        # 税金の計算
        df2 = self.所得税_税額控除.to_dataframe()
        df2.rename(columns={'label1': 'label2', 'label2': 'label3'}, inplace=True)
        df2['label1'] = '税金の計算'
        df = pd.concat([df, df2], ignore_index=True)

        # 修正申告
        df2 = pd.DataFrame([
            ['53', '修正前の第3期分の税額', 0],
            ['54', '第3期分の税額の増加額', 0],
        ], columns=['key', 'label', 'value'])
        df2['label1'] = '修正申告'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        # その他
        df2 = pd.DataFrame([
            ['55', '公的年金等以外の合計所得金額', self.所得金額等.所得金額等_合計],
            ['56', '配偶者の合計所得金額', 0],
            ['57', '専従者給与(控除)額の合計額', 0],
            ['58', '青色申告特別控除額', self.所得金額等.事業_営業等.青色申告特別控除額],
            ['59', '雑所得・一時所得等の 源泉徴収税額の合計額', 0],
            ['60', '未納付の源泉徴収税額', 0],
            ['61', '本年分で差し引く繰越損失額', 0],
            ['62', '平均課税対象金額', 0],
            ['63', '変動・臨時所得金額', 0],
        ], columns=['key', 'label', 'value'])
        df2['label1'] = 'その他'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        # 延納の届出
        df2 = pd.DataFrame([
            ['64', '申告期限までに納付する金額', 0],
            ['65', '延納届出額', 0],
        ], columns=['key', 'label', 'value'])
        df2['label1'] = '延納の届出'
        df2.rename(columns={'label': 'label2'}, inplace=True)
        df = pd.concat([df, df2], ignore_index=True)

        df = df[['key', 'label1', 'label2', 'label3', 'value']]
        return df
