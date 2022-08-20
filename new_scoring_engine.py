#!/usr/bin/python3.6
#from glob import iglob
import os
o = os.popen

points = 0
vulns = 0

#Scoring Report Webpage
#TODO: CHANGE USER IN PATH BELOW
report_startup = open("/home/it_support/Desktop/ScoringReport.html", "w")
website_base_code = ["<!DOCTYPE html>\n\n", "<html lang='en'>\n\n", "<head>\n", "<title>Scoring Report</title>\n", "<meta charset='UTF-8'>\n", "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n", "<meta http-equiv='refresh' content='30;url=ScoringReport.html'>\n\n", "<link rel='stylesheet' href='.ScoringReport.css'>\n", "</head>\n", "<body>\n", "<div class='main'>\n", "<div class='text'>\n", "<div class='binary' data-binary='1010 0001 00011010 10110101'>\n\n", "<h1>CCDC 50 Vulnerability Mojang Image</h1>\n\n", "<p align=center style='width:100%;text-align:center;'>\n", "<img align=middle class='L8_style' src='.layer_8.png' width='212px' height='212px'>\n", "</p>\n\n", "<h2>Report Generated At: <span id='datetime'></span></h2>\n\n", "<h3 class='center'>Current Team ID: CSUN <span style='color:red'>--</span></h3>\n\n", "<h2><span style='color:red' class=sed>p</span> out of <span style='color:red'>100</span> points received</h2>\n\n", "<p><b>This is your most recent scoring report:</b></p>\n\n", "<a href='https://www.youtube.com/watch?v=pBrCzsgDpYA'>Click here to see the most recent scoring report with feedback enabled</a><br>\n", "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Click here to view the public scoreboard</a><br>\n", "<p>\n", "<h3>Connection Status: <span style='color:red'>Working</span></h3>\n\n", "<h3><span style='color:red'>0</span> penalties assessed, for a loss of <span style='color:red'>0</span> points:</h3>\n\n", "<p>\n\n", "</p>\n", "<h3><span style='color:red' class=sed>v</span> out of <span style='color:red'>50</span> scored security issues fixed, for a gain of <span style='color:red' class=sed>p</span> points:</h3>\n", "<p>\n"]
report_startup.writelines(website_base_code)
report_startup.close()
report_append = open("/home/it_support/Desktop/ScoringReport.html", "a")

#Vulns
def account_policy():
        global points
        global vulns
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
                report_append.write("<h3>Uncomplicated Firewall (UFW) Protection has been Enabled&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        if (": on" in str(c[1])):
                points += 2
                vulns += 1
                report_append.write("<h3>Uncomplicated Firewall (UFW) Logging has been Enabled&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
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
        c = o("cat /home/it_support/Desktop/Forensic_Question_1")
        if("nc.traditional" and "1337" in str(c[0])):
                report_append.write("<h3>Forensic Question 1 Is Correct&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
                points = (points + 2)
                vulns = (vulns + 1)
        
        c = o("dpkg -l | grep 'docker'").read().split('\n')
        if("docker" in str(c[0])):
                report_append.write("<h3>Inject Docker Installation Task has been Completed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
                points = (points + 2)
                vulns = (vulns + 1)
def local_policy():
        c = o("grep 'net.ipv4.tcp_syncookies' /etc/sysctf.conf").read().split('\n')
        k = o("cat /proc/sys/net/ipv4/tcp_syncookies").read().split('\n')
        if ("1" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 TCP SYN cookies have been Enabled <i>(net.ipv4.tcp_syncookies = 1)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("1" in str(k[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 TCP SYN cookies have been Enabled <i>(net.ipv4.tcp_syncookies = 1)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'net.ipv4.conf.all.rp_filter' /etc/sysctl.conf").read().split('\n')
        k = o("cat /proc/sys/net/ipv4/conf/all/rp_filter").read().split('\n')
        if ("1" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 IP Spoofing Protection has been Enabled <i>(net.ipv4.conf.all.rp_filter = 1)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")       
        elif ("1" in str(k[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 IP Spoofing Protection has been Enabled <i>(net.ipv4.conf.all.rp_filter = 1)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")       

        c = o("grep 'net.ipv4.ip_forward' /etc/sysctl.conf").read().split('\n')
        k = o("cat /proc/sys/net/ipv4/ip_forward").read().split('\n')
        if ("0" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 Forwarding has been Disabled <i>(net.ipv4.ip_forward = 0)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("0" in str(k[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 Forwarding has been Disabled <i>(net.ipv4.ip_forward = 0)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'net.ipv4.icmp_echo_ignore_broadcasts' /etc/sysctl.conf").read().split('\n')
        k = o("cat /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts").read().split('\n')
        if ("1" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 Ignore Broadcast ICMP ECHO Packets has been Enabled <i>(net.ipv4.icmp_echo_ignore_broadcasts = 1)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")     
        elif ("1" in str(k[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>IPv4 Ignore Broadcast ICMP ECHO Packets has been Enabled <i>(net.ipv4.icmp_echo_ignore_broadcasts = 1)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'kernel.randomize_va_space' /etc/sysctl.conf").read().split('\n')
        k = o("cat /proc/sys/kernel/randomize_va_space").read().split('\n')
        if ("2" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Address Space Layout Randomization (ASLR) is Enabled <i>( = )</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        elif ("2" in str(k[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Address Space Layout Randomization (ASLR) is Enabled <i>( = )</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

def malware():

        c = o("grep '128.149.135.153' /etc/hosts").read().split('\n')
        if ("128.149.135.153" in str(c[0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Removed Malicous Google Configuration in Hosts File&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("netstat -tulpn | grep '1337'").read().split('\n')
        if ("1337" in str(c[0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Removed Netcat Backdoor&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        c = o("find /var/www/html -iname '404.html'").read().split('\n')
        if ("404" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Malicous PHP P0wny webshell is Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

def operating_system_updates():
        c = o("grep 'deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main multiverse restricted universe' /etc/apt/sources.list").read().split('\n')
        if ("deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main multiverse restricted universe" in str([0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Enabled Recommended Updates&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'deb http://security.ubuntu.com/ubuntu/ bionic-security main multiverse restricted universe' /etc/apt/sources.list").read().split('\n')
        if ("deb http://security.ubuntu.com/ubuntu/ bionic-security main multiverse restricted universe" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Enabled Important Security Updates&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
def prohibited_files():
        #TODO: change user in path below
        c = o("find /home/steve/Pictures/ -iname '.meme.png'").read().split('\n')
        if ("meme" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Removed Prohibited png File&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
def service_auditing():
#SSHd
        c = o("grep 'Port' /etc/ssh/sshd_config").read().split('\n')
        if ("2200" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>SSHd Listens on Port 2200 <i>(/etc/ssh/sshd_config)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        
        c = o("grep 'PermitEmptyPasswords' /etc/ssh/sshd_config").read().split('\n')
        if ("no" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>SSH Does Not Permit Empty Passwords <i>(/etc/ssh/sshd_config)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        
        c = o("grep 'Protocol' /etc/ssh/sshd_config").read().split('\n')
        if ("2" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>SSHd uses Protocol 2 <i>(/etc/ssh/sshd_config)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'StrictModes' /etc/ssh/sshd_config").read().split('\n')
        if ("yes" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>SSHd StrictModes is Enabled <i>(/etc/ssh/sshd_config)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'PermitRootLogin' /etc/ssh/sshd_config").read().split('\n')
        if ("no" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>SSH Root Login has been Disabled <i>(/etc/ssh/sshd_config)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        
        c = o("grep 'PrintLastLog' /etc/ssh/sshd_config").read().split('\n')
        if ("yes" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>SSH Prints Last Logged User Login <i>(/etc/ssh/sshd_config)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

#Apache2
        c = o("grep 'ServerSignature' /etc/apache2/apache2.conf").read().split('\n')
        if ("Off" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Apache2 Web Server Signature is Disabled <i>(/etc/apache2/apache2.conf)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("grep 'ServerTokens' /etc/apache2/apache2.conf").read().split('\n')
        if ("Prod" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Apache2 Suppress a Server Token in HTTP Response Headers to a Bare Minimal<i>(/etc/apache2/apache2.conf)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        k = o("grep '<Directory /var/www/html>' /etc/apache2/apache2.conf").read().split('\n')
        c = o("grep 'Options -Indexes' /etc/apache2/apache2.conf").read().split('\n')
        if ("-Indexes" in str(c[0]) and "Directory /var/www/html" in str(k[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Apache2 Directory Listing Disabled <i>(/etc/apache2/apache2.conf)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep 'libapache2-mod-security'").read().split('\n')
        if ("libapache2-mod-security" in str(c[0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Apache2 Web Server Signature is Disabled <i>(/etc/apache2/apache2.conf)</i>&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

def uncategorized_operating_system_settings():
        c = o("grep 'root' /etc/cron.allow").read().split('\n')
        if ("root" in str([0])):
                points += 2
                vulns += 1
                report_append.write("<h3>Only Root is Allowed Access to Cron&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

def unwanted_software():
        c = o("dpkg -l | grep 'telnetd'").read().split('\n')
        if ("telnetd" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Telnetd Service has been Disabled or Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep 'vsftpd'").read().split('\n')
        if ("vsftpd" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>VSFTPd Service has been Disabled or Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep 'minetest-server'").read().split('\n')
        if ("minetest-server" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Minetest-Server Service has been Disabled or Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep 'nmap'").read().split('\n')
        if ("nmap" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Prohibited Software Nmap Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep 'john'").read().split('\n')
        if ("john" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Prohibited Software John Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        c = o("dpkg -l | grep 'hydra'").read().split('\n')
        if ("hydra" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Prohibited Software Hydra Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

        c = o("dpkg -l | grep 'doomsday'").read().split('\n')
        if ("doomsday" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Prohibited Software Doomsday Removed&nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
def user_auditing():
        c = o("grep 'johntheenderman' /etc/passwd").read().split('\n')
        if ("johntheenderman" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Removed &nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")
        c = o("grep 'sudo' /etc/group").read().split('\n')
        if ("johntheenderman" in str([0])):
                return
        else:
                points += 2
                vulns += 1
                report_append.write("<h3>Removed &nbsp;&nbsp;&nbsp;[2 Points]</h3>\n")

account_policy()
defensive_countermeasure()
forensic_question()
local_policy()
malware()
operating_system_updates()
prohibited_files()
service_auditing()
uncategorized_operating_system_settings()
unwanted_software()
user_auditing()

report_append.write("</p>")
report_append.write("<p align='center' style='text-align: center;'><i>This is a part of the CSUN Layer 8 Computer Security Club Cyberpatriot Trainings</i></p>")
report_append.write("</div>")
report_append.write("</div>")
report_append.write("</div>")
report_append.write("<p style='text-align:right; bottom: auto; color:black;'>&copy;Diego Cruz</p>")
report_append.write("</body>")
javascript = ["<script>\n", "var bin = document.querySelectorAll('.binary');\n", "[].forEach.call(bin, function(el) {\n", "	el.dataset.binary = Array(4096).join(el.dataset.binary + ' ')\n","});\n\n", "var dt = new Date();\n\n", "document.getElementById('datetime').innerHTML = (('0'+dt.getHours()).slice(-2)) +':'+ (('0'+dt.getMinutes()).slice(-2)) + ':'+ (('0'+dt.getSeconds()).slice(-2)) + ' '+ ((dt.getFullYear()) +'-'+ (('0'+(dt.getMonth()+1)).slice(-2)) +'-'+ ('0'+dt.getDate()).slice(-2)) + ' UTC';\n", "</script>\n"]
report_append.writelines(javascript)
report_append.close()
#TODO: CHANGE USER IN FILE PATH BELOW
os.system("sed -i 's/class=sed>v</class=sed>{}</g' /home/it_support/Desktop/ScoringReport.html".format(vulns))
os.system("sed -i 's/class=sed>p</class=sed>{}</g' /home/it_support/Desktop/ScoringReport.html".format(points))

#print(int(str(c[1])[14:]) + 1111)