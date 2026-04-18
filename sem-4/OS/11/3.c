#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_P 100
#define MAX_R 100

int nResources, nProcesses;
int total[MAX_R];
int available[MAX_R];
int maxNeed[MAX_P][MAX_R];
int need[MAX_P][MAX_R];
int allocation[MAX_P][MAX_R];
int finished[MAX_P];

int read_next_int(FILE *fp, int *value) {
    int ch;
    char buffer[64];
    int idx = 0;

    while ((ch = fgetc(fp)) != EOF) {
        if (isdigit(ch) || ch == '-') {
            buffer[idx++] = (char)ch;
            break;
        }
    }

    if (ch == EOF) return 0;

    while ((ch = fgetc(fp)) != EOF) {
        if (isdigit(ch)) {
            if (idx < 63) buffer[idx++] = (char)ch;
        } else {
            break;
        }
    }

    buffer[idx] = '\0';
    *value = atoi(buffer);
    return 1;
}

void print_state() {
    int i, j;
    printf("\nCurrent System State:\n");
    printf("Available: ");
    for (j = 0; j < nResources; j++) printf("%d ", available[j]);
    printf("\n");

    printf("Allocation Matrix:\n");
    for (i = 0; i < nProcesses; i++) {
        printf("P%d: ", i);
        for (j = 0; j < nResources; j++) printf("%d ", allocation[i][j]);
        if (finished[i]) printf("(FINISHED)");
        printf("\n");
    }

    printf("Need Matrix:\n");
    for (i = 0; i < nProcesses; i++) {
        printf("P%d: ", i);
        for (j = 0; j < nResources; j++) printf("%d ", need[i][j]);
        if (finished[i]) printf("(FINISHED)");
        printf("\n");
    }
    printf("\n");
}

void release_all_resources(int pid) {
    int j;
    for (j = 0; j < nResources; j++) {
        available[j] += allocation[pid][j];
        allocation[pid][j] = 0;
        need[pid][j] = 0;
    }
    finished[pid] = 1;
    printf("Process P%d has completed. Its allocated resources are released automatically.\n", pid);
}

int is_need_zero(int pid) {
    int j;
    for (j = 0; j < nResources; j++) {
        if (need[pid][j] != 0) return 0;
    }
    return 1;
}

int all_finished() {
    int i;
    for (i = 0; i < nProcesses; i++) {
        if (!finished[i]) return 0;
    }
    return 1;
}

int safety_check(int safeSeq[]) {
    int work[MAX_R];
    int finishTemp[MAX_P];
    int tempAlloc[MAX_P][MAX_R];
    int tempNeed[MAX_P][MAX_R];
    int i, j, count = 0, found;

    for (j = 0; j < nResources; j++) work[j] = available[j];

    for (i = 0; i < nProcesses; i++) {
        finishTemp[i] = finished[i];
        for (j = 0; j < nResources; j++) {
            tempAlloc[i][j] = allocation[i][j];
            tempNeed[i][j] = need[i][j];
        }
    }

    while (count < nProcesses) {
        found = 0;

        for (i = 0; i < nProcesses; i++) {
            if (!finishTemp[i]) {
                int possible = 1;

                for (j = 0; j < nResources; j++) {
                    if (tempNeed[i][j] > work[j]) {
                        possible = 0;
                        break;
                    }
                }

                if (possible) {
                    for (j = 0; j < nResources; j++) {
                        work[j] += tempAlloc[i][j];
                    }
                    finishTemp[i] = 1;
                    safeSeq[count++] = i;
                    found = 1;
                }
            }
        }

        if (!found) break;
    }

    return (count == nProcesses);
}

int can_grant_request(int pid, int req[]) {
    int j;
    int safeSeq[MAX_P];

    if (finished[pid]) {
        printf("P%d is already finished.\n", pid);
        return 0;
    }

    for (j = 0; j < nResources; j++) {
        if (req[j] < 0) {
            printf("Invalid request: negative values not allowed.\n");
            return 0;
        }
        if (req[j] > need[pid][j]) {
            printf("Request exceeds remaining need of P%d.\n", pid);
            return 0;
        }
        if (req[j] > available[j]) {
            printf("Not enough available resources right now.\n");
            return 0;
        }
    }

    for (j = 0; j < nResources; j++) {
        available[j] -= req[j];
        allocation[pid][j] += req[j];
        need[pid][j] -= req[j];
    }

    if (safety_check(safeSeq)) {
        printf("YES, request can be granted.\n");
        printf("Safe sequence: ");
        for (j = 0; j < nProcesses; j++) {
            printf("P%d", safeSeq[j]);
            if (j != nProcesses - 1) printf(" -> ");
        }
        printf("\n");
        return 1;
    } else {
        for (j = 0; j < nResources; j++) {
            available[j] += req[j];
            allocation[pid][j] -= req[j];
            need[pid][j] += req[j];
        }
        printf("NO, request cannot be granted (unsafe state).\n");
        return 0;
    }
}

int process_release(int pid, int rel[]) {
    int j;

    if (finished[pid]) {
        printf("P%d is already finished.\n", pid);
        return 0;
    }

    for (j = 0; j < nResources; j++) {
        if (rel[j] < 0) {
            printf("Invalid release: negative values not allowed.\n");
            return 0;
        }
        if (rel[j] > allocation[pid][j]) {
            printf("P%d cannot release more than allocated.\n", pid);
            return 0;
        }
    }

    for (j = 0; j < nResources; j++) {
        allocation[pid][j] -= rel[j];
        available[j] += rel[j];
    }

    printf("Release accepted.\n");
    return 1;
}

int main(int argc, char *argv[]) {
    FILE *fp;
    int i, j;
    int val;
    int pid;
    char op;
    int vec[MAX_R];

    if (argc != 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    fp = fopen(argv[1], "r");
    if (fp == NULL) {
        printf("Cannot open file: %s\n", argv[1]);
        return 1;
    }

    if (!read_next_int(fp, &nResources)) {
        printf("Invalid file format.\n");
        fclose(fp);
        return 1;
    }

    if (nResources <= 0 || nResources > MAX_R) {
        printf("Invalid number of resources.\n");
        fclose(fp);
        return 1;
    }

    for (j = 0; j < nResources; j++) {
        if (!read_next_int(fp, &total[j])) {
            printf("Invalid file format while reading total resources.\n");
            fclose(fp);
            return 1;
        }
        available[j] = total[j];
    }

    if (!read_next_int(fp, &nProcesses)) {
        printf("Invalid file format while reading number of processes.\n");
        fclose(fp);
        return 1;
    }

    if (nProcesses <= 0 || nProcesses > MAX_P) {
        printf("Invalid number of processes.\n");
        fclose(fp);
        return 1;
    }

    for (i = 0; i < nProcesses; i++) {
        finished[i] = 0;
        for (j = 0; j < nResources; j++) {
            if (!read_next_int(fp, &val)) {
                printf("Invalid file format while reading process needs.\n");
                fclose(fp);
                return 1;
            }
            maxNeed[i][j] = val;
            need[i][j] = val;
            allocation[i][j] = 0;
        }
    }

    fclose(fp);

    printf("System loaded successfully.\n");
    print_state();

    while (!all_finished()) {
        printf("Enter request/release (format: <pid> <a/r> <r0> <r1> ... <rN-1>)\n");
        printf("Example: 0 a 1 0 1 1\n");
        printf("         2 r 0 0 0 3\n");
        printf("Input: ");

        if (scanf("%d %c", &pid, &op) != 2) {
            printf("Invalid input.\n");
            break;
        }

        if (pid < 0 || pid >= nProcesses) {
            printf("Invalid process id.\n");
            while (getchar() != '\n');
            continue;
        }

        for (j = 0; j < nResources; j++) {
            if (scanf("%d", &vec[j]) != 1) {
                printf("Invalid resource vector input.\n");
                return 1;
            }
        }

        if (op == 'a' || op == 'A') {
            if (can_grant_request(pid, vec)) {
                if (is_need_zero(pid)) {
                    release_all_resources(pid);
                }
            }
        } else if (op == 'r' || op == 'R') {
            if (process_release(pid, vec)) {
                if (is_need_zero(pid)) {
                    release_all_resources(pid);
                }
            }
        } else {
            printf("Invalid operation. Use 'a' for allocation or 'r' for release.\n");
        }

        print_state();
    }

    printf("All processes have finished.\n");
    return 0;
}