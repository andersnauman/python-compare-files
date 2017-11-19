#!/usr/bin/env python
""" Compare files in two folder with their sha1 checksum """
import sys
from hashlib import sha1
from os import walk, path

BUFSIZE = 65536

class CompareFiles(object):
    """ Main class """
    def __init__(self):
        print("Comparing files in folder; {0} {1}".format(sys.argv[1], sys.argv[2]))

    def checksum(self, filepath):
        """ Generic sha1 checksum method. Takes an filepath argument and returns the hexdigit sha1-hash """
        sha1hash = sha1()
        with open(filepath, 'rb') as f:
            while True:
                data = f.read(BUFSIZE)
                if not data:
                    break
                sha1hash.update(data)
        return sha1hash.hexdigest()

    def main(self):
        """ Main method """
        for (dirpath, _, filenames) in walk(sys.argv[1]):
            for filename in filenames:
                print("[!] Comparing: {0}".format(filename))

                filepath = dirpath + '/' + filename
                checksum = self.checksum(filepath)
                print("Hash: {0}\t\tFilename: {1}".format(checksum, filepath))
                filepath = filepath.replace(sys.argv[1].strip('/'), sys.argv[2].strip('/'))
                if path.isfile(filepath):
                    checksum = self.checksum(filepath)
                else:
                    checksum = "Do not exist                            " # space = adjust the size so the tabs match up
                print("Hash: {0}\t\tFilename: {1}\n".format(checksum, filepath))

if __name__ == '__main__':
    CompareFiles().main()
