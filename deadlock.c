#include <stdio.h>
#include <stdbool.h>

#define P 5 // number of processes
#define R 3 // number of resources

int main() {
    int i, j, count = 0;

    // Available resources
    int available[R] = {3, 3, 2};

    // Max resource requirements for each process
    int max[P][R] = {
        {7, 5, 3},
        {3, 2, 2},
        {9, 0, 2},
        {2, 2, 2},
        {4, 3, 3}
    };

    // Currently allocated resources to each process
    int allocation[P][R] = {
        {0, 1, 0},
        {2, 0, 0},
        {3, 0, 2},
        {2, 1, 1},
        {0, 0, 2}
    };

    int need[P][R];
    bool finish[P] = {false};
    int safeSeq[P];

    // Calculate the Need matrix
    for (i = 0; i < P; i++) {
        for (j = 0; j < R; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    printf("Process\tAllocation\tMax\t\tNeed\n");
    for (i = 0; i < P; i++) {
        printf("P%d\t", i);
        for (j = 0; j < R; j++) {
            printf("%d ", allocation[i][j]);
        }
        printf("\t\t");
        for (j = 0; j < R; j++) {
            printf("%d ", max[i][j]);
        }
        printf("\t\t");
        for (j = 0; j < R; j++) {
            printf("%d ", need[i][j]);
        }
        printf("\n");
    }

    int work[R];
    for (i = 0; i < R; i++) {
        work[i] = available[i];
    }

    while (count < P) {
        bool found = false;
        for (i = 0; i < P; i++) {
            if (!finish[i]) {
                bool canAllocate = true;
                for (j = 0; j < R; j++) {
                    if (need[i][j] > work[j]) {
                        canAllocate = false;
                        break;
                    }
                }

                if (canAllocate) {
                    for (j = 0; j < R; j++) {
                        work[j] += allocation[i][j];
                    }
                    safeSeq[count++] = i;
                    finish[i] = true;
                    found = true;
                    printf("Process P%d allocated and finished. Work updated: ", i);
                    for (j = 0; j < R; j++) {
                        printf("%d ", work[j]);
                    }
                    printf("\n");
                }
            }
        }

        if (!found) {
            printf("System is NOT in a safe state!\n");
            return 0;
        }
    }

    printf("\nSystem is in a safe state.\nSafe sequence is: ");
    for (i = 0; i < P; i++) {
        printf("P%d ", safeSeq[i]);
    }
    printf("\n");

    return 0;
}
