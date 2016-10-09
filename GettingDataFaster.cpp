#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    char version[8];
    char patientID[80];
    char localRecordingIdentification[80];
    char startdateOfRecording[8];
    
    ifstream data;
    data.open("chb02_01.edf", ios::binary);
    
    if (data.is_open())
    {
      data.read(version, 8);
      cout << version << endl;
      data.read(patientID, 80);
      cout << patientID << endl;
      data.read(localRecordingIdentification, 80);
      cout << localRecordingIdentification << endl;
      data.read(startdateOfRecording, 8);
      cout << startdateOfRecording << endl;
         
      data.close(); 
    }
    else  cout << "The files has not been opened";
    return 0;
}
