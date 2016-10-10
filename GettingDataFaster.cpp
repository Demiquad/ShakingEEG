#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    char version[8];
    char patientID[80];
    char localRecordingIdentification[80];
    char startdateOfRecording[8];
    char startTimeOfRecording[8];
    char nBytesInHeader[8];
    char cnDataRecords[8];
    int nDataRecords = *((int*)cnDataRecords);
    char durationDataRecords[8];
    char cnSignals[4];
    int nSignals = *((int*)cnSignals);
      
    ifstream data;
    data.open("chb02_01.edf", ios::binary);
    
    if (data.is_open())
    {
      data.read(version, 8);
      //cout << version << endl;
      data.read(patientID, 80);
      //cout << patientID << endl;
      data.read(localRecordingIdentification, 80);
      cout << "Local Recording Identification is: " << localRecordingIdentification << endl;
      data.read(startdateOfRecording, 8);
      //cout << startdateOfRecording << endl;
      data.read(startTimeOfRecording, 8);
      //cout << startTimeOfRecording << endl;
      data.read(nBytesInHeader, 8);
      //cout << nBytesInHeader << endl;
      data.seekg(44, ios::cur);
      data.read(cnDataRecords, 8);
      cout << "The number of Data Records per Signal is: " << cnDataRecords << endl;
      data.read(durationDataRecords, 8);
      cout << "Each Data Record's duration is: " << durationDataRecords << endl;
      data.read(cnSignals, 4);
      cout << "The number of Signals is: " << cnSignals << endl;
      
      data.close(); 
    }
    else  cout << "The file has not been opened";
    return 0;
}
