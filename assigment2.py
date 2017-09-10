#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import datetime
from datetime import datetime
import pprint
from pprint import pprint
import csv
import collections
import logging
import logging
import argparse


    
def downloadData(url):
    req = urllib2.Request(url=url)
    response = urllib2.urlopen(req)
    data =  response.read()
    return data
        
def processData (data):
    #newDict = {}
    key_value = [(line.split(',')[0], line.split(',')[1:]) for line in data.splitlines()]
    newDict = dict(key_value)
    for key in newDict:
        try:
            newDict[key][1] = datetime.strptime(newDict[key][1],'%d/%m/%Y').date()
        except ValueError:
            logging.basicConfig(filename='error.log',level=logging.ERROR)
            logging.error('Error processing id %s' % key)

    sortedDict = collections.OrderedDict(sorted(newDict.items()))
    return sortedDict

def displayPerson (_id, personData):
    for key in personData:
        if key == _id:
            print 'Person #', key, ' is', personData[key][0], 'with birthday ', personData[key][1]

def main():
    pass

if __name__ == '__main__':
    url=raw_input("enter url: ")
    if url == "":
        print "Invalid url"
        raise SystemExit
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", action="store_true")
    parser.add_argument("-i", "--id", action="store_true")
    args = parser.parse_args()
    csvData = downloadData(url)
    personData = processData(csvData)
    _id=raw_input("enter id: ")
    try:
        if int(_id) > 0:
            displayPerson(_id, personData)
            while int(_id) > 0:
                 _id=raw_input("enter id: ")
                 if int(_id) > 0:
                    displayPerson(_id, personData)
                 else:
                     break
    except ValueError:
        raise SystemExit
