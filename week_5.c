#include <stdio.h>

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};
    printf("ilk eleman: %d\n", numbers[0]); 
    return 0;
}

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};

    for (int i = 0; i < 5; i++) {
        printf("indexteki eleman %d: %d\n", i, numbers[i]);
    }

    return 0;
}
