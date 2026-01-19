from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 존재하지 않는 키에 대해 빈 리스트를 기본값으로 가지는 딕셔너리
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 알파벳 a-z (26개)의 빈도를 저장할 리스트
            count = [0] * 26 
            for char in s:
                # ord()를 이용해 인덱스 계산 (a=0, b=1, ...)
                count[ord(char) - ord('a')] += 1
            
            # 리스트는 딕셔너리의 키가 될 수 없으므로 튜플(tuple)로 변환
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())