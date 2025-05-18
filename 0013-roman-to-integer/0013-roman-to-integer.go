func romanToInt(s string) int {
    values := [256]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum := 0
    prevValue := 0

    for i := 0; i < len(s); i++ {
        currentValue := values[s[i]]
        if currentValue > prevValue {
            sum += currentValue - 2*prevValue
        } else {
            sum += currentValue
        }
        prevValue = currentValue
    }
    return sum
}