from dataclasses import dataclass

import hydra

from common.root_dir import ROOT_DIR

@dataclass
class Config:
    foo: int
    bar: str


def ingest_config_not_working_with_pathlib(func):
    @hydra.main(config_path=ROOT_DIR / "conf", config_name="config", version_base=None)
    def inner(dict_config):
        config = hydra.utils.instantiate(dict_config)
        func(config)

    return inner


def ingest_config_not_working_absolute_path(func):
    @hydra.main(config_path=str(ROOT_DIR / "conf"), config_name="config", version_base=None)
    def inner(dict_config):
        config = hydra.utils.instantiate(dict_config)
        func(config)

    return inner


def ingest_config_not_working_relative_path(func):
    @hydra.main(config_path="../../conf", config_name="config", version_base=None)
    def inner(dict_config):
        config = hydra.utils.instantiate(dict_config)
        func(config)

    return inner


def ingest_config_working_relative_path(func):
    @hydra.main(config_path="../conf_inside_src", config_name="config", version_base=None)
    def inner(dict_config):
        config = hydra.utils.instantiate(dict_config)
        func(config)

    return inner