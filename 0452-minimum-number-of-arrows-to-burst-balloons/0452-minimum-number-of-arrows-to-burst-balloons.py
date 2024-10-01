class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: -x[1])
        shots = 0 
        while points:
            point = points.pop()
            target = point[1]
            while points and points[-1][0] <= target <= points[-1][1]: 
                points.pop()
            
            shots+=1
            
        
        return shots



            

            