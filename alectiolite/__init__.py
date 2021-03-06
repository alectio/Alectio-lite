from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
import random
import logging
import alectiolite
from .init import init_experiment_, extract_config_
from .curate.classification import UniClassification as curate_classification
from .logger.logger import experiment_logger,complete_loop

__all__ = [
    "backend",
    "curate",
    "proto",
    "callbacks" "init_experiment_",
    "UniClassification",
    "experiment_logger",
    "complete_loop"
]


init = alectiolite.init_experiment_
experiment_config = alectiolite.extract_config_
curate_classification = alectiolite.curate_classification
alectio_logger = alectiolite.experiment_logger
complete_loop = alectiolite.complete_loop
