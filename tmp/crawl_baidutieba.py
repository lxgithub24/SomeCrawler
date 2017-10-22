# -*- coding:utf-8 -*-
import urllib2
import re


def load_Page(url, begin_page, end_page):
    '''
        加载贴吧信息
    '''
    for i in range(begin_page, end_page + 1):
        pn = 50 * (i - 1)
        my_url = url + str(pn)
        html = Get_Html(my_url)
        title = GetMainInfo(html)
        sumTxt = ""
        for item in title:
            sumTxt = sumTxt + item
        print "--------第 %d 页数据开始收集-------" % (i)
        # filename = "第"+str(i)+"页数据.html"
        SaveToTxt(str(i) + ".html", sumTxt)
        print "--------第 %d 页数据收集完毕--------" % (i)


def Get_Html(url):
    """
        抓取网页信息并返回
    """
    User_Agent = "Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11"
    Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    headers = {"User-Agent": User_Agent, "Accept": Accept}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html


def SaveToTxt(filename, txt):
    f = open(filename, 'a')
    f.write(txt)
    f.close()


def GetMainInfo(html):
    regex = re.compile(
        "<div class=\"col2_right j_threadlist_li_right \">(.*)</div>",
        re.S)
    return regex.findall(html)


# mian
if __name__ == "__main__":
    print "请输入贴吧地址"
    url = raw_input()
    print "请输入起始页码"
    begin_page = int(raw_input())
    print "请输入结束页码"
    end_page = int(raw_input())
    load_Page(url, begin_page, end_page)
