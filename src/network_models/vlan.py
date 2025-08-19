# Модели для VLAN

from enum import Flag

from pydantic import BaseModel

from .ethernet import EthernetInterface

class L2Interface:
    """
    Варианты L2 интерфейсов
    Физический порт или L2 интерфейс
    """
    pass


class VlanAdminStatus(Flag):
    """
    Административное состояние VLAN
    """
    enable = True
    disable = False

class VLAN(BaseModel):
    """
    Описание VLAN
    """
    id: int
    name: str = ''
    admin_status: VlanAdminStatus = VlanAdminStatus.enable
    tagged_interfaces: list[L2Interface] = []
    untagged_interfaces: list[L2Interface] = []
    spanning_tree: SpanningTree = SpanningTree()