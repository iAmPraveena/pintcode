# Who is data extractor
The script searches for the required module if not found installs the module and continues to use the module to fetch the expiration date of the domains. If the specified file is empty the code exits with -1 status prompting the user to specify a correct file.  There are 3 arguments required to specify the file: 1. inputfile -- File containing input domain names, 2. outfile -- File to which the csv data is to be published for later consumption. 3. timer -- Delay to be used between requests. 

```bash
python3 main.py --input=inputfile --outfile=output.csv --timer=1*
whois module is not installed, installing the module*
Collecting whois
  Using cached whois-0.9.8-py3-none-any.whl
Installing collected packages: whois
Successfully installed whois-0.9.8
probing google.com
Found Expiry date: 2028-09-14 04:00:00
probing facebook.com
Found Expiry date: 2028-03-30 04:00:00
probing linkedin.com
Found Expiry date: 2022-11-02 15:38:11
probing instagram.com
Found Expiry date: 2027-06-04 13:37:18
Output written to output.csv
Note: If you don't intend to use whois module anymore, please run "pip uninstall -y whois"
blr-mpvf1:FL psuresh$ python3 main.py --input=empty --outfile=output.csv --timer=1
whois module is installed, proceeding with the execution
Empty file specified, exiting this run *
```
