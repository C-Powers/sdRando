'''
Created by cpowers
cjpowers3@gmail.com
Web scraper to automate the gathering of RUSA permanents.
Created for San Diego Randos
'''

import webbrowser, sys, bs4, requests, time

def scrapeSite():
    #url is after using RUSA's perm search function for routes in California
    url = 'https://rusa.org/cgi-bin/permsearch_PF.pl'
    header = {'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    res = requests.get(url, headers = header)
    if res.status_code == requests.codes.ok:
        return res
    else:
        print("not 200")
        return

def getPerms():
    request = scrapeSite()
    print(request)
    for i in range(5):
        if request == None:
            print("failed to scrape site")
            time.sleep(i+3)
            scrapeSite()
        else:
            pass

    rusaSoup = bs4.BeautifulSoup(request.text, "html.parser")
    #permanent info is encompasses in a <td> element,
    #we grab them all before we start to refactor it for
    #SD local perms
    allPermInfo = rusaSoup.select('tr')
    #testing
    somePerms = allPermInfo[1:20]
    sdPerms = []
    for i in range(1, len(allPermInfo)-1):
        #aPerm = somePerms[i]
        aPerm = allPermInfo[i]
        aPermInfo = aPerm.select('td')
        if aPermInfo[0].getText() == 'CA: San Diego':
            '''
            print('+++++++++++')
            print(aPermInfo)
            print('+++++++++++')
            print('location -- ', aPermInfo[0].getText())
            print('Free Route?  ', aPermInfo[1].getText())
            print('Distance -- ', aPermInfo[2].getText(), ' Km')
            print('Climb -- ', aPermInfo[3].getText(), 'ft')
            print('Name -- ', aPermInfo[5].getText())
            print('Organizer -- ', aPermInfo[6].getText())
            print('------')
            '''
            itemsCollect = []
            for items in aPermInfo:
                itemsCollect.append(items.getText())
                #print(itemsCollect)
            if aPermInfo[5].find('a').get('href'):
                itemsCollect.append('https://rusa.org' + aPermInfo[5].find('a').get('href'))
            sdPerms.append(itemsCollect)
    #print("SD PERMS", sdPerms)
    return sdPerms
