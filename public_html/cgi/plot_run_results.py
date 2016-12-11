#!/usr/bin/python

# URL http://192.168.0.133/cgi-bin/plot_run_results.py 
# or  http://98.234.49.76/cgi-bin/plot_run_results.py
# save script in /home/pi/public_html/cgi/input_run_results.py and link it from /usr/lib/cgi-bin

# To dump all the database content to SQL script
# pg_dump -d mile_run -U postgres -f mile_run_dump.sql  
# to restore the database 
# psql -U postgres  -d mile_run
# then \i ~/public_html/cgi/mile_run_dump.sql
 

import os, sys

# CGI module
import cgi, cgitb

# Use this var to change functionality when running directly under unix
if 'REQUEST_METHOD' in os.environ:
    underWebServer = True
    cgitb.enable()
else:
    underWebServer = False

def dbgPrint(*args):
    global underWebServer
    if (not underWebServer):
        print "-dbg-",
        for arg in args:
            print arg,
        print ""

# Postgresql connect
import psycopg2

# Drawing
import matplotlib

# Date manipulations
from datetime import date

# set HOME environment variable to a directory the httpd server can write to
os.environ[ 'HOME' ] = '/tmp/'

# chose a non-GUI backend
if (underWebServer):
    matplotlib.use( 'Agg' )

import pylab

# Deals with inputing data into python from the html form
form = cgi.FieldStorage()


fig, ax = pylab.subplots()

# Connect to SQL
conn = psycopg2.connect(database="mile_run", user="postgres")
cur = conn.cursor()

width = 0.5
dateRange = [date(2100,1,1), date(2000,1,1)]
for runnerName in ['Jacob','Benny']:
    cmd = "SELECT * FROM results WHERE runner_name = '" + runnerName + "'"
    cur.execute(cmd)
    rows = cur.fetchall()

    Dates = []
    RunTimes = []
    for row in rows:
        [name, distance, run_date, run_time] = row[1:5]
        
        dateInDaysSince2016 = (run_date - date(1,1,1)).days
        dbgPrint(name, distance,run_date,"->",dateInDaysSince2016,run_time)
        if (runnerName == 'Jacob'):        
            Dates.append(dateInDaysSince2016)
        else:
            Dates.append(dateInDaysSince2016+0.5)

        # Update min-max date range
        dbgPrint("run_date =",run_date)

        if (run_date > dateRange[1]):
            dateRange[1] = run_date
        if (run_date < dateRange[0]):
            dateRange[0] = run_date

        RunTimes.append(run_time/60.0)

    # Construct your plot
    if (runnerName == 'Jacob'):
        rectsJacob = ax.bar(Dates, RunTimes, width,color='r')
    else:
        rectsBenny = ax.bar(Dates, RunTimes, width,color='y')

dbgPrint(dateRange)

ax.legend((rectsJacob, rectsBenny), ('Jacob', 'Dad'))
ax.set_xticks(dateRange)
ax.set_xticklabels(dateRange)
ax.set_ylabel('Run time, minutes')
ax.set_xlabel('Dates')

#ax.set_xticks([(date(dateRange[1])- date(2016,1,1)).days,340])
#ax.set_xticklabels(dateRange)

if (underWebServer):
    # Running under web server
    print "Content-Type: image/png\n"
    # save the plot as a png and output directly to webserver
    pylab.savefig( sys.stdout, format='png' )
else:
    # Standalone script
    pylab.show()

# Close SQL connection
conn.commit()
conn.close()





