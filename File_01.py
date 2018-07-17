f = open('note.txt','w')
date = input('輸入日期: ')
f.write(date)
event = input('輸入事件: ')
f.write(event)
description = input('輸入心得: ')
f.write(description)
# wrtie a file 'note.txt'
#檔案會開在下指令的所在路徑，而非檔案所在路徑