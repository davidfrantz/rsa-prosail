#!/usr/bin/env python3

## Create Lookup Table (LUT) with ProSAIL
# using 6 free parameters, randomly distributed
# parameters = [N,Cab,Cbrown,Cw,Cm,LAI]
def createLUT():
    import numpy as np
    import prosail
    import argparse

    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameterFile", help="Path to the parameters filename", default= "/data/eocps011/courses/rsa/rsalead/buddenba/prosail/para_n1.txt")
    parser.add_argument("--LUTFile", help="Path to the LUT filename", default= "/data/eocps011/courses/rsa/rsalead/buddenba/prosail/lut.txt")
    args = parser.parse_args()

    # Load prepared parameterFile
    p = np.loadtxt(args.parameterFile)

    # Set fixed parameters
    LUT = np.zeros((len(p), 2101))
    lidfa = 45.
    hspot = 0.
    tts = 55.
    tto = 0.
    psi = 0.

    # Calculate LUT
    rng = range(len(p))
    for x in rng:
        LUT[x,:] = prosail.run_prosail(p[x,0], p[x,1], p[x,1]/4, p[x,2], p[x,3], p[x,4], p[x,5], lidfa, hspot, tts, tto, psi, rsoil=1., psoil=0.5)

    # Save LUT with full spectral resolution
    np.savetxt(args.LUTFile, LUT*10000)

    print("Saved full spectral resolution LUT File to " + args.LUTFile)

if __name__ == "__main__":
    createLUT()