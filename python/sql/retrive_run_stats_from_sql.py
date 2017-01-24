# This file contains function implementing cherrypy html server, which
# retrieves data from SQL and renders it in html table format per user requirements
import random, string, cherrypy, HTML, os, sys, psycopg2

class RUN_STATS_DB:
  statHash = {}
  runsHash = {}

  # Create a small hash with runs information
  def retrieveRunsFromSql(self, runIds):
    # Open sql connection
    conn = psycopg2.connect(host="n8sa09",database="run_stats", user="icd")
    cur = conn.cursor()
    
    # Determine the list of columns in runs table. Each one contains a metrics for a run for ex run)id or run_title
    sqlCmd = "SELECT column_name from information_schema.columns WHERE table_name='runs';"
    cur.execute(sqlCmd)
    runParms = []
    for run_parm in cur.fetchall():
      runParms.append(run_parm)
    # Close sql connection
    cur.close()

  # Fill dictionary statHash with data retrieved from sql. Function is cumulative
  # and returns a list of encountered steps
  def retrieveRunStatsFromSql(self, runIds, selectedParms=[]): 
    # Form  list of steps in the same order as they encounter in the sql table
    Steps = []

    # Open sql connection
    conn = psycopg2.connect(host="n8sa09",database="run_stats", user="icd")
    cur = conn.cursor()

    # Extract statistics for every run
    for run_id in runIds:
      # Form sql query
      sqlCmd = "SELECT r.run_id, s.step, s.name, s.value, s.unit  FROM runs AS r JOIN run_stats AS s ON r.run_id = s.run_id where r.run_id=" + str(run_id)
      isFirstParm = True
      if (len(selectedParms) > 0):
        sqlCmd += " and ("
        for parm_name in selectedParms:
          if (isFirstParm):
            sqlCmd += "s.name='"+parm_name+"'"
            isFirstParm = False
          else:
            sqlCmd += "OR s.name='"+parm_name+"'"
        sqlCmd += ")"
          
      cur.execute(sqlCmd)
      for (run_id, step, parm_name, parm_value, parm_unit) in cur.fetchall():
        self.statHash[(run_id,step,parm_name)] = (parm_value, parm_unit)
        if not step in Steps:
          Steps.append(step)

    # Close sql connection
    cur.close()

    # Return list of Steps
    return(Steps)

  # Display accumulated results as html table
  def getRunStatsAsHtmlTable(self, runIds, selectedSteps, selectedParms):
    tableData = {}
    #print "runIds:", runIds 
    #header = ["runs"] + list(runIds)
    t = HTML.Table(header_row=["   runs =><br>steps              "] + list(runIds))
    for step in selectedSteps:
      step_name_cell = HTML.TableCell(step, bgcolor='Aqua')
      t.rows.append([step_name_cell])
      for parm_name in selectedParms:
        Row = [parm_name]
        for run_id in runIds:
          key = (run_id,step,parm_name)
          if self.statHash.has_key(key):
            (parm_value, parm_unit) = self.statHash[key] 
          else:
             (parm_value, parm_unit) = ("---","")
          
          Row.append(str(parm_value) + " " + str(parm_unit))
        t.rows.append(Row)

    htmlcode = str(t)
    return htmlcode

# End of class RUN_STATS_DB

# This class is listening to HTML client requests
class MainServer(object):

    def __init__(self):

      # This is a form which serves for filtering only relevant runs
      self.runListFilterForm = """
      <form method="post" action="genRunListTable">
          Run title: <input type="text" value="" name="run_title_pattern" />
          User name: <input type="text" value="" name="user_name_pattern" />
          <button type="submit"> Filter</button>
          </form> 
      """  

    # Main page (server_name:8080) prints runs filter form and then all the runs in reverse order (newest first)
    # one line per run
    @cherrypy.expose
    def index(self):
        return '<html>' + self.genRunListTable("","") + '</html>'
         

    # Create a table of runs (one row contains all the basic info for one run), optionally filtered with user given parameters 
    @cherrypy.expose
    def genRunListTable(self,run_title_pattern,user_name_pattern):
      db = RUN_STATS_DB()
      parmsToDisplay =['run_id','run_title','run_date','design_name','tech_name','leaf_cell_count','build_id','hostname','username',]
      t = HTML.Table(header_row=parmsToDisplay)
    
      # Open sql connection
      conn = psycopg2.connect(host="n8sa09",database="run_stats", user="icd")
      cur = conn.cursor()

      # Form sql query and retrieve all the runs which match specified criteria
      sqlCmd = "SELECT " + ",".join(parmsToDisplay) + " FROM runs"
      filterExpr = ""
      if (run_title_pattern != ""):
        if (filterExpr != ""):
          filterExpr += " AND"
        filterExpr += " run_title LIKE '%" + run_title_pattern + "%'"
      if (user_name_pattern !=""):
        if (filterExpr != ""):
          filterExpr += " AND"
        filterExpr += " username LIKE '%" + user_name_pattern + "%'"
      if (filterExpr != ""):
        sqlCmd += " WHERE "+ filterExpr  
      sqlCmd += " ORDER BY run_id DESC;"
      cur.execute(sqlCmd)

      # Append each row (i.e run) to html table, add checkbox before each run_id (first column)
      for Row in cur.fetchall():
        run_id = str(Row[0])
        newRow =list(Row)
        newRow[0] = '<input type="checkbox" name="selectedRunIds" value='+ run_id +'>' + run_id
        t.rows.append(newRow)
    
      # Close sql connection
      cur.close()

      # Generated output: 1) run filter form 2) Table of runs with checkboxes
      return self.runListFilterForm + '<form method="POST" action="genRunStatsTable">' + str(t) + '<br> <button type="submit">Display data for selected runs</button></form>'


    # Print HTML comparison table of metrics for run IDs selected by the user
    @cherrypy.expose
    def genRunStatsTable(self, selectedRunIds):
      # Form returns runIds is a string like "5 7 9" need to be converted to a list of integers
      #runIds = [int(i) for i in  runIdsStr.split()]
      runIds = sorted(map(int,selectedRunIds))

      # Create empty db for rans statistics
      db = RUN_STATS_DB()
      # Populate db and return a list of accumulated steps
      Steps = db.retrieveRunStatsFromSql(runIds)
      
      return db.getRunStatsAsHtmlTable(runIds, Steps, ('DRC_TOTAL','THS','WNS','TNS','elapsed_time'))
      

    @cherrypy.expose
    def myFunc(self,option):
      print option

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(MainServer())