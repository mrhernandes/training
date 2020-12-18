#!/usr/bin/env python3.6
# Script pra criar host no zabbix

from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://104.131.169.47/zabbix")
zapi.login("Admin", "123456")

import csv

f = csv.reader(open('/opt/hostsclientepatati.csv'), delimiter=',')
for [nomedohost,hostip,zgroup,ztemplate] in f:
        zapi.host.create({
                "host": nomedohost,
                "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": hostip,
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "37"
            }
        ],
        "tags": [
            {
                "tag": "Host name",
                "value": "Linux server"
            }
        ],
        "templates": [
            {
                "templateid": "10186"
            }
        ],
        "macros": [
            {
                "macro": "{$USER_ID}",
                "value": "123321"
            },
            {
                "macro": "{$USER_LOCATION}",
                "value": "0:0:0",
                "description": "latitude, longitude and altitude coordinates"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
     })
        print ("Host ",nomedohost," criado com sucesso!")