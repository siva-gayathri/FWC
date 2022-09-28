#include <avr/io.h>
#include <util/delay.h>
int main (void)
{
DDRD=DDRD|(1<<6);
unsigned char a,p,q,r,s,h;
  while (1) {
a=PIND;
p=0b00000100;
q=0b00001000;
r=0b00010000;
s=0b00100000;
p=p&a;
q=q&a;
r=r&a;
s=s&a;
p=p>>2;
q=q>>3;
r=r>>4;
s=s>>5;
h= (~p&s)|(~q&~s)|(p&q&r)|(p&~q&~r);
h=h<<6;
PORTD=h;
  }
  return 0;

}
