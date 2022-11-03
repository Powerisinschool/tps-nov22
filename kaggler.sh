#!/bin/bash
mkdir ~/.kaggle
printf '{"username":"%s","key":"%s"}' $kaggle_username $kaggle_key > ~/.kaggle/kaggle.json
