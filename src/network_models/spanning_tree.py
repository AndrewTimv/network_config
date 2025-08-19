# Модели протокола структурного дерева

from enum import Flag, Enum

from pydantic import BaseModel


class AdminState(Flag):
    """
    Административное состояние
    """
    enable: bool = True
    disable: bool = False

class SpanningTreeMode(str, Enum):
    """
    Режим работы SpanningTree
    flat, per-vlan
    mst не рассматриваем
    """
    flat = 'flat'
    per_vlan = 'per-vlan'

class SpanningTreeInstance(BaseModel):
    """
    Описание экземпляра SpanningTree
    """

class SpanningTree(BaseModel):
    """
    Описание SpanningTree
    """
    admin_state: AdminState = AdminState.enable
    mode = SpanningTreeMode = SpanningTreeMode.per_vlan
    instances = list[SpanningTreeInstance]
