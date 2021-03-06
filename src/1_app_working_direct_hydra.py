from omegaconf import DictConfig, OmegaConf
from common.config import Config

from common.root_dir import ROOT_DIR

import hydra

@hydra.main(config_path=ROOT_DIR / "conf", config_name="config", version_base=None)
def main(config: DictConfig):
    config: Config = hydra.utils.instantiate(config)
    print("I use hydra directly")
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()