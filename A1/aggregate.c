#include "aggregate.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static double _count(double* arr, int size);
static double _min(double* arr, int size);
static double _max(double* arr, int size);
static double _sum(double* arr, int size);
static double _avg(double* arr, int size);
static double _pavg(double* arr, int size);

typedef double (*aggregate_func)(double*, int);

static const char* funcnames[] = { "COUNT", "MIN", "MAX", "SUM", "AVG", "PAVG" };
static aggregate_func funcpointers[] = { &_count, &_min, &_max, &_sum, &_avg, &_pavg };

double aggregate(const char* func, double* arr, int size) {
    if (arr == NULL || size <= 0) {
        fprintf(stderr, "FATAL ERROR in line %d\n", __LINE__);
        exit(1);
    }

    for (int i = 0; i < sizeof(funcnames) / sizeof(funcnames[0]); i++) {
        if (strcasecmp(func, funcnames[i]) == 0) {
            return funcpointers[i](arr, size);
        }
    }

    fprintf(stderr, "Invalid function name: %s\n", func);
    exit(1);
}

static double _count(double* arr, int size) {
    return size;
}

static double _min(double* arr, int size) {
    double min = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

static double _max(double* arr, int size) {
    double max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

static double _sum(double* arr, int size) {
    double sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

static double _avg(double* arr, int size) {
    double sum = _sum(arr, size);
    return sum / size;
}

static double _pavg(double* arr, int size) {
    double min = _min(arr, size);
    double max = _max(arr, size);
    return (min + max) / 2;
}
