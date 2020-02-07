#! /bin/python

import subprocess
def run_sqlplus(sqlplus_script):

    """
    Run a sql command or group of commands against
    a database using sqlplus.
    """

    p = subprocess.Popen(['sqlplus64','/nolog'],stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,stderr) = p.communicate(sqlplus_script.encode('utf-8'))
    stdout_lines = stdout.decode('utf-8').split("\n")

    return stdout_lines

sqlplus_script="""
connect user/password#@hostname:1584/sid
select * from dual;
exit
"""

sqlplus_output = run_sqlplus(sqlplus_script)

for line in sqlplus_output:
    print(line)