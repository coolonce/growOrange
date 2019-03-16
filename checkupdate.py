#!/usr/bin/python
from daemon import runner
from crontab import CronTab
import json
import urllib3
	
class App():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = 'logUpdate.txt'
		self.stderr_path = 'logUpdateErr.txt'
		self.pidfile_path = '/tmp/checkupdatesettings.pid'
		self.pidfile_timeout = 4
	
	def run(self):
		device_id = open('/home/swpi/growOrange/file_ver.info').readline()
		currentSsettings = ""
		with open('settings.info','w+') as fileSettings:
			currentSsettings = fileSettings.readline()
		http = urllib3.PoolManager()		
		r = http.request('GET', '83.220.169.215/api/settings/'+device_id+'/11',headers = {'Content-Type':'application/json'})
		resp = json.loads(r.data)		
		if not currentSsettings == '':
			currentSsettings = json.loads(currentSsettings)
		if(len(currentSsettings) == 0 or not resp['11'] == currentSsettings['11']):
			
			with open('settings.info','w+') as fileSettings:
				fileSettings.write(r.data)
			cron = CronTab(user='swpi')
			create = False
			for job in cron:				
				if job.comment == 'sendSig1':					
					job.hour.on(int(resp['11']))
					cron.write()
					print("modification")
					create = True
					break				
			if(not create):
				job = cron.new(command='/usr/bin/python /home/swpi/growOrange/sendSig.py', comment='sendSig1')
				job.hours.on(int(resp['11']))					
				print("create")
				cron.write()

app = App()
app.run()
daemon_run = runner.DaemonRunner(app)
daemon_run.do_action()