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

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
     
        A = [0] * 46
        
        for i in range(lowLimit, highLimit + 1):
            cur = 0
            
      
            for x in str(i):
                cur += int(x)
                
            A[cur] += 1
        
        return max(A)

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        curr = 0
        for i in range(0, len(nums)-1, 2):
            curr += nums[i]
        return curr

 def canBeEqual(self, target, A):
        return sorted(target) == sorted(A)

    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        ans = []
        col = [[matrix[i][j] for i in range(n)] for j in range(m)]
        max_col = [max(col[i]) for i in range(m)]
        for i in range(n):
            minn = min(matrix[i])
            for j in range(m):
                if matrix[i][j] == minn and matrix[i][j] == max_col[j]:
                    ans.append(matrix[i][j])
        return ans

     def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        peak = 0
        
        while low <= high:
            mid = low + (high - low)/2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                peak = mid
                break
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
                
        return peak

     def maxProduct(self, nums):

        first, second = 0, 0
        for number in nums:
            if number > first:
                first, second = number, first       
            else:
                second = max( number, second)
        
        return (first - 1) * (second - 1)

def maximum69Number(self, num):
    return int(str(num).replace('6', '9', 1))

  def repeatedNTimes(self, A):
        while 1:
            s = random.sample(A, 2)
            if s[0] == s[1]:
                return s[0]

  def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        a = b = 0
        i, j = 0, len(s) - 1
        while i < j:
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1
            j -= 1
        return a == b

class Solution(object):
    def removeOuterParentheses(self, S):  
        count = 0 
        output_S = []
        for c in S:
            if c == ')':
                count -= 1
            
            if count > 0:
                output_S.append(c)
            
            if c == '(':
                count += 1
        
        return ''.join(output_S)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a, b = max(a, n), max(b, min(a, n))
        return (a-1) * (b-1)

def is_self_dividing(x):
    s = str(x)
    for d in s:
        if d=="0" or x%int(d)!=0:
            return False
    return True

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for x in xrange(left, right+1):
            if is_self_dividing(x):
                ans.append(x)
        return ans

def freqAlphabets(self, s: str) -> str:
	out = ""

	for i in range(len(s)):
		first, second, third = "","",""

		if i < len(s):
			first = s[i]
		if i+1 < len(s):
			second = s[i+1]
		if i+2 < len(s):
			third = s[i+2]

		if second != "#" and first != "#":
			if third == "#":
				out += chr(int(first+second)+96)
			else:
				out += chr(int(first)+96)

	return out 

class Solution(object):
   def sumZero(self, n):
    a = range(1, n)
    return a + [-sum(a)]

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = set()
        duplicates = set()
        
        for num in nums:
            if num in seen:
                duplicates.add(num)
            seen.add(num)
        
        return sum(seen.difference(duplicates))

class Solution(object):
    def replaceElements(self, arr):
    
        me,arr[-1] = arr[-1],-1
        
        for i in range(len(arr)-2,-1,-1):
            arr[i],me = me,max(me,arr[i])
            
        return arr

class Solution:
	def balanceBST(self, root: TreeNode) -> TreeNode:
		v = []
		def dfs(node):
			if node:
				dfs(node.left)
				v.append(node.val)
				dfs(node.right)
		dfs(root)

		def bst(v):
			if not v:
				return None
			mid = len(v) // 2
			root = TreeNode(v[mid])
			root.left = bst(v[:mid])
			root.right = bst(v[mid + 1:])
			return root

		return bst(v)

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
	
        self.rec = {}
		
        for i, row in enumerate(rectangle):
            self.rec[i] = row
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
	
        for i in range(row1, row2+1):
            self.rec[i] = self.rec[i][:col1] + [newValue]*(col2-col1+1) + self.rec[i][col2+1:]

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]
