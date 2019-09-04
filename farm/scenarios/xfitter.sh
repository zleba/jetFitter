#!/usr/bin/env bash
cd /nfs/dust/cms/user/zlebcr/xFitting
source setup.sh
cd /nfs/dust/cms/user/zlebcr/xFitting/farm/scenarios/yScan/variants/y$1
ln -s /nfs/dust/cms/user/zlebcr/xFitting/xfitter-2.0.1/datafiles
xfitter
