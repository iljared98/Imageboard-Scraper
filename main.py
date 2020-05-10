# Author : Isaiah Jared

from bs4 import BeautifulSoup
import os
import urllib
from urllib import request
from urllib.request import Request, urlopen
import time
from tqdm import tqdm

def imgScrape():

  running = True
  while running == True: # Used to allow the user to fix their erroneous inputs without having to make
                         # nasty recursive calls.

    try:
      imgPath = input("Please copy-paste the destination folder for your downloaded files: ")
      while imgPath == "":
        print("You didn't enter a path!")
        imgPath = input("Please copy-paste the destination folder for your downloaded files: ")

      userSite = input("\nPlease copy-paste the thread URL you would like to download from: ")
      while userSite == "":
        userSite = input("\nPlease copy-paste the thread URL you would like to download from: ")
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

      print("\nFile downloads are in progress, please wait until they finish\n\n")

      for i in tqdm(range(len(testList))):
        imgLink = str(testList[i])
        filename = imgLink.split('/')[-1]
        fullDownPath = os.path.join(imgPath, filename)
        urllib.request.urlretrieve(imgLink, fullDownPath)
        time.sleep(0.15)
        i += 1

      break

    except:
      print('\n\nYour directory or URL input is invalid. Please re-enter your directory/thread URL and try again!')

  input("\n\nDownloads complete! Press Enter key to exit: ")

imgScrape()
