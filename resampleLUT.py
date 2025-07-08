#!/usr/bin/env python3
## resample_simulation

def resampleLUT():
    import numpy as np
    import argparse

    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--LUTFile", help="Path to the LUT filename", default= "/data/eocps011/courses/rsa/rsalead/buddenba/prosail/lut.txt")
    parser.add_argument("--SRFFile", help="Path to the Spectral Response Functions filename", default= "/data/eocps011/courses/rsa/rsalead/buddenba/prosail/S2-SRF.txt")
    parser.add_argument("--resLUTFile", help="Path to the resampled LUT filename (output)", default= "/data/eocps011/courses/rsa/rsalead/buddenba/prosail/res_lut.txt")
    args = parser.parse_args()

    # Load full res LUT and SRF
    LUT = np.loadtxt(args.LUTFile)
    SRF = np.loadtxt(args.SRFFile, delimiter="\t")

    # Resample through matrix multiplication
    resLUT = np.matmul(LUT,SRF)

    # Save resampled LUT with 10 spectral bands
    np.savetxt(args.resLUTFile, resLUT)

    print("Saved  resampled LUT with 10 spectral bands to " + args.resLUTFile)

if __name__ == "__main__":
    resampleLUT()