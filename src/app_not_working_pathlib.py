from omegaconf import OmegaConf
from common.config import Config, ingest_config_not_working_with_pathlib


@ingest_config_not_working_with_pathlib
def main(config: Config):
    print("I use a pathlib path in the decorator")
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()