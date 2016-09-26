import msvcrt
import time

finish=10
count=0

print "press enter key to get started!"

raw_input()
s_time=time.time()

while(1):
	key=msvcrt.getch()
	if key=='\xe0':
		count=count+1
		print "-->",
		if count==finish:
			break
time_elapsed=time.time()-s_time
print "congrats you have finished the game"
print "time taken is "+str(time_elapsed)
