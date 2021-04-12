from time import sleep
import sys
import subprocess
import argparse as ap
import os

try:
    import whois

    print("whois module is installed, proceeding with the execution")
except ModuleNotFoundError:
    print("whois module is not installed, installing the module")
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'whois'])
    import whois

if __name__ == '__main__':
    required = {'whois'}
    installed = {}
    args_ = ap.ArgumentParser()
    args_.add_argument("--input", default="./inputfile",
                       help="[INPUT]: Enter the inputfilename where the domain names are stored")
    args_.add_argument("--timer", default=3,
                       help="[INPUT]: Enter the desired delay between each query [default::3] in seconds")
    args_.add_argument("--outfile", default="./out.csv",
                       help="[INPUT]: Enter the desired output file name [default::out.csv]")
    args = args_.parse_args()
    if os.path.getsize(args.input) <=0:
        print("Empty file specified, exiting this run")
        sys.exit(-1)
    with open(args.input, "r") as F, open(args.outfile, "w") as O:
        lines = F.readlines()
        #Writing headers for the csv
        O.writelines("Domain,ExpiryDate\n")
        for i in lines:
            print("probing {}".format(i[:-1]))
            expiry = whois.query(i).expiration_date
            print("Found Expiry date: {}".format(expiry))
            O.writelines("{},{}\n".format(i[:-1], expiry))
            sleep(int(args.timer))

    print("Output written to {}".format(args.outfile))
    print("Note: If you don't intend to use whois module anymore, please run \"pip uninstall -y whois\"")
