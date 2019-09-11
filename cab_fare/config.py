# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:34:22 2019

@author: PAT
"""

from pathlib import Path

data_dir = Path('C:/Users/PAT/Documents/edwisor/projects/cab_fare/data/raw')
test_data_path = data_dir  / 'test.csv'
train_data_path = data_dir  / 'train.csv'
processed_data_path = data_dir / '../processed/processed.csv'
submitted_data_path = data_dir / '../submitted/submission.csv'
