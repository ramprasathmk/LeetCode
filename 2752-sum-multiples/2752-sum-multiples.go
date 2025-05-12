func sumOfMultiples(n int) int {
    // multiple of 3, 5, 7
    a := n / 3
    b := n / 5
    c := n / 7
    // multiples of 3&5, 3&7, 5&7
    d := n / 15
    e := n / 21
    f := n / 35
    // multiples of 3, 5, & 7
    g := n / 105

    return (
        // add single multiples
        3*a*(a+1) +
        5*b*(b+1) +
        7*c*(c+1) -
        // subtract double multiples
        15*d*(d+1) -
        21*e*(e+1) -
        35*f*(f+1) +
        // add triple multiples
        105*g*(g+1)) / 2
}
