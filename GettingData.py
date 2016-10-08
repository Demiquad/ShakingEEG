import sys
import time
#import matplotlib.pyplot as plt

start = time.time()

f = open("chb02_01.edf", "rb")
data = f.read()
f.close()

print('######## General Information #########################')
sys.stdout.flush()
a = 0
b = a + 8
version = data[a:b].decode('ascii')
a = b
b = a + 80
patientId = data[a:b].decode('ascii')
a = b
b = a + 80
recordingId = data[a:b].decode('ascii')
a = b
b = a + 8
startDate = data[a:b].decode('ascii')
a = b
b = a + 8
startTime = data[a:b].decode('ascii')
a = b
b = a + 8
numHeader = int(data[a:b])
a = b
b = a + 44
a = b
b = a + 8
nDataRecords = int(data[a:b])
a = b
b = a + 8
durationDataRecords = float(data[a:b])
a = b
b = a + 4
nSignals = int(data[a:b])

label = []
transducer = []
dimension = []
physMinimum = []
physMaximum = []
digitalMinimum = []
digitalMaximum = []
prefiltering = []
nSamples = []


for i in range(nSignals):
  a = b
  b = a + 16
  label.append(data[a:b].decode('ascii'))
for i in range(nSignals):
  a = b
  b = a + 80
  transducer.append(data[a:b].decode('ascii'))
for i in range(nSignals):
  a = b
  b = a + 8
  dimension.append(data[a:b].decode('ascii'))
for i in range(nSignals):
  a = b
  b = a + 8
  physMinimum.append(int(data[a:b]))
for i in range(nSignals):
  a = b
  b = a + 8
  physMaximum.append(int(data[a:b]))
for i in range(nSignals):
  a = b
  b = a + 8
  digitalMinimum.append(int(data[a:b]))
for i in range(nSignals):
  a = b
  b = a + 8
  digitalMaximum.append(int(data[a:b]))
for i in range(nSignals):
  a = b
  b = a + 80
  prefiltering.append(data[a:b].decode('ascii'))
for i in range(nSignals):
  a = b
  b = a + 8
  nSamples.append(int(data[a:b]))
for i in range(nSignals):
  a = b
  b = a + 32

print('There are', nSignals, 'signals recorded.')
print('There are', nDataRecords, "numbers of Data Records")
controlVariable = 1
for i in range(len(nSamples)):
  if nSamples[0] != nSamples[i]:
    controlVariable = 0
if controlVariable == 1:
  print('Each Data Record\'s number of samples is', nSamples[0])
else:
    print('Each Data Record\'s number of samples is', nSamples)
print('Each Data Record\'s duration is', durationDataRecords, 'seconds')
print('####################################################')
sys.stdout.flush()
    
dataSignals = [[] for x in range(nSignals)]
dataRecords = [[[] for x in range(nSignals)] for y in range(nDataRecords)]

print("\r0 records read", end="")
print("   |   0 seconds elapsed", end="")
sys.stdout.flush()
for i in range(nDataRecords):
  for j in range(nSignals):
    for k in range(nSamples[j]):
      a = b
      b = a + 2
      x = int.from_bytes(data[a:b], byteorder='little', signed=True)
      dataRecords[i][j].append(x)
      dataSignals[j].append(x)
  print("\r{} records read".format(i+1), end="")
  print("   |   {} seconds elapsed".format(int(time.time()-start)), end="")
  sys.stdout.flush()

#                 nDataRecords ------> i
#  nSignals     [ nSamples k ]
#  |
#  |
#  v
#  j
