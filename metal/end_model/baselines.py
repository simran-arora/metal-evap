import torch.nn as nn

from metal.end_model import EndModel
from metal.end_model.em_defaults import em_default_config
from metal.utils import recursive_merge_dicts

class LogisticRegression(EndModel):
    """A logistic regression classifier for a binary single-task problem"""
    def __init__(self, input_dim, **kwargs):
        overrides = {
            'batchnorm': False,
            'dropout': 0.0,
            'layer_out_dims': [input_dim],
        }
        kwargs = recursive_merge_dicts(kwargs, overrides, misses='insert',
            verbose=False)
        super().__init__(k=2, **kwargs)

class SoftmaxRegression(EndModel):
    """A softmax regression classifier for a multi-class single-task problem"""
    def __init__(self, input_dim, output_dim, **kwargs):
        overrides = {
            'batchnorm': False,
            'dropout': 0.0,
            'layer_out_dims': [input_dim],
        }
        kwargs = recursive_merge_dicts(kwargs, overrides, misses='insert', 
            verbose=False)
        super().__init__(k=output_dim, **kwargs)