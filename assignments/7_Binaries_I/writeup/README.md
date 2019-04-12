# Writeup 7 - Binaries I

Name: Oscar Bautista

Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Oscar Bautista

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>
#include <stdint.h>

int main() {
  uint32_t a = 0x1ceb00da;
  uint32_t b = 0xfeedface;

  printf("a = %d\n", a);
  printf("b = %d\n", b);

  b = a ^ b;
  a = b ^ a;
  b = a ^ b;

  printf("a = %d\n", a);
  printf("b = %d\n", b);

  return 0;
}
```

### Part 2 (10 Pts)

The program defines two 4 byte variables and then uses three bitwise xors in order to swap the values of the two variables. It shows this by printing the values before and after the bitwise xors.
