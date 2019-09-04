export LD_LIBRARY_PATH_STORED=$LD_LIBRARY_PATH

f=yScan
condor_submit  -batch-name `basename $f` dirName=$f nFiles=4  xfitter.submit
