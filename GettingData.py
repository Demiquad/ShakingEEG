import matplotlib.pyplot as plt

f = open("chb02_01.edf", "r", errors="ignore")
data = f.read()
f.close()

print('######## General Information #########################')
a = 0
b = a + 8
version = data[a:b]
a = b
b = a + 80
patientId = data[a:b]
a = b
b = a + 80
recordingId = data[a:b]
a = b
b = a + 8
startDate = data[a:b]
a = b
b = a + 8
startTime = data[a:b]
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
  label.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 80
  transducer.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 8
  dimension.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 8
  physMinimum.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 8
  physMaximum.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 8
  digitalMinimum.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 8
  digitalMaximum.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 80
  prefiltering.append(data[a:b])
for i in range(nSignals):
  a = b
  b = a + 8
  nSamples.append(int(data[a:b]))
for i in range(nSignals+1):
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
print('Each signal has', nDataRecords/nSignals,'Data Records')
print('####################################################')
    
dataSignals = []
dataRecords = []
'''
for i in range(nDataRecords):
  for j in range(nSignals):
    for k in range(nSamples[j])
      dataRecords.append(data[k])
'''

#                 nDataRecords ------> i
#  nSignals     [ nSamples k ]
#  |
#  |
#  v
#  j
