
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        def testTrip(x, y, z) -> bool:
            if abs(x - y) <= a:
                if abs(y - z) <= b:
                    if abs(x - z) <= c:
                        return True
            return False

        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):  # ✅ Ensure i < j < k
                    if testTrip(arr[i], arr[j], arr[k]):
                        count += 1

        return count
