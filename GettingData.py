import matplotlib.pyplot as plt

f = open("chb02_01.edf", "r")
data = f.read()
f.close()

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
nDataRecords = int(data[a:b]) # indicates how many records per signal
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
dataSignals = []
dataRecords = []

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
for i in range(nSignals):
  a = b
  b = a + 32

for i in range(nSignals):
  for j in range(nSamples[i]*nDataRecords):
    dataRecords.append(data[a])
    a = b
    b = a + 2
  dataSignals.append(ord(dataRecords[i]))
