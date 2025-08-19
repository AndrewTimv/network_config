# Generate config from yaml

import yaml
import importlib


class ConfigGenerator:
    def __init__(self, yaml_config: str):
        self.yaml_config = yaml_config
        self.vendor = ''
        self.model = ''
        self.os = ''

    @staticmethod
    def get_vendor_lib(vendor: str) -> str | None:
        """
        get vendor lib name
        """
        match vendor:
            case 'Alcatel-Lucent':
                result = 'alcatel-lucent'
            case _:
                result = None
        return result

    def generate(self):
        data = yaml.safe_load(self.yaml_config)
        # Get device model and os version
        self.vendor = data.get('vendor')
        self.model = data.get('model')
        self.os = data.get('os')

        vendor_lib = self.get_vendor_lib(self.vendor)

        vendor = importlib.import_module(f'src.drivers.{vendor_lib}')
        driver = vendor.get_driver(self.model, self.os)

        if driver is None:
            raise Exception(f'No such vendor or model or OS version')


        result = driver.generate_config(data)
        return result
