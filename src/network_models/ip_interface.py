# Описание ip интерфейсов

import ipaddress

from pydantic import BaseModel

from .vlan import VLAN

class IpInterface(BaseModel):
    """
    Класс IP интерфейса
    """
    name: str
    address: ipaddress.ip_interface = None
    vlan: VLAN = None
    interface