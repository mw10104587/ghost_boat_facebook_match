<h1>Ghost Boat Project</h1>
<p>
This is a sub-project started on 11.07.2015 in the workshop of CUNY and Columbia University. Based on the assumption that people on the ghost ship know several of each others, so probably they are friends on facebook. We try to compare names of some refugee's facebook friends to the manifest, hoping that we can find more facebook accounts of refugees.
</p>
<p>
This sub-project also aim to build a graph of the refugees, after we collected all of their friend lists. LOL
</p>
<br>
<h3>==== Directory Structure ====</h3>

* ---+--README.md
* ---+--python
	* +--FBFriendListExtractor.py
* ---+--raw
* ---+--csv
	* +--name_mapping.csv
	* +--given_names.csv

<br>
**FBFriendListExtractor.py:**
- compares a person's facebook friends to the manifest and see whether there are similar names.
- the main program that loads a html file in the raw folder, and outputs a txt file in the similar_names directory.

How to execute
> $python python/FBFriendListExtractor.py fb_id

<br>
**raw/:**
- saves the html content copied by labor.
- file has to be in the format [fb_id]_raw_friendlist.html

<br>
**name_mapping.csv:**
- saves the mapping of the name between data on manifest, Facebook account name and Facebook id.
- please input by hand. XDDD

<br>
**given_names.csv:**
- save the manifest data

<br><br>
<h3>==== Goals ====</h3>
1. Compare friendlist of refugee and manifest list
2. Build refugee relationship graph
	- by getting everyone's facebook friends, we can build a relationship graph for the refugees on the ghost boat.

<br><br>
<h3>==== How To Get Friendlist ====</h3>
<p>
Without being authenticated by the user, we can't access the user's friendlist by using facebook api, so here we require some labor work. By going to the /friends of a facebook user, we can scroll all the way down, until they load all of its friends. 
</p>
<p>
By right clicking on the last friend's name (anywhere in friends section), we can press the inspct element. Traverse it's parent element by pressing "left", until we find a <div> element with class="_5h60 _30f". Right click on this element and click copy, and paste it into note pad, sublime text or any text editing application. 
Save it as [FB-ID]_raw_friendlist.html into the raw directory.
</p>
// The way to get [FB-ID] can be learned by the following section.

<br><br>
<h3>==== How to Get Facebook User Id ====</h3>
For example, in the friends page of the user "Abel Ghebru", we have this url in our browser.
> https://www.facebook.com/abel.ghebru/friends?ref=br_rs

by taking "barackobama" into this website 
> http://findmyfbid.com/

we can get facebook id 

> 6815841748

<br>
**Contributor:**
- Chi-An Wang
- Mazin Sidahmed 
