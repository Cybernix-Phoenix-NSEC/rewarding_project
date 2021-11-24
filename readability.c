#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>

float count(string line);

int main(void)
{

    //user prompt
    string line1 = get_string("Text = ");
    float index;

    //calling the function count
    float index1 = count(line1);

    //rounding the index
    int index2 = round(index1);
    if (index2 < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index2 >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index2);
    }

}

float count(string line)
{
    int n = strlen(line);
    int letters = 0;
    int sent = 0;

    //for the last word
    int word = 1;

    //for counting the number of letters, words and sentences
    for (int i = 0; i < n; i++)
    {
        if (((line[i] >= 65) && (line[i] <= 90)) || ((line[i] >= 97) && (line[i] <= 122)))
        {
            letters++;
        }
        if (line[i - 1] == ' ')
        {
            word++;
        }
        if ((line[i] == '.') || (line[i] == '!') || (line[i] == '?'))
        {
            sent++;
        }
    }

    //for finding out the index
    float L = ((float)letters / (float)word * 100);
    float S = ((float)sent / (float)word * 100);
    float index = 0.0588 * L - 0.296 * S - 15.8;
    return index;
}