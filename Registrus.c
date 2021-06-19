#include <stdio.h>
#include <string.h>
#define num 20

typedef struct carro {char marca[16]; int ano; int ano_comprou; char cor[11]; float preco; char placa[9];} Carro;

int menu_principal(){
    int choice=0;

    printf("MENU PRINCIPAL:\n");
    printf("1 - Cadastrar carro\n");
    printf("2 - Localizar carro\n");
    printf("3 - Remover carro\n");
    printf("4 - Relatorios\n");
    printf("0 - Sair\n");
    scanf("%d",&choice);

    return choice;}


int menu_relatorio(){
    int escolha=0;

    printf("1 - Listar carros\n");
    printf("2 - Listar carros por limite de preco\n");
    printf("3 - Listar carros por limite de ano\n");
    printf("4 - Listar carros de uma marca\n");
    printf("5 - Listar carros de marca e ano\n");
    printf("0 - Sair\n");
    scanf("%d",&escolha);

    return escolha;}


int find(int len, Carro vector[num], char placa[9]){
    if(len==0){return 0;}
    for (int g=0; g<len; g++){
        if (strcmp(placa,vector[g].placa) ==0){ printf("Placa ja registrada!\n");return 1;}}

    return 0;}




void ler(Carro vetor[num],int i) {
    do{
        printf("Digite a marca do carro:\n");
        scanf("%s", vetor[i].marca);

        printf("Digite o ano do carro:\n");
        scanf("%d", &vetor[i].ano);

        printf("Digite o ano de aquisicao do carro:\n");
        scanf("%d", &vetor[i].ano_comprou);

        printf("Digite a cor do carro:\n");
        scanf("%s", vetor[i].cor);

        printf("Digite o preco do carro:\n");
        scanf("%f", &vetor[i].preco);

        printf("Digite a placa do carro:\n");
        scanf("%s", vetor[i].placa);
        printf("\n");
    } while (find(i, vetor, vetor[i].placa));}


void imprimi_td(int len, Carro vector [num], int opcao) {
    switch (opcao) {
        case 1:{
            for (int i = 0; i < len; i++) {
                printf("Carro %d:\n", i + 1);
                printf("%s\n", vector[i].marca);
                printf("%d\n", vector[i].ano);
                printf("%d\n", vector[i].ano_comprou);
                printf("%s\n", vector[i].cor);
                printf("R$ %.2f\n", vector[i].preco);
                printf("%s\n", vector[i].placa);
                printf("\n");}break;}

        case 2:{
            float valor;
            printf("Digite o valor maximo para busca:\n");
            scanf("%f", &valor);
            for (int i = 0; i < len; i++) {
                if (vector[i].preco<=valor){
                    printf("Carro %d:\n", i + 1);   //Comecamos a contar os carros a partir do 1, mas nos vetores guardamos a partir do 0
                    printf("%s\n", vector[i].marca);
                    printf("%d\n", vector[i].ano);
                    printf("%d\n", vector[i].ano_comprou);
                    printf("%s\n", vector[i].cor);
                    printf("R$ %.2f\n", vector[i].preco);
                    printf("%s\n", vector[i].placa);
                    printf("\n");}}break;}

        case 3:{
            int ano;
            printf("Digite o ano maximo para busca:\n");
            scanf("%d", &ano);
            for (int i = 0; i < len; i++) {
                if (vector[i].ano<=ano){
                    printf("Carro %d:\n", i + 1);  //Comecamos a contar os carros a partir do 1, mas nos vetores guardamos a partir do 0
                    printf("%s\n", vector[i].marca);
                    printf("%d\n", vector[i].ano);
                    printf("%d\n", vector[i].ano_comprou);
                    printf("%s\n", vector[i].cor);
                    printf("R$ %.2f\n", vector[i].preco);
                    printf("%s\n", vector[i].placa);
                    printf("\n");}}break;}

        case 4:{
            char marca[9];
            printf("Digite a marca para busca:\n");
            scanf("%s",marca);
            for (int i = 0; i < len; i++) {
                if (strcmp(vector[i].marca,marca)==0){
                    printf("Carro %d:\n", i + 1);   //Comecamos a contar os carros a partir do 1, mas nos vetores guardamos a partir do 0
                    printf("%s\n", vector[i].marca);
                    printf("%d\n", vector[i].ano);
                    printf("%d\n", vector[i].ano_comprou);
                    printf("%s\n", vector[i].cor);
                    printf("R$ %.2f\n", vector[i].preco);
                    printf("%s\n", vector[i].placa);
                    printf("\n");}}break;}

        case 5:{
            char marca[9];
            int ano;

            printf("Digite o ano maximo para busca:\n");
            scanf("%d", &ano);
            printf("\nDigite a marca para busca:\n");
            scanf("%s",marca);
            for (int i = 0; i <= len; i++) {
                if (strcmp(vector[i].marca,marca)==0 && vector[i].ano<=ano){
                    printf("Carro %d:\n", i + 1);
                    printf("%s\n", vector[i].marca);
                    printf("%d\n", vector[i].ano);
                    printf("%d\n", vector[i].ano_comprou);
                    printf("%s\n", vector[i].cor);
                    printf("R$ %.2f\n", vector[i].preco);
                    printf("%s\n", vector[i].placa);
                    printf("\n");}}break;}}}


void find_print(int len, Carro vector[num], char placa[9]){
    for (int g=0; g<len; g++){
        if (strcmp(placa,vector[g].placa) ==0){
            printf("Carro %d:\n", g + 1);
            printf("%s\n", vector[g].marca);
            printf("%d\n", vector[g].ano);
            printf("%d\n", vector[g].ano_comprou);
            printf("%s\n", vector[g].cor);
            printf("R$ %.2f\n", vector[g].preco);
            printf("%s\n", vector[g].placa);
            printf("\n");}}}




void exclui_carro(int len,Carro vector[num], char placa[9]){
    int cond=0;
    if (len>0){
        Carro temp;
        for (int g=0; g<len; g++){
            if(strcmp(vector[g].placa, placa)==0){cond=1;}

            if (cond==1){
                strcpy(vector[g].marca, vector[g+1].marca);
                strcpy(vector[g].cor, vector[g+1].cor);
                strcpy(vector[g].placa, vector[g+1].placa);
                vector[g].ano = vector[g+1].ano;
                vector[g].ano_comprou = vector[g+1].ano_comprou;
                vector[g].preco = vector[g+1].preco;}}}}


int main(){
    int idx=0, len=0 ,resp;
    Carro modelos[num];
    char placa [9];


    do{
        resp = menu_principal();
        switch (resp) {
            case 1:{ler(modelos, idx); idx++;len++; break;}

            case 2:{
                printf("Digite a placa a ser procurada:\n");
                scanf("%s",placa);
                find_print(len, modelos, placa);break;}

            case 3:{
                printf("Digite a placa do carro a ser removido:\n");
                scanf("%s",placa);
                exclui_carro(len, modelos, placa); len--;idx--; break;}

            case 4:{
                int escolhe;
                do {
                    escolhe=menu_relatorio();
                    switch (escolhe) {
                        case 1: {imprimi_td(len, modelos,1);break;}
                        case 2: {imprimi_td(len, modelos,2);break;}
                        case 3: {imprimi_td(len, modelos,3);break;}
                        case 4: {imprimi_td(len, modelos,4);break;}
                        case 5: {imprimi_td(len, modelos,5);break;}
                    }} while (escolhe!=0);}

        }} while (resp !=0);


    return 0;}
