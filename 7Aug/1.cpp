#include <iostream>
#include <chrono>
using namespace std;

int recfib(int n)
{   
    // Termination Cases
    if (n == 1)
        return 0;
    else if (n == 2)
        return 1;

    // Recursive Case
    else
        return recfib(n - 1) + recfib(n - 2);
}

int itrfib(int n)
{   
    // Corner Case
    if (n == 1)
        return 0;
    
    // Main Property
    int a=0,b=1;
    while (n>2){
        int temp=b;
        b+=a;
        a=temp;
        n--;
    }return b;
}

int main()
{
    int values[] = {30, 35, 40};

    for (int n : values) {

        // Recursive Part

        // Starts the timer
        auto recstart = chrono::high_resolution_clock::now();

        // Calculates the Fibonacci number
        int recresult = recfib(n);

        // Stops the timer
        auto recend = chrono::high_resolution_clock::now();

        // Calculates the duration
        chrono::duration<double> recduration = recend - recstart;

        
        // Gives the result and the duration
        cout << "Recursive Function for n = " << n << " = " << recresult << "\n";
        cout << "Time taken for n = " << n << ": " << recduration.count() << " seconds\n\n";


        // Iterative Part

        // Starts the timer
        auto itrstart = chrono::high_resolution_clock::now();

        // Calculates the Fibonacci number
        int itrresult = itrfib(n);

        // Stops the timer
        auto itrend = chrono::high_resolution_clock::now();

        // Calculates the duration
        chrono::duration<double> itrduration = itrend - itrstart;

        // Gives the result and the duration
        cout << "Iterative Function for n = " << n << " = " << itrresult << "\n";
        cout << "Time taken for n = " << n << ": " << itrduration.count() << " seconds\n\n";
    }

    return 0;
}