// Code Created for CSE 250A Homework 3 Question 2
// Creator: Jingyuan Li with All rights reserved.
// 10-18-2015 At UCSD
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main(){
    srand(time(NULL));
    int z = 64, n = 10, m = 10000;
    vector<double> res;
    double alpha = 0.35, sum = 0, sum_b7 = 0, p_zb;
    for (int i = 0; i < m; i++){
        int num = rand() % int(pow(2,n));
        p_zb = (1-alpha)/(1+alpha)*pow(alpha, abs(z-num));
        sum += p_zb;
        if ((num >> 6) & 1) sum_b7 += p_zb;
        res.push_back(sum_b7/sum);
    }
    for (int i = 0; i < res.size(); i++){
        cout << res[i] << endl;
    }
    cout << endl;
}