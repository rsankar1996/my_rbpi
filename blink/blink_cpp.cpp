#include <unistd.h>
#include <wiringPi.h>
#include <cstdio>
#include <iostream>

#define LED 15

int main() {
  wiringPiSetup();
  pinMode(LED, OUTPUT);
  while(1) {
    std::cout << "Blink LED" << std::endl;
    digitalWrite(LED, HIGH);
    sleep(1);
    digitalWrite(LED, LOW);
    sleep(1);
  }
}
