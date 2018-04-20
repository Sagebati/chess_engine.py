//
//  patch.c
//
//  Created by Benjamin Cohen on 16/04/2018.
//  Copyright © 2018 Benjamin Cohen. All rights reserved.
//


#include <stdio.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <termios.h>
#include <sys/ioctl.h>

#define MAX 1



int voir_touche(){
    
    char  buffer[3];
    
    read(0, buffer, 3);


    if (buffer[2] == 65){
        return(8);
    }
    else if (buffer[2] == 66){
        return (2);
    }
    else if (buffer[2] == 68){
        return (4);
    }
    else if (buffer[2] == 67){
        return (6);
    }
    else if (buffer[0] == 48){
        return (0);
    }
    else if (buffer[0] == 13){
        return (10);
    }

    return (-1);
    
}




void mode_raw(int activer){
    
    static struct termios cooked;
    static int raw_actif = 0;
    
    if (raw_actif == activer)
        return;
    
    if (activer){
        struct termios raw;
        
        tcgetattr(STDIN_FILENO, &cooked);
        
        raw = cooked;
        cfmakeraw(&raw);
        tcsetattr(STDIN_FILENO, TCSANOW, &raw);
    }
    else{
        tcsetattr(STDIN_FILENO, TCSANOW, &cooked);
    }
    
    raw_actif = activer;
}




void exe(char *tmp[]){
    
        FILE *fp;
        int status;
        char patch[30];
        
        fp = popen(*tmp, "r");
        if (fp == NULL)
        /* Error */
        
        
        while (fgets(patch, 29, fp) != NULL)

        status = pclose(fp);

        if (status == -1) {
            /* Error by pclose() */
        } 

}
    

void loading(int d, int e, int k){


    (k == 1) ? printf("Installation en cours %d/%d...\n\n", (d+1), MAX) : printf("Désinstallation en cours %d/%d...\n\n", (d+1), MAX);

    printf("======================\n");
    printf("+");
    (k == 1) ? printf("\033[30;42m") : printf("\033[30;41m");

    for(int i=0; i<e; i++){
        printf(" ");
    }

    printf("\033[0m");
    printf("+");
    printf("\n+");
    (k == 1) ? printf("\033[30;42m") : printf("\033[30;41m");
    
    for(int i=0; i<e; i++){
        printf(" ");
    }
        
    printf("\033[0m");
    printf("+\n");
    printf("======================\n");

}


int menu(){
    
    
    int choix_tmp= 1,  val_tmp=0;
     
    do{
        system("clear");
        printf("\033[32m");
        printf("#*******************************************************************#\n");
        printf("#                                                                   #\n");
        printf("#                          Patch V 1.0 Beta                         #\n");
        printf("#                                                                   #\n");
        printf("#*******************************************************************#\n\n\n");


            
        printf("\033[31m");
        printf(" Merci de vérifier votre connexion Internet\n");
        printf(" si vous souhaitez utiliser la rubrique installation des packages.\n");
        printf(" Merci de bien vouloir installer au préalable le logiciel python 3.6\n");
        printf(" disponible à l'adresse suivante :\n\n - https://www.python.org/downloads/release/python-360/ \n\n\n");
        printf("\033[0m");

        if(val_tmp==0){
            printf("\033[30;43m");
            printf("==+=> Installation des patchs\n");
            printf("\033[0m");
        }
        else{
            printf("==+=> Installation des patchs\n");
        }
        if(val_tmp==1){
            printf("\033[30;43m");
            printf("==+=> Désinstallation des patchs\n");
            printf("\033[0m");
        }
        else{
            printf("==+=> Désinstallation des patchs\n");
        }
        if(val_tmp==2){
            printf("\033[30;43m");
            printf("==+=> Informations\n");
            printf("\033[0m");
        }
        else{
            printf("==+=> Informations\n");
        }
        if(val_tmp==3){
            printf("\033[30;43m");
            printf("==+=> Quitter\n");
            printf("\033[0m");
        }
        else{
            printf("==+=> Quitter\n");
        }


        mode_raw(1);
        choix_tmp=voir_touche();
        fflush(stdout);
        mode_raw(0);

        system("clear");

        if(choix_tmp==2 && val_tmp<3){
            val_tmp++;
        }
        else if (choix_tmp==8 && val_tmp>0){
            val_tmp--;
        }

    }while(choix_tmp != 10);

   return (val_tmp);
}




int main(int argc, const char * argv[]) {
    
    int choix=1;
    
    char *install[MAX]={
        "python3 -m pip install --user python-chess",
    };
    
    char *uninstall[MAX]={
        "python3 -m pip uninstall --yes python-chess",
    };
    
    
    
   
    do{

        printf("\033[36m");

        choix=menu();

        if(choix==0){
            int j=0;
            for(j=0; j<MAX; j++){
                exe(&install[j]);
                for(int i=0; i<21; i++){
                    loading(j, i, 1);
                    sleep(1);
                    system("clear");
                }
                if(j==MAX-1){
                    system("clear");
                    printf("Modification achevée, vous serez redirigé vers le menu dans quelques secondes.\n\n");
                    sleep(4);
                }
            }   
        }

        else if(choix==1){
            int j=0;
            for(int j=0; j<MAX; j++){
                exe(&uninstall[j]);
                sleep(4);
                for(int i=0; i<21; i++){
                    loading(j, i, 2);
                    sleep(1);
                    system("clear");
                }
                if(j==MAX-1){
                    system("clear");
                    printf("Modification achevée, vous serez redirigé vers le menu dans quelques secondes.\n\n");
                    sleep(4);
                } 
            }   
        }

        else if (choix==2){
            system("clear");
            printf("\033[36m");
            printf("*=======================================================================================*\n");
            printf("*                                                                                       *\n");
            printf("*                                                                                       *\n");
            printf("*          Copyright © 2018 Benjamin Cohen. All rights reserved                         *\n");
            printf("*                                                                                       *\n");
            printf("*                                                                                       *\n");
            printf("*                Ce logiciel a pour fonction de simplifier                              *\n");
            printf("*                l'installation/désinstallation de différents packages python.          *\n");
            printf("*                                                                                       *\n");
            printf("*                Voici la liste des différents packages installés nécessaires           *\n");
            printf("*                pour l'exécution du logiciel chess_engine :                            *\n");
            printf("*                                                                                       *\n");
            printf("*                                                                                       *\n");
            printf("*                 # python-chess                                                        *\n");
            printf("*                                                                                       *\n");
            printf("*                                                                                       *\n");
            printf("*                                                                                       *\n");
            printf("*    Attention : L'installation des différents packages nécessitent une connexion       *\n");
            printf("*                Internet ainsi que l'installation du logiciel python                   *\n");
            printf("*                à partir de la version 3.6.                                            *\n");
            printf("*                Le logiciel est encore une version bêta test ce qui signifie           *\n");
            printf("*                que certains bugs peuvent survenir.                                    *\n");
            printf("*                Dans le cas suivant, merci de contacter le développeur du logiciel.    *\n");                                                          
            printf("*                                                                                       *\n");
            printf("*                                                                                       *\n");
            printf("*                                                                                       *\n");
            printf("*=======================================================================================*\n");
            printf("\n\n#== Appuyer sur rentrée pour revenir au menu ==#\n\n");
            printf("\033[0m");
            getchar();
        }


        else if (choix==3){
            system("clear");
            printf("\033[31m");
            printf("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*++*+*+*+*+*+*+*+*+*\n");
            printf("*                                                                                *\n");
            printf("*         Merci d'avoir utilisé notre logiciel. Au revoir et à bientôt.          *\n");
            printf("*                                                                                *\n");
            printf("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*++*+*+*+*+*+*+*+*+*\n");
            printf("\033[0m");
        }
        
        
        
    }while(choix != 3);
    
    return 0;
}
