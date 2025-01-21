import sys
import os
from pathlib import Path
module_path = os.path.join(Path().resolve(), '../')
sys.path.append(module_path)
os.environ['PYTHONPATH'] = module_path

import hydra
from omegaconf import DictConfig, OmegaConf
from utils.dataset import Memory_Dataset
import datetime

import copy
from tqdm import tqdm
import torch
import numpy as np
import wandb

from utils.logger import setup_experiment
from algos.main import Model_Agent
from algos.MH.algo import MH_naming


def run(cfg):
    """
    params
    ------
    cfg: object
        config.yalm
    """
    # ---------- setup experiment ----------
    _, results_dir, device = setup_experiment(cfg)
    models = [None]*cfg.train.num_agents
    
    # ---------- initialize model ----------
    for agent_itr in range(cfg.train.num_agents):
        print(f"Load Agent{agent_itr}")
        models[agent_itr] = Model_Agent(cfg, f"Agent{agent_itr}", device)
    
    itr_start = 0 #TODO: model load時に設定しなくていい...？ => いい。MHNGの学習途中から再開することはない...??

    # ---------- MH_naming ----------
    mh_naming = MH_naming(
        cfg,
        results_dir,
        models[0],
        models[1],
    )

    # ---------- train ----------
    for itr in tqdm(range(itr_start, cfg.train.train_iteration_MH)):
        mh_naming.train(itr)

@hydra.main(config_path="config", config_name="config")
def main(_cfg_raw: DictConfig) -> None:
    _cfg = copy.deepcopy(_cfg_raw)
    run(_cfg)

if __name__ == "__main__":
    main()