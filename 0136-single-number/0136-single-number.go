func singleNumber(nums []int) int {
    numMap := make(map[int]int)

    for _, val := range nums {
        numMap[val]++
    }

    for k, num := range numMap {
        if num == 1 {
            return k
        }
    }
    return -1
}