#### Imports ####

from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import argparse

#### Argument Parser ####
 
parser=argparse.ArgumentParser(
    description='PhishMonitor (Python Edition) by GameOfPWNZ and Jacob Giannantonio')
parser.add_argument('-p', dest="PORT", type = int, help="Port Number For PhishMonitor")
parser.add_argument('-s1', dest="SCENARIO1", help="Redirect Link for Scenario 1 (Put in Quotes - Ex: 'https://gameofpwnz.com' ")
parser.add_argument('-s2', dest="SCENARIO2", help="Redirect Link for Scenario 2 (Put in Quotes - Ex: 'https://gameofpwnz.com' ")
parser.add_argument('-s3', dest="SCENARIO3", help="Redirect Link for Scenario 3 (Put in Quotes - Ex: 'https://gameofpwnz.com' ")
parser.add_argument('-s4', dest="SCENARIO4", help="Redirect Link for Scenario 4 (Put in Quotes - Ex: 'https://gameofpwnz.com' ")
args=parser.parse_args()

#### Time Variable ####

time = datetime.datetime.now()
timestamp = str(time)
port = args.PORT
scenario1_redirect = args.SCENARIO1
scenario2_redirect = args.SCENARIO2
scenario3_redirect = args.SCENARIO3
scenario4_redirect = args.SCENARIO4

#### User Dictionary ####

targets = {
	"S1-000": "ashton@gameofpwnz.com",
	"S1-001": "gameofpwnz210@gmail.com",
	"S2-000": "jacob@gameofpwnz.com",
	"S2-001": "jmg@gameofpwnz.com",
}


#### PhishServer Class ####

class PhishServer(BaseHTTPRequestHandler):
 
	def do_GET(self):
        
		request_path = self.path
		client_ip = self.client_address[0]
		ua = self.headers.get('user-agent')

#### Setup Redirect ####
        
		self.send_response(301)
        

#### Scenario 1 ####

		if "S1" in str(request_path).upper():
			
			for key, value in targets.items():
		
				if key in str(request_path).upper():
					print(timestamp, " : ", value, " has clicked the link to phishing pretext #1 from ", client_ip, " with user-agent: ", ua)
					f = open('phishing_log.txt', 'a')
					f.write(timestamp + " : user:" + value + " has clicked the link to phishing pretext #1 from ipaddress: " + client_ip + " with user-agent: " + ua + "\n")
					f.close()

			self.send_header('Location',str(scenario1_redirect))
			self.end_headers()

#### Scenario 2 ####

		elif "S2" in str(request_path).upper():

			for key, value in targets.items():
		
				if key in str(request_path).upper():
					print(timestamp, " : ", value, " has clicked the link to phishing pretext #2 from ", client_ip, " with user-agent: ", ua)
					f = open('phishing_log.txt', 'a')
					f.write(timestamp + " : user:" + value + " has clicked the link to phishing pretext #2 from ipaddress: " + client_ip + " with user-agent: " + ua + "\n")
					f.close()

			
			if scenario2_redirect != None:
				self.send_header('Location',str(scenario2_redirect))
				self.end_headers()
			elif scenario2_redirect == None:
				self.send_header('Location','https://gameofpwnz.com')
				self.end_headers()

#### Scenario 3 ####

		elif "S3" in str(request_path).upper():

			for key, value in targets.items():
		
				
				if key in str(request_path).upper():
					print(timestamp, " : ", value, " has clicked the link to phishing pretext #3 from ", client_ip, " with user-agent: ", ua)
					f = open('phishing_log.txt', 'a')
					f.write(timestamp + " : user:" + value + " has clicked the link to phishing pretext #3 from ipaddress: " + client_ip + " with user-agent: " + ua + "\n")
					f.close()

			if scenario3_redirect != None:
				self.send_header('Location',str(scenario3_redirect))
				self.end_headers()
			elif scenario2_redirect == None:
				self.send_header('Location','https://gameofpwnz.com')
				self.end_headers()


#### Scenario 4 ####
		
		elif "S4" in str(request_path).upper():

			for key, value in targets.items():
		
				if key in str(request_path).upper():
					print(timestamp, " : ", value, " has clicked the link to phishing pretext #4 from ", client_ip, " with user-agent: ", ua)
					f = open('phishing_log.txt', 'a')
					f.write(timestamp + " : user:" + value + " has clicked the link to phishing pretext #4 from ipaddress: " + client_ip + " with user-agent: " + ua + "\n")
					f.close()

			if scenario4_redirect != None:
				self.send_header('Location',str(scenario4_redirect))
				self.end_headers()
			elif scenario2_redirect == None:
				self.send_header('Location','https://gameofpwnz.com')
				self.end_headers()


#### Out of Scope Requests ####

		else:
			
			print(timestamp, " : ", "Intruder Alert")
			f = open('intruders.txt', 'a')
			f.write(timestamp + " : " + "You might have an intruder. The offending IP Address: " + ua + "\n")
			self.send_header('Location','https://facebook.com')
			self.end_headers()

#### Main - Start Web Server ####

def main():
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), PhishServer)
    server.serve_forever()
   

main()
