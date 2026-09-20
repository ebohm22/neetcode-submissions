class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        if len(strs) == 0: return "Empty"
        final = ""
        for string in strs:
            cur = string
            for i in range(len(cur)):
                asci = ord(string[i])
                final = final + (str(asci) + "-")
         #   final = final[:-1]
            final += ":"
        final = final[:-1]
        return final
    def decode(self, s: str) -> List[str]:
        if s == "Empty": return []
        asciis = s.split(":")
      #  if asciis == [""]: return asciis
        print(asciis)
        final = []
        for string in asciis:
            code = string.split("-")
            f_string = ""
            for val in code:
                if val == "": 
                    f_string+= ""
                    break
                int_val = int(val)
                f_string+=chr(int_val)

            final.append(f_string)

        return final 
            
            


