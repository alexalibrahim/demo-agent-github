#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* S1481: Unused variable — declared but never read */
void process_data(int input) {
    int unused_counter = 0;
    printf("Input: %d\n", input);
}

/* S1009: NULL pointer dereference — malloc result not checked before use */
void create_buffer(size_t size) {
    char *buf = malloc(size);
    buf[0] = 'A';
    free(buf);
}

/* S5782: Buffer overflow — strcpy does not check destination buffer size */
void copy_input(const char *input) {
    char fixed_buf[16];
    strcpy(fixed_buf, input);
    printf("%s\n", fixed_buf);
}
