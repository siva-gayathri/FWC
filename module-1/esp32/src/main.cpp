

//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

//    Can be client or even host   //
#ifndef STASSID
#define STASSID "vivo1920"  // Replace with your network credentials
#define STAPSK  "g@y@thr!"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

#define P_pin 2
#define Q_pin 3
#define R_pin 4
#define S_pin 5
#define H_pin 6

#define CLK_pin 13
#define CLK_TP 4000
int P,Q,R,S,H;
void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}

//-------------------------------------------------------//

void setup(){
  OTAsetup();

  //-------------------//
  // Custom setup code //
  //-------------------//
	pinMode(H_pin, OUTPUT);
	pinMode(P_pin, INPUT);
	pinMode(Q_pin, INPUT);
	pinMode(R_pin, INPUT);
	pinMode(S_pin, INPUT);


}

void loop() {
  OTAloop();
  delay(10);
  P = digitalRead(P_pin);
  Q = digitalRead(Q_pin);
  R = digitalRead(R_pin);
  S = digitalRead(S_pin);
  H = !(Q&&S) || (!P&&S) || (P&&Q&&R) || (P&& !Q && !R && S);
	  digitalWrite(H_pin,H);
  digitalWrite(CLK_pin,0);
  delay(CLK_TP/2);
  digitalWrite(CLK_pin,1);
  delay(CLK_TP/2);

  // If no custom loop code ensure to have a delay in loop
  //-------------------//
  // Custom loop code  //
  //-------------------//
  	
}


