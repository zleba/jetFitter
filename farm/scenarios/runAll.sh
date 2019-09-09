export LD_LIBRARY_PATH_STORED=$LD_LIBRARY_PATH

#f=yScanAs
f=modelUncEng
nF=`ls -d -1 $f/variants/v*/   | wc -l`
echo $nF
mkdir -p $f/logs
#exit
condor_submit  -batch-name `basename $f` dirName=$f nFiles=$nF  xfitter.submit
