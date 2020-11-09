

import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# Example
addToClipBoard('your text here')

'''
in order to run the script you can create a bat file:
"c:\Program Files Secondary\python\python.exe" "c:\workspace\python\copy_user_clipboard.py"

if you want a taskbar shortcut, create a command prompt shorcut on the taskbar first (shift right click on command prompt)
then edit the shorcut (shift right click/properties) and add to targets:
%windir%\system32\cmd.exe /c "c:\workspace\python\copy_user.bat"
'''

