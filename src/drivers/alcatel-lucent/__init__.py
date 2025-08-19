# Driver for Alcatel-Lucent

import importlib

from logging import Logger

logger = Logger(__name__)

def get_driver(model: str, os: str):
    """
    Get driver for current version
    """
    logger.error(f'{model=}, {os=}')
    match model:
        case 'OS6450' | 'OmniSwitch 6450':
            match os:
                case 'aos_6_6_2_r02' | 'AOS 6.6.2 R02':
                    lib = importlib.import_module('src.drivers.alcatel-lucent.aos_6_6_2_r02')
                    result = lib.NetDriver()
                case _:
                    result = None
        case _:
            result = None

    return result