from collections import Counter

def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_chars = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
            
        return "".join(result)