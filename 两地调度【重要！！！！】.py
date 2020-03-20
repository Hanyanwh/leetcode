# 公司计划面试2N人。第i人飞往A市的费用为costs[i][0]，飞往B市的费用为costs[i][1]。
# 返回将每个人都飞到某座城市的最低费用，要求每个城市都有N人抵达。
#


class Solution:
    """

    
    """
    def twoCitySchedCost(self, costs) -> int:
        mid_valu = costs
        result = 0
        mid_valu.sort(key=lambda x: x[0] - x[1])
        mid = len(mid_valu) // 2
        for i in range(mid):
            result += costs[i][0] + costs[i+mid][1]
        return result
