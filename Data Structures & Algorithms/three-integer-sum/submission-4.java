// import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Integer> currentVals = new HashMap<>();
        Set<List<Integer>> ans = new HashSet<>();

        for (int k = 0; k < nums.length; k++) {
            int twoSumReq = -nums[k];

            for (int j = 0; j < k; j++) {
                int sumReq = twoSumReq - nums[j];

                if (currentVals.containsKey(sumReq)) {
                    // check if there are enough occurrences
                    if (sumReq != nums[j] || currentVals.get(sumReq) > 1) {
                        List<Integer> soln = Arrays.asList(sumReq, nums[j], nums[k]);
                        Collections.sort(soln);
                        ans.add(soln);
                    }
                }
            }

            currentVals.put(nums[k], currentVals.getOrDefault(nums[k], 0) + 1);

            // Debug print if needed
            // System.out.println(currentVals);
        }
        List<List<Integer>> result = new ArrayList<>(ans);
        result.sort((a, b) -> {
            for (int i = 0; i < 3; i++) {
                int cmp = Integer.compare(a.get(i), b.get(i));
                if (cmp != 0) return cmp;
            }
            return 0;
        });

        return result;
    }
}