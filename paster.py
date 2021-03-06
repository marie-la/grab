import sys, os
import pyperclip
import pickle

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    tidbits = pickle.load(open(dir_path+'/tidbits.p', 'rw'))
except:
    tidbits = {}
    open(dir_path+'/tidbits.p', 'wb')

if __name__ == '__main__':
    #print all keys
    if len(sys.argv) == 1:
        keys = tidbits.keys()
        print sorted(keys, key=lambda x: x.lower())

    #delete keypair
    elif sys.argv[1] == 'del':
        keyword = sys.argv[2]
        if keyword in tidbits:
            del tidbits[sys.argv[2]]
        else:
            print "No value to remove"

    elif sys.argv[1] == 'backup':
        f = open(dir_path + '/backup.p', 'wb')
        pickle.dump(tidbits, f)
        print 'Backed up to ' + dir_path

    elif sys.argv[1] == 'restore':
        try:
            tidbits = pickle.load(open(dir_path+'/backup.p', 'rw'))
        except:
            print 'No backup! Use \'grab backup\' to backup keypair file first.'
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

pickle.dump(tidbits, open(dir_path+'/tidbits.p', 'w'))
