#!/usr/bin/env python


from shutil import copyfile
import os
if not os.path.exists('variants'):
    os.mkdir('variants')

scales = ((1,1), (2,1), (0.5,1), (1,2), (1,0.5), (2,2), (0.5,0.5) )

def valErr(cnt, err1, err2 = -999):
    if err2 == -999:
        return [cnt, cnt+err1, cnt-err1]
    else:
        return [cnt, cnt+err1, cnt+err2]


pars['mCh']  =  [1.47, 1.53, 1.41]
pars['mBt'] =  [4.5, 4.75, 4.25]
pars['fS'] = [ 0.4, 0.5, 0.3]
pars['mu']      =  [(1,1), (2,1), (0.5,1), (1,2), (1,0.5), (2,2), (0.5,0.5) ] #7 point variation
pars['Q0']      =  [1.9, 2.2, 1.6]
pars['q2MinData'] = [3.5, 5.0, 2.5]
        
variations = ("mu", "mCh", "mBt", "fS", "q2MinData")

def nVars():
    nv = 0;
    for v in variations:
        nv += len(pars[v]) - 1
    return nv+1


def getSh(v):
    iv = 0
    for v in variations:
        nv += len(pars[v]) - 1

v = 0
for vName in variations:
    for 
    for fTag in ("steering", "minuit.in", "ewparam"):
        for v in range(nVars()):
            dirName = 'variants/v'+str(v)
            if not os.path.exists(dirName):
                os.mkdir(dirName)

            fName = 'variants/v'+str(v) + '/' + fTag + '.txt'

            fin = open(fTag + '.super', "rt")

            print fName
            with open(fName, "wt") as fout:

                for line in fin:


                    for 

                    #scale variations unc., 7 points
                    vs = v
                    if v >= 7:
                        vs = 0
                    
                    line = line.replace('$muR', str(scales[vs][0]))
                    line = line.replace('$muF', str(scales[vs][1]))

                    #Starting scale of evolution




                    #DIS Q2 cut unc
                    if v == 7:
                        line = line.replace('$q2MinData', str(5.0))
                    elif v == 8:
                        line = line.replace('$q2MinData', str(2.5))
                    else:
                        line = line.replace('$q2MinData', str(3.5))


                    #charm mass
                    if v == 9:
                        line = line.replace('$mCh', str(1.53))
                    elif v == 10:
                        line = line.replace('$mCh', str(1.41))
                    else:
                        line = line.replace('$mCh', str(1.47))

                    #bottom mass
                    if v == 11:
                        line = line.replace('$mBt', str(4.75))
                    elif v == 12:
                        line = line.replace('$mBt', str(4.25))
                    else:
                        line = line.replace('$mBt', str(4.5))

                    #fS variation
                    if v == 13:
                        line = line.replace('$fS', str(0.5))
                    elif v == 14:
                        line = line.replace('$fS', str(0.3))
                    else:
                        line = line.replace('$fS', str(0.4))




                    fout.write(line)


