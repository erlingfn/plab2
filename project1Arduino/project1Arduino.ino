//pin vars
int btnPin = 7; //pin to read btnState
int dashPin = 8; //pin to light on dash
int dotPin = 9; //pin to light on dot

//vars to check if button state changes
int btnVal = 0; 
int lastBtnVal = 0;

//timer vars
unsigned long startMillis;
unsigned long currentMillis;
int timeDiff;

//signal vars
const unsigned long period = 500; //period agreed upon by sender and recievers
int pause = 0;
int signalToSend = 0;

void setup() {
    pinMode(btnPin, INPUT);
    pinMode(dashPin, OUTPUT);
    pinMode(dotPin, OUTPUT);
    Serial.begin(9600);
    //start timer
    startMillis = millis();
}

//Return 0 for short signal, 1 for medium and 2 for long
int calcPause(int mlsec) {
    if(mlsec <= period) {
        return 0;
    } else if(mlsec <= 3 * period)  {
        return 1;
    } else {
        return 2;
    }
}

int calcSignal(int lastVal, int pause) {
    //short pause
    if(lastVal == 0 && pause == 0) {
        return 4;
    //medium pause
    } else if(lastVal == 0 && pause == 1){
        return 2;
    //long pause
    } else if(lastVal == 0 && pause == 2){
        return 3;
    //short push(dot)
    } else if(lastVal == 1 && pause == 0){
        digitalWrite(dotPin, HIGH);
        return 0;
    //medium push(dash)
    } else if(lastVal == 1 && (pause == 1 || pause == 2 )){
        digitalWrite(dashPin, HIGH);
        return 1;
    }
}

//check for btn debounce
boolean debounceCheck(int mlsec) {
    if(mlsec < 50) {
        return true;
    }
    return false;
}

void loop() {
    btnVal = digitalRead(btnPin);
    if(btnVal == lastBtnVal){
        currentMillis = millis();
        timeDiff = currentMillis - startMillis;
        if(timeDiff > 7000){
            //reset LEDs
            digitalWrite(dashPin, LOW);
            digitalWrite(dotPin, LOW);
        }
        return;
    } else {
        currentMillis = millis();
        //Serial.println(btnVal);
        //Serial.println(startMillis);
        timeDiff = currentMillis - startMillis;
        if(debounceCheck(timeDiff)) {
            return;
        }
        //reset LEDs
        digitalWrite(dashPin, LOW);
        digitalWrite(dotPin, LOW);
        //find long short or medium pause
        pause =  calcPause(timeDiff);
        //calculate signal
        signalToSend = calcSignal(lastBtnVal, pause);
        //reset timer
        startMillis = millis();
        lastBtnVal = btnVal;
        //do not send signal on short pause
        if(signalToSend != 4){
            Serial.println(signalToSend);
        }
    }
}
