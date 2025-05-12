func addDigits(num int) int {
    sum := 0
    for num > 0 {
        digit := num % 10
        sum += digit
        num /= 10
        if num == 0 {
            if sum < 10 { return sum; }
            num = sum
            sum = 0
        }
    }
    return 0
}