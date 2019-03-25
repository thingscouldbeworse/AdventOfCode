import time
import datetime

time_map = []
guard_time = {}

with open('input.txt', 'r') as inputfile:
  for line in inputfile:
    otime = line.split("]")[0][1:]
    otime = datetime.datetime.strptime(otime, "%Y-%m-%d %H:%M")
    content = line.split("] ")[1][:-1]
    time_map.append([otime, content])

time_map = sorted(time_map, key=lambda tup: tup[0])
    
for i in range(0,len(time_map)):
  if '#' in time_map[i][1]:
    guard = time_map[i][1].split("#")[1].split(" ")[0]
    fall_asleep = time_map[i+1][0]
    wake_up = time_map[i+2][0]
    difference = wake_up - fall_asleep
    
    if guard not in guard_time:
      guard_time[guard] = difference
    else:
      guard_time[guard] += difference
  
print(guard_time)
max_time = datetime.timedelta(seconds=0)
max_guard = ""
for guard in guard_time:
  if guard_time[guard] > max_time:
    max_time = guard_time[guard]
    max_guard = guard
  
print(max_guard)
print(max_time) 
  

