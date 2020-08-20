import requests
import re
import execjs
import pprint


class Cookies(object):
    def __init__(self):
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",

        }
        self.data={
            "draw": 6,
            "start": 0,
            "length": 30,
        }
        self.url='http://bj.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=11&areaid=110000&noticeTitle=&regOrg='

    def fetchJS(self):
        scriptRep=requests.post(self.url,headers=self.headers,data=self.data)
        scriptRep.encoding="utf-8"
        jsluidh=scriptRep.headers["Set-Cookie"].split(';')[0]
        self.headers['Cookie']=jsluidh
        return scriptRep.text

    def calculateJS(self,scriptRep):

        wind_cook='navigator={appCodeName:"Mozilla",appMinorVersion:"0",appName:"Netscape",appVersion:"5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",browserLanguage:"zh-CN",cookieEnabled:true,cpuClass:"x86",language:"zh-CN",maxTouchPoints:0,msManipulationViewsEnabled:true,msMaxTouchPoints:0,msPointerEnabled:true,onLine:true,platform:"Win32",pointerEnabled:true,product:"Gecko",systemLanguage:"zh-CN",userAgent:"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",userLanguage:"zh-CN",vendor:"",vendorSub:"",webdriver:false},window=this,window.navigator=navigator;'
        JS=re.findall('<script>(.*?)</script>',scriptRep,re.S)[0]
        print(JS)
        if 'setTimeout(function()' in JS:
            print('1')
            new_ss = re.sub('},.*?\);}else\{', '}else{', JS)
            new_ss1 = re.sub('setTimeout\(function\(\)\{', '', new_ss)

            print(new_ss1)
        new_ss1 = re.sub("document.*?'ie']=", 'return ', new_ss1)
        new_ss1 = new_ss1.replace(';go({', 'data=go({')
        window_cookie = 'navigator={appCodeName:"Mozilla",appMinorVersion:"0",appName:"Netscape",appVersion:"5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",browserLanguage:"zh-CN",cookieEnabled:true,cpuClass:"x86",language:"zh-CN",maxTouchPoints:0,msManipulationViewsEnabled:true,msMaxTouchPoints:0,msPointerEnabled:true,onLine:true,platform:"Win32",pointerEnabled:true,product:"Gecko",systemLanguage:"zh-CN",userAgent:"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",userLanguage:"zh-CN",vendor:"",vendorSub:"",webdriver:false},window=this,window.navigator=navigator;function atob(str){return Buffer.from(str,"base64").toString("binary")};' + new_ss1
        print(window_cookie)
        context = execjs.compile(window_cookie)
        cookie = context.eval('data')
        clearance=cookie.split(';')[0]
        print(cookie)
        self.headers['Cookie']+=';'+clearance

    def testCookie(self):
        rsp=requests.post(self.url,headers=self.headers,data=self.data)
        print(rsp.json())
        with open('qiye.html','w',encoding='utf-8')as f:
            f.write(rsp.text)



        # if '}setTimeout(' in JS:
        #     print('11')
        #     if re.search('\);}else\{_',JS):
        #
        #     if re.search(',.*?\);}else{',JS):
        #         print('aa')
        # else:
        #
        #     JS=re.sub('setTimeout,','',JS)
        # print(JS)





if __name__=="__main__":
    ck=Cookies()
    scriptRep=ck.fetchJS()
    ck.calculateJS(scriptRep)
    ck.testCookie()
