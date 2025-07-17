func findMiddleIndex(nums []int) int {
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }

    leftSum := 0
    for idx, num := range nums {
        rightSum := totalSum - leftSum - num
        if leftSum ==  rightSum { 
            return idx 
        }
        leftSum += num
    }
    return -1
}