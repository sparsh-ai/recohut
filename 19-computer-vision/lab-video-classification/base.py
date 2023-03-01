from typing import List, Optional, Callable, Union, Any, Tuple

import os
import sys

import warnings
warnings.filterwarnings('ignore')

from utils import *


class Recommendation:
    """
    Base recommendation class
    """

    def __init__(self, root_path=None, load=True):
        self.root_path = root_path
        self.init_raw_paths()
        self.init_processed_paths()
        self._download()
        self._process()
        if load:
            self.load()


    @property
    def raw_file_names(self) -> Union[str, List[str], Tuple]:
        """The name of the files in the raw_path folder that must
        be present in order to skip downloading."""
        return ['carts.csv.gz', 'products.csv.gz', 'adventures.csv.gz', 'sights.csv.gz']


    @property
    def processed_file_names(self) -> Union[str, List[str], Tuple]:
        """The name of the files in the processed_path folder that
        must be present in order to skip training."""
        raise NotImplementedError


    @property
    def raw_dir(self) -> str:
        return os.path.join(self.root_path, 'raw')


    @property
    def processed_dir(self) -> str:
        return os.path.join(self.root_path, 'processed')


    @property
    def raw_paths(self) -> List[str]:
        """The absolute filepaths that must be present in order to skip
        downloading."""
        files = to_list(self.raw_file_names)
        return [os.path.join(self.raw_dir, f) for f in files]


    @property
    def processed_paths(self) -> List[str]:
        r"""The absolute filepaths that must be present in order to skip
        processing."""
        files = to_list(self.processed_file_names)
        return [os.path.join(self.processed_dir, f) for f in files]


    def _download(self):
        if files_exist(self.raw_paths):
            return

        makedirs(self.raw_dir)
        self.download()


    def _process(self):
        if files_exist(self.processed_paths):
            return

        print('Processing...', file=sys.stderr)

        makedirs(self.processed_dir)
        self.process()

        print('Done!', file=sys.stderr)


    def __repr__(self) -> str:
        arg_repr = str(len(self)) if len(self) > 1 else ''
        return f'{self.__class__.__name__}({arg_repr})'


    def init_raw_paths(self):
        """
        initiate the file paths for raw data
        """
        self.raw_path_carts = os.path.join(self.raw_dir, 'carts.csv.gz')
        self.raw_path_products = os.path.join(self.raw_dir, 'products.csv.gz')
        self.raw_path_adventures = os.path.join(self.raw_dir, 'adventures.csv.gz')
        self.raw_path_sights = os.path.join(self.raw_dir, 'sights.csv.gz')
        self.raw_path_occassions = os.path.join(self.raw_dir, 'occassions.csv.gz')

        self.raw_path_trip_personas = os.path.join(self.raw_dir, 'trip_personas.csv.gz')
        self.raw_path_trip_persona_adventure = os.path.join(self.raw_dir, 'trip_persona_adventure.csv.gz')
        self.raw_path_trip_persona_occassion = os.path.join(self.raw_dir, 'trip_persona_occassion.csv.gz')
        self.raw_path_trip_persona_sight = os.path.join(self.raw_dir, 'trip_persona_sight.csv.gz')

        self.raw_path_trips = os.path.join(self.raw_dir, 'trips.csv.gz')
        self.raw_path_destinations = os.path.join(self.raw_dir, 'destinations.csv.gz')
        self.raw_path_trip_guests = os.path.join(self.raw_dir, 'trip_travellers.csv.gz')
        self.raw_path_product_pricing = os.path.join(self.raw_dir, 'product_pricings.csv.gz')
        self.raw_path_product_computed_pricings = os.path.join(self.raw_dir, 'product_computed_pricings.csv.gz')
        self.raw_path_budgets = os.path.join(self.raw_dir, 'budgets.csv.gz')
        self.raw_path_trip_budget = os.path.join(self.raw_dir, 'trip_budget.csv.gz')

        self.raw_path_countries = os.path.join(self.raw_dir, 'countries.csv.gz')
        self.raw_path_calendar_product = os.path.join(self.raw_dir, 'calendar_product.csv.gz')

        self.raw_path_customer_product_feedbacks = os.path.join(self.raw_dir, 'customer_product_feedbacks.csv.gz')
        self.raw_path_product_ratings = os.path.join(self.raw_dir, 'product_ratings.csv.gz')
        self.raw_path_vendor_ratings = os.path.join(self.raw_dir, 'vendor_ratings.csv.gz')

        self.raw_path_images_adventures = os.path.join(self.raw_dir, 'images', 'adventures')
        
        self.raw_path_kinetics_classnames = os.path.join(self.raw_dir, 'kinetics_classnames.json')
        
        self.raw_path_bounce_products = os.path.join(self.raw_dir, 'product_bounce_rates.csv')
        

    def init_processed_paths(self):
        """
        initiate the file paths for processed data
        """
        raise NotImplementedError


    def download(self):
        """Downloads the dataset to the raw folder."""
        pass


    def process(self):
        """
        load the raw data, process it and save into processed data folder
        """
        raise NotImplementedError


    def load(self):
        """
        load the processed data from processed data folder into memory
        """
        raise NotImplementedError


    def recommend(self, interest_subcategory_id, interest_type='adventure', topk=5):
        """
        recommend the products
        """
        raise NotImplementedError