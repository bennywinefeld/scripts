#!/usr/bin/env python
import cgi
import cgitb
import psycopg2
cgitb.enable()


print "Content-type: text/html\n\n"

form = cgi.FieldStorage()

# Postgresql connect
import psycopg2

runner = str(form.getvalue('runner'))
distance = str(1)
[month,day,year] = str(form.getvalue("date")).split("/")
date = year + "-" + month + "-" + day
[minutes, seconds] = str(form.getvalue("time")).split(":")
time = str(int(minutes)*60+int(seconds))
cmd = "insert into results(runner_name,distance,date,run_time) values ('" + runner + "','" + distance + "','" + date + "','" + time + "')"

debug = False
if (debug):
    print "<body><table>"
    print "<tr> runner= ", runner, "</tr>"
    print "<tr> date= ",date, "</tr>"
    print "<tr> raw time= ", str(form.getvalue("time")) , "</tr>" 
    print "<tr> time= ",time, "</tr>"
    print "</table>"
    print "<tr>",cmd,"</tr>"
    print "</body>"
else:
    # Go back to main page right after execution of the cgi
    print "<head><meta http-equiv=\"refresh\" content=\"0; url=../run_results.html\" /></head>"
    # Connect to SQL
    conn = psycopg2.connect(database="mile_run", user="postgres")
    cur = conn.cursor()
    cur.execute(cmd);
    conn.commit()
    conn.close()



'''print "<table>"
for field in form.keys():
    print "<tr>"
    print "<td>",field,"</td>"
    print "<td>",form.getvalue(field),"</td>"
    print "</tr>"
print "</table>"'''