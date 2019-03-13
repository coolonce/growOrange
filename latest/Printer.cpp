#include "Printer.h"

void Printer::addSensorData(int sensorId, float sensorData) {
  
	if (msg == "") {
		msg += "{\"sensors\": [";
		msg += "{\"id\":" + String(sensorId) + ", \"data\":" + String(sensorData, 2) + "}";
	}
	else {
		msg += ",";
		msg += "{\"id\":" + String(sensorId) + ", \"data\":" + String(sensorData, 2) + "}";
	}	
}

void Printer::addSensorId(int id) {
	msg += " ], \"device_id\":" + String(id) + "}\0";
}

String Printer::printToSerial() {
	String result = msg;
	msg = "";
	return result;
}
