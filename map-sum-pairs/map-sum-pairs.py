class MapSum:
    dic = {}

    def __init__(self):
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key in self.dic.keys():
            if len(key) < len(prefix): continue
            flag = True
            for i in range(len(prefix)):
                if key[i] != prefix[i]:
                    flag = False
                    break
            if flag: res += self.dic.get(key)
        return res