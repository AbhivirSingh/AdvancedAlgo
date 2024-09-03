#include <iostream>
#include <chrono>
#include <vector>

using namespace std;

unsigned long long catalan(int n) {
    if (n <= 1) return 1;
    
    unsigned long long result = 0;
    for (int i = 0; i < n; ++i) {
        result += catalan(i) * catalan(n - 1 - i);
    }
    
    return result;
}

int main() {
    vector<int> values = {10, 15, 20}; // Example large values for n
    
    for (int n : values) {
        auto start = chrono::high_resolution_clock::now();
        unsigned long long result = catalan(n);
        auto end = chrono::high_resolution_clock::now();
        chrono::duration<double> duration = end - start;
        
        cout << "catalan(" << n << ") = " << result << "\n";
        cout << "Time taken: " << duration.count() << " seconds\n";
        cout << "--------------------------------------------\n";
    }
    
    return 0;
}
