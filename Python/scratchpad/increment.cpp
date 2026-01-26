#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;


int main(){
    auto start = high_resolution_clock::now();
    
    for (int i = 0; i < 10000000; i++){
        cout << i << "\n";
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);

    cout << duration.count() << endl;
}
