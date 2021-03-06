# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/datasets/datasets.lastfm.ipynb (unless otherwise specified).

__all__ = ['LastfmDataset']

# Cell
import os
import os.path as osp
import numpy as np
import pandas as pd
from pandas import Timedelta

from .bases.session import SessionDatasetv3
from ..utils.common_utils import download_url, extract_tar

# Cell
class LastfmDataset(SessionDatasetv3):
    url = 'http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-1K.tar.gz'

    def __init__(self, root, interval=Timedelta(hours=8), n=40000):
        use_cols = [0, 1, 2]
        super().__init__(root, use_cols, interval, n)

    @property
    def raw_file_names(self) -> str:
        return 'userid-timestamp-artid-artname-traid-traname.tsv'

    def download(self):
        path = download_url(self.url, self.raw_dir)
        extract_tar(path, self.raw_dir)
        from shutil import move, rmtree
        move(osp.join(self.raw_dir, 'lastfm-dataset-1K', 'userid-timestamp-artid-artname-traid-traname.tsv'),
                osp.join(self.raw_dir, 'userid-timestamp-artid-artname-traid-traname.tsv'))
        rmtree(osp.join(self.raw_dir, 'lastfm-dataset-1K'))
        os.unlink(path)