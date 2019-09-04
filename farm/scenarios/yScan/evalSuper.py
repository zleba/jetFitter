#!/usr/bin/env python


#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("super_steering", help="input super-steering file")
#args = parser.parse_args()

from shutil import copyfile
import os
if not os.path.exists('variants'):
    os.mkdir('variants')


for y in range(4):
    dirName = 'variants/y'+str(y)
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    fName = 'variants/y'+str(y) + '/steering.txt'

    fin = open('steering.super', "rt")

    print fName
    with open(fName, "wt") as fout:

        for line in fin:

            for ynow in range(4):
                if ynow == y:
                    line = line.replace('$y'+str(ynow), ' ')
                else:
                    line = line.replace('$y'+str(ynow), '!')
            
            line = line.replace('$nFiles', str(7 + 1))
            line = line.replace('$nCorrs', str(1))


            fout.write(line)


    copyfile('minuit.in.super', 'variants/y'+str(y)+'/minuit.in.txt')
    copyfile('../../ewparam.txt', 'variants/y'+str(y)+'/ewparam.txt')

    #if not os.path.exists(dirName+'/logs'):
    #    os.mkdir(dirName+'/logs')
