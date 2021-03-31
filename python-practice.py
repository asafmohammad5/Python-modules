spam = 0
while spam < 5:
  print('Hello, world.')
  spam = spam + 1


def greeting(name, saying="Hello"):
    print(saying, name)

def average(num1, num2):
    return (num1/num2)


print(average(6, 2))

quarters = ['First', 'Second', 'Third', 'Fourth']
print(enumerate(quarters))
print(enumerate(quarters, start=1))


def find_index(elements, value):
    index = bisect.bisect_left(elements, value)
    if index < len(elements) and elements[index] == value:
        return index

 public int sumOfUnique(int[] nums) {
        int[] cnt = new int[101];
        for (int n : nums) {
            ++cnt[n];
        }
        int sum = 0;
        for (int i = 1; i <= 100; ++i) {
            if (cnt[i] == 1) {
                sum += i;
            }
        }
        return sum;
    }

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for s in str:
            if ord('A') <= ord(s) <= ord('A')+25:
                res += chr(ord(s)-ord('A')+ord('a'))
            else:
                res += s
        return res

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        counter = 0
        
        for number in nums:
            
            if len( str(number) ) % 2 == 0:
                
                counter += 1
                
        return counter
    
class Solution:
    def reverseString(self, s: List[str]) -> None:
       
        size = len(s)

        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]
