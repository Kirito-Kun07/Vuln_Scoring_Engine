#!/usr/bin/python3.6
from glob import iglob
import os
o = os.popen

points = 0
vulns = 0

#Scoring Report Webpage
#TODO: CHANGE USER IN PATH BELOW
report_startup = open("/home/it_support/Desktop/ScoringReport.html", "w")
website_base_code = ["<!DOCTYPE html>\n\n", "<html lang='en'>\n\n", "<head>\n", "<title>Scoring Report</title>\n", "<meta charset='UTF-8'>\n", "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n", "<meta http-equiv='refresh' content='30;url=ScoringReport.html'>\n\n", "<link rel='stylesheet' href='.ScoringReport.css'>\n", "</head>\n", "<body>\n", "<div class='main'>\n", "<div class='text'>\n", "<div class='binary' data-binary='1010 0001 00011010 10110101'>\n\n", "<h1>CP Linux Beginner/Intermediate Training Image#2</h1>\n\n", "<p align=center style='width:100%;text-align:center;'>\n", "<img align=middle class='L8_style' src='.layer_8.png' width='212px' height='212px'>\n", "</p>\n\n", "<h2>Report Generated At: <span id='datetime'></span></h2>\n\n", "<h3 class='center'>Current Team ID: PRO <span style='color:red'>--</span></h3>\n\n", "<h2><span style='color:red' class=sed>p</span> out of <span style='color:red'>100</span> points received</h2>\n\n", "<p><b>This is your most recent scoring report:</b></p>\n\n", "<a href='https://www.youtube.com/watch?v=pBrCzsgDpYA'>Click here to see the most recent scoring report with feedback enabled</a><br>\n", "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Click here to view the public scoreboard</a><br>\n", "<p>\n", "<h3>Connection Status: <span style='color:red'>Epic</span></h3>\n\n", "<h3><span style='color:red'>0</span> penalties assessed, for a loss of <span style='color:red'>0</span> points:</h3>\n\n", "<p>\n\n", "</p>\n", "<h3><span style='color:red' class=sed>v</span> out of <span style='color:red'>50</span> scored security issues fixed, for a gain of <span style='color:red' class=sed>p</span> points:</h3>\n", "<p>\n"]
report_startup.writelines(website_base_code)
report_startup.close()
report_append = open("/home/it_support/Desktop/ScoringReport.html", "a")

#Vulns
def account_policy():
        c = o("grep 'PASS_MAX_DAYS' /etc/login.defs").read().split('\n')
        #Password Policies
        if ((int(str(c[1])[14:]) >= 60) and (int(str(c[1])[14:]) <= 90)):
                points += 2
                vulns += 1
                report_append.write("<h3>A Default Maximum Password Age is Set (60-90)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'PASS_MIN_DAYS' /etc/login.defs").read().split('\n')
        if ((int(str(c[1])[14:]) >= 8) and (int(str(c[1])[14:]) <= 10)):
                points += 2
                vulns += 1
                report_append.write("<h3>A Default Minimum Password Age is Set (8-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'PASS_WARN' /etc/login.defs").read().split('\n')
        if ((int(str(c[1])[14:]) >= 7) and (int(str(c[1])[14:]) <= 14)):
                points += 2
                vulns += 1
                report_append.write("<h3>A Default Warning Password Age is Set (7-14)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep libpam-crack").read().split('\n')
        if ("libpam-crack" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Extra Dictionary Based Password Strength Checks Enabled&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'minlen=' /etc/pam.d/common-password").read().split('\n')
        if ("minlen=8" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>A Secure Minimum Password Length is Required (8-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("minlen=9" in str(c[0])):
                points += 2
                vulns +=1
                report_append.write("<h3>A Secure Minimum Password Length is Required (8-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("minlen=10" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>A Secure Minimum Password Length is Required (8-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1' /etc/pam.d/common-password").read().split('\n')
        if ("ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Passwords Must Meet Complexity Requirements (1 uppercase, 1 lowercase, 1 digit, 1 special character)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'remember=5' /etc/pam.d/common-password").read().split('\n')
        if ("remember=5" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Previous passwords are remembered (5-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("remember=6" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Previous passwords are remembered (5-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("remember=7" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Previous passwords are remembered (5-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("remember=8" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Previous passwords are remembered (5-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("remember=9" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Previous passwords are remembered (5-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("remember=10" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Previous passwords are remembered (5-10)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep -R 'sha512' /etc/pam.d/common-password").read().split('\n')
        if ("sha512" in str(c[1])):
                points += 2
                vulns += 1
                report_append.write("<h3>A Secure Password Hashing Algorithm is Used (Sha512)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

def defensive_countermeasure():
        c = o("sudo ufw status verbose").read().split('\n')
        #c = str(c[0])
        #Firewall enabled, logging on, logging mode set
        if (": active" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Uncomplicated Firewall (UFW) Protection Has Been Enabled&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        if (": on" in str(c[1])):
                points += 2
                vulns += 1
                report_append.write("<h3>Uncomplicated Firewall (UFW) Logging Has Been Enabled&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        if ("(medium)" in str(c[1])):
                points += 2
                vulns += 1
                report_append.write("<h3>Uncomplicated Firewall (UFW) Logging Level is Set (Medium - High)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("(high)" in str(c[1])):
                points += 2
                vulns += 1
                report_append.write("<h3>Uncomplicated Firewall (UFW) Logging Level is Set (Medium - High)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("ufw status verbose | grep '1337'").read().split('\n')
        if ("1337" and "DENY" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Proper UFW Firewall 'DENY' Rule is Set (Port:1337)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        
        c = o("ufw status verbose | grep '80'").read().split('\n')
        if ("80" and "ALLOW" in str(c[0])):
                c = o("ufw status verbose | grep '2200'").read().split('\n')                
                if ("2200" and "ALLOW" in str(c[0])):
                        points += 2
                        vulns += 1
                        report_append.write("<h3>Proper UFW Firewall 'ALLOW' Rules Are Set (Ports:80,2200 / SSH,Apache)&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep 'clamav'").read().split('\n')
        if ("clamav" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>ClamAV Antivirus is Installed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        
        c = o("dpkg -l | grep 'lynis'").read().split('\n')
        if ("lynis" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Lynis is Installed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        
        c = o("dpkg -l | grep 'rkhunter'").read().split('\n')
        if ("rkhunter" in str([0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Rkhunter is Installed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

def forensic_question():

def local_policy():

def malware():

def operating_system_updates():

        
        c = o("grep 'deb http://security.ubuntu.com/ubuntu/ bionic-security main multiverse restricted universe' /etc/apt/sources.list").read().split('\n')
        if ("deb http://security.ubuntu.com/ubuntu/ bionic-security main multiverse restricted universe" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Enabled Important Security Updates&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
def prohibited_files():

def service_auditing():

def uncategorized_operating_system_settings():

def unwanted_software():

def user_auditing():
        return

report_append.close()
#TODO: CHANGE USER IN FILE PATH BELOW
os.system("sed -i 's/class=sed>v</class=sed>{}</g' /home/it_support/Desktop/ScoringReport.html".format(vulns))
os.system("sed -i 's/class=sed>p</class=sed>{}</g' /home/it_support/Desktop/ScoringReport.html".format(points))

#print(int(str(c[1])[14:]) + 1111)