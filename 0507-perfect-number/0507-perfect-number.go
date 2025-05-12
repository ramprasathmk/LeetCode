func checkPerfectNumber(num int) bool {
    if num <=1 { return false }

    sum := 1
    sqrtNum := int(math.Sqrt(float64(num)))
    
    for i := 2; i <= sqrtNum; i++ {
        if num%i == 0 {
            sum += i
            if i != num/i {
                sum += num/i
            }
        }
    }

    return num == sum
}
