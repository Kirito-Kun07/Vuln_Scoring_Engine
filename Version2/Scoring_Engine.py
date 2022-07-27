#!/usr/bin/python3.5
import os

#Create files to better score for now
def grep_files():
	c = os.system
	cls = c("clear")

	#not needed for forensics questions

	#Critical Services:
	#SSHD
	c("grep 'PermitRootLogin' /etc/ssh/sshd_config | tee /opt/v/sshd_conf1.txt | clear")
	c("grep 'PermitEmptyPasswords' /etc/ssh/sshd_config | tee /opt/v/sshd_conf2.txt | clear")
	c("grep 'Protocol' /etc/ssh/sshd_config | tee /opt/v/sshd_conf3.txt | clear")

	#HTTPD
	c("dpkg -l | grep apache2 | tee /opt/v/apache_install.txt | clear")
	c("grep '' /etc/apache2/apache2.conf | tee /opt/v/apache_conf1.txt | clear")
	c("grep '' /etc/apache2/apache2.conf | tee /opt/v/apache_conf2.txt | clear")
	#c("grep 'PrintMotd' /etc/ssh/sshd_config | tee /opt/v/sshd_conf3.txt | clear")
	#c("cat /etc/issue.net | tee /opt/v/sshd_conf4.txt | clear")

	#Users
	c("grep 'creeper' /etc/passwd | tee /opt/v/unauth_users1.txt | clear")
	#c("grep 'robl0xru1es' /etc/passwd | tee /opt/v/unauth_users2.txt | clear")
	c("grep 'trolls' /etc/group | tee /opt/v/unauth_group.txt | clear")
	c("grep 'allow-guest' /etc/lightdm/lightdm.conf | tee /opt/v/guest.txt | clear")
	c("grep 'greeter-hide-users' /etc/lightdm/lightdm.conf | tee /opt/v/login1.txt | clear")
	c("grep 'greeter-show-manual-login' /etc/lightdm/lightdm.conf | tee /opt/v/login2.txt | clear")

	#Password Policies
	c("grep 'PASS_MAX_DAYS' /etc/login.defs | tee /opt/v/password_pol1.txt | clear")
	c("grep 'PASS_MIN_DAYS' /etc/login.defs | tee /opt/v/password_pol2.txt | clear")
	c("grep 'PASS_WARN' /etc/login.defs | tee /opt/v/password_pol3.txt | clear")
	c("clear")

	#Firewall
	c("sudo ufw status | tee /opt/v/firewall_conf1.txt | clear")
	c("sudo ufw status verbose | tee /opt/v/firewall_conf2.txt | clear")
	c("sudo ufw status verbose | tee /opt/v/firewall_conf3.txt | clear")
	c("sudo ufw status verbose | tee /opt/v/firewall_conf3-5.txt | clear")

	#Prohibited Programs
	c("dpkg -l | grep ophcrack | tee /opt/v/h_tools1.txt | clear")
	c("dpkg -l | grep hydra | tee /opt/v/h_tools2.txt | clear")
	c("dpkg -l | grep netcat | tee /opt/v/h_tools3.txt | clear")
	c("dpkg -l | grep minetest | tee /opt/v/game1.txt | clear")
	c("clear")

	#Backdoor
	c("crontab -u mcserver -l | grep 'nc' | tee /opt/v/mal_cron.txt | clear")

	#Security Tools Task
	c("dpkg -l | grep lynis | tee /opt/v/sec_tool1.txt | clear")
	c("dpkg -l | grep clamav | tee /opt/v/sec_tool2.txt | clear")

	#Prohibted Files
	c("ls /cave/ | tee /opt/v/malware.txt | clear")
	c("find /home/steve/  -iname '*.jpg' | tee /opt/v/picture1.txt | clear")
	c("find /home/kirito/ -iname '.*.jpg' | tee /opt/v/picture2.txt | clear")

	#Updates
	c("grep 'deb http://security.ubuntu.com/ubuntu/ xenial-security restricted multiverse' /etc/apt/sources.list | tee /opt/v/security_updates.txt | clear")
	c("grep 'deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates restricted multiverse universe main' /etc/apt/sources.list | tee /opt/v/recommended_updates.txt | clear ")
	#c("grep '' / | tee ")

grep_files()
c = os.system

points = 0
vulns = 0

#Scoring Report

report_startup = open("/home/it_support/Desktop/ScoringReport.html", "w")
#website_base_code = ["<!DOCTYPE html>\n", "<head>\n", "<title>My Own Scoring Report</title>\n\n", "<meta charset='UTF-8'>\n", "<meta name='viewport' content='width=device-width,initial-scale=1.0'>\n", "<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n", "<link rel='stylesheet' href='.Scoring_Report.css'>\n", "</head>\n", "<p style='font-size:40px;font-weight:bolder;'><u>Scoring Report for Beginners Linux Image (WIP)</u></p>\n","<center>\n" , "<h2><span class='title1'>0 out of 100 Points Recieved</h2>\n", "<h2><span class='title2'>0 out of 17 Scored Security Issues Fixed</h2>\n", "</center>\n" , "<br/>\n", "<div class='white_box'>\n"]
website_base_code = ["<!DOCTYPE html>\n\n", "<html lang='en'>\n\n", "<head>\n", "<title>Scoring Report</title>\n", "<meta charset='UTF-8'>\n", "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n", "<meta http-equiv='refresh' content='30;url=ScoringReport.html'>\n\n", "<link rel='stylesheet' href='.ScoringReport.css'>\n", "</head>\n", "<body>\n", "<div class='main'>\n", "<div class='text'>\n", "<div class='binary' data-binary='1010 0001 00011010 10110101'>\n\n", "<h1>CP Linux Beginner/Intermediate Training Image#2</h1>\n\n", "<p align=center style='width:100%;text-align:center;'>\n", "<img align=middle class='L8_style' src='.layer_8.png' width='212px' height='212px'>\n", "</p>\n\n", "<h2>Report Generated At: <span id='datetime'></span></h2>\n\n", "<h3 class='center'>Current Team ID: PRO <span style='color:red'>--</span></h3>\n\n", "<h2><span style='color:red' class=sed>100</span> out of <span style='color:red'>100</span> points received</h2>\n\n", "<p><b>This is your most recent scoring report:</b></p>\n\n", "<a href='https://www.youtube.com/watch?v=pBrCzsgDpYA'>Click here to see the most recent scoring report with feedback enabled</a><br>\n", "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Click here to view the public scoreboard</a><br>\n", "<p>\n", "<h3>Connection Status: <span style='color:red'>Epic</span></h3>\n\n", "<h3><span style='color:red'>0</span> penalties assessed, for a loss of <span style='color:red'>0</span> points:</h3>\n\n", "<p>\n\n", "</p>\n", "<h3><span style='color:red' class=sed>35</span> out of <span style='color:red'>21</span> scored security issues fixed, for a gain of <span style='color:red' class=sed>100</span> points:</h3>\n", "<p>\n"]
report_startup.writelines(website_base_code)
report_startup.close()

#Forensic Questions
f_file1 = open("/home/it_support/Desktop/Forensic_Question_1.txt")
f_file2 = open("/home/it_support/Desktop/Forensic_Question_2.txt")
#SSHD vulns
sshd_file1 = open("/opt/v/sshd_conf1.txt", "r")
sshd_file2 = open("/opt/v/sshd_conf2.txt", "r")
sshd_file3 = open("/opt/v/sshd_conf3.txt", "r")
#sshd_file4 = open("/opt/v/sshd_conf4.txt", "r")
#Apache Vulns
httpd_file1 = open("/opt/v/apache_install.txt", "r")
httpd_file2 = open("/opt/v/apache_conf1.txt", "r")
httpd_file3 = open("/opt/v/apache_conf2.txt", "r")
#User Vulns
bad_user1 = open("/opt/v/unauth_users1.txt", "r")
bad_group = open("/opt/v/unauth_group.txt", "r")
#bad_user2 = open("/opt/v/unauth_users2.txt", "r")
#bad_admin = open("/opt/v/unauth_admin.txt", "r")
guest_file = open("/opt/v/guest.txt", "r")
login_file1 = open("/opt/v/login1.txt", "r")
login_file2 = open("/opt/v/login2.txt", "r")
#Password Policies
pass_file1 = open("/opt/v/password_pol1.txt", "r")
pass_file2 = open("/opt/v/password_pol2.txt", "r")
pass_file3 = open("/opt/v/password_pol3.txt", "r")
#Firewall
fwall_file1 = open("/opt/v/firewall_conf1.txt", "r")
fwall_file2 = open("/opt/v/firewall_conf2.txt", "r")
fwall_file3 = open("/opt/v/firewall_conf3.txt", "r")
fwall_file3_5 = open("/opt/v/firewall_conf3-5.txt", "r")
#Security Tools
sec_tool1 = open("/opt/v/sec_tool1.txt", "r")
sec_tool2 = open("/opt/v/sec_tool2.txt", "r")
#Hacking Tools
hack_file1 = open("/opt/v/h_tools1.txt", "r")
hack_file2 = open("/opt/v/h_tools2.txt", "r")
hack_file3 = open("/opt/v/h_tools3.txt", "r")
#Games
game_file1 = open("/opt/v/game1.txt", "r")
#Malware
mal_file = open("/opt/v/malware.txt", "r")
mal_cron = open("/opt/v/mal_cron.txt", "r")
#Prohibited Files
#music_file1 = open("/opt/v/music1.txt", "r")
#music_file2 = open("/opt/v/music2.txt", "r")
pic_file1 = open("/opt/v/picture1.txt", "r")
pic_file2 = open("/opt/v/picture2.txt", "r")
#Updates
sec_up_file = open("/opt/v/security_updates.txt", "r")
rec_up_file = open("/opt/v/recommended_updates.txt", "r")

report_append = open("/home/it_support/Desktop/ScoringReport.html", "a")


#Forensic Questions
if("Run_4_Free_Netherite.sh" and "creeper" and "trolls" in f_file1.read()):
        report_append.write("<h3>Forensic Question 1 Is Correct&nbsp;&nbsp;&nbsp;[10 Points]</h3>\n")
        points = (points + 10)
        vulns = (vulns + 1)
if("1337" in f_file2.read()):
        report_append.write("<h3>Forensic Question 2 Is Correct&nbsp;&nbsp;&nbsp;[10 Points]</h3>\n")
        points = (points + 10)
        vulns = (vulns + 1)
#SSH
if("PermitRootLogin" and "no" in sshd_file1.read()):
	report_append.write("<h3>SSH Root Login has been Disabled&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points + 3)
	vulns = (vulns + 1)
if("PermitEmptyPasswords" and "no" in sshd_file2.read()):
	report_append.write("<h3>Permitting Empty Passwords on SSH has been Disabled&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points + 3)
	vulns = (vulns + 1)
if("Protocol 2" in sshd_file3.read()):
	report_append.write("<h3>SSH Protocol 2 Enabled&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points +3)
	vulns = (vulns + 1)
#Apache
if("apache2" in httpd_file1.read()):
	report_append.write("<h3>Installed and Deployed HTTP Apache2 Web Server&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points

#if("PrintMotd" and "yes" in sshd_file3.read()):
#	report_append.write("<h3>SSH Message of the Day Banner is Enabled&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
#	points = (points +3)
#	vulns = (vulns + 1)
#if("warning" and "unauthorized" in sshd_file4.read()):
#	report_append.write("<h3>SSH Banner Contains an Authentication Warning&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
#	points = (points + 3)
#	vulns = (vulns + 1)
#Users
#if("iddinnerbone" in bad_user1.read()):
#	print("")
#else:
#	report_append.write("<h3>Unauthorized User iddinnerbone is Removed&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
#	points = (points + 6)
#	vulns = (vulns + 1)
#if("robl0xru1es" in bad_user2.read()):
#	print("")
#else:
#	report_append.write("<h3>Unauthorized User robl0xru1es is Removed&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
#	points = (points + 6)
#	vulns = (vulns + 1)
#if("notch" in bad_admin.read()):
#	print("")
#else:
#	report_append.write("<h3>Unauthorized Admin notch is Removed&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
#	points = (points + 5)
#	vulns = (vulns + 1)
if("creeper" in bad_user1.read()):
	print("")
else:
	report_append.write("<h3>Removed user 'creeper' for Unethical Computer Use&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points = (points + 5)
	vulns = (vulns + 1)
if("trolls" in bad_group.read()):
	print("")
else:
	report_append.write("Removed Unauthorized group 'trolls'<br>")
	points = (points + 5)
	vulns = (vulns + 1)
#Password Pol
if("PASS_MAX_DAYS" and "90" in pass_file1.read()):
	report_append.write("<h3>A Default Maximum Password Age is Set&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points + 3)
	vulns = (vulns + 1)
if("PASS_MIN_DAYS" and "10" in pass_file2.read()):
	report_append.write("<h3>A Default Minimum Password Age is Set&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points +3)
	vulns = (vulns +1)
if("PASS_WARN_AGE" and "7" in pass_file3.read()):
	report_append.write("<h3>A Default Warning Password Age is Set&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points + 3)
	vulns = (vulns + 1)
#Firewall
if("Status: active" in fwall_file1.read()):
	report_append.write("<h3>Uncomplicated Firewall (UFW) is Enabled&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points = (points + 5)
	vulns = (vulns + 1)
if("Logging: on" in fwall_file2.read()):
	report_append.write("<h3>Uncomplicated Firewall (UFW) has Logs Enabled &nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points = (points + 5)
	vulns = (vulns + 1)
if("high" in fwall_file3.read() or "medium" in fwall_file3_5.read()):
	report_append.write("<h3>Uncomplicated Firewall (UFW) Logs Include Detailed Events&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points = (points + 5)
	vulns = (vulns + 1)
#Hacking tools
if("ophcrack" in hack_file1.read()):
	print("")
else:
	report_append.write("<h3>Prohibited Software Ophcrack Password Cracking Tool Removed&nbsp;&nbsp;&nbsp;[4 Points]</h3>")
	points = (points + 4)
	vulns = (vulns + 1)
if("hydra" in hack_file2.read()):
	c("clear")
else:
	report_append.write("<h3>Prohibited Software Hydra Network Logon Cracker Removed&nbsp;&nbsp;&nbsp;[4 Points]</h3>")
	points = (points + 4)
	vulns = (vulns + 1)
if("netcat" in hack_file3.read()):
	c("clear")
else:
	report_append.write("<h3>Netcat Backdoor & Program Removed&nbsp;&nbsp;&nbsp;[4 Points]</h3>")
	points = (points + 4)
	vulns = (vulns + 1)
#Prohibited Files
if("meme" in pic_file1.read()):
	c("clear")
else:
	report_append.write("<h3>Prohibited 'Meme' Media File Removed&nbsp;&nbsp;&nbsp;[3 Points]</h3>")
	points = (points + 3)
	vulns = (vulns +1)
if("squidgame" in pic_file2.read()):
	c("clear")
else:
	report_append.write("<h3>Prohibited 'SquidGame' Media File Removed&nbsp;&nbsp;&nbsp;[3 Points]</h3>")
	points = (points +3)
	vulns = (vulns + 1)
if(".sh" in mal_file.read()):
	c("clear")
else:
	report_append.write("<h3>Prohibited Bash Malicious Program Removed&nbsp;&nbsp;&nbsp;[10 Points]</h3>")
	points = (points +10)
	vulns = (vulns + 1)
#Updates
if("deb http://security.ubuntu.com/ubuntu/ xenial-security restricted multiverse" in sec_up_file.read()):
	report_append.write("<h3>Enabled  Important Security Updates&nbsp;&nbsp;&nbsp;[5 Points]</h3>")
	points = (points + 5)
	vulns = (vulns +1)
if("deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates restricted multiverse universe" in rec_up_file.read()):
	report_append.write("<h3>Enabled Important Recommended Updates&nbsp;&nbsp;&nbsp;[5 Points]</h3>")
	points = (points + 5)
	vulns = (vulns + 1)


report_append.write("</p>")
report_append.write("<p align='center' style='text-align: center;'><i>This is a part of the CSUN Layer 8 Computer Security Club Cyberpatriot Trainings</i></p>")
report_append.write("</div>")
report_append.write("</div>")
report_append.write("</div>")
report_append.write("<p style='text-align:right; bottom: auto; color:black;'>&copy;Diego Cruz</p>")
report_append.write("</body>")
javascript = ["<script>\n", "var bin = document.querySelectorAll('.binary');\n", "[].forEach.call(bin, function(el) {\n", "	el.dataset.binary = Array(4096).join(el.dataset.binary + ' ')\n","});\n\n", "var dt = new Date();\n\n", "document.getElementById('datetime').innerHTML = (('0'+dt.getHours()).slice(-2)) +':'+ (('0'+dt.getMinutes()).slice(-2)) + ':'+ (('0'+dt.getSeconds()).slice(-2)) + ' '+ ((dt.getFullYear()) +'-'+ (('0'+(dt.getMonth()+1)).slice(-2)) +'-'+ ('0'+dt.getDate()).slice(-2)) + ' UTC';\n", "</script>\n"]
report_append.writelines(javascript)
f_file1.close()
f_file2.close()
sshd_file1.close()
sshd_file2.close()
#sshd_file3.close()
#sshd_file4.close()
httpd_file1.close()
httpd_file2.close()
httpd_file3.close()
bad_user1.close()
bad_group.close()
#bad_user2.close()
#bad_admin.close()
pass_file1.close()
pass_file2.close()
pass_file3.close()
fwall_file1.close()
fwall_file2.close()
fwall_file3.close()
fwall_file3_5.close()
sec_tool1.close()
sec_tool2.close()
hack_file1.close()
hack_file2.close()
pic_file1.close()
pic_file2.close()
#music_file1.close()
#music_file2.close()
mal_file.close()
mal_cron.close()
sec_up_file.close()
rec_up_file.close()
report_append.close()
os.system("sed -i 's/class=sed>35</class=sed>{}</g' /home/it_support/Desktop/ScoringReport.html".format(vulns))
os.system("sed -i 's/class=sed>100</class=sed>{}</g' /home/it_support/Desktop/ScoringReport.html".format(points))
print("Scoring Engine Ran Successfully.\nCheck Your Scoring Report.")


#Forensic Qustions
#Critical Services
#Users
#Password Policies
#Firewall
#Hacking Tools
#Prohibited files
#Updates

