from bs4 import BeautifulSoup
import urllib
import pandas as pd

pages = 20
rec_count = 0
gname = []
genres = []
critic = []
platform = []
publisher = []
sales_na = []
sales_eu = []
sales_jp = []
sales_ot = []
sales_pal = []
release = []

def genre(url):
	r = urllib.urlopen(url).read()
	soup = BeautifulSoup(r, "lxml")
	info = soup.find("div", id="gameGenInfoBox")
	tt = info.find("h2",text="Genre")
	return tt.next_element.next_element

urlhead = 'http://www.vgchartz.com/games/games.php?page='
urltail = '&results=200&name=&console=&keyword=&publisher=&genre=&order=TotalSales&ownership=Both&boxart=Both&showdeleted=&region=All&goty_year=&developer=&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=0&alphasort='

c=1
for page in range(1,pages):
	surl = urlhead + str(page) + urltail
	r = urllib.urlopen(surl).read()
	soup = BeautifulSoup(r, "lxml")
	print page
	chart_div = soup.find("div", id="generalBody")
	chart = chart_div.find("table")
	for row in chart.find_all('tr')[3:]:
		print c
		col = row.find_all('td')
		na = col[2].find("a").string.strip()
		na = na.replace(','," ")
		try:
			gen = genre(col[2].find("a")["href"])
			gen = gen.string.strip()
		except:
			gen = "None"
		cons = col[3].find("img")['alt']
		cons = cons.replace(','," ")
		pub = col[4].string.strip()
		pub = pub.replace(','," ")
		score = col[5].string.strip()
		na_sales = col[7].string.strip()
		pal_sales = col[8].string.strip()
		j_sales = col[9].string.strip()
		o_sales = col[10].string.strip()
		r_date = col[11].string.strip()
		#print r,na,cons
		#consoles.add(cons)
		#publisher.add(pub)

		#Add Data to columns
		#Adding data only if able to read all of the columns

		gname.append(na)
		platform.append(cons)
		publisher.append(pub)
		genres.append(gen)
		critic.append(score)
		sales_na.append(na_sales)
		sales_pal.append(pal_sales)
		sales_jp.append(j_sales)
		sales_ot.append(o_sales)
		release.append(r_date)
		c+=1

columns = {'name': gname, 'platform': platform, 'publisher': publisher, 'genre': genres,'critic': critic,
		   'sales_na': sales_na, 'sales_pal': sales_pal, 'sales_jp': sales_jp, 'sales_ot': sales_ot, 'release': release}
df = pd.DataFrame(columns)
df = df[['name','platform','publisher','genre','critic','sales_na','sales_pal','sales_jp','sales_ot','release']]
del df.index.name
df = df.sample(frac=1)
df.to_csv("Game_Sales.csv",sep=",",encoding='utf-8')
