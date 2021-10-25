#!/usr/bin/python3.5
import os

#Create files to better score
def grep_files():
	c = os.system
	cls = c("clear")

	#not needed for forensics 

	c("grep 'PermitRootLogin' /etc/ssh/sshd_config | tee /opt/v/sshd_conf1.txt")
	c("clear")
	c("grep 'Protocol' /etc/ssh/sshd_config | tee /opt/v/sshd_conf2.txt")
	c("clear")

	c("grep 'iddinnerbone' /etc/passwd | tee /opt/v/unauth_users1.txt | clear")
	c("grep 'robl0xru1es' /etc/passwd | tee /opt/v/unauth_users2.txt | clear")
	c("grep 'sudo' /etc/group | tee /opt/v/unauth_admin.txt | clear")

	c("grep 'PASS_MAX_DAYS' /etc/login.defs | tee /opt/v/password_pol1.txt | clear")
	c("clear")
	c("grep 'PASS_MIN_DAYS' /etc/login.defs | tee /opt/v/password_pol2.txt | clear")
	c("clear")
	c("grep 'PASS_WARN' /etc/login.defs | tee /opt/v/password_pol3.txt | clear")
	c("clear")

	c("ufw status | tee /opt/v/firewall_conf.txt | clear")
	c("clear")

	c("dpkg -l | grep john | tee /opt/v/h_tools1.txt | clear")
	c("clear")
	c("dpkg -l | grep nmap | tee /opt/v/h_tools2.txt | clear")
	c("clear")

	c("find /home/creeper/ -iname '*.py' | tee /opt/v/malware.txt | clear")
	c("find /home/steve/Downloads/ -iname '*.mp3' | tee /opt/v/music1.txt | clear")
	c("find /home/johntheenderman/Desktop/ -iname '*.mp3' | tee /opt/v/music2.txt | clear")

	c("grep 'deb http://security.ubuntu.com/ubuntu/ xenial-security restricted multiverse' /etc/apt/sources.list | tee /opt/v/security_updates.txt | clear")

	#c("grep '' / | tee ")

grep_files()
c = os.system

points = 0
vulns = 0

#Scoring Report

report_startup = open("/home/it_support/Desktop/Scoring_Report.html", "w")
website_base_code = ["<!DOCTYPE html>\n", "<head>\n", "<title>My Own Scoring Report</title>\n\n", "<meta charset='UTF-8'>\n", "<meta name='viewport' content='width=device-width,initial-scale=1.0'>\n", "<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n", "<link rel='stylesheet' href='.Scoring_Report.css'>\n", "</head>\n", "<p style='font-size:40px;font-weight:bolder;'><u>Scoring Report for Beginners Linux Image (WIP)</u></p>\n","<center>\n" , "<h2><span class='title1'>0 out of 100 Points Recieved</h2>\n", "<h2><span class='title2'>0 out of 17 Scored Security Issues Fixed</h2>\n", "</center>\n" , "<br/>\n", "<div class='white_box'>\n"]
report_startup.writelines(website_base_code)
report_startup.close()

#Forensic Questions
f_file1 = open("/home/it_support/Desktop/Forensic_Question_1.txt")
f_file2 = open("/home/it_support/Desktop/Forensic_Question_2.txt")
#SSHD vulns
sshd_file1 = open("/opt/v/sshd_conf1.txt", "r")
sshd_file2 = open("/opt/v/sshd_conf2.txt", "r")
#User Vulns
bad_user1 = open("/opt/v/unauth_users1.txt", "r")
bad_user2 = open("/opt/v/unauth_users2.txt", "r")
bad_admin = open("/opt/v/unauth_admin.txt", "r")
#Password Policies
pass_file1 = open("/opt/v/password_pol1.txt", "r")
pass_file2 = open("/opt/v/password_pol2.txt", "r")
pass_file3 = open("/opt/v/password_pol3.txt", "r")
#Firewall
fwall_file = open("/opt/v/firewall_conf.txt", "r")
#Hacking Tools
hack_file1 = open("/opt/v/h_tools1.txt", "r")
hack_file2 = open("/opt/v/h_tools2.txt", "r")
#Prohibited Files
mal_file = open("/opt/v/malware.txt", "r")
music_file1 = open("/opt/v/music1.txt", "r")
music_file2 = open("/opt/v/music2.txt", "r")
#Updates
sec_up_file = open("/opt/v/security_updates.txt", "r")

report_append = open("/home/it_support/Desktop/Scoring_Report.html", "a")


#Forensic Questions
if("mojang mcserver steve alex notch junkboy irong0lem" in f_file1.read()):
        report_append.write("<h3>Forensic Question 2 Is Correct&nbsp;&nbsp;&nbsp;[10 Points]</h3>\n")
        points = (points + 10)
        vulns = (vulns + 1)
if("Your Lame Server has been PWNED" and "John" in f_file2.read()):
        report_append.write("<h3>Forensic Question 1 Is Correct&nbsp;&nbsp;&nbsp;[10 Points]</h3>\n")
        points = (points + 10)
        vulns = (vulns + 1)
#SSH
if("PermitRootLogin" and "no" in sshd_file1.read()):
	report_append.write("<h3>SSH Root Login has been Disabled&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points + 6)
	vulns = (vulns + 1)
if("Protocol 2" in sshd_file2.read()):
	report_append.write("<h3>SSH Protocol 2 has been Enabled&nbsp;&nbsp;&nbsp;[3 Points]</h3>\n")
	points = (points + 6)
	vulns = (vulns + 1)
#Users
if("iddinnerbone" in bad_user1.read()):
	print("")
else:
	report_append.write("<h3>Unauthorized User iddinnerbone is Removed&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points = (points + 6)
	vulns = (vulns + 1)
if("robl0xru1es" in bad_user2.read()):
	print("")
else:
	report_append.write("<h3>Unauthorized User robl0xru1es is Removed&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points = (points + 6)
	vulns = (vulns + 1)
if("notch" in bad_admin.read()):
	print("")
else:
	report_append.write("<h3>Unauthorized Admin notch is Removed&nbsp;&nbsp;&nbsp;[5 Points]</h3>\n")
	points = (points + 5)
	vulns = (vulns + 1)
#Password Pol
if("PASS_MAX_DAYS" and "90" in pass_file1.read()):
	report_append.write("<h3>A Default Maximum Password Age is Set&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
	points = (points + 4)
	vulns = (vulns + 1)
if("PASS_MIN_DAYS" and "10" in pass_file2.read()):
	report_append.write("<h3>A Default Minimum Password Age is Set&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
	points = (points +4)
	vulns = (vulns +1)
if("PASS_WARN_AGE" and "7" in pass_file3.read()):
	report_append.write("<h3>A Default Warning Password Age is Set&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
	points = (points + 4)
	vulns = (vulns + 1)
#Firewall
if("Status: active" in fwall_file.read()):
	report_append.write("<h3>Uncomplicated Firewall (UFW) is Enabled&nbsp;&nbsp;&nbsp;[4 Points]</h3>\n")
	points = (points + 5)
	vulns = (vulns + 1)
#Hacking tools
if("john" in hack_file1.read()):
	print("")
else:
	report_append.write("<h3>Prohibited Software John the Ripper Removed&nbsp;&nbsp;&nbsp;[4 Points]</h3>")
	points = (points + 4)
	vulns = (vulns + 1)
if("nmap" in hack_file2.read()):
	c("clear")
else:
	report_append.write("<h3>Prohibited Software NMAP Removed&nbsp;&nbsp;&nbsp;[4 Points]</h3>")
	points = (points + 4)
	vulns = (vulns + 1)
#Prohibited Files
if("Calm" in music_file1.read()):
	c("clear")
else:
	report_append.write("<h3>Prohibited 'Minecraft Calm' Music File Removed&nbsp;&nbsp;&nbsp;[1 Points]</h3>")
	points = (points + 3)
	vulns = (vulns +1)
if("Sucks" in music_file2.read()):
	c("clear")
else:
	report_append.write("<h3>Prohibited 'Minecraft Sucks' Music File Removed&nbsp;&nbsp;&nbsp;[1 Points]</h3>")
	points = (points +3)
	vulns = (vulns + 1)
if(".py" in mal_file.read()):
	print("")
	c("clear")
else:
	report_append.write("<h3>Prohibited Python Malicious Program Removed&nbsp;&nbsp;&nbsp;[10 Points]</h3>")
	points = (points +10)
	vulns = (vulns + 1)
#Security Updates
if("deb http://security.ubuntu.com/ubuntu/ xenial-security restricted multiverse" in sec_up_file.read()):
	report_append.write("<h3>Install Updates from Important Security Updates&nbsp;&nbsp;&nbsp;[5 Points]</h3>")
	points = (points + 10)
	vulns = (vulns +1)

report_append.write("</div>")
report_append.write("<p style='text-align:right; bottom: auto; color:black;'>&copy;Diego Cruz</p>")
f_file1.close()
f_file2.close()
sshd_file1.close()
sshd_file2.close()
bad_user1.close()
bad_user2.close()
bad_admin.close()
pass_file1.close()
pass_file2.close()
pass_file3.close()
fwall_file.close()
hack_file1.close()
hack_file2.close()
music_file1.close()
music_file2.close()
mal_file.close()
sec_up_file.close()
report_append.close()
os.system("sed -i 's/0 out of 17 Scored Security Issues Fixed/{} out of 17 Scored Security Issues Fixed/g' /home/it_support/Desktop/Scoring_Report.html".format(vulns))
os.system("sed -i 's/0 out of 100 Points Recieved/{} out of 100 Points Recieved/g' /home/it_support/Desktop/Scoring_Report.html".format(points))
print("Scoring Engine Ran Successfully.\nCheck Your Scoring Report.")


#Forensic Qustions
#Critical Services
#Users
#Password Policies
#Firewall
#Hacking Tools
#Prohibited files
#Updates

