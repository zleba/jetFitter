#!/usr/bin/env python


import os
if not os.path.exists('variants'):
    os.mkdir('variants')

pars = {}
pars['Q02']      =  [1.9, 2.15, 1.6]
pars['mCh']  =  [1.47, 1.53, 1.41]
pars['mBt'] =  [4.5, 4.75, 4.25]
pars['fS'] = [ 0.4, 0.5, 0.3]
pars['q2MinData'] = [3.5, 5.0, 2.5]
pars['Dg']  =  ['**', '  ']
pars['Ddv'] =  ['**', '  ']
pars['mu']      =  [(1,1), (2,1), (0.5,1), (1,2), (1,0.5), (2,2), (0.5,0.5) ] #7 point variation
        
variations = ('Q02', 'mCh', 'mBt', 'fS', 'q2MinData', 'Dg', 'Ddv', 'mu')

v = 0
for vName in variations:
    s = 0 if v == 0 else 1
    for val in pars[vName][s:]:

        dirName = 'variants/v'+str(v)
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        if os.path.exists(dirName+'/datafiles'):
            os.unlink(dirName+'/datafiles')
        os.symlink('../../../../datafiles', dirName+'/datafiles')

        for fTag in ("steering", "minuit.in", "ewparam"):

            fName = 'variants/v'+str(v) + '/' + fTag + '.txt'
            fin = open(fTag + '.super', "rt")

            print fName
            with open(fName, "wt") as fout:

                for line in fin:
                    for vNow in variations:
                        if vNow == 'mu': #for scale variations
                            if vNow == vName:
                                line = line.replace('@'+vNow+'R', str(val[0]))
                                line = line.replace('@'+vNow+'F', str(val[1]))
                            else:
                                line = line.replace('@'+vNow+'R', str(pars[vNow][0][0]))
                                line = line.replace('@'+vNow+'F', str(pars[vNow][0][1]))
                            continue
                        #if vNow == 'Dg'

                        if vNow == vName:
                            line = line.replace('@'+vNow, str(val))
                        else: #replace by central value
                            line = line.replace('@'+vNow, str(pars[vNow][0])) 
                        if line[0:2] == '**':
                            line = ''


                    fout.write(line)
        v += 1

