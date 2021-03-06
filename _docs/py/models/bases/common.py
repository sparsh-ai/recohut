# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/models/bases/models.bases.common.ipynb (unless otherwise specified).

__all__ = ['PointModel']

# Cell
from typing import Any, Iterable, List, Optional, Tuple, Union, Callable

import torch
from torch import nn

from pytorch_lightning import LightningModule

from ...evaluation.metrics import get_eval_metrics

import warnings
warnings.filterwarnings('ignore')

# Cell
class PointModel(LightningModule):
    def __init__(self, n_neg=4, k=10, loss_type='CL', optim_type='adamw', lr=0.005):
        """
        Args:
            n_neg: number of negative samples
            k: top-k recommendations
            loss_type: CL/SL
            optim_type: adam/adamw/sgd
            lr: learning rate
        """
        super().__init__()
        self.n_neg = n_neg
        self.k = k
        self.loss_type = loss_type
        self.optim_type = optim_type
        self.lr = lr

    def forward(self, users, items):
        raise NotImplementedError

    def training_step(self, batch, batch_idx):
        pos, score = batch
        users, pos_items = pos[:, 0], pos[:, 1]

        # negative sampling
        neg_items = torch.multinomial(score, self.n_neg)
        items = torch.cat((pos_items.view(-1, 1), neg_items), dim=1)

        labels = torch.zeros(items.shape)
        labels[:, 0] += 1
        users = users.view(-1, 1).repeat(1, items.shape[1])

        users = users.view(-1, 1).squeeze()
        items = items.view(-1, 1).squeeze()
        labels = labels.view(-1, 1).squeeze()

        logits = self(users, items)
        loss = self.loss_fn(logits, labels)

        return {
            "loss": loss,
            "logits": logits.detach(),
        }

    def training_epoch_end(self, outputs):
        # This function recevies as parameters the output from "training_step()"
        # Outputs is a list which contains a dictionary like:
        # [{'pred':x,'target':x,'loss':x}, {'pred':x,'target':x,'loss':x}, ...]
        pass

    def validation_step(self, batch, batch_idx):
        pos, items, labels = batch
        n_items = items.shape[1]
        users = pos[:, 0].view(-1, 1).repeat(1, n_items)

        users = users.view(-1, 1).squeeze()
        items = items.view(-1, 1).squeeze()
        labels = labels.view(-1, 1).squeeze()

        logits = self(users, items)
        loss = self.loss_fn(logits, labels)

        items = items.view(-1, n_items)
        logits = logits.view(-1, n_items)
        item_true = pos[:, 1].view(-1, 1)
        item_scores = [dict(zip(item.tolist(), score.tolist())) for item, score in zip(items, logits)]
        ncdg, apak, hr = get_eval_metrics(item_scores, item_true, self.k)
        metrics = {
            'loss': loss.item(),
            'ncdg': ncdg,
            'apak': apak,
            'hr': hr,
        }
        self.log("Val Metrics", metrics, prog_bar=True)

        return {
            "loss": loss.item(),
            "logits": logits,
        }

    def validation_epoch_end(self, outputs):
        pass

    def test_step(self, batch, batch_idx):
        pos, items, labels = batch
        n_items = items.shape[1]
        users = pos[:, 0].view(-1, 1).repeat(1, n_items)

        users = users.view(-1, 1).squeeze()
        items = items.view(-1, 1).squeeze()
        labels = labels.view(-1, 1).squeeze()

        logits = self(users, items)
        loss = self.loss_fn(logits, labels)

        items = items.view(-1, n_items)
        logits = logits.view(-1, n_items)
        item_true = pos[:, 1].view(-1, 1)
        item_scores = [dict(zip(item.tolist(), score.tolist())) for item, score in zip(items, logits)]
        ncdg, apak, hr = get_eval_metrics(item_scores, item_true, self.k)
        metrics = {
            'loss': loss.item(),
            'ncdg': ncdg,
            'apak': apak,
            'hr': hr,
        }
        self.log("Test Metrics", metrics, prog_bar=True)

        return {
            "loss": loss.item(),
            "logits": logits,
        }

    def test_epoch_end(self, outputs):
        pass

    def configure_optimizers(self):
        if self.optim_type == 'adamw':
            return torch.optim.AdamW(self.parameters(), lr=self.lr)
        elif self.optim_type == 'adam':
            return torch.optim.Adam(self.parameters(), lr=self.lr)
        elif self.optim_type == 'sgd':
            return torch.optim.SGD(self.parameters(), lr=self.lr)
        else:
            raise ValueError(f'Invalid optimizer type: {self.optim_type}')

        # optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
        # scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        #     optimizer, patience=10, factor=0.1
        # )
        # return {
        #     "optimizer": optimizer,
        #     "lr_scheduler": scheduler,
        #     "monitor": "valid_loss",
        # }

    def loss_fn(self, logits, labels):
        if self.loss_type == 'CL':
            return nn.BCEWithLogitsLoss(reduction='sum')(logits, labels)
        elif self.loss_type == 'SL':
            return nn.MSELoss(reduction='sum')(logits, labels)
        else:
            raise ValueError(f'Invalid loss type: {self.loss_type}')