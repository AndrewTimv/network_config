# Модели для Ethernet

from enum import Enum, Flag

from pydantic import BaseModel


class EthernetSpeed(str, Enum):
    """
    Скорость на портах Ethernet
    """
    auto = 'auto'
    ten = '10'
    hundred = '100'
    gigabit = '1000'
    tengigabit = '10000'

class EthernetDuplex(str, Enum):
    """
    Режим дуплекса
    """
    auto = 'auto'
    half = 'half-duplex'
    full = 'full_duplex'

class EthernetCrossover(str, Enum):
    """
    MDI/MDIX
    """
    auto = 'auto'
    mdi = 'MDI'
    mdix = 'MDIX'


class InterfaceType(str, Enum):
    """
    Тип физического интерфейса
    """
    ethernet = '10 BaseT'
    fast_ethernet = '10/100 BaseT'
    gigabit_ethernet = '10/100/1000 BaseT'
    ten_gigabit_ethernet = '10G Ethernet'
    forty_gigabit_ethernet = '40G Ethernet'
    one_hundred_gigabit_ethernet = '100G Ethernet'
    sfp = 'SFP'
    sfp_plus = 'SFP+'


class InterfaceAdminState(Flag):
    """
    Административное состояние интерфейса
    """
    up = True
    down = False


class DigitalDiagnosticMonitoring(Flag):
    """
    Включение DDM на интерфейсах
    """
    enable = True
    disable = False


class EnergyEfficientEthernet(Flag):
    """
    Energy Efficient Ethernet (802.3az)
    """
    enable = True
    disable = False


class EthernetInterface(BaseModel):
    """
    Физический интерфейс
    """
    name: str
    description: str = ''
    combo: bool = False
    type: InterfaceType = InterfaceType.gigabit_ethernet
    admin_state: InterfaceAdminState = InterfaceAdminState.up
    autonegotiation: bool = True
    configured_line_speed: EthernetSpeed = EthernetSpeed.auto
    configured_duplex_mode: EthernetDuplex = EthernetDuplex.auto
    configured_crossover_mode: EthernetCrossover = EthernetCrossover.auto
    link_trap: bool = False
    ddm: DigitalDiagnosticMonitoring = None
    eee: EnergyEfficientEthernet = None