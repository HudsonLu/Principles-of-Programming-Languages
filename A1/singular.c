#include <stddef.h>
#include "singular.h"
#include <stdio.h>

void print(double a[], size_t size) {
    for (size_t i = 0; i < size; i++) {
        printf("%g ", a[i]);
    }
    printf("\n");
}

void shift(double a[], size_t size, double by) {
    for (size_t i = 0; i < size; i++) {
        a[i] += by;
    }
}

size_t filter(double a[], size_t count, enum filter_type t, double threshold) {
    size_t filtered_count = 0;
    switch (t) {
        case EQ:
            for (size_t i = 0; i < count; i++) {
                if (a[i] == threshold) {
                    a[filtered_count++] = a[i];
                }
            }
            break;
        case NEQ:
            for (size_t i = 0; i < count; i++) {
                if (a[i] != threshold) {
                    a[filtered_count++] = a[i];
                }
            }
            break;
        case GEQ:
            for (size_t i = 0; i < count; i++) {
                if (a[i] >= threshold) {
                    a[filtered_count++] = a[i];
                }
            }
            break;
        case LEQ:
            for (size_t i = 0; i < count; i++) {
                if (a[i] <= threshold) {
                    a[filtered_count++] = a[i];
                }
            }
            break;
        case LESS:
            for (size_t i = 0; i < count; i++) {
                if (a[i] < threshold) {
                    a[filtered_count++] = a[i];
                }
            }
            break;
        case GREATER:
            for (size_t i = 0; i < count; i++) {
                if (a[i] > threshold) {
                    a[filtered_count++] = a[i];
                }
            }
            break;
    }
    return filtered_count;
}
