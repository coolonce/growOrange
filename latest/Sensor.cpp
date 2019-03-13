#include "Sensor.h"


Sensor::Sensor(int type) {
	sensorType = type;
}

void Sensor::initialize() {
	pinMode(sensorType, HIGH);
}

void Sensor::activate() {
  digitalWrite(sensorType, HIGH);
}

void Sensor::deactivate() {
  digitalWrite(sensorType, LOW);
}

int Sensor::getData() {
	return analogRead(sensorType);
}
