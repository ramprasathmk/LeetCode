class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int bitCount = 0;
        int length = bits.length - 1;
        
        while (bitCount < length) {
            if (1 == bits[bitCount]) {
                bitCount += 2;
            } else {
                bitCount++;
            } 
        }

        return bitCount == length;
    }
}