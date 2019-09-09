export LD_LIBRARY_PATH_STORED=$LD_LIBRARY_PATH

#f=yScanAs
#f=modelUncHERA
for f in modelUncHighQ  modelUncHighQHERA
#for f in modelUncAsHighQ
do
    nF=`ls -d -1 $f/variants/v*/   | wc -l`
    echo $nF
    mkdir -p $f/logs
    #exit
    condor_submit  -batch-name `basename $f` dirName=$f nFiles=$nF  xfitter.submit
done
