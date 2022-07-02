from omegaconf import OmegaConf
from common.config import Config, ingest_config_not_working_relative_path


@ingest_config_not_working_relative_path
def main(config: Config):
    print("I use a relative path in the decorator")
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()