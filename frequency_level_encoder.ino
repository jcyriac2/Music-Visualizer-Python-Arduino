const int CLK = 10;
const int DATA = 12;
const int RESET = 13;
char serial_data;
byte b = B0;
int i;

void setup() {
  
  pinMode(CLK, OUTPUT);
  pinMode(DATA, OUTPUT);
  pinMode(RESET, OUTPUT);
  
  digitalWrite(RESET, LOW);
  delay(100);
  digitalWrite(RESET, HIGH);
  
  Serial.begin(9600);
  Serial.write("Serial Connection Ready");
}

void loop() {

    if(Serial.available()){
      serial_data = Serial.read();
      b=B0;
      for(i=0;i<serial_data;i++){
        b=b<<1;
        b=b|(B1);
      } 
      shiftOut(DATA, CLK, LSBFIRST, b);
    }
}

