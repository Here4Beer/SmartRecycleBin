#include <WiFi.h>

//Testing example for esp32

const char* wifi_name = "A1_A1C2CA"; // Your Wifi network name here
const char* wifi_pass = "72041880";    // Your Wifi network password here
WiFiServer server(80);    // Server will be at port 80
// defines pins numbers
const int stepPin = 26; 
const int dirPin = 25; 
int currentState  = 0; //0 - yellow, 1 - green, 2 - blue

void setup()
{
  
  Serial.begin (115200);

  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);

  Serial.print ("Connecting to ");
  Serial.print (wifi_name);
  WiFi.begin (wifi_name, wifi_pass);     // Connecting to the wifi network

  while (WiFi.status() != WL_CONNECTED) // Waiting for the response of wifi network
  {
    delay (500);
    Serial.print (".");
  }
  Serial.println("");
  Serial.println("Connection Successful");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("Type the above IP address into browser search bar");
  server.begin();
}

void loop()
{
  WiFiClient client = server.available();
  if (client)
  {
    boolean currentLineIsBlank = true;
    String buffer = "";
    while (client.connected())
    {
      if (client.available())
      {
        char c = client.read();
        buffer+=c;
        if (c == '\n' && currentLineIsBlank)
        {
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println();
          client.print("<HTML><title>ESP32</title>");
          client.print("<body><h1>ESP32 Standalone Relay Control </h1>");
          client.print("<p>Relay Control</p>");
          client.print("<a href=\"/?yellow\"\"><button>yellow</button></a>");
          client.print("<a href=\"/?green\"\"><button>green</button></a>");
          client.print("<a href=\"/?blue\"\"><button>blue</button></a>");

          client.print("</body></HTML>");
          break;        // break out of the while loop:
        }
        if (c == '\n') {
          currentLineIsBlank = true;
          buffer="";
        }
        else
          if (c == '\r') {
          if(buffer.indexOf("GET /?yellow")>=0){
            Serial.print ("yellow");
            if(currentState != 0) {
              Serial.println("In handleRequest %d");
              Serial.println(currentState);
              handleRequest(0);
            }
          }
          if(buffer.indexOf("GET /?green")>=0){
            Serial.print ("green");
            if(currentState != 1) {
              Serial.println("In handleRequest %d");
              Serial.println(currentState);
              handleRequest(1);
            }
          }
          if(buffer.indexOf("GET /?blue")>=0) {
            Serial.print ("blue");
            if(currentState != 2){
              Serial.println("In handleRequest %d");
              Serial.println(currentState);
              handleRequest(2);         
            }
          }
        }
        else {
          currentLineIsBlank = false;
        }
      }
    }
    client.stop();
  }
}

void handleRequest(int nextState){
  
  Serial.println(currentState);
  Serial.print(" state");
  Serial.println("");
  if(currentState == 0) {
    if (nextState == 1) {
      move_120_forward();
    }
    else if (nextState == 2) {
      move_120_backward();
    }
    else if (nextState == 0) {
      Serial.print ("Otvori kosha neshtastnik");

    }
  } else if (currentState == 1) {
    if (nextState == 0) {
      move_120_backward();
    }
    else if (nextState == 2) {
      move_120_forward();
    }
    else if(nextState == 1){
      Serial.print ("Otvori kosha neshtastnik");
    }
  } else if (currentState == 2) {
    if (nextState == 0) {
      move_120_forward();
    }
    else if (nextState == 1) {
      move_120_backward();    
    }
    else if (nextState == 2){
      Serial.print ("Otvori kosha neshtastnik");
    }
  }  
  delay(5200);
  //change the current state
  currentState = nextState;
  
}

void move_360_forward(){
  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(2000); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(2000); 
  }
  delay(1000); // One second delay
}

void move_360_backward() {
  digitalWrite(dirPin,LOW); //Changes the rotations direction
  // Makes 400 pulses for making two full cycle rotation
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(2000);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(2000);
  }
  delay(1000);
}

void move_120_forward(){
  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 67; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(6000); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(6000); 
  }
  delay(1000); // One second delay
}

void move_120_backward(){
  digitalWrite(dirPin,LOW); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 67; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(6000); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(6000); 
  }
  delay(1000); // One second delay
}
