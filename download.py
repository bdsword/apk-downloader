#!/usr/bin/env python2

from googleplay_api import list
from googleplay_api import categories
from googleplay_api import download
import sqlite3
import time
import sys
import random
import os

if os.path.exists('report.sqlite3'):
    os.remove('report.sqlite3')
 
conn = sqlite3.connect('report.sqlite3')
c = conn.cursor()

c.execute('''CREATE TABLE apps 
             (app_id text, version text, app_size text, rating text, num_download text)''')

categories = categories.get_categories()
for category in categories:
    if not os.path.exists('download/' + category):
        os.makedirs('download/' + category)
    apps = list.list(category, 'apps_topselling_free')
    for app in apps:
        c.execute("INSERT INTO apps VALUES (?,?,?,?,?)", (app[0], app[1], app[2], app[3], app[4]))
        conn.commit()

        download.download(app[0], 'download/' + category + '/' + app[0] + '.apk')
        time.sleep(random.randint(20, 30)) # prevent banned by google
print("Download all complete!")
conn.close()
