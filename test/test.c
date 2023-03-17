#include <stdio.h>
#include <stdlib.h> // for exit()
#include <unistd.h> // for fork(), and sleep()
 
int main()
{
    // Creating a Child Process
    int pid = fork();
   
    if (pid > 0)         // True for Parent Process 
        sleep(60);                  
    else if (pid == 0)   // True for Child Process
        {
            printf("Zombie Process Created Successfully!");
            exit(0);
        }
    else                 // True when Child Process creation fails
        printf("Sorry! Child Process cannot be created...");
   
    return 0;
}