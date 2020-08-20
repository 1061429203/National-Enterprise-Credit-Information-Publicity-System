import re
import execjs

with open('aaa.txt','r',encoding='utf-8')as fp:
    JS=fp.read()
print(JS)
if 'setTimeout(function()' in JS:
    new_ss = re.sub('},.*?\);}else\{', '}else{', JS)
    print(new_ss)
    new_ss1=re.sub('setTimeout\(function\(\)\{','',new_ss)
    print(new_ss1)
    new_ss1=re.sub("document.*?'ie']=",'return ',new_ss1)
    new_ss1=new_ss1.replace(';go({','data=go({')
    print(new_ss1)

elif
window_cookie = 'navigator={appCodeName:"Mozilla",appMinorVersion:"0",appName:"Netscape",appVersion:"5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",browserLanguage:"zh-CN",cookieEnabled:true,cpuClass:"x86",language:"zh-CN",maxTouchPoints:0,msManipulationViewsEnabled:true,msMaxTouchPoints:0,msPointerEnabled:true,onLine:true,platform:"Win32",pointerEnabled:true,product:"Gecko",systemLanguage:"zh-CN",userAgent:"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",userLanguage:"zh-CN",vendor:"",vendorSub:"",webdriver:false},window=this,window.navigator=navigator;function atob(str){return Buffer.from(str,"base64").toString("binary")};'+new_ss1
print(window_cookie)
context=execjs.compile(window_cookie)
location=context.eval('data')
print(location)