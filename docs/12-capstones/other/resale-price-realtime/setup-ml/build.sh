#! /bin/sh
python train_model.py
bentoml delete ford_price_predictor:1.0.0
bentoml build --version 1.0.0
bentoml containerize ford_price_predictor:1.0.0
