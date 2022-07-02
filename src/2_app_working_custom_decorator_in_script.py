import functools
from omegaconf import DictConfig, OmegaConf
from common.config import Config

from common.root_dir import ROOT_DIR

import hydra

def ingest_config(func):
    @functools.wraps(func)
    @hydra.main(config_path=ROOT_DIR / "conf", config_name="config", version_base=None)
    def inner(dict_config):
        config = hydra.utils.instantiate(dict_config)
        func(config)

    return inner
    

@ingest_config
def main(config: Config):
    print("I use hydra directly")
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()