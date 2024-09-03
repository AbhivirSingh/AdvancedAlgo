#include <iostream>
#include <chrono>
#include <limits>
#include <stdexcept>

using namespace std;

// Recursive function to calculate the factorial of a number
unsigned long long recursive_factorial(int n)
{
    if (n < 0)
        throw invalid_argument("Negative numbers do not have factorials.");
    if (n == 0 || n == 1)
        return 1;
    return n * recursive_factorial(n - 1);
}

// Iterative function to calculate the factorial of a number
unsigned long long iterative_factorial(int n)
{
    if (n < 0)
        throw invalid_argument("Negative numbers do not have factorials.");
    unsigned long long result = 1;
    for (int i = 2; i <= n; ++i)
    {
        result *= i;
    }
    return result;
}

int main()
{
    int n = 1000;

    try
    {
        auto start = chrono::high_resolution_clock::now();
        unsigned long long recur_result = recursive_factorial(n);
        auto end = chrono::high_resolution_clock::now();
        chrono::duration<double> recur_duration = end - start;
        cout << "Recursive approach: " << recur_result << " (Time: " << recur_duration.count() << " seconds)" << endl;
    }
    catch (const overflow_error &e)
    {
        cout << "Recursive approach failed: " << e.what() << endl;
    }
    catch (const invalid_argument &e)
    {
        cout << "Invalid input: " << e.what() << endl;
    }

    // Measure time for iterative solution
    try
    {
        auto start = chrono::high_resolution_clock::now();
        unsigned long long iter_result = iterative_factorial(n);
        auto end = chrono::high_resolution_clock::now();
        chrono::duration<double> iter_duration = end - start;
        cout << "Iterative approach: " << iter_result << " (Time: " << iter_duration.count() << " seconds)" << endl;
    }
    catch (const overflow_error &e)
    {
        cout << "Iterative approach failed: " << e.what() << endl;
    }
    catch (const invalid_argument &e)
    {
        cout << "Invalid input: " << e.what() << endl;
    }

    return 0;
}