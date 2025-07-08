#!/usr/bin/env python3
def createRandomParameters():
    import numpy as np
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--parameterFile", help="Path to the parameters filename", default= "/data/eocps011/courses/rsa/rsalead/buddenba/prosail/para_n1.txt")
    parser.add_argument("--LUTsize", help="Size of the Lookup Table", default= "10000")
    #parser.add_argument("--mins", help="Minimum values of N, Cab, Cbrown, Cw, Cm, LAI", default="[0.8, 10, 0, 0.001, 0.001, 0.5]")
    #parser.add_argument("--maxs", help="Maximum values of N, Cab, Cbrown, Cw, Cm, LAI", default= "[2.5, 80, 1, 0.04, 0.03, 8]")
    parser.add_argument("--minN", help="Minimum values of N", default="0.8")
    parser.add_argument("--maxN", help="Maximum values of N", default= "3.0")
    parser.add_argument("--minCab", help="Minimum values of Cab", default="10")
    parser.add_argument("--maxCab", help="Maximum values of Cab", default= "80")
    parser.add_argument("--minCbrown", help="Minimum values of Cbrown", default="0")
    parser.add_argument("--maxCbrown", help="Maximum values of Cbrown", default= "1")
    parser.add_argument("--minCw", help="Minimum values of Cw", default="0.002")
    parser.add_argument("--maxCw", help="Maximum values of Cw", default= "0.05")
    parser.add_argument("--minCm", help="Minimum values of Cm", default="0.001")
    parser.add_argument("--maxCm", help="Maximum values of Cm", default= "0.02")
    parser.add_argument("--minLAI", help="Minimum values of LAI", default="0.5")
    parser.add_argument("--maxLAI", help="Maximum values of LAI", default= "8")
    args = parser.parse_args()

    LUTsize   = int(args.LUTsize)
    parameterFile = args.parameterFile
    mins      = np.zeros(6)
    maxs      = np.zeros(6)
    mins[0]   = args.minN
    maxs[0]   = args.maxN
    mins[1]   = args.minCab
    maxs[1]   = args.maxCab
    mins[2]   = args.minCbrown
    maxs[2]   = args.maxCbrown
    mins[3]   = args.minCw
    maxs[3]   = args.maxCw
    mins[4]   = args.minCm
    maxs[4]   = args.maxCm
    mins[5]   = args.minLAI
    maxs[5]   = args.maxLAI

    p = np.zeros((LUTsize, len(mins)))
    for x in range(len(maxs)):
        p[:,x] = mins[x] + (maxs[x]-mins[x]) * np.random.random(LUTsize)
    
    np.savetxt(parameterFile, p)

    print("Saved Parameters File to " + parameterFile)

if __name__ == "__main__":
    createRandomParameters()