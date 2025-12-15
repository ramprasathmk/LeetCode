class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> jewelsSet = new HashSet<>();
        for (char j: jewels.toCharArray()) {
            jewelsSet.add(j);
        }

        int jewelsCount = 0;

        for (char s: stones.toCharArray()) {
            if (jewelsSet.contains(s)) {
                jewelsCount++;
            }
        }

        return jewelsCount;
    }
}