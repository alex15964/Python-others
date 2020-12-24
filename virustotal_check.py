import requests
import json
import time
import sys #導入module
import csv

YOUR_API_KEY_HERE = '3fb09c12dff597daace850a7af4a7c79f2bf6354bf9448ccba287aa1fa4181d7'
scantime = 9 #每筆掃描間隔，防止error
errorlist = []#debug模組
bufferlist = []#buffer模組
outputdict = [] #掃描後接資料用
sn = 0 #序列號
def intputoutput(urlitem='',iporhostitem='',postitem='',totalitem='',statuscode=0): #根據掃描結果，給予不同值
    global sn
    if statuscode == 1: #正常掃描
        outputdict.append([sn, urlitem, iporhostitem, postitem, totalitem, 'OK'])
    elif statuscode == 2: #輸入domain，找不到對應IP
        outputdict.append([sn, urlitem, 'NA', postitem, totalitem, 'IP_not_found'])
    elif statuscode == 3: #輸入Domaion/IP，查詢不到
        outputdict.append([sn, urlitem, 'NA', 'NA', 'NA', 'Domain_or_IP_not_found'])
    elif statuscode == 4: #掃描後判斷為無毒網站
        outputdict.append([sn, urlitem, 'NA', 'NA', 'NA', 'This_site_is_OK'])
    else: #輸入輸出錯誤
        outputdict.append([sn, urlitem, 'NA', 'NA', 'NA', 'Sth_Wrong!'])
    sn += 1

def checksite(site): #確認輸入值並給予輸出
    try:
        queryurl = site
        if domain_of_url(queryurl): #判斷輸入為doamion或IP
            domainsite = True
            print('This is domain')
        else:
            domainsite = False
            print('This is IP')

        if domainsite: #依輸入domaion或IP，給不同查詢的url
            url = 'https://www.virustotal.com/vtapi/v2/domain/report'
            params = '?'+'domain='+queryurl+'&'+'apikey='+YOUR_API_KEY_HERE
        else:
            url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
            params = '?'+'ip='+queryurl+'&'+'apikey='+YOUR_API_KEY_HERE
        response = requests.get(url+params)

        if response.status_code == requests.codes.ok: #如果網站有回應
            json_response = response.json()
            #print(json.dumps(json_response, indent=1, ensure_ascii=False))#For debug
            if json_response['response_code']!=1: #輸入的doamion或IP查詢不到時，response_code不為1
                #print('response_code error')
                print(json_response['verbose_msg'])
                print('response_code: ', json_response['response_code'])
                intputoutput(site,'','','',3)
            else:
                if json_response['detected_urls']!= [] and json_response['detected_urls'][0]['positives']>0: #檢查網站存在病毒且偵測到的網站不只一個
                    print('detected_urls',json_response['detected_urls'][0]['url'])
                    if len(json_response['resolutions']) !=0: #輸入domaion可查詢到對應IP
                        if domainsite: #如果輸入是domaion
                            print('IP is '+json_response['resolutions'][0]['ip_address'])
                            intputoutput(site,json_response['resolutions'][0]['ip_address'],str(json_response['detected_urls'][0]['positives']),str(json_response['detected_urls'][0]['total']),1)
                        else: #如果輸入是IP
                            print('Hostname is '+json_response['resolutions'][0]['hostname'])
                            intputoutput(site,json_response['resolutions'][0]['hostname'],str(json_response['detected_urls'][0]['positives']),str(json_response['detected_urls'][0]['total']),1)
                    else: #輸入dmoaion查不到對應IP
                        print('Can not find address IP')
                        intputoutput(site,'',str(json_response['detected_urls'][0]['positives']),str(json_response['detected_urls'][0]['total']),2)
                    print('positives/total:',str(json_response['detected_urls'][0]['positives'])+'/'+str(json_response['detected_urls'][0]['total']))
                else: #檢查網站不存在病毒
                    print('In virsutotal, this is ok')
                    intputoutput(site,'','','',4)
        else: #網站沒有回應，將該筆輸入放進buffer
            print('response_code:'+str(response.status_code))
            print('Add '+site+' into Buffer')
            bufferlist.append(site)
            breakpoint
    except:
        print('error happen!')
        errorlist.append('Read_list_error:'+site)
    print('---------------------')

def checkbuffer(): #將buffer的url重新查詢
    while len(bufferlist) !=0:
        time.sleep(scantime)
        item = bufferlist.pop()
        checksite(item)

def showexplain(): #使用者輸入-h參數時，show出使用說明
    print('-h')
    print('python [file] [-h | -u url | -r file.txt(txt only) ]')
    print('-h : print this help, end')
    print('-u : read only one url, end')
    print('-r file.txt : read a txt file')
    print('created by lin17 & AlexLin')

def domain_of_url(url): #判斷輸入為doamain或IP
    for item in url:
        if item.isalpha():
            return True
    return False

if str(sys.argv[1]) == '-h': #參數-h為說明
    showexplain()
elif str(sys.argv[1]) == '-u': #參數-u為讀後方url參數
    print('Check url:'+str(sys.argv[2])+'...')
    print('---------------------')
    checksite(str(sys.argv[2]))
    checkbuffer()
elif str(sys.argv[1]) == '-r': #參數-r為讀取txt檔案
    with open(sys.argv[2], "r") as f:#開啟檔案，argv表cmd後輸入的檔案
        for item in f:
            time.sleep(scantime)
            item = str(item.strip())
            print('Check url:'+item+'...')
            print('---------------------')
            checksite(item) 
        checkbuffer()
    with open('result4.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['', 'url', 'IP/Hostname','positives','total','desc'])
        writer.writerows(outputdict)
        #print(outputdict)
else:showexplain()

#Debug log
if len(errorlist) > 0: #如果存在輸入錯誤，則產出log並存入錯誤輸入
    with open('error_log.txt', "w") as f2:
        for i in errorlist:f2.write(i+'\n')