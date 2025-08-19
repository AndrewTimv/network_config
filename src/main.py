# Get config

from src.drivers.config_generator import ConfigGenerator


def main():
    with open('samples/sample_one.yaml') as f:
        yaml_data = f.read()
    conf_gen = ConfigGenerator(yaml_data)
    config = conf_gen.generate()

    print(config)


if __name__ == '__main__':
    main()