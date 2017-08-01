import sys, os
import pyperclip
import pickle

try:
    tidbits = pickle.load(open('tidbits.p', 'rw'))
except:
    tidbits = {}

if __name__ == '__main__':
    #print all keys
    if len(sys.argv) == 1:
        keys = tidbits.keys()
        print sorted(keys, key=lambda x: x.lower())

    #delete keypair
    elif sys.argv[1] == 'del':
        del tidbits[sys.argv[2]]

    else:
        keyword = sys.argv[1]
        if len(sys.argv) == 2:
            #entry exists?
            if keyword in tidbits:
                pyperclip.copy(tidbits[keyword])
                print tidbits[keyword]
            #adding new entry
            else:
                val = raw_input('Add entry: ')
                if len(val) > 0:
                    tidbits[keyword] = val
        #adding entry
        if len(sys.argv) == 3:
            val = sys.argv[2]
            if len(val) > 0:
                val = sys.argv[2]
                tidbits[keyword] = val

pickle.dump(tidbits, open('tidbits.p', 'wb'))
