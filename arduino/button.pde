/*
License:
    This file is part of Futurice Taxi Button package.

    Futurice Taxi Button is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License version 3 as published by
    the Free Software Foundation.

    Futurice Taxi Button is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Futurice Taxi Button.  If not, see <http://www.gnu.org/licenses/>.

Readme:
    Upload this to your Arduino, assuming you connected button to analog 0. Otherwise,
    remember to change sensorPin variable below.
    For connecting button to Arduino, check out
    http://www.arduino.cc/en/Tutorial/Button

    Please note that in Arduino tutorial, button is connected to digital 2.
*/

int sensorPin = A0;
int sensorValue = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // read the value from the button:
  sensorValue = analogRead(sensorPin);    
  if (sensorValue > 500) {
    Serial.println("."); 
  }
  delay(50);
}
