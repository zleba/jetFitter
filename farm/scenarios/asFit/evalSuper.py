#!/usr/bin/env python


#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("super_steering", help="input super-steering file")
#args = parser.parse_args()

from shutil import copyfile
import os
if not os.path.exists('variants'):
    os.mkdir('variants')

scales = ((1,1), (2,1), (0.5,1), (1,2), (1,0.5), (2,2), (0.5,0.5) )

for s in range(7):
    dirName = 'variants/v'+str(s)
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    fName = 'variants/v'+str(s) + '/steering.txt'

    fin = open('steering.super', "rt")

    print fName
    with open(fName, "wt") as fout:

        for line in fin:

            line = line.replace('$muR', str(scales[s][0]))
            line = line.replace('$muF', str(scales[s][1]))

            fout.write(line)


    copyfile('minuit.in.super', 'variants/v'+str(s)+'/minuit.in.txt')
    copyfile('../../ewparam.txt', 'variants/v'+str(s)+'/ewparam.txt')

    #if not os.path.exists(dirName+'/logs'):
    #    os.mkdir(dirName+'/logs')
