# AutomateSwitchBackup-Python-Netmiko
Create an automated solution for backing up various switch configurations

The Problem:
Tasked with implementing a light weight solution for automating a handful of startup-configuration files for various (mostly legacy and weird) network devices. 
Rather than implement a full automation platform, I wanted a simple and stable solution. 

The Tech:
Python
Netmiko
TFTP server

The Solution:
This script utilizes Python x Netmiko to interact and login to various network devices.
Once it establishes a connection, it executes the commmands needed to copy the startup-configuration files to a designated TFTP server.
I use a cron job to run on a schedule.

Issues:
Some devices are a little hairy and require timeouts and tinkering. 
All switch models included in the script work within our enviorment, but no promises that they will out of the box work in yours. 
