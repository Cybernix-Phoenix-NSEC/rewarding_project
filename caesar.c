#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//command-line argument
int main(int argc, string argv[])
{
    
    //checking whether the user has input multiple numbers
    if (argc != 2)
    {
        printf(" Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        
        //when the user has input only one number as the key
        int m = strlen(argv[1]);
        int l = 0;
        
        //checking whether the key is a number
        for (int i = 0; i < m; i++)
        {
            if (isdigit(argv[1][i]))
            {
                l++;
            }
        }
        if (l != m)
        {
            printf(" Usage: ./caesar key\n");
            return 1;
        }
        else
        {
            //when the key is a number
            int key = atoi(argv[1]);
            printf("Success\n");
            string text = get_string("plaintext: ");
            int n = strlen(text);
        
            //copying the plaintext into an array of data type char
            char cip[strlen(text)];
            strcpy(cip, text);
            printf("ciphertext: ");
        
            //checking whether a letter is lowercase, uppercase
            for (int i = 0; i < n; i++)
            {
                if (islower(cip[i]))
                {
                    printf("%c", (((cip[i] + key) - 97) % 26) + 97);
                }
                else if (isupper(cip[i]))
                {
                    printf("%c", (((cip[i] + key) - 65) % 26) + 65);
                }
                else
                {
                    printf("%c", cip[i]);
                }
            }
            printf("\n");
            return 0;
        }
    }
    
}