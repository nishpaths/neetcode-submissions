class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((timestamp,value))  

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0, len(self.time_dict[key])-1
        time_index = -1
        if key not in self.time_dict:
            return ""
        while l <= r:
            m = (l + r)//2
            if self.time_dict[key][m][0] <= timestamp:
                time_index = m
                l = m + 1
            else:
                r = m - 1
        if time_index == -1:
            return ""
        return self.time_dict[key][time_index][1]
            