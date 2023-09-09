#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include "mathpipe.h"
#include "singular.h"
#include "aggregate.h"

double mathpipe(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Failed to open file: %s\n", filename);
        exit(1);
    }

    double data[100];
    int size = 0;
    char line[100];

    while (fgets(line, sizeof(line), file) != NULL) {
        data[size] = atof(line);
        size++;
    }

    fclose(file);
    
    double result = aggregate("SUM", data, size);
    printf("Result: %.2f\n", result);

    return result;
}

int main() {
    const char* filename = "sample.txt";
    mathpipe(filename);
    // cases in singular.c in the assignment
    double arr[] = {4, 5, 6, 1, -1, 8, 2};

    print(arr, 1);
    print(arr, 0);
    shift(arr, 4, 0.5);
    filter(arr, 5, LEQ, 6);
    print(arr, sizeof(arr) / sizeof(arr[0]));

    // cases in aggregate.h in the assignment
    static double arrStatic[] = {1, 4, 5, 6, -1};
    double m = aggregate("MIN", arrStatic, 5);
    printf("%f\n", m); // -1.000000

    double data[] = {10.5, 20.3, 15.7, 18.2};
    int size = sizeof(data) / sizeof(data[0]);

    double result = aggregate("SUM", data, size);
    printf("Sum: %.2f\n", result);

    double* invalidArr = NULL;
    result = aggregate("COUNT", invalidArr, size);
    printf("Result: %.2f\n", result);

    return 0;
}
