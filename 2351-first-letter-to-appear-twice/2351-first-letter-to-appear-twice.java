class Solution {
    public char repeatedCharacter(String s) {
        Set<Character> seenLetters = new HashSet<>();

        for (char ch: s.toCharArray()) {
            if (seenLetters.contains(ch)) {
                return ch;
            } else {
                seenLetters.add(ch);
            }
        }

        return '\0';
    }
}