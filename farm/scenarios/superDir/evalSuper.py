#!/usr/bin/env python


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("superDir", help="input super-steering directory")
args = parser.parse_args()

orders   = ['nll', 'nnlo']

dataSets = ['ak4', 'ak7', 'hera']

asType = ['as118', 'asFit']

def makeDir(d):
    import os
    if not os.path.exists(d):
        os.mkdir(d)

makeDir(args.superDir +'/variants')

for Ord in orders:
    for data in dataSets:
        for asT in asType:
            if data == 'ak7' and Ord == 'nll':
                continue
            if data == 'ak4' and Ord == 'nnlo':
                continue

            dName = Ord+'_'+data+'_'+asT

            makeDir(args.superDir +'/variants/' + dName)

            from shutil import copyfile
            copyfile(args.superDir+'/ewparam.super', args.superDir +'/variants/' + dName + '/ewparam.str')
            copyfile(args.superDir+'/minuit.in.super', args.superDir +'/variants/' + dName + '/minuit.in.str')

            with open(args.superDir + '/steering.super', "rt") as fin:
                with open(args.superDir + '/variants/'+dName + '/steering.str', "wt") as fout:
                    #print fName
                    for line in fin:
                        #Data replacement
                        if 'ak' in data:
                            line = line.replace('$nFiles', '11')
                            line = line.replace('$nCorr', '4')
                            for y in range(4):
                                line = line.replace('$jetY'+str(y), '      ')

                            if data == 'ak4':
                                line = line.replace('$cone', 'ak4')
                            elif data == 'ak7':
                                line = line.replace('$cone', 'ak7')
                        elif data == 'hera':
                            line = line.replace('$nFiles', '7')
                            line = line.replace('$nFilesCorr', '0')
                            for y in range(4):
                                line = line.replace('$jetY'+str(y), '      ')

                        #Order replacement
                        if 'nnlo' == Ord:
                            line = line.replace('$order', 'nnlo')
                            line = line.replace('$ORDER', 'NNLO')
                        elif 'nll' == Ord:
                            line = line.replace('$order', 'nll')
                            line = line.replace('$ORDER', 'NLO')
                        
                        #Type replacement
                        if 'as118' == asT:
                            line = line.replace('$asType', '0.000')
                        elif 'asFit' == asT:
                            line = line.replace('$asType', '0.001')

                        fout.write(line)

            import subprocess
            #Extend the steerings
            subprocess.call('python ../evalSingle.py '+  args.superDir +'/variants/' + dName  , shell=True)
