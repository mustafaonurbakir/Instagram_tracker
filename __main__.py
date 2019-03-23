from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import time

from InstagramAPI import InstagramAPI
import sqlite3

# izelin idsi= '1177732294'
# kendi id'm= api.username_id

class Calculator(QObject):
	#ilk yapilacak esitlemeleri yapiyor
	#DB baglantisini hazir aliyor
	def __init__(self, db, conn):
		QObject.__init__(self)
		self.db = db
		self.conn = conn
		
		persontoTakeResult = 0
		
		global followers_global
		followers_global = ""
		global eklenen_followers_global
		eklenen_followers_global = ""
		global silinen_followers_global
		silinen_followers_global = ""
		
		global followings_global
		followings_global = ""
		global eklenen_followings_global
		eklenen_followings_global = ""
		global silinen_followings_global
		silinen_followings_global = ""
		
		global myfollowers_global
		myfollowers_global = ""
		global myfollowings_global
		myfollowings_global = ""
		global myfavourite_global
		myfavourite_global = ""
		global myfavourite_global2
		myfavourite_global2 = ""
		
		global person_no
		person_no = 0
		global person_id
		person_id = ""
		global person_fullname_gelen
		person_fullname = ""
		global person_ilk_sorgulama
		person_ilk_sorgulama = True
		
	#ne ise yaradiklarini anlamadigim seyler. Sanirim degisimin sinyalini gonderiyor
	sendMyInfoResult = pyqtSignal(int, arguments=['sendMyInfo'])
	takedataResult = pyqtSignal(int, arguments=['takedata'])
	takePersonResult = pyqtSignal(int, arguments=['person'])
	persontoTakeResult = pyqtSignal(int, arguments=['isthereproblem'])
	
	#login bilgilerini aliyor,
	#benim takip ve takipcilerimi aliyor
	@pyqtSlot('QString', 'QString', result=int)
	def sendMyInfo(self, arg1, arg2):
		userId = arg1
		userPassword = arg2
		global api
		global myfollowers_global
		global myfollowings_global
		global myfavourite_global
		
		#instagram apisine giris yapiyor
		api = InstagramAPI(userId, userPassword)
		login_ok = api.login()
		
		if login_ok != True:
			return int(0)
		
		# 1. kisinin kullanici id'si
		user_id = api.username_id
		
		# 1. kisinin (benim) takipcilerimi aliyor"
		myfollowers_global = getMyFollowers(api, user_id, db)
		# 1. kisinin (benim) takip ettiklerimi aliyor
		myfollowings_global, myfavourite_global = getMyFollowing(api, user_id, db)
		#myfavourite_global = getMyFavourite(
		return int(1)
	
	#2. kisinin takip ve takipci listelerini aliyor
	@pyqtSlot()
	def takedata(self):
		global db
		global person_no
		global person_id
		global person_fullname
		global api
		global followers_global
		global eklenen_followers_global
		global silinen_followers_global
		global followings_global
		global eklenen_followings_global
		global silinen_followings_global
		
		#2. kisinin bilgileri kisiler tablosuna DB'e kayit ediliyor
		try:
			print(db.execute('''INSERT INTO kisiler (userno, userid, fullname) VALUES (''' + str(person_no) + ''',''' + person_id + ''',''' + person_fullname + ''')'''))
			print("hayirdir insallah1")
		except:
			global person_ilk_sorgulama
			person_ilk_sorgulama = False
			print("hayirdir insallah2")
		
		conn.commit()
		
		#followers aliyor
		followers_global, eklenen_followers_global, silinen_followers_global = getTotalFollowers(api, person_no, db, person_ilk_sorgulama)
		conn.commit()
		
		#following aliyor
		followings_global, eklenen_followings_global, silinen_followings_global = getTotalFollowing(api, person_no, db, person_ilk_sorgulama)
		
		#DB'e kayit ediyor
		conn.commit()
		conn.close()
	
	#bu ve alttaki 4 fonksiyon qml dosyalarina data aktariyor
	#benim takipcilerim
	@pyqtSlot(result=str)
	def takemyfollowers(self):
		global myfollowers_global
		return myfollowers_global
	
	#benim takip ettiklerim
	@pyqtSlot(result=str)
	def takemyfollowings(self):
		global myfollowings_global
		return myfollowings_global
	
	#2. kisinin takipcileri
	@pyqtSlot(result=str)
	def takefollowers(self):
		global followers_global
		return followers_global
	
	
	@pyqtSlot(result=str)
	def takeeklenenfollowers(self):
		global eklenen_followers_global
		return eklenen_followers_global
	
	@pyqtSlot(result=str)
	def takesilinenfollowers(self):
		global silinen_followers_global
		return silinen_followers_global
	
	@pyqtSlot(result=str)
	def takeeklenenfollowings(self):
		global eklenen_followings_global
		return eklenen_followings_global
	
	@pyqtSlot(result=str)
	def takesilinenfollowings(self):
		global silinen_followings_global
		return silinen_followings_global
	
	
	#2. kisinin takip ettikleri
	@pyqtSlot(result=str)
	def takefollowings(self):
		global followings_global
		return followings_global
	
	#listesine ulasmak istedigin kisinin userid'si geliyor
	@pyqtSlot(str, str, str)
	def takeperson(self, person_no_gelen, person_id_gelen, person_fullname_gelen):
		global person_no
		global person_id
		global person_fullname
		if len(person_no_gelen) != 0:
			person_no = int(person_no_gelen)
			person_id = person_id_gelen
			person_fullname = person_fullname_gelen
			print ("user: ", person_id)
			self.persontoTakeResult.emit(1)
	
	#favori insanlari atiyor. Sonra guncellemeleri atiyor
	@pyqtSlot(result=str)
	def takemyfavourite(self):
		global myfavourite_global
		aaa = myfavourite_global
		myfavourite_global = ""
		return aaa
	
	#favori listesine eklenmesini sagliyor
	@pyqtSlot(str, str, str)
	def takepersontolist(self, person_no_gelen, person_id_gelen, person_fullname_gelen):
		if len(person_no_gelen) != 0:
			person_no_ = int(person_no_gelen)
			person_id_ = person_id_gelen
			person_fullname_ = person_fullname_gelen
			print ("user: ", person_id)
			#rooot = engine.rootObjects()[0]
			global myfavourite_global2
			myfavourite_global2 =  "," + str(person_no_) + "," + person_id_ + "," + person_fullname_
			#rooot.catchdata(1, 1, 1)
			#rooot.catchdata(person_no_, person_id_, person_fullname_)
	#asagi al butonuna basinca verinin esitlenmesine izin veriyor
	@pyqtSlot()
	def guncelleme(self):
		global myfavourite_global
		global myfavourite_global2
		myfavourite_global =  myfavourite_global2
		
def getTotalFollowers(api, person_no, db, person_ilk_sorgulama):
	followers = []
	old_followers = []
	new_followers= ""
	new_followers_list= []
	silinen_followers = ""
	silinen_followers_list = []
	eklenen_followers = ""
	eklenen_followers_list = []
	next_max_id = True
	
	#instagramdan verileri aliyor
	while next_max_id:
		# first iteration hack
		if next_max_id is True:
			next_max_id = ''
		_ = api.getUserFollowers(person_no, maxid=next_max_id)
		followers.extend(api.LastJson.get('users', []))
		next_max_id = api.LastJson.get('next_max_id', '')
	
	#DB'den eski tum kullanicilari aliyor
	#db'den eski verileri siliyor
	db.execute('''SELECT userno, userid, fullname FROM users INNER JOIN takipciler ON users.userno=takipciler.user_no WHERE takipciler.takipedilen_no=''' + str(person_no))
	old_followers = db.fetchall()
	db.execute('''DELETE FROM takipciler WHERE takipciler.takipedilen_no=''' + str(person_no))
	
	#alinan datalari parse ediyor
	#DB eklemeleri yapiyor
	for x in range(len(followers)):
		#bir kisinin ozelliklerini ayiriyor
		one_follower = str(followers[x]).split(',')
		#userno ekliyor
		one_follower_no = (one_follower[0].split(':'))[1]
		#userid ekliyor
		one_follower_id = (one_follower[1].split(':'))[1]
		#fullname ekliyor
		one_follower_fullname = (one_follower[2].split(':'))[1]
		##nizami liste
		new_followers_list.append([int(one_follower_no), one_follower_id, one_follower_fullname])
		
		#daha kolay oldugu icin string yaparak gonderiyor
		new_followers = new_followers + "," + one_follower_no + "," + one_follower_id + "," + one_follower_fullname
		
		try:
			#print("hayirdir insallah3")
			db.execute('''INSERT INTO users (userno, userid, fullname) VALUES (''' + one_follower_no + ''',''' + one_follower_id + ''',''' + one_follower_fullname + ''')''')
		except:
			#print("hayirdir insallah4")
			pass
		
		try:
			#print("hayirdir insallah5")
			db.execute('''INSERT INTO takipciler (takipedilen_no,user_no) VALUES (''' + str(person_no) + ''',''' + one_follower_no + ''')''')
		except:
			#print("hayirdir insallah6")
			pass
	
	
	#eklenenler
	for x in range(len(new_followers_list)):
		varmi = False
		for y in range(len(old_followers)):
			if int(new_followers_list[x][0]) == int(old_followers[y][0]):
				varmi = True
				break
		if varmi == False:
			print ("ee falseee")
			eklenen_followers_list.append(new_followers_list[x])
			eklenen_followers = eklenen_followers + "," + str(new_followers_list[x][0]) + "," + new_followers_list[x][1] + "," + new_followers_list[x][2]
		
	#silinenler
	for x in range(len(old_followers)):
		varmi = False
		for y in range(len(new_followers_list)):
			if old_followers[x][0] == new_followers_list[y][0]:
				varmi = True
				break;
		if varmi == False:
			silinen_followers_list.append(old_followers[x])
			silinen_followers = silinen_followers + "," + str(old_followers[x][0]) + "," + old_followers[x][1] + "," + old_followers[x][2]

	
	return new_followers, eklenen_followers, silinen_followers

def getTotalFollowing(api, user_id, db, person_ilk_sorgulama):
	followings = []
	old_followings = []
	new_followings = ""
	new_followings_list= []
	silinen_followings = ""
	silinen_followings_list = []
	eklenen_followings = ""
	eklenen_followings_list = []
	next_max_id = True
	
	#liste al
	while next_max_id:
		# first iteration hack
		if next_max_id is True:
			next_max_id = ''
		_ = api.getUserFollowings(user_id, maxid=next_max_id)
		followings.extend(api.LastJson.get('users', []))
		next_max_id = api.LastJson.get('next_max_id', '')
	
		
	#DB'den eski tum kullanicilari aliyor
	#db'den eski verileri siliyor
	db.execute('''SELECT userno, userid, fullname FROM users INNER JOIN takipedilenler ON users.userno=takipedilenler.user_no WHERE takipedilenler.takipedilen_no=''' + str(person_no))
	old_followings = db.fetchall()
	db.execute('''DELETE FROM takipedilenler WHERE takipedilenler.takipedilen_no=''' + str(person_no))
	
	#alinan datalari parse ediyor
	#DB eklemeleri yapiyor
	for x in range(len(followings)):
		#bir kisinin ozelliklerini ayiriyor
		one_following = str(followings[x]).split(',')
		#userno ekliyor
		one_following_no = (one_following[0].split(':'))[1]
		#userid ekliyor
		one_following_id = (one_following[1].split(':'))[1]
		#fullname ekliyor
		one_following_fullname = (one_following[2].split(':'))[1]
		##nizami liste
		new_followings_list.append([int(one_following_no), one_following_id, one_following_fullname])
		
		#daha kolay oldugu icin string yaparak gonderiyor
		new_followings = new_followings + "," + one_following_no + "," + one_following_id + "," + one_following_fullname
		
		try:
			#print("hayirdir insallah3")
			db.execute('''INSERT INTO users (userno, userid, fullname) VALUES (''' + one_following_no + ''',''' + one_following_id + ''',''' + one_following_fullname + ''')''')
		except:
			#print("hayirdir insallah4")
			pass
		
		try:
			#print("hayirdir insallah5")
			db.execute('''INSERT INTO takipedilenler (takipedilen_no,user_no) VALUES (''' + str(person_no) + ''',''' + one_following_no + ''')''')
		except:
			#print("hayirdir insallah6")
			pass
	
		
	
	#eklenenler
	for x in range(len(new_followings_list)):
		varmi = False
		for y in range(len(old_followings)):
			if new_followings_list[x][0] == old_followings[y][0]:
				varmi = True
				break;
		if varmi == False:
			eklenen_followings_list.append(new_followings_list[x])
			eklenen_followings = eklenen_followings + "," + str(new_followings_list[x][0]) + "," + new_followings_list[x][1] + "," + new_followings_list[x][2]
		
	#silinenler
	for x in range(len(old_followings)):
		varmi = False
		for y in range(len(new_followings_list)):
			if old_followings[x][0] == new_followings_list[y][0]:
				varmi = True
				break;
		if varmi == False:
			silinen_followers_list.append(old_followings[x])
			silinen_followers = silinen_followers + "," + str(old_followings[x][0]) + "," + old_followings[x][1] + "," + old_followings[x][2]
	
	
	return new_followings , eklenen_followings, silinen_followings

def getMyFollowers(api, user_id, db):
	followers2 = []
	next_max_id = True
	
	#liste al
	while next_max_id:
		# first iteration hack
		if next_max_id is True:
			next_max_id = ''
		_ = api.getUserFollowers(user_id, maxid=next_max_id)
		followers2.extend(api.LastJson.get('users', []))
		next_max_id = api.LastJson.get('next_max_id', '')
	
	#alinan datalari parse ediyor
	#daha kolay oldugu icin string yaparak gonderiyor
	new_followers2= ""
	for x in range(len(followers2)):
		new_list = str(followers2[x]).split(',')
		#userno ekliyor
		new_list2 = new_list[0].split(':')
		#userid ekliyor
		new_list3 = new_list[1].split(':')
		#fullname ekliyor
		new_list4 = new_list[2].split(':')
		#birlestiriyor
		new_followers2 = new_followers2 + "," + new_list2[1] + "," + new_list3[1] + "," + new_list4[1]
		
		if db.execute('''SELECT COUNT(userno) FROM users WHERE userid=''' + new_list3[0]) != 1:
			list33 = ""
			list44 = ""
			for y in range(len(new_list3[1])):
				if new_list3[1][y].isalpha or new_list3[1][y].isdigit:
					list33 += new_list3[1][y]
				else:
					list33 += '_'
			for y in range(len(new_list4[1])):
				if new_list4[1][y].isalpha or new_list4[1][y].isdigit:
					list44 += new_list4[1][y]	
				else:
					list44 += '_'
			try:
				db.execute('''INSERT INTO users (userno, userid, fullname) VALUES (''' + new_list2[1] + ''',''' + list33 + ''',''' + list44 + ''')''')
			except:
				pass
				#print(list33, list44)
	return new_followers2

def getMyFollowing(api, user_id, db):
	followings2 = []
	kisilerim = ""
	next_max_id = True
	
	#take values
	while next_max_id:
		# first iteration hack
		if next_max_id is True:
			next_max_id = ''
		_ = api.getUserFollowings(user_id, maxid=next_max_id)
		followings2.extend(api.LastJson.get('users', []))
		next_max_id = api.LastJson.get('next_max_id', '')
	
	db.execute('''SELECT userno, userid, fullname FROM kisiler''')
	kisiler_liste = db.fetchall()
	
	#alinan datalari parse ediyor
	#daha kolay oldugu icin string yaparak gonderiyor
	new_followings = ""
	for x in range(len(followings2)):
		new_list = str(followings2[x]).split(',')
		#userno ekliyor
		new_list2 = new_list[0].split(':')
		#userid	ekliyor
		new_list3 = new_list[1].split(':')
		#fullname ekliyor
		new_list4 = new_list[2].split(':')
		#birlestiriyor
		for y in range(len(kisiler_liste)):
			if kisiler_liste[y][0] == int(new_list2[1]):
				kisilerim = kisilerim + "," + new_list2[1] + "," + new_list3[1] + "," + new_list4[1]
		new_followings = new_followings + "," + new_list2[1] + "," + new_list3[1] + "," + new_list4[1]
		
		try:
			db.execute('''INSERT INTO users (userno, userid, fullname) VALUES (''' + new_list2[1] + ''',''' + list33 + ''',''' + list44 + ''')''')
		except:
			pass
	
	return new_followings, kisilerim

if __name__ == "__main__":
	import sys
	
	#DB baglantileri
	conn = sqlite3.connect('PR_DB.db')
	db = conn.cursor()

	# Create an instance of the application
	app = QGuiApplication(sys.argv)
	# Create QML engine
	engine = QQmlApplicationEngine()
	# Create a calculator object
	calculator = Calculator(db, conn)
	# And register it in the context of QML
	engine.rootContext().setContextProperty("calculator", calculator)
	# Load the qml file into the engine

	try:
		engine.load("qml/Main.qml")
		engine.quit.connect(app.quit)
		sys.exit(app.exec_())
	except:
		pass
	
	
	
	
	
	
	



    
    
