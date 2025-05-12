func sumOfMultiples(n int) int {
    // the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
    multiples := []int{ 3, 5, 7 }
    // the sum variable to store their sum value
    sum := 0
    for i := 1; i <= n ; i++ {
        for _, num := range multiples {
            if i%num==0 {
                sum += i
                break // Add only once, then skip to next i
            }
        }
    }
    return sum
}