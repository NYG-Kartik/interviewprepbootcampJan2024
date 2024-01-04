class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int x = strs.size();
        map1 = {};
        if(x == 1){
            return strs;
        }
        else{
            for(int i =0; i<x; i++){
                if(strs[i] == x && strs[i] == map1[i]){
                    return strs[i];
                }
            }
        }


        
    }
};
