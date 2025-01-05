from contextlib import contextmanager
from dataclasses import dataclass, replace

from meta.介護保険 import I介護保険
from meta.住民税 import I住民税_基礎控除, I住民税_税率一覧
from meta.健康保険 import I健康保険
from meta.厚生年金保険 import I厚生年金保険
from meta.国民健康保険 import I国民健康保険
from meta.所得税 import I所得税_基礎控除, I所得税_税率
from meta.給与所得控除 import I給与所得控除
from meta.雇用保険 import I雇用保険


@dataclass
class Context:
    """
    年に対する定数
    """
    # 給与所得
    給与所得控除: I給与所得控除|None = None

    # 所得税
    所得税_基礎控除: I所得税_基礎控除|None = None
    所得税_税率: I所得税_税率|None = None

    # 住民税
    住民税_基礎控除: I住民税_基礎控除|None = None
    住民税_税率一覧: I住民税_税率一覧|None = None

    # 社会保険
    厚生年金保険: I厚生年金保険|None = None
    健康保険: I健康保険|None = None
    介護保険: I介護保険|None = None
    雇用保険: I雇用保険|None = None

    # 国民健康保険
    国民健康保険: I国民健康保険|None = None


# stack

context_stack: list[Context] = [Context()]

def push_context(context: Context) -> Context:
    """
    コンテキストを追加して切り替える
    """
    context_stack.append(context)
    return context

def pop_context() -> None:
    """
    コンテキストを削除して抜ける
    """
    context_stack.pop()

@contextmanager
def open_context(context: Context|None = None):
    """
    with文の中のみコンテキストを切り替える

    args:
        context (Context|None): with文の中のみ有効にするコンテキスト、Noneの場合は新たに作成する
    """
    context = context or Context()
    push_context(context)
    try:
        yield context
    finally:
        pop_context()

@contextmanager
def open_clone_context():
    """
    現行のコンテキストをコピーし、with文の中のみ切り替える
    """
    clone_context = replace(get_context())
    with open_context(clone_context):
        yield clone_context

def get_context() -> Context:
    """
    現行のコンテキストを返す
    """
    if len(context_stack)==0:
        raise NotImplementedError('not exists context')
    return context_stack[-1]

def set_context(context: Context):
    """
    現行のコンテキストを書き換える
    """
    if len(context_stack)==0:
        raise NotImplementedError('not exists context')
    context_stack[-1] = context
