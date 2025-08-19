# Alcatel-Lucent AOS 6.6.2 R02
from src.network_models.ethernet import EthernetInterface, EthernetSpeed
from src.network_models.system import System


class NetDriver:
    """
    NetDriver for Alcatel-Lucent OmniSwitch 6450 AOS 6.6.2 R02
    """
    def __init__(self):
        pass

    def generate_config(self, yaml_data: dict) -> str:
        """
        Generate config from YAML data
        """
        result = ''
        print(f'{yaml_data}')

        # System
        system_json = yaml_data['system']
        system = System.model_validate(system_json)

        # DDM
        if system.ddm:
            result += f'interfaces transceiver ddm enable\n'

        # Ethernet
        ethernet_json = yaml_data['ethernet']
        print(ethernet_json)
        interfaces = []
        for key in ethernet_json:
            if_number = f'1/{key}'
            interface_json = {'name': f'{if_number}'} | ethernet_json[key]
            print(interface_json)
            interfaces.append(EthernetInterface.model_validate(interface_json))


        for interface in interfaces:
            # Trap
            if interface.link_trap:
                result += f'trap {interface.name} port link enable\n'

            # Admin status
            if not interface.admin_state:
                result += f'interfaces {interface.name} admin down\n'

            # Alias
            if interface.description:
                result += f'interfaces {interface.name} alias "{interface.description}"\n'

            # Autonegotiation
            if not interface.autonegotiation:
                result += f'interfaces {interface.name} autoneg disable\n'

            # Speed
            if interface.configured_line_speed != EthernetSpeed.auto:
                result += f'interface {interface.name} speed {interface.configured_line_speed}\n'

        return result