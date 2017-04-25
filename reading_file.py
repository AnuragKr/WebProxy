# Project Title      : DISPLAYING TOP VISITED WEBSITES
# Group members      : ANURAG KR. SINGH, ANUSHAATH.P, BONALA SANDEEP, SAI PRANEETH BUSA
# Project details    : Display top n websites by accessing web-proxy log files.
# Project description   : 1.Input Format -python project_code.py
#                           Output - It will display websites in top visisted order.
#                         2.Input Format -python project_code.py 8
#                           Output - It will display top 8 website visited.
#                         3.Input Format -python project_code.py 10 google
#                           Output - It will display websites from top 10 which will match keyword google.
import re
import operator, sys
top = 10000
#------------------------------------------------------
#Command Line check
if (len(sys.argv)==2):
  if not sys.argv[1].isdigit():
     print("No numeric given! EXIT!")
     sys.exit(0)
  else:
    top= int(sys.argv[1])

if (len(sys.argv)==3):
  if not sys.argv[2].isalpha():
    print("No proper keyword given! EXIT!")
    sys.exit(0)
  if not sys.argv[1].isdigit():
     print("No numeric given! EXIT!")
     sys.exit(0)
  else:
    top= int(sys.argv[1])
#-------------------------------------------------------
#Regular expression to extract website url
regex = re.compile("\shttps?://(.+?)/")
#--------------------------------------------------------
domain_dict = {}
total_websites = 0
#--------------------------------------------------------
#Adding dictionary with url as key and no. of hits as value
for lines in open("new_log.txt","r"):
  total_websites = total_websites + 1
  match = regex.search(lines)
  if(match):
      domain = match.group(1)
  else:
      print("No match found")
  domain_name = domain
  if not domain_name in domain_dict:
    domain_dict[domain_name]=domain_dict.setdefault(domain_name,1)
  else:
    domain_dict[domain_name]+=1
#---------------------------------------------------------
#Calculating % of the total visits and sorting it in order
for k,v in domain_dict.items():
    domain_dict[k]=(domain_dict.get(k,1) / total_websites )*100
ranked = sorted(domain_dict.items(), key=operator.itemgetter(1),reverse=True) #Sorting Dictionary As per value not key.For key we need to use key=operator.itemgetter(0)
#---------------------------------------------------------
#Printing the top n websites
count=1
other=0
str_other="Other"
for i in ranked:
  if len(sys.argv)==3:
    if sys.argv[2] in i[0]:
      if count <= top:
        print(i[0].center(40,' '),round(i[1]),"%")
        count+=1
        other+=i[1]
  else:
    if count <= top:
      print(i[0].center(40,' '),round(i[1]),"%")
      count+=1
      other+=i[1]
if count ==1:
  print("The string you searched for has no matches")
print(str_other.center(40,' '),round(100-other),"%")
