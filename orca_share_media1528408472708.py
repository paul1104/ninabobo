# -*- coding: utf-8 -*-

import CHROME
from CHROME.lib.curve.ttypes import *
from datetime import datetime
#from Helper.main import qr
from time import time
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from urllib3 import HTTPConnectionPool
import time,random,sys,json,codecs,threading,glob,re,subprocess,os,requests,goslate,ctypes
import ast
import subprocess
import urllib
import urllib2
import urllib3
import cookielib
import wikipedia
import shutil

cl = CHROME.LINE() #V2 
cl.login(token="Esdk1SckTz1VVkXStAlb.ggNCLqZ5irfKOvdzgQfq2W.iGqw2biU4ifOYMbatkExc7jMittEN6hxL42e8ru0vQk=") 
cl.loginResult()

botStart = time.time()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

keyMessage = """╔═══════════════
║┏━━ೋ• ❄ •ೋ━━━┓
║ ❁ 🛡  кєи кαиєкι! ＢＯＴ  🛡 ❁    
║┗━━ೋ• ❄ •ೋ━━━┛
╠═══════════════
║「ĸeyword」
╠═══════════════
║╔❂͜͡➣「/ѕιderѕ」
║╠❂͜͡➣「/pυвlιc」
║╠❂͜͡➣「/ѕearcнιng」
║╠❂͜͡➣「/newғιтυre」
║╠❂͜͡➣「/cancel」
║╠❂͜͡➣「/aвoυт」
║╚❂͜͡➣「/ĸelυar」
╚═══════════════ """

newMessage ="""⚘ 🐯 new fiture area 🐯 ⚚
❂͜͡☆➣ https://tinyurl.com/newfiture (cek disini)
❂͜͡☆➣ https://tinyurl.com/newfiture2 (cek disini)
❂͜͡☆➣ cυaca「naмa ĸoтa」= cek cuaca kota
❂͜͡☆➣ ѕнolaт「naмa ĸoтa」= cek jadwal sholat di kota
❂͜͡☆➣ cpoѕт 「υѕernaмe ιg ĸaмυ」= untuk cek post terakhir mu yang berupa foto
❂͜͡☆➣ cvιd「υѕernaмe ιg ĸaмυ」= untuk cek post terakhir mu yang berupa video
❂͜͡☆➣ ѕcreen 「υѕernaмe ιg ĸaмυ」= untuk screenshoot ig kamu
❂͜͡☆➣ loĸaѕι「yang ιngιn ĸaмυ carι」= υnтυĸ мencarι loĸaѕι
❂͜͡☆➣ /lιrιĸ「jυdυl lagυ」= υnтυĸ мencarι lιrιĸ lagυ
❂͜͡☆➣ /lagυ「jυdυl lagυ」= untuk mencari lagu joox
❂͜͡☆➣ ιnғo ѕaya = вυaт lυcυ lυcυ an

ada ιngιn мenyaranĸan ғιтυre? cнaт ĸe http://line.me/ti/p/%40ish7215m"""

sidersMessage =""" 🛡  кєи кαиєкι v2! ＢＯＴ  🛡

⚘ 🐯 cнecĸ ѕιderѕ area 🐯 ⚚
❂͜͡☆➣ ѕeтlaѕтpoιnт = cнecĸ ѕιderѕ
❂͜͡☆➣ vιewlaѕтѕeen = cнecĸ ѕιderѕ
❂͜͡☆➣ ѕeтpoιnт = cнecĸ ѕιderѕ
❂͜͡☆➣ read = cнecĸ ѕιderѕ"""

publicMessage =""" ⚘ 🐯 pυвlιc area 🐯 ⚚
❂͜͡☆➣ creaтor = conтacт peмвυaт вoт
❂͜͡☆➣ apaĸaн 「тeхт yang ιngιn ĸaмυ тanyaĸan」 (ѕeperтι ĸerang ajaιв)
❂͜͡☆➣ ĸedapĸedιp「тeхт yang ιngιn dιĸedap ĸedιpĸan」 = coвa aja
❂͜͡☆➣ doѕa @「naмe」 = вυaт lυcυ2an
❂͜͡☆➣ paнala @「naмe」 = вυaт lυcυ2an
❂͜͡☆➣ gcreaтor = мenυnjυĸĸan peмвυaт grυp
❂͜͡☆➣ gιnғo = ιnғo grυp
❂͜͡☆➣ ѕpaмтag @ 「naмe」= ѕpaм yang dιтag
❂͜͡☆➣ /ѕpaм: on/oғғ + jυмlaн + ĸaтa = ѕpaм dengan jυмlaн ĸaтa
❂͜͡☆➣ мenтιon all = мenтιon ѕeмυa
❂͜͡☆➣ мenтιon = мenтιon ѕeмυa
❂͜͡☆➣ тag all = мenтιon ѕeмυa
❂͜͡☆➣ тagall = мenтιon ѕeмυa
❂͜͡☆➣ ѕay = coвa aja ĸeтιĸ ѕay"""

searchingMessage =""" ⚘ 🐯 ѕearcнιng area 🐯 ⚚
❂͜͡☆➣ proғιleιg 「υѕernaмe」
❂͜͡☆➣ ιnѕтagraм 「υѕernaмe」
❂͜͡☆➣ .ιnѕтagraм 「υѕernaмe」
❂͜͡☆➣ wιĸιpedιa 「тeхт」
❂͜͡☆➣ gιмage「тeхт」
❂͜͡☆➣ тr-en 「тeхт」
❂͜͡☆➣ тr-ιd 「тeхт」
❂͜͡☆➣ ιd@en
❂͜͡☆➣ en@ιd
❂͜͡☆➣ ιd@jp
❂͜͡☆➣ jp@ιd
❂͜͡☆➣ ιd@тн
❂͜͡☆➣ тн@ιd
❂͜͡☆➣ ιd@jp
❂͜͡☆➣ ιd@ar
❂͜͡☆➣ ar@ιd
❂͜͡☆➣ ιd@ĸo
❂͜͡☆➣ ĸo@ιd
❂͜͡☆➣ yт: [jυdυl]
❂͜͡☆➣ ceĸ (тanggal)-(вυlan)-(тaнυn)
❂͜͡☆➣ /ιg 「υѕernaмe」
❂͜͡☆➣ ѕearcнιd: 「ιd lιne」"""

cancelMessage ="""ғιтυr вerѕтaтυѕ oғғlιne!"""

welcomeMessage="""тerιмa ĸaѕιн тelaн мengυndang вoт ιnι! 
ιnvιтe aĸυ ĸe grυp ĸalιan ya :)
⭐ υnтυĸ мengeтaнυι adмιn ĸeтιĸ "creaтor"!
⭐ υnтυĸ мengeтaнυι ғιтυre apa ѕaja darι вoт ιnι ĸeтιĸ "нelp"
⭐ υnтυĸ вoт вeĸerja ѕecara мaхιмal ѕιlaнĸan ιnvιтe creaтor вoт! тнanĸyoυ!❤
"""

meMessage="""⭐ нow тo υѕe ιт::
- !say 「тeхт」
- @say 「тeхт」
- #say 「тeхт」
- $say 「тeхт」
- %say 「тeхт」
- ^say 「тeхт」
- &say 「тeхт」
- *say 「тeхт」
- (say 「тeхт」
- )say 「тeхт」
"""

sayMessage ="""⭐ Kode Baнaѕa ⭐
aғ : Aғrιĸaanѕ
ѕq : Alвanιan
ar : Araвιc
нy : Arмenιan
zн : Cнιneѕe
nl : Dυтcн
ғr : Frencн
de : Gerмan
en : Englιѕн
ιd : Indoneѕιan
ja : Japaneѕe
ĸo : Korean
ιт : Iтalιan
la : Laтιn
pт : Porтυgυeѕe
ro : Roмanιan
rυ : Rυѕѕιan
eѕ : Spanιѕн
тн : Tнaι
vι : Vιeтnaмeѕe
ѕυ : ѕυи∂α 
נω : נαωα
⭐ Tнanĸ Yoυ ⭐
"""

mulai = time.time()
KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid]
admin=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
owner=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
protectname=[]

wait = {
    'contact':False,
    'autoJoin':True,
    'sticker':False,
    'autoCancel':{"on":True,"members":10},
    "spam":{},
    "detectMention":False,
    "Members":1,
    "wordban":{},
    'leaveRoom':True,
    'likeOn':True,
    'comment1':"Auto Like By http://line.me/ti/p/%40ish7215m",
    'timeline':True,
    'autoAdd':True,
    'atjointicket':True,
    "alwaysRead":True,
    "linkticket":False,
    "cpp":False,
    "cpg":False,
    'message':"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "lang":"JP",
    "comment":"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "commenty":"Auto Like by кєи кαиєкι\n\nhttp://line.me/ti/p/%40ish7215m",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "teman":{},
    "winvite":False,
    "likeOn":True,
    "protection":False,
    "welcomemsg":True,
    "welmsg":" welcome to ",
    "pname":{},
    "pro_name":{},
    "Pap":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

settings = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "timeRestart": "18000",
    "simiSimi":{},
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    
   
hasil = {
    "result":False,
    "posts":False,
    "postInfo":False,
    "liked":{}
    }
    
wordban = {
    "kontol":{},
    "kontl":{},
    "kntl":{},
    "memek":{},
    "anjing":{},
    "njing":{},
    "anjeng":{}
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
profile = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendKontok(self, HelloWorld, midUrang):
      msg = Message()
      msg.contentMetadata = {'mid': midUrang}
      msg.to = HelloWorld
      msg.contentType = 13
      return self.Talk.client.sendMessage(0, msg)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        time.sleep(5)
        restartBot()
       
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version: #If the Current Version of Python is 3.0 or above
        import urllib.request #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else: #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
 
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
 
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item) #Append all the links in the list named 'Links'
            time.sleep(0.1) #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        msg = Message()
        msg.contentType = 0
        msg.text = text_
        msg.contentMetada = {'MENTION':'{"MENTIONEES":['+aa+']}'}
        cl.sendMessage(msg)
    except Exception as error:
        print error
        
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "• @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def yt(query):
    with requests.session() as s:
        isi = []
        if query == "":
            query = "S1B nrik"
        s.headers['user-agent'] = 'Mozilla/5.0'
                     
        url    = 'http://www.youtube.com/results'
        params = {'search_query': query}
                     
        r    = s.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html5lib')
                     
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&List' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=','')
                    isi += ['youtu.be' + b]
        return isi

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        
#-------------------------------------------
              
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                else:
                                    cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja?\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
 
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・ " + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------------------------------

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            c = Message(to=op.param1, from_=None, text=None, contentType=13)
                            c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                            cl.sendMessage(c)
                            cl.sendText(op.param1,"мaaғ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!")
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            xname = cl.getContact(op.param2).displayName
                            c = Message(to=op.param1, from_=None, text=None, contentType=13)
                            c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                            cl.sendMessage(c)
                            cl.sendText(op.param1, "тerιмa ĸaѕιн "+"@"+xname+" тelaн мengυndang вoт ιnι!\n\nwajιв add oa dιaтaѕ! \nĸeтιĸ нelp υnтυĸ мelιнaт ғιтυre вoт ιnι!")
   #                         cl.acceptGroupInvitation(op.param1)    
  #                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
  #                          c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
  #                          cl.sendMessage(c)
  #                          cmem = cl.getContacts(op.param2)
 #                           mid = cmem.mid
   #                         zx = ""
  #                          zxc = "тerιмa ĸaѕιн "
  #                          zx2 = []
  #                          pesan2 = "@a"" "
   #                         xlen = str(len(zxc))
    #                        xlen2 = str(len(zxc)+len(pesan2)-1)
   #                         zx = {'S':xlen, 'E':xlen2, 'M':'ub8530f15ff4020c3cc2d1ad2f066aa4b'}
    #                        zx2.append(zx)
   #                         zxc += pesan2
    #                        msg = Message()
   #                         msg.contentType = 0
   #                         msg.text = zxc+" тelaн мengυndang вoт ιnι!\n\nwajιв add oa dιaтaѕ! \nĸeтιĸ нelp υnтυĸ мelιнaт ғιтυre вoт ιnι!"
   #                         msg.contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}                       
   #                         cl.sendMessage(msg)                                                            
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                        cl.sendMessage(c)
                        cl.sendText(op.param1, "wajιв add oa dιaтaѕ! \nĸeтιĸ нelp υnтυĸ мelιнaт ғιтυre вoт ιnι!")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.acceptGroupInvitation(op.param1)
                        c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                        cl.sendMessage(c)
                        cl.sendText(op.param1,"мaaғ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!")
                        cl.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
     
#        if op.type == 17:
	#       if wait["welcomemsg"] == True:
	#           if op.param2 not in Bots:
	#                 ginfo = cl.getGroup(op.param1)
	 #                    xcont = cl.getContact(op.param2)
      #                  xname = cl.getContact(op.param2).displayName
     #                    xlen = str(len(xname)+1)
      #                   c = Message(to=op.param1, from_=None, text=None, contentType=13)
     #                    c.contentMetadata={'mid':op.param2}
      #                   cl.sendMessage(c)  
     #                    msg = Message(to=op.param1, from_=None, contentType=0)
    #                     msg.text = "Hallo @"+xname+ "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini (ﾉ*>∀<)ﾉ♡"            
      #                   msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(xcont.mid)+'}]}','EMTVER':'4'}
      #                   cl.sendMessage(msg)      
      #                   zx = ""
     #                    zxc = "Hallo "
       #                  zx2 = []
       #                  pesan2 = "@a "                                                
         #                xlen = str(len(zxc))
           #              xlen2 = str(len(zxc)+len(pesan2)-1)
       #                  zx = {'S':xlen, 'E':xlen2, 'M':op.param2}
          #               zx2.append(zx)
       #                  zxc += pesan2 + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini (ﾉ*>∀<)ﾉ♡"               
        #                 msg.text = pesan2+ zxc + "\n🔔 %"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
       #                  lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
             #            print lol
         #                msg.contentMetadata = lol
          #               try:
      #                     cl.sendMessage(msg)
        #                 except Exception as error:
         #                      print error
      #                   pass
       #                  msg.contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
        #                 cl.sendMessage(msg)
        if op.type == 17:
	        if wait["welcomemsg"] == True:
	           if op.param2 not in Bots:
	                 ginfo = cl.getGroup(op.param1)
                         contact = cl.getContact(op.param2)
                         c = Message(to=op.param1, from_=None, text=None, contentType=13)
                         c.contentMetadata={'mid':op.param2}
                         cl.sendMessage(c)
                         cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini (ﾉ*>∀<)ﾉ♡")  
        
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
                            
#                if msg.contentType == 16:
#                 if wait['likeOn'] == True:
#                      url = msg.contentMetadata["postEndUrl"]
#                      cl.like(url[25:58], url[66:], likeType=1005)
#                      cl.comment(url[25:58], url[66:], wait["comment1"])                      cl.sendText(msg.to,"Like Success")                     
#                      wait['likeOn'] = False
                     
        if op.type == 26:       
            msg = op.message
            msg.text = str(msg.text)
            text = msg.text        
            to = msg.to               
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     cl.sendText(msg.from_, "kenapa tag aku digrup kak?\n\nhttp://line.me/ti/p/%40ish7215m (add)")
             #        xname = cl.getContact(msg.from_).displayName
             #        xlen = str(len(xname)+1)
             #        balas = "@"+xname+" ngapain ya kak? "
             #        msg.to = op.param1
             #        msg.contentType = 0
              #       balas = "@"+xname+ " \n Kenapa tag saya di grup? \n", "@"+xname+ " \n jangan tag kalo gamau tanggung jawab :v \n","@"+xname+ " \nada perlu apa yah? \n","@"+xname+ " \n anda siapa ea? \n","@"+xname+ " \n kebiasaan niih suka tag ga jelas \n","@"+xname+ " \n chat disini aja kuy. dari pada tag di gc \n"
              #       msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
               #      cl.sendMessage(msg)
            
 #                    c = Message(to=msg.to, from_=None, text=None, contentType=13)
 #                    c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
#                     cl.sendMessage(c)
#                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
#                     ret_ = "[Auto Respond] " + random.choice(balas)
#                     name = re.findall(r'@(\w+)', msg.text)
#                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
 #                    mentionees = mention['MENTIONEES']
#                     for mention in mentionees:
#                           if mention['M'] in Bots:
#                                  cl.sendText(msg.to,ret_)
#                                  break     
                        
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        
        if op.type == 26:
            msg = op.message
            msg.text = str(msg.text)
            to = msg.to
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
                                
        if op.type == 26:
            msg = op.message
            msg.text = str(msg.text)
            to = msg.to
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                              
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu))
                        
            elif msg.contentType == 7:
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass
                    
            elif msg.contentType == 1:
            	if msg.from_ in admin:
            	     if msg.toType == 2:
                            if wait["cpg"] == True:
                                path = cl.downloadObjectMsgId(msg.id)
                                wait["cpg"] = False
                                cl.updateGroupPicture(msg.to, path)
                                cl.sendText(msg.to,"Foto grup telah di perbaharui !")
                     if wait["cpp"] == True:
                        path = cl.downloadObjectMsgId(msg.id)
                        wait["cpp"] = False
                        cl.updateProfilePicture(path)
                        cl.sendText(msg.to, "success change profile picture")
                        
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
                    
#-----------INFO GROUP CREATOR---------------#
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
              
            elif "Oa" in msg.text:
              if msg.from_ in admin:
                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                cl.sendKontok(msg.to, Oa)

            elif "Ayat:" in msg.text:
              try:
                 sep = text.split(" ")
                 ayat = text.replace(sep[0] + " ","")
                 path = "http://islamcdn.com/quran/media/audio/ayah/ar.alafasy/" + ayat
                 cl.sendAudioWithURL(msg.to, path)
              except Exception as error:
                 cl.sendText(msg.to, str(error))

            elif "Jadwal: " in msg.text:
                    try:
                        txt = msg.text.split(" ")
                        teks = msg.text.replace("Jadwal: "+txt[1]+" ","")
                        response = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=kanekipubot&id="+txt[1]+"")
                        data = response.json()
                        pictig = str(data['status'])
                        hasil = str(data['url'])
                        text = "Status : "+pictig+"\n"+hasil+""
                        cl.sendText(msg.to, text)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
   
            elif "Call: " in msg.text:
                no = msg.text.replace("Call: ","")
                r = requests.get("http://apisora.herokuapp.com/prank/call/?no="+str(no))
                data = r.json()
                result = data["result"].replace('</br>', '\n')
                tgb = "[ Prank Call ]\n\n"
                tgb += "Status: "+str(data["status"])+"\n"
                tgb += "Result "+str(result)+"\n\n[ Finish ]"
                cl.sendText(msg.to,str(tgb))
                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                cl.sendKontok(msg.to, Oa)
        
            #elif '/login chrome ' in msg.text.lower:
             #  user = msg.text.replace('/login chrome ',' ')
              # data = {
               #    'nama' : '{}'.format(user),
                #   'sumbit1' : ' '
                 #  }
              # link = 'https://lazybot.us/snip/'
              # r = requests.post(url = link, data = data)
               #qr = r.text
               #cl.sendMessage(msg.to, "{}".format(qr))

           # elif '/done ' in msg.text.lower:
            #   user = msg.text.replace('/done ',' ')
             #  r = requests.get('https://206.189.95.201/token-{}.text' .format(user))
              # token = r.text
               #cl.sendMessage(msg.from_, "{}".format(token))
              
            elif "Sms: " in msg.text:
                    try:
                        txt = msg.text.split(" ")
                        teks = msg.text.replace("Sms: "+txt[1]+" ","")
                        response = requests.get("http://corrykalam.gq/sms.php?no="+txt[1]+"&text="+teks+"")
                        data = response.json()
                        pictig = str(data['status'])
                        hasil = str(data['detail'])
                        text = "Status : "+pictig+"\n\n"+hasil+""
                        cl.sendText(msg.to, text)
                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                        cl.sendKontok(msg.to, Oa)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
           
            elif "detectout" in msg.text:
               if msg.from_ in admin:
                groups = cl.getGroupIdsJoined()
                for group in groups:               	
                    G = cl.getGroup(group)
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        c = Message(to=group, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                        cl.sendMessage(c)
                        cl.sendText(group,"мaaғ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!")
                        cl.leaveGroup(group)
         
            elif "meme: " in msg.text.lower():
                    try:
                        txt = msg.text.split(" ")
                        teks = msg.text.lower().replace("meme: "+txt[1]+" ","")
                        data = []
                        r = requests.get("http://captaintools.tk/bot.php")
                        r = eval(r.text)
                        for a in r:
                            data.append(a)
                        c = random.choice(data)
                        foto = "https://memegen.link/"+c+"/"+txt[1]+"/"+teks+".jpg"
                        cl.sendImageWithURL(msg.to, foto)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif "Short: " in msg.text:
                no = msg.text.replace("Short: ","")
                r = requests.get("https://short.helloworld404.me/api/?key=Y2hXOO8wTHGJ&url="+str(no))
                data = r.json()
                result = data["short"]
                tgb = "[ Shorten URL ]\n\n"
                tgb += "Result: "+str(result)+"\n\n[ Finish ]"
                cl.sendText(msg.to,str(tgb))
                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                cl.sendKontok(msg.to, Oa)

            elif "Playstore " in msg.text.lower():
                    tob = msg.text.lower().replace("Playstore ","")
                    cl.sendText(msg.to,"Loading")
                    cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    cl.sendText(msg.to,"Done")
            
            elif "Retro: " in msg.text:
                    try:
                        txt = msg.text.split(" ")
                        teks = msg.text.replace("Retro: "+txt[1]+" ","")
                        satu = ["1","2","3","4","5"]
                        dua = ["1","2","3","4"]
                        k = random.choice(satu)
                        w = random.choice(dua)
                        response = requests.get("http://corrykalam.gq/retrowave.php?text1="+txt[1]+"&text2="+teks+"&text3=&btype="+k+"&ttype="+w+"")
                        data = response.json()
                        hasil = str(data['image'])
                        download = str(data['image'])                      
                        cl.sendText(msg.to, download)
                        cl.sendImageWithURL(msg.to, hasil)
                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                        cl.sendKontok(msg.to, Oa)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif "Pcid: " in msg.text:
            	txt = msg.text.split(" ")
                teks = msg.text.replace("Pcid: "+txt[1]+" ","")
                x = cl.findContactsByUserid(txt[1])
                a = cl.getContact(msg.from_)
                cl.sendText(x.mid,"Anda mendapatkan pesan dari "+a.displayName+"\n\n"+teks)
                cl.sendText(msg.to,"Sukses mengirim pesan ke "+x.displayName+"\nDari: "+a.displayName+"\nPesan: "+teks)
                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                cl.sendKontok(msg.to, Oa)

            elif "Gbcon: " in msg.text:
              if msg.from_ in admin:
                print "[Group Broadcast Execute]"
                n = cl.getGroupIdsJoined()   
                y = msg.text.split(" ")
                k = msg.text.replace("Gbcon: "+y[1]+" ","")
                Oa = y[1]
                for people in n:                	
                	cl.sendKontok(people, Oa)

            elif "Fs: " in msg.text:
                    try:
                        txt = msg.text.split(" ")
                        teks = msg.text.replace("Fs: "+txt[1]+" ","")
                        response = requests.get("https://farzain.xyz/api/premium/fs.php?apikey=kanekipubot&id="+txt[1]+"")
                        data = response.json()
                        pictig = str(data['status'])
                        hasil = str(data['url'])
                        text = "Status : "+pictig+""
                        cl.sendText(msg.to, text)
                        cl.sendImageWithURL(msg.to, hasil)
                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                        cl.sendKontok(msg.to, Oa)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif "/apakah " in msg.text:
              if msg.from_ in admin:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
              if msg.from_ in admin:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                


            elif "/berapa " in msg.text:
              if msg.from_ in admin:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
       
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------INFO GROUP CREATOR---------------#
            elif msg.text in ["Blocklist"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Aku belum mandi")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tapi masih cantik juga")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"apalagi kalau sudah mandi")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Pasti cantik sekali")
                cl.sendText(msg.to,"yiha")
                cl.sendText(msg.to,"Kalau orang lain melihatku")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Badak aku taba bana")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tak tuntuang")
                cl.sendText(msg.to,"Tapi kalau langsuang diidu")
                cl.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Atagfirullah baunya")
                cl.sendText(msg.to,"Males lanjutin ah")
                cl.sendText(msg.to,"Sepi bat")
                cl.sendText(msg.to,"Iya sepi udah udah")
                cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                cl.sendText(msg.to,"Nah")
                cl.sendText(msg.to,"Mending gua makan dulu")
                cl.sendText(msg.to,"Siyap")
                cl.sendText(msg.to,"Okeh")
                cl.sendText(msg.to,"Katanya owner kita Jomblo ya")
                cl.sendText(msg.to,"Iya emang")
                cl.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                cl.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
#-------------Fungsi Spam Finish---------------------#  
            elif "Info saya" in msg.text:
              kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong")
              wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur")
              status = ("Menikah","Pacaran","Jones")
              k = random.choice(kelamin)
              w = random.choice(wajah)
              s = random.choice(status)
              cl.sendText(msg.to,"• Nama : "+cl.getContact(msg.from_).displayName+"\n• Kelamin : "+k+"\n• Wajah : "+w+"\n• Status Kehidupan : "+s)
#-------------Fungsi Pap-----------------------------#
            elif "Blacklist all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Blacklist all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Semua Telah Di Hapus")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Success Boss")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")
            
            elif "Unban all" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban all","")
						gs = cl.getGroup(msg.to)
						cl.sendText(msg.to,"Semua Telah Di Hapus")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Tidak Ada Boss Syahraqa")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
								except:
									cl.sendText(msg.to,"Done Boss Syahraqa")
									
            elif "Gimage " in msg.text:
                      googl = msg.text.replace("Gimage ","")
                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl
                      raw_html = (download_page(url))
                      items = []
                      items = items + (_images_get_all_items(raw_html))
                      path = random.choice(items)
                      try:
                          start = time.time()
                          cl.sendImageWithURL(msg.to,random.choice(items))
                          cl.sendImageWithURL(msg.to,random.choice(items))
                          cl.sendImageWithURL(msg.to,random.choice(items))
                          cl.sendText(msg.to,"Total Image Links ="+str(len(items)))
                      except Exception as njer:
		            cl.sendText(msg.to, str(njer))
    
            elif "Pap set:" in msg.text:
                wait["Pap"] = msg.text.replace("Pap set:","")
                cl.sendText(msg.to,"Pap Has Ben Set To")
                
            elif msg.text in [".Pap","Pap"]:
                cl.sendImageWithURL(msg.to,wait["Pap"])
#-------------Fungsi Pap-----------------------------#

#---------------Mention Tag--------------------------#
            elif "!say " in msg.text.lower():
                    query = msg.text.replace("!say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'af', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Surat:" in msg.text.lower():
               try:
                  sep = msg.text.split(" ")
                  surah = int(text.lower().replace(sep[0] + " ",""))
                  if 0 < surah < 115:
                      if surah not in [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 18, 20, 21, 23, 26, 37]:
                          if len(str(surah)) == 1:
                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                              cl.sendAudioWithURL(msg.to, audionya)
                          elif len(str(surah)) == 2:
                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                              cl.sendAudioWithURL(msg.to, audionya)
                          else:
                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                              cl.sendAudioWithURL(msg.to, audionya)
                      else:
                          cl.sendText(msg.to, "Surah terlalu panjang")
                  else:
                      cl.sendText(msg.to, "Quran hanya 114 surah")
              except Exception as error:
                  cl.sendText(msg.to, "error\n"+str(error))

            elif "neon: " in msg.text.lower():
                    try:
                        txt = msg.text.split(" ")
                        teks = msg.text.lower().replace("neon: ","")
                        color = ["red","yellow","green","purple","violet","blue"]
                        k = random.choice(color)
                        foto = "https://ari-api.herokuapp.com/neon?text="+teks+"&color="+k+""
                        cl.sendImageWithURL(msg.to, foto)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif "@say " in msg.text.lower():
                    query = msg.text.replace("@say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'sq', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "#say " in msg.text.lower():
                    query = msg.text.replace("#say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'ar', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "$say " in msg.text.lower():
                    query = msg.text.replace("$say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'hy', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "%say " in msg.text.lower():
                    query = msg.text.replace("%say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'zh', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "^say " in msg.text.lower():
                    query = msg.text.replace("^say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'nl', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "&say " in msg.text.lower():
                    query = msg.text.replace("&say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'fr', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "*say " in msg.text.lower():
                    query = msg.text.replace("*say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'de', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "(say " in msg.text.lower():
                    query = msg.text.replace("(say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif ")say " in msg.text.lower():
                    query = msg.text.replace(")say ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'id', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-ja " in msg.text.lower():
                    query = msg.text.replace("Say-ja ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'ja', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-ko " in msg.text.lower():
                    query = msg.text.replace("Say-ko ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'ko', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-it " in msg.text.lower():
                    query = msg.text.replace("Say-it ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'it', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-la " in msg.text.lower():
                    query = msg.text.replace("Say-la ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'la', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)

            elif "Halo" in msg.text:
              if msg.from_ in admin:
                  sendMentionV2(op.param1, "Halo @! juga", [op.param2])

            elif "Say-pt " in msg.text.lower():
                    query = msg.text.replace("Say-pt ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'pt', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-ro " in msg.text.lower():
                    query = msg.text.replace("Say-ro ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'ro', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-ru " in msg.text.lower():
                    query = msg.text.replace("Say-ru ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'ru', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-es " in msg.text.lower():
                    query = msg.text.replace("Say-es ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'es', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-th " in msg.text.lower():
                    query = msg.text.replace("Say-th ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            
            elif "Say-vi " in msg.text.lower():
                    query = msg.text.replace("Say-vi ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'vi', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
                        
            elif "Say-jw " in msg.text.lower():
                    query = msg.text.replace("Say-jw ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'jw', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
                        
            elif "Say-su " in msg.text.lower():
                    query = msg.text.replace("Say-su ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'su', 'speed': '1', 'query': query}
                        r = s.get(url, params=params)
                        mp3 = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
                        
            elif "@🎋Syahraqaa🐾" in msg.text:
                tanya = msg.text.replace("@🎋Syahraqaa🐾 ","")
                jawab = ("Jangan Tag Si 🎋Syahraqaa🐾!!","Berisik jangan tag si 🎋Syahraqaa🐾 dia masih tidur")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#---------------Mention Tag--------------------------#

#---------------STALK--------------------------------#
#            elif "Stalk " in msg.text:
#                 print "[Command]Stalk executing"
#                 stalkID = msg.text.replace("Stalk ","")
#                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
#                 files = glob.glob("tmp/*.jpg")
#                 for file in files:
#                     os.rename(file,"tmp/tmp.jpg")
#                 fileTmp = glob.glob("tmp/tmp.jpg")
#                 if not fileTmp:
#                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
#                     print "[Command]Stalk executed - no image found"
#                 else:
#                     image = upload_tempimage(client)
#                     cl.sendText(msg.to, format(image['link']))
#                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
#                     print "[Command]Stalk executed - succes"
#---------------STALK--------------------------------#

#-------------------FUNGSI RESTART---------------------#
            elif msg.text in ["restart"]:
	 	        if msg.from_ in admin:
	 	            cl.sendText(msg.to, "Tunggu Sebentar..")
	 	            cl.sendText(msg.to, "Bot has been restarted")
		            restart_program()
		            print "@Restart"
	        	else:
		            cl.sendText(msg.to, "No Access")
#-------------------FUNGSI RESTART---------------------#

            elif msg.text in ["Kreator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                jawab = ("This is my Creator","My creator is handsome","My creator is cool")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
#-----------------------------------------------
            elif "Cek " in msg.text:
                tanggal = msg.text.replace("Cek ","")
                r=requests.get('http://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
                
            elif "Pict group " in msg.text:
                saya = msg.text.replace('Pict group ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                        
#------------------------CHECK SYSTEM------------------------#    
                         
            elif msg.text.lower().startswith("story "):
                            sep = msg.text.replace("story ","")
                            url = "http://rahandiapi.herokuapp.com/instastory/"+sep+"?key=betakey"
                            with requests.session() as web:
                                web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["url"] != []:
                                    items = data["url"]["link"]
                                    cl.sendImageWithURL(msg.to, items)
                                    
            elif msg.text.lower().startswith("sholat "):
                location = msg.text.replace("sholat ","")
                params = {'lokasi':location}
                with requests.session() as web:
                    r = requests.get("http://api.corrykalam.net/apisholat.php?" + urllib.urlencode(params))                      
                    data = r.text
                    data = json.loads(data)
                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                        ret_ = "[ Prayer Schedule ]"
                        ret_ += "\n\nLocation : " + data[0]
                        ret_ += "\n" + data[1]
                        ret_ += "\n" + data[2]
                        ret_ += "\n" + data[3]               
                        ret_ += "\n" + data[4]
                        ret_ += "\n" + data[5]
                    else:
                           ret_ = "[ Prayer Schedule ] Error : Location not found" 
                    cl.sendText(msg.to, str(ret_))
            
            elif msg.text.lower().startswith("lokasi "):
                location = msg.text.lower().replace("lokasi ","")
                params = {'lokasi':location}
                with requests.session() as web:
                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                    r = requests.get("http://api.corrykalam.net/apiloc.php?"+ urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    if data[0] != "" and data[1] != "" and data[2] != "":
                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                        ret_ = "[ Details Location ]"
                        ret_ += "\n\nLocation : " + data[0]
                        ret_ += "\nGoogle Maps : " + link
                    else:
                           ret_ = "[ Details Location ] Error : Location not found"
                    cl.sendText(msg.to, str(ret_))
            
            elif msg.text.lower().startswith("twitter "):               
                       user = msg.text.lower().replace("twitter ","")
                       with requests.session() as s: 
                            s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0' 
                            url    = 'https://twitter.com/'+user
                            r    = s.get(url)
                            soup = BeautifulSoup(r.content, 'html5lib')
                            hasil = soup.select_one('.ProfileHeaderCard')
                            hasil = hasil.findAll(msg.text)
                            tweet = soup.find('span', class_ = 'ProfileNav-value').get_text()
                            fllwng = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--following').get_text()
                            fllwr = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--followers').get_text()
                            fav = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--favorites').get_text()
                            img = soup.find('img', class_ = 'ProfileAvatar-image')
                            cl.sendImageWithURL(msg.to,img['src'])
                            cl.sendMessage(msg.to,'Name: '+hasil[2]+'\nUsername: '+hasil[7]+hasil[8]+'\nBio: '+hasil[12]+hasil[13]+' '+hasil[15]+hasil[16]+'\nLoc: '+hasil[20]+'\nWeb: '+hasil[26]+'\nJoined: '+hasil[32]+'\nBorn: '+hasil[37])
                            cl.sendMessage(msg.to,'Tweets: '+tweet+'\nFollowing: '+fllwng.replace('Following','')+'\nFollowers: '+fllwr.replace('Followers','')+'\nLikes:'+fav.replace('Likes',''))
                            
            elif msg.text.lower().startswith("image "):
                            sep = msg.text.replace("image ","")
                            url = "http://rahandiapi.herokuapp.com/imageapi?key=betakey&q="+sep+""
                            with requests.session() as web:
                                web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendImageWithURL(msg.to, str(path))
        
            elif msg.text.lower().startswith("cuaca "):
                location = msg.text.lower().replace("cuaca ","")
                with requests.session() as web:
                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                    r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib2.quote(location)))
                    data = r.text
                    data = json.loads(data)
                    if "result" not in data:
                        ret_ = "╔══『 Status Cuaca 』"
                        ret_ += "\n╠ ⌬.「 Lokasi 」 : " + data[0].replace("Temperatur di kota ","")
                        ret_ += "\n╠ ⌬.「 Suhu 」 : " + data[1].replace("Suhu : ","")
                        ret_ += "\n╠ ⌬.「 Kelembaban 」: " + data[2].replace("Kelembaban : ","")
                        ret_ += "\n╠ ⌬.「 Tekanan Udara 」 : " + data[3].replace("Tekanan udara : ","")
                        ret_ += "\n╠ ⌬.「 Kecepatan Angin」 : " + data[4].replace("Kecepatan angin : ","")
                        ret_ += "\n╚══『 Status Cuaca 』"
                    else:
                        ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                    cl.sendText(msg.to, str(ret_))
              
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == "cfotogroup":
                if msg.from_ in admin:
                  wait["cpg"] = True
                  cl.sendText(msg.to,"please send an image for group profile.")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
            elif msg.text.lower() == "changepict":
                if msg.from_ in admin:
                   wait["cpp"] = True
                   cl.sendText(msg.to,"please send an image")
                else:
                	 cl.sendText(msg.to,"command denied")
                	 cl.sendText(msg.to,"creator permission recuired")
#============================================================================================================
            elif msg.text.lower() == "join url":
                if msg.from_ in admin:
                   wait["linkticket"] = True
                   cl.sendText(msg.to,"please send a link URL to me")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                 
#--------------------------------- INSTAGRAM --------------------------------
 #           elif "http://line.me/R/ti/g/" in msg.text.lower():
  #                           if wait["linkticket"] == True:
        #                            tiket = msg.text.replace("http://line.me/R/ti/g/","")
               #                     bahan = "http://line.me/R/ti/g/" + tiket
               #                     group = cl.findGroupByTicket(bahan)
                  #                  cl.acceptGroupInvitationByTicket(group.id,bahan)
                       #             wait["linkticket"] = False
               #                     cl.sendText(msg.to, "succes joined to group %s" % str(group.name))
                         
            elif 'ytmp3: ' in text:
               url_= text.replace('ytmp3: ','')
               params = {'key':'betakey','q':url_}
               path = 'http://rahandiapi.herokuapp.com/youtubeapi?'
               r = requests.get(path,params=params).json()
               cl.sendText(msg.to, r['result']['audiolist'][4]['url'])

            elif "/lirik " in msg.text:
                    try:
                        instagram = msg.text.replace("/lirik ","")
                        response = requests.get("http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q="+instagram+"")
                        data = response.json()
                        pictig = str(data['title'])
                        hasil = str(data['lyric'])
                        text = "Judul : "+pictig+"\n\n"+hasil+""
                        cl.sendText(msg.to, text)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
           
            elif "Screen " in msg.text:
                    try:
                        print "[SCREEN]"
                        instagram = msg.text.replace("Screen ","")
                        response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link=www.instagram.com/"+instagram+"")
                        data = response.json()
                        pictig = data['result']
                        cl.sendImageWithURL(msg.to, pictig)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
              
            elif "Cvid " in msg.text:
                    try:
                        print "[CVID]"
                        instagram = msg.text.replace("Cvid ","")
                        cl.sendText(msg.to, "Tunggu video sedang di proses!")
                        response = requests.get("http://rahandiapi.herokuapp.com/instapost/"+instagram+"/1?key=betakey")
                        data = response.json()
                        post = str(data['media']['mediatype'])
                        caption = str(data['media']['caption'])
                        comment = str(data['media']['comment_count'])
                        likec = str(data['media']['like_count'])
                        profiley = data['media']['url']
                        textnya = "Post Ke : "+post+"\nCaption : "+caption+"\nJumlah Comment : "+comment+"\nJumlah Like : "+likec+""
                        cl.sendVideoWithURL(msg.to, profiley)
                        cl.sendText(msg.to, str(textnya))
                    except Exception as e:
                        cl.sendText(msg.to, "Akunmu private/tidak ditemukan!")
                        
            elif "Cpost " in msg.text:
                    try:
                        print "[CPOST]"
                        instagram = msg.text.replace("Cpost ","")
                        cl.sendText(msg.to, "Tunggu foto sedang di proses!")
                        response = requests.get("http://rahandiapi.herokuapp.com/instapost/"+instagram+"/1?key=betakey")
                        data = response.json()
                        post = str(data['media']['mediatype'])
                        caption = str(data['media']['caption'])
                        comment = str(data['media']['comment_count'])
                        likec = str(data['media']['like_count'])
                        profiley = data['media']['url']
                        textnya = "Post Ke : "+post+"\nCaption : "+caption+"\nJumlah Comment : "+comment+"\nJumlah Like : "+likec+""
                        cl.sendImageWithURL(msg.to, profiley)
                        cl.sendText(msg.to, str(textnya))
                    except Exception as e:
                        cl.sendText(msg.to, "Akunmu private/tidak ditemukan!")
                        
            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendImageWithURL(msg.to, profileIG)
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif "/ti/g/" in msg.text:
              if msg.from_ in admin:
                   if wait["atjointicket"] == True:
                  	tiket = msg.text.replace("/ti/g/","")     
                        group = cl.findGroupByTicket(tiket)
                        cl.sendText(msg.to, "I've found group name 「%s」 Trying to join" % str(group.name))
                        cl.acceptGroupInvitationByTicket(group.mid,tiket)
                        cl.sendText(msg.to, "Succes to join group 「%s」" % str(group.name))
  #                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
 #                     links = link_re.findall(text)
   #                   n_links = []
   #                   for l in links:
 #                         if l not in n_links:
  #                            n_links.append(l)
  #                    for ticket_id in n_links:
   #                       group = cl.findGroupByTicket(ticket_id)
   #                       cl.sendText(msg.to, "I've found group name 「%s」 Trying to join" % str(group.name))
   #                       cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
    #                      cl.sendText(msg.to, "Succes to join group 「%s」" % str(group.name))
                          
            elif 'instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
                	
            elif "/postig" in msg.text:
              if msg.from_ in admin:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 2):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                        
            elif "yt: " in msg.text.lower():
                query = msg.text.split(":")
                try:
                    if len(query) == 3:
                        isi = yt(query[2])
                        hasil = isi[int(query[1])-1]
                        cl.sendText(msg.to, 'Hasil Pencarian = ' + str(len(isi)) + " ini adalah hasil pencarian ke [" + str(query[1]) + "]")
                        cl.sendText(msg.to, hasil)
                    else:
                        isi = yt(query[1])
                        cl.sendText(msg.to, "Hasil Pencarian = " + str(len(isi)))
                        cl.sendText(msg.to, isi[0])
                except Exception as e:
                    print(e)
                    
            elif "/ig " in msg.text.lower():
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig ","")
                nk1 = nk0.rstrip('  ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s http://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"Tunggu Sebentar...")
                        cl.sendText(msg.to,"Profile "+username+"\n\nUrl : https://www.instagram.com/"+username+"\n\nUsername : "+username+"\nLink : "+url+"\nFull Name : "+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following)) 
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found... Contoh /ig boomsyah")
                else:
                    cl.sendText(msg.to,"Contoh /ig boomsyah")
#----------------------------------------------------------------------------
            elif 'wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "http://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            
            elif "Steal group pict" in msg.text:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithURL(msg.to,path)
            
            elif "Turn off bots" in msg.text:
               if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
            
            elif "Bot1 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot1 rename:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"change name: "+string+"\nsucces")
                    
            elif "Steal bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
            
            elif "Message:" in msg.text:
              if msg.from_ in admin:
                wait["message"] = msg.text.replace("Message:","")
                cl.sendText(msg.to,"bot message\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif "Add message:" in msg.text:
              if msg.from_ in admin:
                wait["message"] = msg.text.replace("Add message:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
                  
            elif "Update welcome:" in msg.text:
              if msg.from_ in admin:
                wait["welmsg"] = msg.text.replace("Update welcome:","")
                cl.sendText(msg.to,"update welcome message succes"+ datetime.today().strftime('%H:%M:%S'))
            
            elif "Sider on" in msg.text:
              ginfo = cl.getGroup(msg.to)
              gCreator = ginfo.creator.mid
              if msg.from_ in gCreator:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
              ginfo = cl.getGroup(msg.to)
              gCreator = ginfo.creator.mid
              if msg.from_ in gCreator:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Heh Belom Di Set")
                    
            elif "Sider on" in msg.text:
              if msg.from_ in admin:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
              if msg.from_ in admin:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Heh Belom Di Set")
        
            elif msg.text in ["Check welcome message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])
                    
            elif msg.text in ["Check message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
                    
            elif msg.text in ["sticker on"]:
               if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
               else:
                     pass
     
            elif msg.text in ["Welcome message:on"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on")
            
            elif msg.text in ["Welcome message:off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))           
            
#===========================================
            elif msg.text.lower() == 'responsename':
                profile = cl.getProfile()
                text = profile.displayName + ""
                cl.sendText(msg.to, text)

#===============================================
            elif msg.text in ["debug speed","Debug speed"]:
                cl.sendText(msg.to, "Measuring...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
#========================================

            elif 'group list' in msg.text.lower():
                gs = cl.getGroupIdsJoined()
                L = "『 Groups List 』\n"
                for i in gs:
                    L += "[≫] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                
            elif "Autolike" in msg.text:
                if msg.from_ in admin:
                    autoLike()
                    time.sleep(500)
                    
#---------------------------------- SONG ------------------------------------

            elif "yt:" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        cl.sendText(msg.to, str(ret_))
             
            elif "/lirik" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                cl.sendText(msg.to, str(ret_))
                        except:
                            cl.sendText(msg.to, "Lirik tidak ditemukan")
           
            elif "/lagu" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ reading Audio ]"
                                cl.sendText(msg.to, str(ret_))
                                cl.sendAudioWithURL(msg.to, song[3])
                        except:
                            cl.sendText(msg.to, "Musik tidak ditemukan")
#----------------------------------------------------------------------------

#--------------------------------- YOUTUBE ----------------------------------
#            elif "/youtube " in msg.text:
#                query = msg.text.replace("/youtube ","")
#                with requests.session() as s:
#                    s.headers['user-agent'] = 'Mozilla/5.0'
#                    url = 'http://www.youtube.com/results'
#                    params = {'search_query':query}
#                    r = s.get(url, params=params)
#                    soup = BeautifulSoup(r.content, 'html5lib')
#                    hasil = ""
#                    for a in soup.select('.yt-lockup-title > a[title]'):
#                        if '&list=' not in a['href']:
#                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
#                    cl.sendText(msg.to,hasil)
#                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------

#-------------------------------- PP BY TAG ---------------------------------
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#--------------------------------- TRANSLATE -------------------------------
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO ENGLISH----\n" + "" + result + "\n------SUKSES-----")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM EN----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif "/id " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("/id ","")
                try:
                   translator = Translator()
                   trs = translator.translate(txt,'id')
                   A = trs.text
                   A = A.encode('utf-8')
                   cl.sendText(msg.to,A)
                   print '[Command] Translate ID'
                except:
                   cl.sendText(msg.to,'Failed.')
                   
            elif "/eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("/eng ","")
                try:
                   translator = Translator()
                   trs = translator.translate(txt,'en')
                   A = trs.text
                   A = A.encode('utf-8')
                   cl.sendText(msg.to,A)
                   print '[Command] Translate EN'
                except:
                   cl.sendText(msg.to,'Failed.')
                   
            elif "tr-en " in msg.text:
                txt = msg.text.replace("tr-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "tr-id " in msg.text:
                txt = msg.text.replace("tr-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
            
#----------------------------------------------------------------------------
            elif text.lower() == '/about':
                    try:
                        arr = []
                        owner = "ud4082219b6754e7b610f84d07d3b436b"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(owner)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[ About Public Bot ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠═══════"
                        ret_ += "\n╠ Version : Public Bot 1"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚═══════"
                        cl.sendText(msg.to, str(ret_))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
              
            elif text.lower() == 'groupinfo':
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    cl.sendText(msg.to, str(ret_))
                    cl.sendImageWithURL(msg.to, path)
                    
            elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        cl.sendText(msg.to, str(ret_))
          
            elif "Searchid: " in msg.text:
                msgg = msg.text.replace('Searchid: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)
#--------------------------------- HI / HAI ---------------------------------
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
                
#=================================================
            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))

            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
                        
            elif msg.text == "Lurking":
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    
            elif msg.text == "Lurking Result":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʙᴇғᴏʀᴇ ʀᴇᴀᴅ ᴛʜᴇ sɪᴅᴇʀs")
						
#========================================
                
            elif msg.text.lower() in ["hi","hai","apa"]:
                if msg.from_ in admin:
                    beb = "Hi sayang " + cl.getContact(msg.from_).displayName #+ " 􀸂􀆇starry heart􏿿"
                    cl.sendText(msg.to,beb)
                else:
                    hi = "Hi " + cl.getContact(msg.from_).displayName
                    cl.sendText(msg.to,hi)
#----------------------------------------------------------------------------
#--------------------------------- DUGEM ------------------------------------
            elif 'crash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub8530f15ff4020c3cc2d1ad2f066aa4b',"}
                cl.sendMessage(msg)

            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#----------------------------------------------------------------------------
#--------------------------------- Remove Chat ------------------------------
            elif "/removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#----------------------------------------------------------------------------

#------------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#-----------------------------------------------
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)

            elif "Rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Rename:","")
                if len(string.decode('utf-8')) <= 999999999:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    
            elif "Sampul @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Sampul @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
                
            elif "Midpict " in msg.text:
                umid = msg.text.replace("Midpict ","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Ambilkan " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Ambilkan ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
                    
            elif "Setpoint" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "Read" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "++++TERCIDUK++++\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
			
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
	              
            elif msg.text in ["welcome","Welcome","Wc","wc","kam","Kam"]:
                cl.sendText(msg.to,"ѕєℓαмαт ∂αтαиg вσѕкυ! ѕємσgα вєтαн ∂ιѕιиι уα!")
                
            elif msg.text in ["Say-","say","Say","say-"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,meMessage)
                else:
                    cl.sendText(msg.to, "error")
                    
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            
#----------------------
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya " + tanya + "adalah " + jawaban + " Banyak banyak tobat Nak ")
#----------------------
	    elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("0%","20%","40%","50%","60%","Tak ada")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")

            elif "/InviteMeTo: " in msg.text:
                if msg.from_ in owner:
                    gid = msg.text.replace("/InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.sendText(msg.to,"Tunggu sebentar..")
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin pasukan tidak di dalam grup itu!")
                            
            elif "Saan copy @" in msg.text:
                if msg.from_ in owner:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Saan copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.cloneContactProfile(target)
                               cl.sendText(msg.to, "Succes Copy profile ~")
                            except Exception as e:
                                print e
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
            
            elif "Steal mid" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
                
            elif "Steal contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
              
            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
                
            elif "stealgroupimage" in msg.text:
                group = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Gambar Grup :\n=> http://dl.profile.line-cdn.net/" + group.pictureStatus)
                
            elif msg.text in ["Backup","backup"]:
              if msg.from_ in owner:
                    try:
                       cl.updateDisplayPicture(mybackup.pictureStatus)
                       cl.updateProfile(mybackup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
                    
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
                    
            elif "Spam @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"ƠƬƜ ƧƤƛM ƬƛƦƓЄƬ 😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  ��")
                       cl.sendText(g.mid,"Spam  ����")
                       cl.sendText(g.mid,"Spam  ??")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  ??")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  ��")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  ??")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  ��")
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")  
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"Spam  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  ��")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(msg.to, "ƊƠƝЄ ƧƤƛM  😂")
                       print "Done spam" 
            
#----------------------------- TAG ALL MEMBER -------------------------------
            elif msg.text in ["tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "Done : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
            
            elif msg.text in ["Panggil semua"]:
			      group = cl.getGroup(msg.to)
			      nama = [contact.mid for contact in group.members]
			      nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
			      if jml <= 100:
			         mention(msg.to, nama)
			      if jml > 100 and jml < 200:
			         for i in range (0, 99):
			                nm1 += [nama[i]]
			         mention(msg.to, nm1)
			         for j in range (100, len(nama)-1):
			                nm2 += [nama[j]]
			         mention(msg.to, nm2)
			      if jml > 200 and jml < 300:
			         for i in range (0, 99):
			                nm1 += [nama[i]]
			         mention(msg.to, nm1)
			         for j in range (100, 199):
			                nm2 += [nama[j]]
			         mention(msg.to, nm2)
			         for k in range (200, len(nama)-1):
			                nm3 += [nama[k]]
			         mention(msg.to, nm3)       
			      if jml > 300 and jml < 400:
			         for i in range (0, 99):
			                nm1 += [nama[i]]
			         mention(msg.to, nm1)
			         for j in range (100, 199):
			                nm2 += [nama[j]]
			         mention(msg.to, nm2)
			         for k in range (200, 299):
			                nm3 += [nama[k]]
			         mention(msg.to, nm3)           
			         for l in range (300, len(nama)-1):
			             nm4 += [nama[l]]
			         mention(msg.to, nm4)
			      cnt = Message()
			      cnt.text = "Done:"+str(jml)
			      cnt.to = msg.to
			      cl.sendMessage(cnt)
#----------------------------------------------------------------------------

            elif "Check:" in msg.text:
                midd = msg.text.replace("Check:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":midd}
                cl.sendMessage(msg)

            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"()Update Names👉 " + string + "👈 ")
                       
            elif "Spam " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 60:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 100:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
            
            elif msg.text in ["Lang-list"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,sayMessage)
                else:
                    cl.sendText(msg.to, "error")
                    
            elif msg.text in ["Saan Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, keyMessage)
                    c = Message(to=msg.to, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                    cl.sendMessage(c)
                else:
                    cl.sendText(msg.to, "error")
                    
            elif msg.text in ["/public","/Public","/publik"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, publicMessage)
                    c = Message(to=msg.to, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                    cl.sendMessage(c)
                else:
                    cl.sendText(msg.to, "error")
            
            elif msg.text in ["/siders","/Siders","/sider"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, sidersMessage)
                    c = Message(to=msg.to, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                    cl.sendMessage(c)
                else:
                    cl.sendText(msg.to, "error")
            
            elif msg.text in ["/newfiture","/Newfiture","/new fiture"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, newMessage)
                    c = Message(to=msg.to, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                    cl.sendMessage(c)
                else:
                    cl.sendText(msg.to, "error")
     
            elif msg.text in ["/searching","/Searching","/search"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, searchingMessage)
                    c = Message(to=msg.to, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                    cl.sendMessage(c)
                else:
                    cl.sendText(msg.to, "error")
                    
            elif msg.text in ["/cancel","/Cancel","/cncel"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, cancelMessage)
                    c = Message(to=msg.to, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                    cl.sendMessage(c)
                else:
                    cl.sendText(msg.to, "error")
            
            elif "Saan copy @" in msg.text:
            	if msg.from_ in owner:
                  print "[COPY] Ok"
                  _name = msg.text.replace("Saan copy @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                      if _nametarget == g.displayName:
                           targets.append(g.mid)
                      if targets == []:
                          cl.sendText(msg.to, "Not Found...")
                      else:
                          for target in targets:
                               try:
                                  cl.CloneContactProfile(target)
                                  cl.sendText(msg.to, "Succes Copy profile ~")
                               except Exception as e:
                                   print e
                                
            elif msg.text in ["Gcreator:inv"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                   ginfo = cl.getGroup(msg.to)
                   gCreator = ginfo.creator.mid
                   try:
                      cl.findAndAddContactsByMid(gCreator)
                      cl.inviteIntoGroup(msg.to,[gCreator])
                      print "success inv gCreator"
                   except:
                      pass
                  
            elif msg.text in ["Gcreator:kick"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                   ginfo = cl.getGroup(msg.to)
                   gCreator = ginfo.creator.mid
                   try:
                      cl.kickoutFromGroup(msg.to,[gCreator])
                      print "success inv gCreator"
                   except:
                      pass
            
            elif msg.text in ["Gas unicode"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Hello!3xploi7 BuG.1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.")
                
            elif msg.text in ["Creator","creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ub8530f15ff4020c3cc2d1ad2f066aa4b'}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ud4082219b6754e7b610f84d07d3b436b'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Ini contact bos aku!↖")
                  
  #          elif msg.text in ["Reject invite"]:
   #           if msg.from_ in admin:
   #                  gid = cl.getGroupIdsInvited()
     #                for i in gid:
       #                  cl.rejectGroupInvitation(i)
       #              if wait["lang"] == "JP":
        #                 cl.sendText(msg.to,"All invitations have been rejected")
    #                 else:
       #                  cl.sendText(msg.to,"Done")
                   
            elif ("Saan Haey " in msg.text):
               if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           random.choice(KAC).kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
                          
#-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Tag all"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = "" 
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
    
    #-------------Fungsi Tagall User Finish By :ᴋᴀʀɪᴀ -------------#
    #-------REMOTE MODE-----------#
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = True
                    cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = False
                    cl.sendText(msg.to,"Success deactive simisimi")
         #-------REMOTE MODE-----------#
                                   
            elif "/Spam: " in msg.text:
                    cond = msg.text.split(" ")
                    value = int(cond[2])
                    text = msg.text.replace("/Spam: " + str(cond[1]) + " " + str(value) + " ","")
                    ballon1 = value * (text + "\n")
                    if cond[1] == "on":
                        if value <= 10:
                            for x in range(value):
                                cl.sendText(msg.to, text)
                        else:
                            cl.sendText(msg.to,"Jumlah spamming melebihi batas. Max 10")
                    elif cond[1] == "off":
                        if value <= 100:
                            cl.sendText(msg.to,ballon1)
                        else:
                            cl.sendText(msg.to,"Jumlah spamming melebihi batas")
                    else:
                        cl.sendText(msg.to,"Error condition")
            
            
            elif "Admin add @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Admin remove @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif msg.text in ["Adminlist","adminlist"]:
                if admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
                    
            elif ("Saan Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Saan Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    
            elif ("Cv1 gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                
 #================================================================           
            elif msg.text in ["Invite user"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
#============================================================

            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
                
            elif "Leave all" in msg.text:
              if msg.from_ in owner:
               gid = cl.getGroupIdsJoined()
               for a in gid:
                   cl.leaveGroup(a)
                 
            elif "Cv1 Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#-----------------------------------------------
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
                
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
                
            elif "Getgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
                
            elif "Urlgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
                
            elif "Steal " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
#-----------------------------------------------
            elif "Steal @" in msg.text:
                    if msg.toType == 2:
                        steal = msg.text.replace("Steal @","")
                        stealname = steal.rstrip(" ")
                        group = cl.getGroup(msg.to)
                        targets = []
                        if steal == "":
                            cl.sendText(msg.to,"Invalid user")
                        else:
                            for i in group.members:
                                if stealname == i.displayName:
                                    targets.append(i.mid)
                            if targets == []:
                                cl.sendText(msg.to,"User tidak ditemukan")
                            else:
                                for target in targets:
                                    try:
                                        contact = cl.getContact(target)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        try:
                                            cover = cl.channel.getCover(contact)
                                        except:
                                            cover = ""
                                        try:
                                            cl.sendText(msg.to,"Gambar Foto Profilenya")
                                            cl.sendImageWithURL(msg.to,image)
                                            if cover == "":
                                                cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                                            else:
                                                cl.sendText(msg.to,"Gambar Covernya")
                                                cl.sendImageWithURL(msg.to,cover)
                                        except Exception as error:
                                            cl.sendText(msg.to,(error))
                                            break
                                    except:
                                        cl.sendText(msg.to,"Error!")
                                        break
                    else:
                        cl.sendText(msg.to,"Tidak bisa dilakukan di luar wilayah")
#-----------------------------------------------
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}                
                cl.sendMessage(msg)   
            elif msg.text in ["Bot Started"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}                
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Kmid}                
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Lmid}                
                cl.sendMessage(msg)
            elif msg.text in ["Cv1"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
            elif msg.text in ["Cv2"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                cl.sendMessage(msg)
                
            elif msg.text.lower() == 'spam gift':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                
#            elif msg.text in ["Saan cancel","Saan Cancel"]:
#                if msg.toType == 2:
#                    X = cl.getGroup(msg.to)
            #        if X.invitee is not None:
     #                   gInviMids = [contact.mid for contact in X.invitee]
                 #       cl.cancelGroupInvitation(msg.to, gInviMids)
      #              else:
                  #      if wait["lang"] == "JP":
          #                  cl.sendText(msg.to,"No one is inviting")
       #                 else:
           #                 cl.sendText(msg.to,"Sorry, nobody absent")
        #        else:
         #           if wait["lang"] == "JP":
                   #     cl.sendText(msg.to,"Can not be used outside the group")
            #        else:
                       # cl.sendText(msg.to,"Not for use less than group")
                        
      #      elif msg.text in ["Cv cancel","Bot cancel"]:
             #   if msg.toType == 2:
      #              G = cl.getGroup(msg.to)
       #             if G.invitee is not None:
  #                      gInviMids = [contact.mid for contact in G.invitee]
  #                      cl.cancelGroupInvitation(msg.to, gInviMids)
   #                 else:
   #                     if wait["lang"] == "JP":
      #                      cl.sendText(msg.to,"No one is inviting")
   #                     else:
   #                         cl.sendText(msg.to,"Sorry, nobody absent")
    #            else:
  #                  if wait["lang"] == "JP":
    #                    k3.sendText(msg.to,"Can not be used outside the group")
  #                  else:
      #                  k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
                
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            #-----------------------------------------------
            elif "Steal " in msg.text:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
                        
#-----------------------------------------------
            elif "Steal @" in msg.text:
                    if msg.toType == 2:
                        steal = msg.text.replace("Steal @","")
                        stealname = steal.rstrip(" ")
                        group = cl.getGroup(msg.to)
                        targets = []
                        if steal == "":
                            cl.sendText(msg.to,"Invalid user")
                        else:
                            for i in group.members:
                                if stealname == i.displayName:
                                    targets.append(i.mid)
                            if targets == []:
                                cl.sendText(msg.to,"User tidak ditemukan")
                            else:
                                for target in targets:
                                    try:
                                        contact = cl.getContact(target)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        try:
                                            cover = cl.channel.getCover(contact)
                                        except:
                                            cover = ""
                                        try:
                                            cl.sendText(msg.to,"Gambar Foto Profilenya")
                                            cl.sendImageWithURL(msg.to,image)
                                            if cover == "":
                                                cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                                            else:
                                                cl.sendText(msg.to,"Gambar Covernya")
                                                cl.sendImageWithURL(msg.to,cover)
                                        except Exception as error:
                                            cl.sendText(msg.to,(error))
                                            break
                                    except:
                                        cl.sendText(msg.to,"Error!")
                                        break
                    else:
                        cl.sendText(msg.to,"Tidak bisa dilakukan di luar wilayah")
#-----------------------------------------------

            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["TL:"]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
              if msg.from_ in owner:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = cl.getProfile()
                    profile_B.displayName = string
                    cl.updateProfile(profile_B)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = cl.getProfile()
                    profile_B.displayName = string
                    cl.updateProfile(profile_B)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
              if msg.from_ in admin:                                
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
              if msg.from_ in admin:                                 
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:                                
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:                                
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
              if msg.from_ in admin:                               
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin:                                
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin:                                 
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin:                                
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin:                               
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
                        
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
       #     elif msg.text in ["Saan Cancelall","Cancelall"]:
  #              gid = cl.getGroupIdsInvited()
      #          for i in gid:
   #                cl.rejectGroupInvitation(i)
        #        if wait["lang"] == "JP":
          #          cl.sendText(msg.to,"All invitations have been refused")
        #        else:
       #             cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:                                
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:                                
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
              if msg.from_ in admin:                                
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
              if msg.from_ in admin:                                 
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
              if msg.from_ in admin:                                
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã���‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
              if msg.from_ in admin:                                 
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
              if msg.from_ in admin:                                
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:                                 
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
              if msg.from_ in admin:                                
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢��èª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
              if msg.from_ in owner:                                 
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
              if msg.from_ in owner:                                 
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
              if msg.from_ in owner:                                 
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
                    
            elif "Upname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Upname:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
                    
            elif msg.text in ["Up"]:
              if msg.from_ in owner:                                 
                if wait["cName"] == True:
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"]
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name Update!")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "$set":                               
                    cl.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":                              
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
                        
            elif msg.text == "Cctv":
                    cl.sendText(msg.to, "Cek CCTV")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Ciduk":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "||Di Read Oleh||%s\n||By : Saan BOT||\n\n>Pelaku CCTV<\n%s-=CCTV=-\n•Bintitan\n•Panuan\n•Kurapan\n•Kudisan\n\nAmiin Ya Allah\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Koplak\nBaru Ketil Ciduk\nDASAR PIKUN ♪")
            
            elif "Set member: " in msg.text:
		        if msg.from_ in admin:
		            jml = msg.text.replace("Set member: ","")
		            wait["Members"] = int(jml)
		            cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

#-------Cek sider biar mirip kek siri-----------------------------
            elif "Setlastpoint" in msg.text:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "csider off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Cek Sider already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "Viewlastseen" in msg.text:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Sider:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
                    
            elif msg.text == "check":
                      cl.sendText(msg.to, "I have set a read point ♪\n「lihat」I will show you who I have read ♪")
                      try:
                          del wait2['readPoint'][msg.to]
                          del wait2['readMember'][msg.to]
                      except:
                          pass
                      wait2['readPoint'][msg.to] = msg.id
                      wait2['readMember'][msg.to] = ""
                      wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                      wait2['ROM'][msg.to] = {}
                      print wait
            if msg.text == "lihat":                            
                      if msg.to in wait2['readPoint']:
                          if wait2["ROM"][msg.to].items() == []:
                              chiya = ""
                          else:
                              chiya = ""
                              for rom in wait2["ROM"][msg.to].items():
                                  print rom
                                  chiya += rom[1] + "\n"

                          cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                      else:
                          cl.sendText(msg.to, "An already read point has not been set.\n「check」you can send ♪ read point will be created ♪")
#-----------------------------------------------

#-----------------------------------------------

            elif "Contact bc " in msg.text:
               if msg.from_ in admin:
                  print "BroadCast Done"
                  bctxt = msg.text.replace("Contact bc ", "")
                  n = cl.getAllContactIds()
                  for people in n:
                      cl.sendText(people, (bctxt))
                      
            elif "Spamcontact @" in msg.text:                         
                 _name = msg.text.replace("Spamcontact @","")
                 _nametarget = _name.rstrip(' ')
                 gs = cl.getGroup(msg.to)
                 for g in gs.members:
                     if _nametarget == g.displayName:
                        cl.sendText(g.mid,"Spammed !")
                        cl.sendText(g.mid,"Spammed !")  
                        cl.sendText(g.mid,"Spammed !")  
                        cl.sendText(g.mid,"Spammed !")
                        cl.sendText(msg.to, "Done")
                        print " Spammed !"
#-----------------------------------------------
            elif msg.text in ["/out"]:                                
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.LeaveGroup(msg.to)
                    except:
                        pass
                    
            elif "/keluar" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	c = Message(to=msg.to, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':'ud4082219b6754e7b610f84d07d3b436b'}
                        cl.sendMessage(c)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
              if msg.from_ in admin:                                
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Fuck You")
                        cl.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
                 
            elif "haiii.." in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("haiii..","")
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"「 Mayhem\nMayhem is STARTING♪\n' abort' to abort♪")
                    cl.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in admin:
                                try:
                                   klist=[cl,ki,kk,kc,k1,ks,ka,kb,ko,ke]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   cl.sendText(msg.to,"Mayhem done")
            
            elif "Mayhem" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"「 Mayhem\nMayhem is STARTING♪\n' abort' to abort♪")
                    cl.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in admin:
                                try:
                                   klist=[cl,ki,kk,kc,k1,ks,ka,kb,ko,ke]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   cl.sendText(msg.to,"Mayhem done")
                                   
                 #----->Total Friend and Group<-----#
            elif msg.text in ["Result"]:
                    mE = cl.getProfile()
                    gT = cl.getGroupIdsJoined()
                    fT = cl.getAllContactIds()
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"「"+mE.displayName+"」 \n\nGroup total : " + str(len(gT))+ "\nFriend total: " +str(len(fT))+ "\nPending Group: " + str(len(ginv)))       
                    
            elif msg.text in ["/ListGroup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

#List details group *Termasuk yang tertunda + gid + jmlh member + jmlh pendingan + creator
            elif msg.text in ["List group"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""                                                                                                                                          
                for i in gid:
                    h += "║❂͜͡➣【%s】\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"▒▒▓█[List Group]█▓▒▒\n"+ h +"Total Group =" +"["+str(len(gid))+"]")
                
            elif msg.text in ["/ListDetailsGroup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

#Details grup lewat gid + gid + jmlh member + jmlh pendingan + creator + picture
            elif "/DetailsGroup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
    
            elif "Gbcont" in msg.text:
              if msg.from_ in admin:
                print "[Group Broadcast Execute]"
                n = cl.getGroupIdsJoined()                
                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                for people in n:                	
                	cl.sendKontok(people, Oa)
                        
            elif "Gbc " in msg.text:
              if msg.from_ in admin:
                print "[Group Broadcast Execute]"
                bctxt = msg.text.replace("Gbc ","")
                n = cl.getGroupIdsJoined()                
                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                for people in n:                	
                	cl.sendText(people, bctxt)
                        cl.sendKontok(people, Oa)
            
            elif "Allbc " in msg.text:
              if msg.from_ in owner:
                print "[All Bot Broadcast to Group Execute]"
                bctxt = msg.text.replace("Allbc ","")
                a = cl.getGroupIdsJoined()
                for taf in a:
                    cl.sendText(taf,"[Broadcast]"+  (bctxt))
                
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = ncl.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc,k1,ks,ka,kb,ko,ke]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Succes Cv")
                                    cl.sendText(msg.to,"Fuck You")
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes Cv")
                                except:
                                    cl.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes Cv")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes Cv")
                            except:
                                cl.sendText(msg.to,"Succes Cv")
#-----------------------------------------------
            elif msg.text in ["Test"]:
                cl.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                cl.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
                cl.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Cv say hi"]:
                cl.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Cv say hinata pekok"]:
                cl.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                cl.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har����")
                cl.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                cl.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har��")
            elif msg.text in ["Cv say chomel pekok"]:
                cl.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har����")
                cl.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                cl.sendText(msg.to,"Selamat datang di Saan Bot Family Room")
                cl.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                cl.sendText(msg.to,"PONG ��􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Respon","respon"]:
                cl.sendText(msg.to,"hadir!")
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#------------------------------------------------------------------

# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif "mention" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
             
            elif msg.text.lower() in ["tmention"]:          	
                sendMessageWithMention(msg.to, msg.from_)
                
            elif msg.text.lower() in ["mention all"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                    cnt = Message()
                    cnt.text = "Done : " + str(jml) +  " Members"
                    cnt.to = msg.to
                    cl.sendMessage(cnt) 
                    
            elif ("Ban repeat " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned ")
                   except:
                      pass        
                  
            elif msg.text in ["Ban"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif "Clear banlist" in msg.text:
		      if msg.from_ in admin:
		        wait["blacklist"] = {}
		        cl.sendText(msg.to,"Done")
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "☠。" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:                                
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        cl.kickoutFromGroup(msg.to,[jj])
                        cl.kickoutFromGroup(msg.to,[jj])
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
    #        elif msg.text in ["Clear"]:
#              if msg.from_ in admin:                                 
  #              if msg.toType == 2:
#                    group = cl.getGroup(msg.to)
   #                 gMembMids = [contact.mid for contact in group.invitee]
    #                for _mid in gMembMids:
    #                    cl.cancelGroupInvitation(msg.to,[_mid])
    #                cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
              if msg.from_ in admin:                                
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
                        
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass  
                
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☀。" + Name
                        wait2['ROM'][op.param1][op.param2] = "☠。" + Name
                else:
                    cl.sendText
            except:
                  pass
              
        if op.type == 26:
            msg = op.message
            msg.text = str(msg.text)
            text = msg.text
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg.from_ in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg.from_]
                        else:
                            pass
                    except:
                        pass
                else:
                    pass
            except KeyboardInterrupt:
                         sys.exit(0)
            except Exception as error:
                print error
                print ("\n\nRECEIVE_MESSAGE\n\n")
                return
          
        if op.type == 59:
            print op


    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
            
def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["commenty"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
