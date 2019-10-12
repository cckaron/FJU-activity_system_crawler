# -*- coding: utf-8 -*-
"""
Created on Thu May 24 00:42:36 2018

@author: chaos
"""

# 引用必要套件
import requests
from bs4 import BeautifulSoup

mylist = []

res = requests.get("http://activity.dsa.fju.edu.tw/ActivityList.jsp?searchType=searchByContent&&order=1")
soup = BeautifulSoup(res.text,"html5lib")

table = soup.select('table')[7]

for tr in table.select('tr'):
    tds = tr.find_all('td')
    count = 0
    temp = []
    for td in tds:
        temp.append(td.text.strip())
    mylist.append(temp)

for i in range(2,len(mylist)):
    tempList1 = [x for x in mylist[i][1].split("                      ")]
    tempList2 = [x for x in mylist[i][2].split("\n                     ")]
    tempList3 = [x for x in mylist[i][3].split("\n")]
    tempList4 = [x for x in mylist[i][5].split("\n                      \n                      ")]
    tempList5 = [x for x in mylist[i][6].split("\n                         \n                     ")]
    tempList6 = [] #社會適應能力
    tempList7 = [x for x in mylist[i][7].split("\n                        \n                      ")]
    
    if (len(tempList3) < 2):
        tempList3.append("無協辦單位")
        
    if (tempList4[0] == "不需報名"):
        tempList4.append("")
        tempList4.append("")
    elif(len(tempList4[0]) == 0):
        tempList4.append("")
        tempList4.append("")
        tempList4.append("")
    
    for data in tempList5:
        for i2 in range(len(data)):
            if data[i2].isdigit():
                index = i2
        tempList6.append(data[0:index+1])
        tempList6.append(data[index+2:])
    
 
    act_id = mylist[i][0]
    act_category = tempList1[0]
    act_child_category = tempList1[1]
    act_name = tempList2[0]
    act_speaker = tempList2[1]
    act_organizer = tempList3[0]
    act_co_organizer = tempList3[1]
    act_content = mylist[i][4]
    act_signup_way = tempList4[0]
    act_signup_time_start = tempList4[1]
    act_signup_time_end = tempList4[2]
    act_social_ability = tempList6
    act_participant = tempList7

    #you can print any activity field above
    print("活動標題:", act_name, "\t社會適應能力:", act_social_ability)


    
