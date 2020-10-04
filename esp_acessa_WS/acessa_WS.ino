/**
   BasicHTTPClient.ino

    Created on: 24.05.2015

*/

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include <ESP8266HTTPClient.h>

#include <WiFiClient.h>

ESP8266WiFiMulti WiFiMulti;

const char* ssid ="Nome_da_rede_wifi";
const char* password ="Senha_da_rede_wifi";

void setup() {

  Serial.begin(115200);
  // Serial.setDebugOutput(true);

  Serial.println();
  Serial.println();
  Serial.println();

//  for (uint8_t t = 4; t > 0; t--) {
//    Serial.printf("[SETUP] WAIT %d...\n", t);
//    Serial.flush();
//    delay(1000);
//  }

  WiFi.mode(WIFI_STA);
//  WiFiMulti.addAP(ssid, password);
  WiFi.begin(ssid, password);
  Serial.println("");
  
// Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  pinMode (2, OUTPUT);
  

}

void loop() {

  String payload;
  
  // wait for WiFi connection]
  if ((WiFiMulti.run() == WL_CONNECTED)) {

    WiFiClient client;

    HTTPClient http;

//    Serial.print("[HTTP] begin...\n");
//    if (http.begin(client, "http://jigsaw.w3.org/HTTP/connection.html")) {  // HTTP

    Serial.print("[HTTP] begin...\n");
    if (http.begin(client, "http://35.211.13.184/check?consumer_unit=Barra")) {  // HTTP


      Serial.print("[HTTP] GET...\n");
      // start connection and send HTTP header
      int httpCode = http.GET();

      // httpCode will be negative on error
      if (httpCode > 0) {
        // HTTP header has been send and Server response header has been handled
        Serial.printf("[HTTP] GET... code: %d\n", httpCode);

        // file found at server
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          payload = http.getString();
          Serial.println(payload);
        }
      } else {
        Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }

      http.end();
    } else {
      Serial.printf("[HTTP} Unable to connect\n");
    }
  }

   switch (payload[13])
{
   case 't':
     digitalWrite(2, LOW);
   break;

   case 'f':
     digitalWrite(2, HIGH);
   break;

   default:
     digitalWrite(2, LOW);
}
  
  delay(20000);
}
