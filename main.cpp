#include <Arduino.h>
#include <driver/adc.h>

#define width_bith ADC_WIDTH_BIT_9 //9,10,11,12
#define LED 2
hw_timer_t *My_timer = NULL;
volatile bool FLAG = true;

int values[1000];
int valores[1000];
void IRAM_ATTR onTimer() {
  FLAG = false;
  digitalWrite(LED, !digitalRead(LED));
}

void wait_for_interrupt(){
  while(true){
    delay(1);
    if(FLAG==false){
      FLAG = true;
      break;
    }
  }
} 

int16_t getValue(){

    int value = analogRead(4);
    return value;
}

void setup() {
  Serial.begin(115200);
  adc1_config_width(ADC_WIDTH_12Bit);
  adc1_config_channel_atten(ADC1_CHANNEL_0, ADC_ATTEN_0db);


  pinMode(LED, OUTPUT);
  My_timer = timerBegin(0, 80, true);
  timerAttachInterrupt(My_timer, &onTimer, true);
  timerAlarmWrite(My_timer, 10000000, true);
  timerAlarmEnable(My_timer);  //Just Enable

}

void loop() {
 int adc1_get_voltage(adc1_channel_t channel);
while(1) {
  wait_for_interrupt();  
  for(int i = 0; i<1000; i++){
    valores[i] = getValue();
  }

  for(int i = 0; i<1000; i++){
    Serial.printf("%d,", valores[i]);
  }
    Serial.printf("\n\n\n");

  }
 }