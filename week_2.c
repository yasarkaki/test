#include <stdio.h>
int main(){


    int number1 = 10;
    int number2 = 2;
    int number1 = 10 , number2 = 2;

    int sum = number1 + number2;
    int modulo = number1 % number2 

    printf("Summation : %d , and Modulo  : %d\n") ;
    printf("Adress : %d " , &sum) ;

    int number1 , number2 ; 
    printf("Please give me number1:");
    scanf("%d",&number1);
    printf("Please give me number2:");
    scanf("%d",&number2);

    int sum = number1 + number2 ;
    int mod = number1 % number2 ;

    printf("Summation: %d , and Modulo : %d\n",sum,mod)

    int a = 5;
    int b = a++;
    int c = ++a
    printf("a: %d\n",a)
    printf("b: %d\n",b)
    printf("c: %d\n",c)



    for(int myVar = 0 ; myVar <=10 ; myVar++)
        printf("MyVar is : %d\n" , myVar)
        printf("MyVar is : %d\n" , myVar)


    int age = 20 ;
    if (age >= 18)
        printf("You are an adult.\n");
    else if (age < 16)
        printf("You cannot get moto DL.")
    else 
        printf("You are a minor.\n")
    


    return 0;
}