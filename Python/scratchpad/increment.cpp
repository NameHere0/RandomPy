#include <iostream>

int main(){
    using Clock = std::chrono::system_clock;

    const Clock::time_point start = Clock::now();
    foo();
    const Clock::time_point end = Clock::now();

std::cout << (end-start).count() << "us\n";


    for (i = 0; i < 10000000; i++){
        std::cout << i << "\n";
    }




}
