class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        if not isinstance(target, int):
            raise Exception(f"{target=} must be an Integer")

        if not isinstance(hours, List):
            raise Exception(f"{hours=} must be a Type: `List`")

        if not isinstance(hours, list):
            raise Exception(f"{hours=} must be a Type: `list`")

        return sum(num >= target for num in hours)
        