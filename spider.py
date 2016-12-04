# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import time

class Spider:

    def __init__(self):
        self.siteURL = 'http://ku.ent.sina.com.cn/star'

    def getPage(self,pageIndex):
        url = self.siteURL + "?page_no=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        
        pattern = re.compile('<li><a href=.*?<img src="(.*?)".*?<p>.*?</span>(.)</p>.*?</li>',re.S)
        items = re.findall(pattern,page)
        pattern1 = re.compile('<li><a href=.*?<img src=.*?title="(.*?)".*?></a>.*?</li>',re.S)
        items1 = re.findall(pattern1,page)
        gender=[]
        i = 0

        folder_female ='female'
        folder_male='male'
        male = '男'.decode('utf-8')
        female='女'.decode('utf-8')

        for it in items1:
            gender.append(it)
            i=i+1
        j = 0
        #m = 0
        #n = 0
        for item in items:

            if item[1]==male:
                picpath='E:\\Images\\%s' % (folder_male)
                target = picpath+'\\%s.jpg' % gender[j]
                print 'Downloading image to location: '+item[0]
                try:
                    urllib.urlretrieve(item[0],target)
                except:
                    return

                #target = picpath+'\\%s' % pageIndex +'_%s.jpg' % str(m)
                #urllib.urlretrieve(item[0],target)
                #m = m + 1
                
                
            elif item[1]==female:
                picpath='E:\\Images\\%s' % (folder_female)
                target = picpath+'\\%s.jpg' % gender[j]
                print 'Downloading image to location: '+item[0]
                try:
                    urllib.urlretrieve(item[0],target)

                except:
                    return
                
                #target = picpath+'\\%s' % pageIndex +'_%s.jpg' % str(n)
                #urllib.urlretrieve(item[0],target)
                #n = n + 1
            j = j + 1
            #print item[0],item[1]#,item[2]

        #for j in range(0,i):
            #print gender[j]

spider = Spider()
for i in range(100,200):    #100
    print 'page ' + str(i)
    spider.getContents(i)
