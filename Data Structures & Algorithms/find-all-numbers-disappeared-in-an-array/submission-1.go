func findDisappearedNumbers(nums []int) []int {
    n := len(nums)
    seen := make([]bool, n+1)   

    for _, num := range nums{
        seen[num] = true
    }

    var res []int
    for i:=1 ; i<=n ; i++{
        if !seen[i]{
            res = append(res,i)
        }
    }
    return res
}
