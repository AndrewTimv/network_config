from pydantic import BaseModel

from .ethernet import EthernetInterface
from .spanning_tree import SpanningTree
from .vlan import VLAN


class L3Switch(BaseModel):
    """
    Коммутатор 3 уровня
    """
    sysname: str = ''
    description: str = ''
    location: str = ''
    model = ''
    interfaces: list[EthernetInterface] = []
    vlans: list[VLAN]
    spantree: SpanningTree = SpanningTree()