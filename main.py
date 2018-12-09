import re
import requests
import tldextract
from urllib.parse import urlparse

pattern = re.compile('https:[\/0-9a-zа-я\.\-_]+')
domain_list=list()
domains=list()
free_domains=list()
flag=True


f=open("csv","r", encoding='utf-8')
domain_file=open("free_domains.txt","w")

for line in f:   
   domain_list.extend(pattern.findall(line))
   

for item in domain_list:
   domain=urlparse(item)
   for i in domains:
      if (i==domain.netloc):
         flag=False
   if flag:
      domains.append(domain.netloc)   
      try:
         response=requests.get('http://api.whois.vu/?q='+tldextract.extract(domain.netloc).registered_domain).json()['available']
         
         if response=='yes':
            free_domains.append(domain.netloc)
            domain_file.write(domain.netloc+"\n")
            
      except Exception:
         print('Ошибочка')
   flag=True

print(free_domains)
f.close()
domain_file.close()
