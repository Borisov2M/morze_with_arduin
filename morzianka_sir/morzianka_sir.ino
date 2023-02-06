#define LED 13

// Using http://slides.justen.eng.br/python-e-arduino as refference

void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    while (!Serial.available()) {

    }
      
    while (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == '.') {
            digitalWrite(LED, HIGH);
            delay(250);
            digitalWrite(LED, LOW);
            delay(500);
        }
        else if (serialListener == '-') {
            digitalWrite(LED, HIGH);
            delay(750);
            digitalWrite(LED, LOW);
            delay(500);            
        }
        else if (serialListener == ' '){
            digitalWrite(LED, LOW);
            delay(1000);
        }                
        else{
          digitalWrite(LED, LOW);
        }     
    }
}
