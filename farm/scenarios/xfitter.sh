#!/usr/bin/env bash
#cd /nfs/dust/cms/user/zlebcr/xFitting

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH_STORED
cd /nfs/dust/cms/user/zlebcr/xFitting/farm/scenarios/yScan/variants/y$1
ln -s /nfs/dust/cms/user/zlebcr/xFitting/farm/datafiles
xfitter
