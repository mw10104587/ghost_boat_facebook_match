from bs4 import BeautifulSoup
import csv
import sys
import Levenshtein
# 100005207580058 is the German guy, who got lots of refugee friends on facebook 

# this is the threshold that filters the similarity of names
thresholdOfNameSimilarity = 0.75
fbId = "100005207580058"

if len(sys.argv) < 2:
		print "incorrect input format"
		print "Correct Format: <fb_id>"
else:
	fbId = sys.argv[1]


# feed in the html saved by hand
with open("../raw/" + fbId + "_raw_friendlist.html", "r") as friendListFile:

	# the list of extracting names from html
	listName = []

	soup = BeautifulSoup(friendListFile, 'html.parser')

	# by observing the structure, we extract all the names by getting the div with class "fcb"
	for nameWrap in soup.findAll("div", {"class":"fcb"}):

		# it's inside the a tag, so we get the tag and get it's text inside.
		name = nameWrap.find("a").get_text()
		listName.append(name)
		# print name

	# the knownNameFile is the manifest spreadsheet
	with open("../csv/given_names.csv", "r") as knownNameFile:
		
		similarNameList = []

		csvFile = csv.DictReader(knownNameFile)
		for name in csvFile:
			# print name["NAME"]
			for friend in listName:

				# use the library Levenshtein to get similar names
				similarityDistance = Levenshtein.seqratio(unicode(name["NAME"]).lower().split(" "), friend.lower().split(" "))
				
				if similarityDistance > thresholdOfNameSimilarity:
					print "============================="
					print "Name of friend list: " + friend 
					print "is similar to: " + str(similarityDistance)
					print "Name of spreadSheat: " + name["NAME"]
					
					similarNameList.append({
						"d": similarityDistance,
						"manifest_name": name["NAME"],
						"friendlist_name": friend
						})

		# output this file into a txt file.
		with open("../similar_names/" + fbId + ".csv", "w") as of:
			fieldNames = ["manifest_name", "friendlist_name","d"]
			writer = csv.DictWriter(of, fieldnames=fieldNames)
			writer.writeheader()

			for similarName in similarNameList:
				writer.writerow(similarName)
