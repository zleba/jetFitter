source /cvmfs/sft.cern.ch/lcg/views/LCG_94/x86_64-slc6-gcc7-opt/setup.sh
export LHAPDF_DATA_PATH=/cvmfs/sft.cern.ch/lcg/external/lhapdfsets/current/:`lhapdf-config --datadir`

export PATH=$PWD/qcdnum/bin:$PATH
export PATH=$PWD/xfitterBuild/bin:$PATH
