#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Digite o numero de linhas do triangulo de pascal");
    char numero[128];
    scanf("%127s", numero);
    int n = atoi(numero);
    int i = 0;
    while (i<n) {
        int j = 0;
        int valor = 1;
        while (j<=i) {
            printf("%d %s", (int)(valor), " ");
            valor = valor*(i-j)/(j+1);
            j = j+1;
        }
        printf("\n");
        i = i+1;
    }
    printf("Digite o primeiro lado do triangulo:");
    char aInput[128];
    scanf("%127s", aInput);
    printf("Digite o segundo lado do triangulo:");
    char bInput[128];
    scanf("%127s", bInput);
    printf("Digite o terceiro lado do triangulo:");
    char cInput[128];
    scanf("%127s", cInput);
    double a = atof(aInput);
    double b = atof(bInput);
    double c = atof(cInput);
    if (a<=0 || b<=0 || c<=0) {
        printf("Erro: todos os lados devem ser positivos.");
    }
    else 
    if (a+b<=c || a+c<=b || b+c<=a) {
        printf("Medidas invalidas — nao formam um triangulo.");
    }
    else 
    if (a==b && b==c) {
        printf("Triangulo equilatero valido.");
    }
    else 
    if (a==b || a==c || b==c) {
        printf("Triangulo isosceles valido.");
    }
    else {
        printf("Triangulo escaleno valido.");
    }
    return 0;
}