#include <iostream>
#include <cmath>
#include <stdlib.h>

using namespace std;

int main()
{
    double denominator = 10; // start with 10 as nothing below 10 is realistic
    double lowerNumerator = 0;
    double upperNumberator = 0;
    double storeNumerator = 1;
    double storeDenominator = 1;
    double ratio = 0;
    double storeRatio = 0;
    double difference = 0;
    double storeDifference = 1;

    while (denominator < 1000000)
    {
        lowerNumerator = round(3 * denominator);
        upperNumberator = round(3.2 * denominator);

        for (double numerator = lowerNumerator; numerator <= upperNumberator; numerator++)
        {
            // cout << "Ratio is " << numerator << "/" << denominator << endl;
            ratio = numerator / denominator;
            // cout << "Calcuated ratio is " << ratio << endl;
            difference = abs(M_PI - ratio);
            // cout << "Difference is " << difference << endl << endl;

            if (difference < storeDifference)
            {
                storeNumerator = numerator;
                storeDenominator = denominator;
                storeRatio = ratio;
                storeDifference = difference;
            }
        }
        
        denominator++;
    }

    // print numerator and denominator as well as calculated ratio of pi
    cout << "Ratio was " << storeNumerator << "/" << storeDenominator << endl;
    cout << "Calcuated ratio of " << storeRatio << endl;
    cout << "Actual value of PI " << M_PI << endl;

    return 0;
}
