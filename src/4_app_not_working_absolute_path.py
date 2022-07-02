from omegaconf import OmegaConf
from common.config import Config, ingest_config_not_working_absolute_path


@ingest_config_not_working_absolute_path
def main(config: Config):
    print("I use an absolute path in the decorator")
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()