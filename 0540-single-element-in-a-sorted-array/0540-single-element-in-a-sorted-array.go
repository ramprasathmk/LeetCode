func singleNonDuplicate(nums []int) int {
    var nothing int = -1

    filterMap := make(map[int]int)
    for _, num := range nums {
        filterMap[num]++
    }

    for index, count := range filterMap {
        if count == 1 {
            return index
        }
    }
    return nothing
}