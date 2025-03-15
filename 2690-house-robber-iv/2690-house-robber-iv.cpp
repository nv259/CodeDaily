class Solution {
public:
    int minCapability(vector<int>& nums, int k) {
        int n = nums.size();

        int l = 0, r = 1'000'000'000;
        while (l < r) {
            int mid = (l + r) >> 1;

            int num = 0;
            for(int i = 0; i < n; ++i) 
            if (nums[i] <= mid) ++num, ++i;
            
            if (num >= k) r = mid;
            else l = mid + 1;
        }

        return l;
    }
};