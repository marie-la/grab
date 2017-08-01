import sys
import pyperclip
import os


fname = 'tidbits.txt'
dir_path = os.path.dirname(os.path.realpath(__file__))
fpath = os.path.join(dir_path+'/', fname)
tidbits = {}

#looks like I could have used pickle, but this works and is human readable.
with open(fpath, 'rw') as f:
    content = f.readlines()

for line in content:
    x = line.split(', ', 1)
    if len(x) == 2:
        tidbits[x[0]] = x[1][:-1] #removes \0 at end

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print tidbits.keys()
    if len(sys.argv) == 2:
        if sys.argv[1] in tidbits:
            pyperclip.copy(tidbits[sys.argv[1]])
            print tidbits[sys.argv[1]]
        else:
            val = raw_input('Add entry: ')
            if len(val) > 0:
                with open(fpath, "a") as myfile:
                    myfile.write(str(sys.argv[1])+", "+str(val)+"\n")
                myfile.close()
    if len(sys.argv) == 3:
        val = sys.argv[2]
        if len(val) > 0:
            with open(fpath, "a") as myfile:
                myfile.write(str(sys.argv[1])+", "+str(val)+"\n")
            myfile.close()
