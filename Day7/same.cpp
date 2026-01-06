#include <vector>
#include <algorithm>
class Solution {
public:
    int sumOfEncryptedInt(vector<int>& nums) {
        int totalSum = 0;
        
        for (int num : nums) {
            int temp = num;
            int maxDigit = 0;
            int repUnit = 0;
            
            while (temp > 0) {
                int digit = temp % 10;
                maxDigit = max(maxDigit, digit);
                repUnit = repUnit * 10 + 1;
                temp /= 10;
            }
            
            totalSum += (maxDigit * repUnit);
        }
        
        return totalSum;
    
    }
};