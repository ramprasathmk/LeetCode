func romanToInt(s string) int {
	romanNumerals := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	sum := 0
	prev := 0

	for i := len(s) - 1; i >= 0; i-- {
		curr := romanNumerals[rune(s[i])]
		if curr < prev {
			sum -= curr
		} else {
			sum += curr
		}
		prev = curr
	}

	return sum
}
