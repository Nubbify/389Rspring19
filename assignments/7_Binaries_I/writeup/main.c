/*
 * Name: Oscar Bautista
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Oscar Bautista
 */

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
