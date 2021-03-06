import hashlib
import optparse
import random
import string
import sys

'''
    Newer random generation function.  Takes length as an argument
    , generates a sha512() digest and returns a portion.  
    Should be good for passwords up to 240 chars long.  
'''
def sha_rand(length):
    parts = random.sample(xrange(10000000), 60)
    m = hashlib.sha512()
    m.update(''.join(["%s" % x for x in parts]))
    digest = str(m.hexdigest()) + str(m.hexdigest)
    return digest[:length]

'''
    Regular random generation function.  Takes the length as an argument
    and generates a password with letters, punctions and numbers.
    Hard to read or remember.
'''
def rand(length):
    s = string.letters
    s += string.punctuation
    s += string.digits
    return ''.join(random.choice(s) for i in range(length))

def main():
    parser = optparse.OptionParser(usage="usage: %prog [options] arg", version="%prog 1.0")
    parser.add_option("-l", dest="length", help="The length of the password to generate")

    #parse the command line arguments and see what we got
    (opts, args) = parser.parse_args();

    if opts.length is None:
        print "Please specifiy the length of the password to generate with the -l option"
        parser.print_help()
        sys.exit(-1)

    length = opts.length
    print "Your password is: " + sha_rand(int(length))


if __name__ == "__main__":
    main()
