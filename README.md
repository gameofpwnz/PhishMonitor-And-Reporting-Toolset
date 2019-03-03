# PhishMonitor-And-Reporting-Toolset
PhishMonitor and Reporting Toolset

Will add more about usage soon!

```
usage: phishmonitor.py [-h] [-p PORT] [-s1 SCENARIO1] [-s2 SCENARIO2]
                       [-s3 SCENARIO3] [-s4 SCENARIO4]

PhishMonitor (Python Edition) by GameOfPWNZ and Jacob Giannantonio

optional arguments:
  -h, --help     show this help message and exit
  -p PORT        Port Number For PhishMonitor
  -s1 SCENARIO1  Redirect Link for Scenario 1 (Put in Quotes - Ex:
                 'https://gameofpwnz.com'
  -s2 SCENARIO2  Redirect Link for Scenario 2 (Put in Quotes - Ex:
                 'https://gameofpwnz.com'
  -s3 SCENARIO3  Redirect Link for Scenario 3 (Put in Quotes - Ex:
                 'https://gameofpwnz.com'
  -s4 SCENARIO4  Redirect Link for Scenario 4 (Put in Quotes - Ex:
                 'https://gameofpwnz.com'
```                 
Example:          
                 
root@kali:~/projects/phishing# python3 phishmonitor.py -p 80 -s1 'https://gameofpwnz.com'
Listening on localhost:80

In the phishmonitor.py, make sure to change the targets!

```
targets = {
	"S1-000": "ashton@gameofpwnz.com",
	"S1-001": "gameofpwnz210@gmail.com",
	"S2-000": "jacob@gameofpwnz.com",
	"S2-001": "jmg@gameofpwnz.com",
}
```

  
    
 ```     
  usage: phishstats.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE] [-p PRETEXTS]
                     [-s1 SCENARIO1] [-s2 SCENARIO2] [-s3 SCENARIO3]
                     [-s4 SCENARIO4] [-c1 CREDS1] [-c2 CREDS2] [-c3 CREDS3]
                     [-c4 CREDS4] [-t TOTAL] [-s STRING] [-c COMPANY]
                     [-w WATERMARK] [-v CLIENT] [-r RECOMMENDATIONS]
                     [-sf SCENARIOS] [-ex SUMMARY] [--style STYLE]

Phish Stats: The complementary tool to PhishMonitor (Python Edition) by
GameOfPWNZ and Jacob Giannantonio

optional arguments:
  -h, --help          show this help message and exit
  -i INPUT_FILE       Input file (Default: phishing_log.txt)
  -o OUTPUT_FILE      Output file (HTML)
  -p PRETEXTS         Total Number of Scenarios Run
  -s1 SCENARIO1       Total Emails Sent For Scenario 1
  -s2 SCENARIO2       Total Emails Sent For Scenario 2
  -s3 SCENARIO3       Total Emails Sent For Scenario 3
  -s4 SCENARIO4       Total Emails Sent For Scenario 4
  -c1 CREDS1          Harvested Creds File From Scenario 1
  -c2 CREDS2          Harvested Creds File From Scenario 2
  -c3 CREDS3          Harvested Creds File From Scenario 3
  -c4 CREDS4          Harvested Creds File From Scenario 4
  -t TOTAL            Total Number of Emails Sent
  -s STRING           STRING to search Harvested Creds (Only if Harvested
                      Creds File(s) is/are supplied. Ex: (COMPANYNAME)
  -c COMPANY          Company Name
  -w WATERMARK        Company Watermark (PNG Recommended)
  -v CLIENT           Client Name
  -r RECOMMENDATIONS  File with Recommendations (See Example Provided With
                      Phish Stats For Format)
  -sf SCENARIOS       File with Scenario Descriptions (See Example Provided
                      With Phish Stats For Format)
  -ex SUMMARY         File with Executive Summary - Replaces Default Summary
                      (See Example Provided With Phish Stats For Format)
  --style STYLE       MatPlotLib Style: Default (seaborn-darkgrid)
                      https://tonysyu.github.io/raw_content/matplotlib-style-
                      gallery/gallery.html

```
Example:

python3 phishstats.py -i phishing_log.txt -o output.html -c1 harvested_creds.txt -c2 harvested_creds.txt -c3 harvested_creds.txt -c4 harvested_creds.txt  -t 40 -s test -p 4 -s1 10 -s2 10 -s3 10 -s4 10 -c PWNZ -w gop.png -v "Fake Client" -r recommendations.txt -sf scenarios.txt -ex summary.txt
