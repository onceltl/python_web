#coding='utf-8'
import urllib
import urllib2
import re
import jieba
urllist=[]
fo=open("debug.txt","w+")
dict={}
use={}
tot=0
def dealinfo(info,url):
		#fo.write(info)
		have={}
		pattern_title=re.compile('<title>(.*?)</title>',re.S)
		pattern_ac=re.compile('<article.*?>(.*?)</article>',re.S)
		#pattern_time=re.compile(' <div class="articletime"><i class="thunews-clock-o"></i>(.*?)</div>')
		item=re.search(pattern_title,info)
		title_seg=list(jieba.cut_for_search(item.group(1)))
		
		for ys in title_seg:
			if have.get(ys):
				continue
			have[ys]=url
			if dict.get(ys):
				dict[ys].append(url)
			else:
				dict[ys]=[]
				dict[ys].append(url)
				
		item=re.search(pattern_ac,info)
		notinfo=item.group(1)
		article=''
		ok=0
		for i in range(0,len(notinfo)):
			if notinfo[i]=='<' :
				ok^=1
			if ok==0:
				article+=notinfo[i]
			if notinfo[i]=='>':
				ok^=1
		title_seg=list(jieba.cut_for_search(article))
		for ys in title_seg:
			if have.get(ys):
				continue
			have[ys]=url
			if dict.get(ys):
				dict[ys].append(url)
			else:
				dict[ys]=[]
				dict[ys].append(url)
		print dict['2016'.decode('utf-8')]
		return
def search(info,url):
	global tot
	pattern_url=re.compile('<a href="(.*?)"',re.S)
	allitem = re.findall(pattern_url,info)
	for item in allitem:
		if len(item)<5:
			continue
		if item[0]=='/' and item[1]=='p':
			item='http://news.tsinghua.edu.cn'+item
			if use.get(item):
				continue
			use[item]=1
			fo.write(item+' %d\n'%(tot))
			urllist.append(item)
	return
	
root_url='http://news.tsinghua.edu.cn/publish/thunews/9658/2016/20160907154523034541391/20160907154523034541391_.html'
urllist.append(root_url)
use[root_url]=1
i=0
while(i<len(urllist)):
	item=urllist[i]
	i+=1
	try:
		request=urllib2.Request(item)
		response=urllib2.urlopen(request).read()
		#dealinfo(response,item)
		search(response,item)
	except:
		continue
