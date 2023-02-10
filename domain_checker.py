# importing modules
import whois
import sys
 
# # reading form a file

# f = open('input.txt', 'r+')
# fnames = f.readlines()

# Use exception handle program
# and get information from whois
def check_domain(i):
    try:
        domain = whois.whois(i)
        if domain.domain_name == None:
            sys.exit(1)
        
    except :
        return "available"
    else:
        return "taken"

# for i in fnames:
#     check_domain(i)
