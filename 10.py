class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = ""
        for i in range(len(address)):
            if address[i]==".":
                answer +="[.]"
            else:
                answer += address[i]
        return answer