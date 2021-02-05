class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        output = ""
        i = 0
        while(i<n):
            if command[i]=="G":
                output += "G"
                i += 1
                if i<n and command[i]=="(" :
                    if command[i+1]==")":
                        output += "o"
                        i += 2
                else :
                    output += "al"
                    i += 4
        return output