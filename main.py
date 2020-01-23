# Author      : Isaiah Jared
# Description : Multi-purpose scraper.



from bs4 import BeautifulSoup
import os
import urllib
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import time


def selectPurpose():
  userSelect = input("Please select an option below:\n 1. 4chan image downloader\n 2. Analyze Amazon item prices\n\n")
  while userSelect not in ("1","2"):
    userSelect = input("Please select an option below:\n 1. Mass download images\n 2. Analyze Amazon item prices\n\n")
  if userSelect == "1":
    imgScrape()
  elif userSelect == "2":
    priceScrape()

def imgScrape():
  imgPath = input("Copy-paste the destination folder for your downloaded files: ")
  while imgPath == "":
    print("You didn't enter a path!")
    imgPath = input("Copy-paste the destination folder for your downloaded files: ")

  userSite = input("\n\nPlease copy-paste the 4chan thread URL you would like to download from: ")
  while userSite == "":
    userSite = input("\n\nPlease copy-paste the 4chan thread URL you would like to download from: ")
    print("Please enter a URL!")

  req = Request("{}".format(userSite), headers={'User-Agent': 'Mozilla/5.0'})  # Prevents request being denied.
  url = urlopen(req).read()
  bs = BeautifulSoup(url, 'html.parser')
  dataList = []

  images = bs.find_all('div', {"class": "fileText"})  # Finds all images/webms on the page
  for image in images:
    if image.find('a', target="_blank"):
      dataList.append(image.find('a')['href'])
      dataList.append(image.find('a').text)

  # Ensures that only the links to the actual images/webms are in the list for later use.
  del dataList[1::2]

  testList = []
  for i in range(len(dataList)):
    listStr = str(dataList[i])
    http = "http:" + listStr  # Since the anchor tag's link doesn't include the http: I just concatenate it here
    # so Urllib can actually interact with it.
    testList.append(http)

  # print(testList)
  print("\nFile downloads are in progress, please wait until they finish :^) ")

  for i in range(len(testList)):
    imgLink = str(testList[i])
    filename = imgLink.split('/')[-1]
    fullDownPath = os.path.join(imgPath, filename)
    urllib.request.urlretrieve(imgLink, fullDownPath)
    time.sleep(0.15)
    print(f'\n{filename} ..... Download Done!')
    i += 1

  input("\n\nDownloads complete! Press Enter key to exit: ")

# WIP
def priceScrape():
  dataPath = input("Enter the relative path for the scraped price data: ")
  userSite = input("Please copy-paste the URL you would like to scrape from: ")
  while userSite == "":
    userSite = input("Please copy-paste the URL you would like to scrape from: ")
    print("user")




selectPurpose()
