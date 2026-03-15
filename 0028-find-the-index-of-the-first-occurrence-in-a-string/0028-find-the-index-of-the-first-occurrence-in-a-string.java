class Solution {
    public int strStr(String haystack, String needle) {
        int hLen = haystack.length();
        int nLen = needle.length();

        for (int i = 0; i <= hLen - nLen; i++) {
            String sub = haystack.substring(i, i + nLen);
            if (needle.equals(sub)) {
                return i;
            }
        }

        return -1;
    }
}