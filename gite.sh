#!/bin/bash
cd dist
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
git lfs track "*.csv"
git add train.csv
git add test.csv
cd ../
