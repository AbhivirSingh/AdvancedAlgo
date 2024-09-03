#include <iostream>
#include <chrono>
#include <vector>
#include <string>

using namespace std;

void reverseStringRec(string &str, int start, int end) {
    if (start >= end) {
        return;
    }
    swap(str[start], str[end]);
    reverseStringRec(str, start + 1, end - 1);
}

void reverseStringIter(string &str) {
    int start = 0;
    int end = str.length() - 1;
    while (start < end) {
        swap(str[start], str[end]);
        start++;
        end--;
    }
}

int main() {
    // Define test cases with large string lengths
    vector<int> lengths = {10000, 50000, 100000};
    
    for (int len : lengths) {
        // Create a test string of the specified length
        string testString(len, 'a'); // Fill the string with 'a'

        // Measure recursive function time
        string recString = testString;
        auto start = chrono::high_resolution_clock::now();
        reverseStringRec(recString, 0, recString.length() - 1);
        auto end = chrono::high_resolution_clock::now();
        chrono::duration<double> recDuration = end - start;

        // Measure iterative function time
        string iterString = testString;
        start = chrono::high_resolution_clock::now();
        reverseStringIter(iterString);
        end = chrono::high_resolution_clock::now();
        chrono::duration<double> iterDuration = end - start;

        // Output results
        cout << "String length: " << len << "\n";
        cout << "Time taken (recursive): " << recDuration.count() << " seconds\n";
        cout << "Time taken (iterative): " << iterDuration.count() << " seconds\n";
        cout << "--------------------------------------------\n";
    }

    return 0;
}
