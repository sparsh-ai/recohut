# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/datasets/bases/datasets.bases.common.ipynb (unless otherwise specified).

__all__ = []

# Cell
from typing import List, Optional, Callable, Union, Any, Tuple

import numpy as np
import pandas as pd
from tqdm import tqdm
tqdm.pandas()

from abc import *
from pathlib import Path
import os
import os.path as osp
from collections.abc import Sequence
import sys
import tempfile
import shutil
import pickle
import time
import csv
import math
import operator
import itertools
from collections import defaultdict
import datetime
from datetime import date, timezone, timedelta
from pandas import Timedelta

import torch

from ...utils.common_utils import download_url, extract_zip, extract_gz, makedirs

# Internal Cell
def to_list(value: Any) -> Sequence:
    if isinstance(value, Sequence) and not isinstance(value, str):
        return value
    else:
        return [value]

def files_exist(files: List[str]) -> bool:
    # NOTE: We return `False` in case `files` is empty, leading to a
    # re-processing of files on every instantiation.
    return len(files) != 0 and all([osp.exists(f) for f in files])

# Internal Cell
class Dataset:
    """Dataset base class
    """
    @property
    def raw_file_names(self) -> Union[str, List[str], Tuple]:
        r"""The name of the files in the :obj:`self.raw_dir` folder that must
        be present in order to skip downloading."""
        raise NotImplementedError

    @property
    def processed_file_names(self) -> Union[str, List[str], Tuple]:
        r"""The name of the files in the :obj:`self.processed_dir` folder that
        must be present in order to skip processing."""
        raise NotImplementedError

    def download(self):
        r"""Downloads the dataset to the :obj:`self.raw_dir` folder."""
        raise NotImplementedError

    def process(self):
        r"""Processes the dataset to the :obj:`self.processed_dir` folder."""
        raise NotImplementedError

    def __init__(self, root=None):
        self.root = root

        if 'download' in self.__class__.__dict__:
            self._download()

        # if 'process' in self.__class__.__dict__:
        #     self._process()

    @property
    def raw_dir(self) -> str:
        return osp.join(self.root, 'raw')

    @property
    def processed_dir(self) -> str:
        return osp.join(self.root, 'processed')

    @property
    def raw_paths(self) -> List[str]:
        r"""The absolute filepaths that must be present in order to skip
        downloading."""
        files = to_list(self.raw_file_names)
        return [osp.join(self.raw_dir, f) for f in files]

    @property
    def processed_paths(self) -> List[str]:
        r"""The absolute filepaths that must be present in order to skip
        processing."""
        files = to_list(self.processed_file_names)
        return [osp.join(self.processed_dir, f) for f in files]

    def _download(self):
        if files_exist(self.raw_paths):  # pragma: no cover
            return

        makedirs(self.raw_dir)
        self.download()

    def _process(self):
        if files_exist(self.processed_paths):  # pragma: no cover
            return

        print('Processing...', file=sys.stderr)

        makedirs(self.processed_dir)
        self.process()

        print('Done!', file=sys.stderr)

    def __repr__(self) -> str:
        arg_repr = str(len(self)) if len(self) > 1 else ''
        return f'{self.__class__.__name__}({arg_repr})'