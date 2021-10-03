#include<stdio.h>
#include<conio.h>
 main()
{ 
	
	float num1;
	float num2;
	char op;
	float result;
	char option;
	
 
 do{
    printf("  enter the first number:");	
    scanf("%f",&num1);
	
	printf("enter the operation:");
	scanf(" %c",&op);
	
	printf("enter the second number:");
	scanf("%f",&num2);
	
	switch(op)

{
        case '+':
		result=num1+num2;
	printf("the result is: %f",result);
	break;
		
		case '-':
		result=num1-num2;
	printf("the result is: %f",result);
	break;
		
		case '*':
		result=num1*num2;
	printf("the result is: %f",result);
	break;
		
		case '/':
		result=num1/num2;
	printf("the result is: %f",result);
	break;
		
		default :
		printf("the operator is not valid");
	    
}  
     printf("\n do u want to continue y/n?\n");
	 option=getch();
    
	  
}	   
	   while(option=='y');
	getch();     
   
}	
 


	   


    



    
      

