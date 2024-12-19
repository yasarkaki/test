#include <stdio.h>

int main() {
    int sayilar[5] = {10, 20, 30, 40, 50};
    printf("ilk eleman: %d\n", sayilar[0]); 
    return 0;
}

int main() {
    int sayilar[5] = {10, 20, 30, 40, 50};

    for (int i = 0; i < 5; i++) {
        printf("indexteki eleman %d: %d\n", i, sayilar[i]);
    }

    return 0;
}
