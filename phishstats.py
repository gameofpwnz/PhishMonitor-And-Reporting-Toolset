#### Imports ####

import argparse
import webbrowser
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import textwrap
import re
import datetime

#### Argument Parser ####

parser=argparse.ArgumentParser(
    description='Phish Stats: The complementary tool to PhishMonitor (Python Edition) by GameOfPWNZ and Jacob Giannantonio')
parser.add_argument('-i', dest="INPUT_FILE", help="Input file (Default: phishing_log.txt)")
parser.add_argument('-o', dest="OUTPUT_FILE", help="Output file (HTML)")
parser.add_argument('-p', dest="PRETEXTS", type=int, help="Total Number of Scenarios Run")
parser.add_argument('-s1', dest="SCENARIO1", type=int, help="Total Emails Sent For Scenario 1")
parser.add_argument('-s2', dest="SCENARIO2", type=int, help="Total Emails Sent For Scenario 2")
parser.add_argument('-s3', dest="SCENARIO3", type=int, help="Total Emails Sent For Scenario 3")
parser.add_argument('-s4', dest="SCENARIO4", type=int, help="Total Emails Sent For Scenario 4")
parser.add_argument('-c1', dest="CREDS1", help="Harvested Creds File From Scenario 1")
parser.add_argument('-c2', dest="CREDS2", help="Harvested Creds File From Scenario 2")
parser.add_argument('-c3', dest="CREDS3", help="Harvested Creds File From Scenario 3")
parser.add_argument('-c4', dest="CREDS4", help="Harvested Creds File From Scenario 4")
parser.add_argument('-t', dest="TOTAL", type=int, help="Total Number of Emails Sent")
parser.add_argument('-s', dest="STRING", help="STRING to search Harvested Creds (Only if Harvested Creds File(s) is/are supplied. Ex: (COMPANYNAME)")
parser.add_argument('-c', dest="COMPANY", help="Company Name")
parser.add_argument('-w', dest="WATERMARK", help="Company Watermark (PNG Recommended)")
parser.add_argument('-v', dest="CLIENT", help="Client Name")
parser.add_argument('-r', dest="RECOMMENDATIONS", help="File with Recommendations (See Example Provided With Phish Stats For Format)")
parser.add_argument('-sf', dest="SCENARIOS", help="File with Scenario Descriptions (See Example Provided With Phish Stats For Format)")
parser.add_argument('-ex', dest="SUMMARY", help="File with Executive Summary - Replaces Default Summary (See Example Provided With Phish Stats For Format)")
parser.add_argument('--style', dest="style", help="MatPlotLib Style: Default (seaborn-darkgrid) https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html")
args=parser.parse_args()

#### Setting Style ####
style = str(args.style)

if style != "None":
	plt.style.use(style)
else:
	plt.style.use('seaborn-darkgrid')

#### Variables ####

inputFile = args.INPUT_FILE
outFile = args.OUTPUT_FILE
totalClicks = 0
linesSeen = set()
linesSeenCreds1 = set()
linesSeenCreds2 = set()
linesSeenCreds3 = set()
linesSeenCreds4 = set()
linesSeenCredsCombined = set()
uniqueTotal = int(0)
emailTotal = args.TOTAL
s1_uniqCount = 0
s2_uniqCount = 0
s3_uniqCount = 0
s4_uniqCount = 0
campaigns = args.PRETEXTS
scenario1Total = args.SCENARIO1
scenario2Total = args.SCENARIO2
scenario3Total = args.SCENARIO3
scenario4Total = args.SCENARIO4
creds1File = args.CREDS1
creds2File = args.CREDS2
creds3File = args.CREDS3
creds4File = args.CREDS4
s1_uniqCredsCount = 0
s2_uniqCredsCount = 0
s3_uniqCredsCount = 0
s4_uniqCredsCount = 0
combined_uniqCredsCount = 0
oneThruSeven = 0
str_oneThruSeven = "<7"
eight = 0
str_eight = "8"
nineThruTwelve = 0
str_nineThruTwelve = "9-12"
thirteenPlus = 0
str_ThirteenPlus = "13+"
pwWithCompany = 0
compName = args.STRING
str_company = str(compName).upper()
pwWithPassword = 0
str_password = "PASSWORD"
pwWithSeason = 0
str_season = "SEASONS"
totalPasswords = 0
companyName = args.COMPANY
watermark = args.WATERMARK
date = datetime.datetime.today().strftime('%Y-%m-%d')
clientName = args.CLIENT
recommendations = args.RECOMMENDATIONS
str_recommendations = ""
scenarios = args.SCENARIOS
str_scenarios = ""
summary = args.SUMMARY
str_summary = ""

#### Open File ####

f=open(str(inputFile), 'r')
lines = f.readlines()

#### Getting Total Clicks (Not Unique) ####

for line in lines:
	
	totalClicks += 1

str_totalClicks = str(totalClicks)

#### Parsing Only Target and Pretext ####

parsed = open("parsed.txt", "w")
for line in lines:

	parsedText = re.search('user:(.*)ipaddress', line)
	parsedGroup = parsedText.group(1)
	parsed.write(str(parsedGroup) + "\n")
parsed.close()


#### Create Unique Clicks File ####

uniqueClicks = open("unique_clicks.txt", "w")
parseOpen=open('parsed.txt', 'r')
parseLines = parseOpen.readlines()
for x in parseLines:
	print(str(x))
	if str(x) not in linesSeen:
		uniqueClicks.write(str(x))
		uniqueTotal+=1
		linesSeen.add(str(x))
uniqueClicks.close()
parseOpen.close()
print(uniqueTotal)

#### Quick Math - Unique Clicks out of Total Emails Sent ####

percentTotal = uniqueTotal / emailTotal
print("{0:.0%}".format(percentTotal))

noClickTotal = emailTotal - uniqueTotal

#### Create Unique Clicks File Per Pretext (Up to 4) ####

uniqueS1 = open("scenario1_unique.txt", "w")
uniqueS2 = open("scenario2_unique.txt", "w")
uniqueS3 = open("scenario3_unique.txt", "w")
uniqueS4 = open("scenario4_unique.txt", "w")
uniqueOpen = open('unique_clicks.txt', 'r')
parseUnique = uniqueOpen.readlines()
for y in parseUnique:
	print(str(y))
	if "#1" in y:
		uniqueS1.write(str(y))
		s1_uniqCount += 1
	elif "#2" in y:
		uniqueS2.write(str(y))
		s2_uniqCount += 1
	elif "#3" in y:
		uniqueS3.write(str(y))
		s3_uniqCount += 1
	elif "#4" in y:
		uniqueS4.write(str(y))
		s4_uniqCount += 1

uniqueS1.close()
uniqueS2.close()
uniqueS3.close()
uniqueS4.close()
uniqueOpen.close()
print(s2_uniqCount)

#### Quick Math - Unique Clicks Each Scenario ####
if scenario1Total != None:
	percentS1 = s1_uniqCount / scenario1Total
	noClickS1 = scenario1Total - s1_uniqCount

if scenario2Total != None:
	percentS2 = s2_uniqCount / scenario2Total
	noClickS2 = scenario2Total - s2_uniqCount

if scenario3Total != None:
	percentS3 = s3_uniqCount / scenario3Total
	noClickS3 = scenario3Total - s3_uniqCount

if scenario4Total != None:
	percentS4 = s4_uniqCount / scenario4Total
	noClickS4 = scenario4Total - s4_uniqCount


#### Pie Chart for Total (All Emails) ####

labels_All = 'Clicked', 'No Click'
values_All = [uniqueTotal, noClickTotal]
colors = ['red', 'green']
explode = (0.1, 0)
plt.title("Click Rate Percentage (All Emails)")
plt.pie(values_All, explode=explode, labels=labels_All, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.savefig('ClickRate_All_Pie.png')
plt.close()

#### Pie Chart for Scenario 1 ####

if scenario1Total != None:

	labels_All = 'Clicked', 'No Click'
	values_All = [s1_uniqCount, noClickS1]
	colors = ['red', 'green']
	explode = (0.1, 0)
	plt.title("Click Rate Percentage (Scenario 1)")
	plt.pie(values_All, explode=explode, labels=labels_All, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

	plt.axis('equal')
	plt.savefig('ClickRate_Scenario1_Pie.png')
	plt.close()


#### Pie Chart For Scenario 2 ####

if scenario2Total != None:
	labels_All = 'Clicked', 'No Click'
	values_All = [s2_uniqCount, noClickS2]
	colors = ['red', 'green']
	explode = (0.1, 0)
	plt.title("Click Rate Percentage (Scenario 2)")
	plt.pie(values_All, explode=explode, labels=labels_All, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

	plt.axis('equal')
	plt.savefig('ClickRate_Scenario2_Pie.png')
	plt.close()

#### Pie Chart For Scenario 3 ####

if scenario3Total != None:
	labels_All = 'Clicked', 'No Click'
	values_All = [s3_uniqCount, noClickS3]
	colors = ['red', 'green']
	explode = (0.1, 0)
	plt.title("Click Rate Percentage (Scenario 3)")
	plt.pie(values_All, explode=explode, labels=labels_All, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

	plt.axis('equal')
	plt.savefig('ClickRate_Scenario3_Pie.png')
	plt.close()

#### Pie Chart For Scenario 4 ####

if scenario4Total != None:

	labels_All = 'Clicked', 'No Click'
	values_All = [s4_uniqCount, noClickS4]
	colors = ['red', 'green']
	explode = (0.1, 0)
	plt.title("Click Rate Percentage (Scenario 4)")
	plt.pie(values_All, explode=explode, labels=labels_All, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

	plt.axis('equal')
	plt.savefig('ClickRate_Scenario4_Pie.png')
	plt.close()

#### Open Harvested Creds File (Scenario 1)####

if creds1File != None:

	uniquecredsS1 = open("unique_creds_Scenario1.txt", "w")
	parseCreds1Open=open(str(creds1File), 'r')
	parse1Creds = parseCreds1Open.readlines()
	for x in parse1Creds:
		print(str(x))
		if str(x) not in linesSeenCreds1:
			uniquecredsS1.write(str(x))
			s1_uniqCredsCount+=1
			linesSeenCreds1.add(str(x))

	uniquecredsS1.close()
	parseCreds1Open.close()
	print(s1_uniqCredsCount)


#### Open Harvested Creds File (Scenario 2) ####

if creds2File != None:

	uniquecredsS2 = open("unique_creds_Scenario2.txt", "w")
	parseCreds2Open=open(str(creds2File), 'r')
	parse2Creds = parseCreds2Open.readlines()
	for x in parse2Creds:
		print(str(x))
		if str(x) not in linesSeenCreds2:
			uniquecredsS2.write(str(x))
			s2_uniqCredsCount+=1
			linesSeenCreds2.add(str(x))

	uniquecredsS2.close()
	parseCreds2Open.close()
	print(s2_uniqCredsCount)

#### Open Harvested Creds File (Scenario 3)####

if creds3File != None:

	uniquecredsS3 = open("unique_creds_Scenario3.txt", "w")
	parseCreds3Open=open(str(creds3File), 'r')
	parse3Creds = parseCreds3Open.readlines()
	for x in parse3Creds:
		print(str(x))
		if str(x) not in linesSeenCreds3:
			uniquecredsS3.write(str(x))
			s3_uniqCredsCount+=1
			linesSeenCreds3.add(str(x))

	uniquecredsS3.close()
	parseCreds3Open.close()
	print(s3_uniqCredsCount)

#### Open Harvested Creds File (Scenario 4)####

if creds4File != None:

	uniquecredsS4 = open("unique_creds_Scenario4.txt", "w")
	parseCreds4Open=open(str(creds4File), 'r')
	parse4Creds = parseCreds4Open.readlines()
	for x in parse4Creds:
		print(str(x))
		if str(x) not in linesSeenCreds4:
			uniquecredsS4.write(str(x))
			s4_uniqCredsCount+=1
			linesSeenCreds4.add(str(x))

	uniquecredsS4.close()
	parseCreds4Open.close()
	print(s4_uniqCredsCount)

#### Combine Unique Harvested Creds Files ####

if creds4File != None:
	filenames = ["unique_creds_Scenario4.txt", "unique_creds_Scenario3.txt", "unique_creds_Scenario2.txt", "unique_creds_Scenario1.txt"]

elif creds3File != None:
	filenames = ["unique_creds_Scenario3.txt", "unique_creds_Scenario2.txt", "unique_creds_Scenario1.txt"]

elif creds2File != None:
	filenames = ["unique_creds_Scenario2.txt", "unique_creds_Scenario1.txt"]

if creds2File != None:

	with open('combined_harvested_creds.txt', 'w') as outfile:
		for fname in filenames:
			with open(fname) as infile:
				for line in infile:
					outfile.write(line)

if creds2File != None:

	uniquecredsCombined = open("unique_creds_combined.txt", "w")
	parseCredsCombinedOpen=open(str(creds1File), 'r')
	parseCombinedCreds = parseCredsCombinedOpen.readlines()
	for x in parseCombinedCreds:
		print(str(x))
		if str(x) not in linesSeenCredsCombined:
			uniquecredsCombined.write(str(x))
			combined_uniqCredsCount+=1
			linesSeenCredsCombined.add(str(x))

	uniquecredsCombined.close()
	parseCredsCombinedOpen.close()
	print(combined_uniqCredsCount)


#### Get Passwords Only ####

	f=open(str("unique_creds_combined.txt"), 'r')
	lines = f.readlines()
	parsedPass = open("unique_creds_combined_pass_only.txt", "w")
	for line in lines:

		parsedText = re.search(':::(.*):::', line)
		parsedGroup = parsedText.group(1)
		parsedPass.write(str(parsedGroup) + "\n")
	parsedPass.close()


#### Audit Passwords ####

#### Open File ####

if creds1File != None:

	if creds2File != None:

		f=open('unique_creds_combined_pass_only.txt', 'r')

		lines = f.readlines()

	else:

		f=open('unique_creds_Scenario1_pass_only.txt', 'r')

		lines = f.readlines()

#### Counting Characters in Passwords ####



	for line in lines:

		totalPasswords+=1

		if len(line) - 1 < 8:

   			oneThruSeven+=1


		elif len(line) - 1  == 8:

			eight+=1



		elif len(line) -1 > 8 and len(line) - 1 < 13:

			nineThruTwelve+=1
	


		elif len(line)-1  >= 13:

			thirteenPlus+=1



	print_Total = str(totalPasswords)

	print_oneThruSeven = str(oneThruSeven)

	print_eight = str(eight)

	print_nineThruTwelve = str(nineThruTwelve)

	print_thirteenPlus = str(thirteenPlus)



#### Counting Passwords with Seasons ####



	for line in lines:

		if "WINTER" in str(line).upper():

			pwWithSeason+=1

		elif "FALL" in str(line).upper():

			pwWithSeason+=1

		elif "SPRING" in str(line).upper():

			pwWithSeason+=1

		elif "SUMMER" in str(line).upper():

			pwWithSeason+=1

		elif "AUTUMN" in str(line).upper():

			pwWithSeason+=1

	print_season = str(pwWithSeason)



#### Counting Passwords with Password ####



	for line in lines:

		if "PASSWORD" in str(line).upper():

			pwWithPassword+=1

	print_password = str(pwWithPassword)



#### Counting Passwords with Company Name or Initials (User Input) ####



	for line in lines:

		if str(compName).upper() in str(line).upper():

			pwWithCompany+=1

	print_custom = str(pwWithCompany)


#### Creating Bar Chart For Character Count ####

	

	charcount_x = [str_oneThruSeven, str_eight, str_nineThruTwelve, str_ThirteenPlus]

	charcount = [oneThruSeven, eight, nineThruTwelve, thirteenPlus]



	char_x_pos = [i for i, _ in enumerate(charcount_x)]



	plt.bar(char_x_pos, charcount, align='center')

	plt.xlabel("Character Count")

	plt.ylabel("Password Count")

	plt.title("Passwords by Character Count")



	plt.xticks(char_x_pos, charcount_x)



	plt.savefig('character_count.png')

	plt.close()



#### Creating Bar Chart For Containing String ####



	strcount_x = [str_company, str_password, str_season]

	strcount = [pwWithCompany, pwWithPassword, pwWithSeason]



	str_x_pos = [i for i, _ in enumerate(strcount_x)]



	plt.bar(str_x_pos, strcount)

	plt.xlabel("Strings (Case Insensitive)")

	plt.ylabel("Password Count")

	plt.title("Passwords by String Count")



	plt.xticks(str_x_pos, strcount_x)



	plt.savefig('string_count.png')

	plt.close()


	
#### Bar Chart for All Creds ####

if creds1File != None:

	if creds2File != None:


		if creds4File != None:
			charcount_x = ["1", "2", "3", "4"]	
			charcount = [s1_uniqCredsCount, s2_uniqCredsCount, s3_uniqCredsCount, s4_uniqCredsCount]

		elif creds3File != None: 
			charcount_x = ["1", "2", "3"]	
			charcount = [s1_uniqCredsCount, s2_uniqCredsCount, s3_uniqCredsCount]

		elif creds2File != None: 
			charcount_x = ["1", "2"]	
			charcount = [s1_uniqCredsCount, s2_uniqCredsCount]

		char_x_pos = [i for i, _ in enumerate(charcount_x)]

		plt.bar(char_x_pos, charcount, align='center')
		plt.xlabel("Scenario")
		plt.ylabel("Unique Credentials Harvested")
		plt.title("Unique Credentials Harvested by Scenario")

		plt.xticks(char_x_pos, charcount_x)

		plt.savefig('creds_harvested.png')
		plt.close()

#### Reading the Recommendations File ####

if recommendations != None:
	with open(str(recommendations), 'r') as myfile:
		data = myfile.read()
		str_recommendations += str(data)

#### Reading the Scenarios File ####

if scenarios != None:
	with open(str(scenarios), 'r') as myfile:
		data = myfile.read()
		str_scenarios += str(data)

#### Reading the Scenarios File ####

if summary != None:
	with open(str(summary), 'r') as myfile:
		data = myfile.read()
		str_summary += str(data)

#### Creating HTML ####

h = open(outFile, 'w')

html = """<html>
<head><b><h1 style="color:blue; font: 18px;"><center>Phishing Observations, Statistics, and Reporting</center></h1></b></head>
<title>Phishing Statistics</title>
<body>
<center> 
<p>"""
if watermark != None:
	html += """<img src='"""
	html += str(watermark)
	html += """')> </center></br>"""
if clientName != None:
	html += """<center><b>Performed for: </b>"""
	html += str(clientName)
	html += """</br><b> Report Generated On: </b>"""
	html += str(date)
	html += """</center></br></br>"""
html += """<center> <h2 style="font: 15px;"><b>Table of Contents</h2></b> </br>"""
html += """<a href="#description">Summary</a></br>
<a href="#clickrate">Click Rate Statistics</a></br></center>"""
if creds1File != None:
	html += """<center><a href="#creds">Harvested Credentials Statistics</a></br>
	<a href="#audit">Harvested Credentials Password Audit</a></br>
	<a href="#recommendations">Recommendations</a></center></br></center>"""
	html += """<b><p id="description"><h2 style="font: 15px;">Summary</h2></p></b></br>"""
if summary == None:	
	if companyName != None:
		html += str(companyName)
		html += """ conducted a phishing campaign with """
	elif companyName == None:
		html += """</br>GameOfPWNZ conducted a phishing campaign with """
	html += str(campaigns)
	html += """ different scenarios. A total of """
	html += str(emailTotal)
	html += """ emails were sent out during the campaign. """
	if companyName != None:
		html += str(companyName)
	elif companyName ==None:
		html += """GameOfPWNZ"""

	html += """ observed clicks on links with unique identifiers tied to users that were targeted in the campaigns """

	if creds1File != None:
		html += """as well as credentials harvested from users using fake login pages. """
	elif creds1File != None:
		html += """."""
elif summary != None:
	html += str(str_summary)

if scenarios != None:
	html += """</br><b><p id="scenarios"> <h2 style="font: 15px;">Scenarios</h2></p></b></br>"""
	html += str(str_scenarios)
	html += """<br>"""


#if scenario1Total != None:
#	html += """ </br></br> For scenario 1, """
#	html += str(scenario1Total)
#	html += """ emails were sent. """

#if scenario2Total != None:
#	html += """ </br></br> For scenario 2, """
#	html += str(scenario2Total)
#	html += """ emails were sent. """

#if scenario3Total != None:
#	html += """ </br></br> For scenario 3, """
#	html += str(scenario3Total)
#	html += """ emails were sent. """

#if scenario4Total != None:
#	html += """ </br></br> For scenario 4, """
#	html += str(scenario4Total)
#	html += """ emails were sent. """


html += """</br></br><b><p id="clickrate"><h2 style="font: 15px;">Click Rate Statistics</h2></p></b></br>"""



html += """<img src='ClickRate_All_Pie.png')></br>"""

if scenario1Total != None:
	html += """<img src='ClickRate_Scenario1_Pie.png')>"""

if scenario2Total != None:
	html += """<img src='ClickRate_Scenario2_Pie.png')>"""

if scenario3Total != None:
	html += """<img src='ClickRate_Scenario3_Pie.png')>"""

if scenario4Total != None:
	html += """<img src='ClickRate_Scenario4_Pie.png')>"""


if creds2File != None:
	html += """</br></br><b><p id="creds"><h2 style="font: 15px;">Harvested Credentials Statistics</h2></p></b></br>"""
	html += """<img src='creds_harvested.png')>"""

if creds1File != None:
	html += """</br></br><b><p id="audit"><h2 style="font: 15px;">Harvested Credentials Password Audit</h2></p></b></br>"""	
	html += """<img src='character_count.png')>"""
	html += """<img src='string_count.png')>"""

if recommendations != None:
	html += """</br><b><p id="recommendations"> <h2 style="font: 15px;">Recommendations</h2></p></b></br>"""
	html += str(str_recommendations)
	html += """<br>"""
html +="""
</p>
</body>
</html>"""

h.write(html)
h.close()

webbrowser.open(outFile)
