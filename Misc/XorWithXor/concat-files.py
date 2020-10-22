import shutil
import time, glob, os

outfilename = 'all_' + str((int(time.time()))) + ".txt"

filenames = sorted(glob.glob('*.dat'), key=os.path.getmtime)

with open(outfilename, 'wb') as outfile:
    for i in range(1000):
        with open(f'{i}.dat', 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)