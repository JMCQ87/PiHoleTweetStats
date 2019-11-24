#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.get_config import get_cfgip as cfgIP

import urllib.request
import json

def check_ipstack():

    import requests

    key = cfgIP()
    ip = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
    address = "http://api.ipstack.com/" + ip + "?access_key=" + key + "&output=json&fields=region_name,continent_name"
    url = urllib.request.urlopen(address)
    url_json = json.loads(url.read().decode())

    success = url.getcode()

    try:
       badip = url_json["region_name"]
    except KeyError as e:
       print("invalid access key \nipstack API URL\n" + address)

    if badip != None:
        print(str(success) + "\nipstack API URL\n" + address)
    else:
        if badip == None:
            print("please check your IP address \nipstack API URL\n" + address)
        else:
           print("something is really broke")

def speedtest_ip():

    import os

    jstring = os.popen("speedtest-cli --share --json").read()
    data = json.loads(jstring)
    client = data["client"]

    ulByte = data["bytes_sent"]/1024/1024
    dlByte = data["bytes_received"]/1024/1024
    us = data["upload"]/1000000
    ds = data["download"]/1000000
    pg = data["ping"]
    isp = client["isp"]
    share = data["share"]
    ip = client["ip"]

    key = cfgIP()
    address = "http://api.ipstack.com/" + ip + "?access_key=" + key + "&output=json&fields=region_name,continent_name"

    with urllib.request.urlopen(address) as url:
         ipstack = json.loads(url.read().decode())

    uls = round(us, 2)
    dls = round(ds, 2)
    pings = round(pg, 2)
    dlMB = round(dlByte, 2)
    ulMB = round(ulByte, 2)

    ping = str(pings) + " ms"

    ul = str(uls) + " Mbps"
    dl = str(dls) + " Mbps"
    speed = ul + "/" + dl

    ulMBs = str(ulMB) + " MB"
    dlMBs = str(dlMB) + " MB"
    Sdata = ulMBs + "/" + dlMBs

    ip = '.'.join(ip.split('.')[:2]) + '.xx.xx'
    region = ipstack['region_name']
    continent = ipstack['continent_name']

    return (ping, speed, Sdata, ip, isp, region, continent, share)