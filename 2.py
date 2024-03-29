import random
import collections


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#!https://leetcode.com/problems/find-the-difference/


class Solution(object):
    def findTheDifference(self, s, t):
        if s == "":
            return t
        arr1 = list(s)
        arr2 = list(t)
        d1 = {}
        d2 = {}
        for i in arr1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in arr2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        for i in d1:
            if i in d2 and d2[i] == d1[i]:
                del d2[i]
            elif i in d2:
                d2[i] = d2[i]-d1[i]
        string = ""
        for i in d2:
            string += i*d2[i]
        return string

#!https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        arr = []
        for i in range(rowIndex+1):
            arr.append([1])
        arr[1].append(1)

        for i in range(2, rowIndex+1):
            for j in range(1, len(arr[i-1])):
                arr[i].append(arr[i-1][j-1]+arr[i-1][j])
            arr[i].append(1)
        return arr[rowIndex]

#!https://leetcode.com/problems/verifying-an-alien-dictionary/


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in words:
            d[i] = []
            for j in range(len(i)):
                arr = d[i]
                arr.append(order.index(i[j]))
                d[i] = arr
        res = d.values()
        tot = []
        for i in res:
            tot.append(i)
        messi = sorted(tot)
        if messi == tot:
            return True
        return False

#!https://leetcode.com/problems/add-strings/


class Solution(object):
    def addStrings(self, num1, num2):
        return str(int(num1)+int(num2))

#!https://leetcode.com/problems/add-to-array-form-of-integer/


class Solution(object):
    def addToArrayForm(self, num, k):
        ks = str(k)
        if len(ks) < len(num):
            while len(ks) != len(num):
                ks = "0"+ks
        numb = ""
        for i in num:
            numb += str(i)
        numb = int(numb)
        result = int(ks)+numb
        total = []
        for i in str(result):
            total.append(int(i))
        return total

#!https://leetcode.com/problems/add-binary/


class Solution(object):
    def addBinary(self, a, b):
        def getDecimal(binary):
            total = 0
            for i in range(len(binary)-1, -1, -1):
                if int(binary[i]) == 1:
                    total += pow(2, len(binary)-1-i)
            return total

        def makeBinary(x):
            string = ""
            for i in bin(x):
                string += i
            return string[2:]
        a = getDecimal(a)
        b = getDecimal(b)
        return makeBinary(a+b)

#!https://leetcode.com/problems/valid-palindrome/


class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        string = ""
        for i in s:
            if i in arr:
                string += i
        print(string)
        if string == string[::-1]:
            return True
        return False

#!https://leetcode.com/problems/guess-number-higher-or-lower/


class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n
        while True:
            m = (l+r)//2
            res = guess(m)
            if res == 1:
                l = m+1
            elif res == -1:
                r = m-1
            else:
                return m

#!https://leetcode.com/problems/shuffle-the-array/submissions/892524765/


class Solution(object):
    def shuffle(self, nums, n):
        arr1 = nums[:n][::-1]
        arr2 = nums[n:][::-1]
        res = []
        for i in range(n):
            res.append(arr1.pop())
            res.append(arr2.pop())
        return res

#!https://leetcode.com/problems/excel-sheet-column-title/


class Solution(object):
    dicty = {i: chr(65+i) for i in range(26)}

    def convertToTitle(self, columnNumber: int) -> str:
        i = 0
        while True:
            if columnNumber-26**i < 0:
                i -= 1
                break
            columnNumber -= 26**i
            i += 1
        res = ""
        for j in range(i, -1, -1):
            res = res+self.dicty[columnNumber//(26**j)]
            columnNumber -= 26**j*(columnNumber//(26**j))
        return res

#!https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = []
        coll = collections.Counter(s)
        for i in coll:
            arr.append([i, coll[i]])
        for i in arr:
            if i[1] == 1:
                return s.index(i[0])
        return -1

#!https://leetcode.com/problems/self-dividing-numbers/


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right+1):
            if '0' not in str(i):
                if len(str(i)) == 1:
                    arr.append(i)
                else:
                    for digit in str(i):
                        digit = int(digit)
                        if i % digit != 0:
                            break
                    if str(digit) == str(i)[len(str(i))-1] and i % digit == 0:
                        arr.append(i)
        return arr

#!https://leetcode.com/problems/valid-palindrome-ii/


class Solution(object):
    def validPalindrome(self, s):
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
        return True

    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

#!https://leetcode.com/problems/height-checker/


class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count

#!https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count

#!https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/


class Solution(object):
    def maximumCount(self, nums):
        n, p = 0, 0
        for i in nums:
            if i < 0:
                n += 1
            elif i > 0:
                p += 1
        return max(n, p)

#!https://leetcode.com/problems/student-attendance-record-i/


class Solution(object):
    def checkRecord(self, s):
        # Absent Check
        def absentCheck(arr):
            if arr.count('A') < 2:
                return True
            return False

        # Late Check
        def lateCheck(arr):
            for i in range(len(arr)-2):
                if arr[i] == 'L' and arr[i+1] == 'L' and arr[i+2] == 'L':
                    return False
            return True
        arr = list(s)
        if absentCheck(arr) and lateCheck(arr):
            return True
        return False

#!https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution(object):
    def countOdds(self, low, high):
        if low % 2 == 1 and high % 2 == 1:
            return (high-low)/2+1
        elif low % 2 == 0 and high % 2 == 0:
            return (high-low)/2
        else:
            return int(math.floor((high-low)/2)+1)

#!https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        if count == n:
            return head.next

        if count == 1:
            return ListNode("")
        if count <= n:
            return head
        if count == 2:
            if n == 2:
                return ListNode(head.next.val)
            if n == 1:
                return ListNode(head.val)
        if count == 3:
            if n == 1:
                node = ListNode(head.val)
                node.next = ListNode(head.next.val)
                return node
            if n == 2:
                node = ListNode(head.val)
                node.next = ListNode(head.next.next.val)
                return node
            if n == 3:
                node = ListNode(head.next.val)
                node.next = ListNode(head.next.next.val)
                return node
        index = count-n-1
        i = 0
        temp = head
        while temp.next:
            if i == index:
                temp.next = temp.next.next
                break
            temp = temp.next
            i += 1
        return head

#!https://leetcode.com/problems/maximum-subarray/


class Solution(object):
    def maxSubArray(self, nums):
        max_sum, cur_sum = -100000, 0
        for i in nums:
            cur_sum = max(cur_sum+i, i)
            max_sum = max(max_sum, cur_sum)
        return max_sum

#!https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution(object):
    def search(self, nums, target):

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

#!https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution(object):
    def searchRange(self, nums, target):
        r, l = len(nums)-1, 0
        arr = [-1, -1]
        while r >= l:
            print(l, r, nums[l], nums[r])
            if nums[l] == target:
                arr[0] = l
            if nums[r] == target:
                arr[1] = r
            if arr[1] == -1:
                r -= 1
            if arr[0] == -1:
                l += 1
            if arr[0] != -1 and arr[1] != -1:
                break
        return arr

#!https://leetcode.com/problems/reverse-linked-list-ii/


class Solution(object):
    def reverseBetween(self, head, left, right):
        left = left-1
        right = right-1
        if left == right:
            return head
        arr = []

        def helper(node):
            if not node:
                return
            arr.append(node.val)
            helper(node.next)
        helper(head)
        total = arr[:left]+arr[left:right+1][::-1]+arr[right+1:]
        total = total[::-1]
        node = ListNode()
        temp = node
        while len(total) > 0:
            temp.val = total.pop()
            if len(total) > 0:
                temp.next = ListNode()
                temp = temp.next
        return (node)

#!https://leetcode.com/problems/minimum-distance-between-bst-nodes/


class Solution(object):
    def minDiffInBST(self, root):
        arr = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            arr.append(node.val)
            helper(node.right)
        helper(root)
        m = 100000
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i]-arr[j]) < m:
                    m = abs(arr[i]-arr[j])
        return m

#!https://leetcode.com/problems/rotate-list/


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        if head == None:
            return ListNode('')

        def helper(head):
            if not head:
                return
            arr.append(head.val)
            helper(head.next)
        helper(head)
        k = k % len(arr)
        i = 0
        while i < k:
            arr = arr[len(arr)-1:]+arr[:len(arr)-1]
            i += 1
        arr = arr[::-1]
        node = ListNode()
        temp = node
        while len(arr) > 0:
            temp.val = arr.pop()
            if len(arr) > 0:
                temp.next = ListNode()
                temp = temp.next
        return (node)

#!https://leetcode.com/problems/reorder-list/


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []

        def helper(head):
            if not head:
                return
            arr.append(head.val)
            helper(head.next)
        helper(head)
        print(arr)
        l, r = 0, len(arr)-1
        res = []
        while r >= l:
            res.append(arr[l])
            res.append(arr[r])
            r -= 1
            l += 1
        if len(arr) % 2 == 1:
            res = res[:len(res)-1]
        print(res)
        res = res[::-1]
        temp = head
        while len(res) > 0:
            temp.val = res.pop()
            if len(res) > 0:
                temp.next = ListNode()
                temp = temp.next

#!https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        def helper(head):
            if not head:
                return
            arr.append(head.val)
            helper(head.next)
        helper(head)
        if len(arr) == 1:
            return ListNode("")
        midindex = math.floor(len(arr)/2)
        arr.pop(midindex)
        arr = arr[::-1]
        node = ListNode()
        temp = node
        while len(arr) > 0:
            temp.val = arr.pop()
            if len(arr) > 0:
                temp.next = ListNode()
                temp = temp.next
        return node

#!https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


class Solution(object):
    def deleteDuplicates(self, head):
        arr = []

        def helper(head):
            if not head:
                return
            arr.append(head.val)
            helper(head.next)
        helper(head)
        res = []
        for i in arr:
            if arr.count(i) == 1:
                res.append(i)
        if res == [0]:
            return ListNode(0)
        node = ListNode()
        temp = node
        res = res[::-1]
        while len(res) > 0:
            temp.val = res.pop()
            if len(res) > 0:
                temp.next = ListNode()
                temp = temp.next
        if node.val == 0 and not node.next and res == []:
            return ListNode('')
        return node

#!https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class Solution(object):
    def flatten(self, root):
        arr = []

        def linkedtoarr(root):
            if not root:
                return
            arr.append(root.val)
            linkedtoarr(root.left)
            linkedtoarr(root.right)
        linkedtoarr(root)
        arr = arr[::-1]
        node = root
        temp = node
        while len(arr) > 0:
            temp.val = arr.pop()
            if len(arr) > 0:
                temp.right = TreeNode()
                temp.left = None
                temp = temp.right

#!https://leetcode.com/problems/single-element-in-a-sorted-array/


class Solution(object):
    def singleNonDuplicate(self, nums):
        col = collections.Counter(nums)
        for i in col:
            if col[i] == 1:
                return i

#!https://leetcode.com/problems/reverse-string-ii/


class Solution(object):
    def reverseStr(self, s, k):
        i = 0
        string = ""
        while i < len(s):
            if i+k*2 > len(s) and len(s)-i > k:
                temp = s[i:i+k][::-1]+s[i+k:len(s)]
                string += temp
                i = len(s)
            else:
                temp = s[i:i+k][::-1]+s[i+k:i+k*2]
                string += temp
                i = i+2*k
        return string

#!https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution(object):
    def shipWithinDays(self, weights, days):
        def helper(weights, days, goal):
            j = 0
            for i in range(days):
                total = 0
                while True:
                    if j < len(weights) and total+weights[j] <= goal:
                        total += weights[j]
                        j += 1
                    else:
                        break
            if j == len(weights):
                return True
            return False
        i = max(weights)
        maxi = sum(weights)
        res = maxi
        while maxi >= i:
            mid = (i+maxi)//2
            if helper(weights, days, mid):
                res = min(mid, res)
                maxi = mid - 1
            else:
                i = mid + 1
        return res

#!https://leetcode.com/problems/partition-list/


class Solution(object):
    def partition(self, head, x):
        arr = []

        def helper(head):
            if not head:
                return
            arr.append(head.val)
            helper(head.next)
        helper(head)
        smaller = []
        bigger = []
        for i in arr:
            if i < x:
                smaller.append(i)
            else:
                bigger.append(i)
        res = smaller+bigger
        res = res[::-1]
        real = ListNode()
        node = real
        while len(res) > 0:
            node.val = res.pop()
            if len(res) > 0:
                node.next = ListNode()
                node = node.next
        if not real.next and real.val == 0:
            real.val = ""
            return real
        return real

#!https://leetcode.com/problems/sort-list/


class Solution(object):
    def sortList(self, head):
        temp = head
        array = []
        while temp != None:
            array.append(temp.val)
            temp = temp.next
        array.sort()
        array = array[::-1]
        node = ListNode()
        tmp = node
        while len(array) > 0:
            tmp.val = array.pop()
            if len(array) > 0:
                tmp.next = ListNode()
                tmp = tmp.next
        if not node.next and node.val == 0:
            return ListNode('')
        return node

#!https://leetcode.com/problems/design-hashset/


class MyHashSet(object):

    def __init__(self):
        self.arr = []

    def add(self, key):
        if key not in self.arr:
            self.arr.append(key)

    def remove(self, key):
        if key in self.arr:
            self.arr.remove(key)

    def contains(self, key):
        if key in self.arr:
            return True
        return False

#!https://leetcode.com/problems/min-stack/submissions/


class MinStack(object):

    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        self.arr.pop()

    def top(self):
        return self.arr[len(self.arr)-1]

    def getMin(self):
        return min(self.arr)

#!https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue(object):

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.insert(0, x)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[len(self.arr)-1]

    def empty(self):
        if len(self.arr) > 0:
            return False
        return True

#!https://leetcode.com/problems/implement-stack-using-queues/


class MyStack(object):
    array = []

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]

    def empty(self):
        return len(self.stack) == 0

#!https://leetcode.com/problems/ugly-number/


class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n = n // i

        return n == 1

#!https://leetcode.com/problems/reverse-nodes-in-k-group/


class Solution(object):
    def reverseKGroup(self, head, k):
        arr = []

        def helper(head):
            if not head:
                return
            arr.append(head.val)
            helper(head.next)
        helper(head)

        i = 0
        res = []
        while i + k <= len(arr):
            res += arr[i:i+k][::-1]
            i = i+k
        res += arr[i:]
        res = res[::-1]

        temp = ListNode()
        node = temp
        while len(res) > 0:
            node.val = res.pop()
            if len(res) > 0:
                node.next = ListNode()
                node = node.next
        return (temp)

#!https://leetcode.com/problems/sort-an-array/


class Solution(object):
    def sortArray(self, nums):
        return sorted(nums)

#!https://leetcode.com/problems/first-bad-version/


class Solution(object):
    def firstBadVersion(self, n):
        l, r = 0, n
        result = 0
        while l <= r:
            m = int((r+l)/2)
            if isBadVersion(m):
                result = m
                r = m - 1
            else:
                l = m + 1
        return result

#!https://leetcode.com/problems/range-sum-query-immutable/


class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])

#!https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


class Solution(object):
    def removeDuplicates(self, nums):
        same = True
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
        for i in arr:
            if nums.count(i) > 2:
                for j in range(nums.count(i) - 2):
                    nums.remove(i)
                    nums.append('_')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != '_':
                return i+1

#!https://leetcode.com/problems/search-in-rotated-sorted-array-ii/


class Solution(object):
    def search(self, nums, target):
        if target in nums:
            return True
        return False


#!https://leetcode.com/problems/duplicate-zeros/
class Solution(object):
    def duplicateZeros(self, arr):
        array = []
        for i in arr:
            array.append(i)
            if i == 0:
                array.append(0)
        print(array)
        for i in range(len(arr)):
            arr[i] = array[i]

#!https://leetcode.com/problems/crawler-log-folder/


class Solution(object):
    def minOperations(self, logs):
        stack = []
        for i in logs:
            if i == "../":
                if len(stack) > 0:
                    stack.pop()
            else:
                if i != "./":
                    stack.append(i)
        return len(stack)

#!https://leetcode.com/problems/kth-missing-positive-number/


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        num = 1
        while count != k:
            if num not in arr:
                count += 1
            num += 1
        return num-1

#!https://leetcode.com/problems/last-stone-weight/


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max(stones))
            max2 = max(stones)
            stones.remove(max(stones))
            if max1-max2 != 0:
                stones.append(abs(max1-max2))
        if len(stones) == 0:
            return 0
        return stones[0]

#!https://leetcode.com/problems/majority-element-ii/


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)/3
        arr = []
        dp = collections.Counter(nums)
        for i in dp:
            if dp[i] > size:
                arr.append(i)
        return arr

#!https://leetcode.com/problems/most-frequent-even-element/


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if i % 2 == 0:
                arr.append(i)
        if len(arr) == 0:
            return -1
        print(arr)
        maksi = 0
        maksi_res = 0
        dp = collections.Counter(arr)
        for i in dp:
            if dp[i] > maksi:
                maksi = dp[i]
                maksi_res = i
            elif dp[i] == maksi and i < maksi_res:
                maksi = dp[i]
                maksi_res = i
        return maksi_res


#!https://leetcode.com/problems/linked-list-random-node/


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.arr)-1)
        return self.arr[rand]

#!https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = []
        for i in magazine:
            arr.append(i)
        for i in ransomNote:
            if i not in arr:
                return False
            else:
                arr.remove(i)
        return True

#!https://leetcode.com/problems/baseball-game/


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in operations:
            if i == "C":
                arr.pop()
            elif i == "D":
                arr.append(arr[len(arr)-1]*2)
            elif i == "+":
                arr.append(sum(arr[len(arr)-2:len(arr)]))
            else:
                arr.append(int(i))
        return sum(arr)

#!https://leetcode.com/problems/binary-number-with-alternating-bits/


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def dtb(n):
            return bin(n).replace("0b", "")
        res = dtb(n)
        for i in range(len(res)-1):
            if res[i] == res[i+1]:
                return False
        return True

#!https://leetcode.com/problems/design-hashmap/


class MyHashMap:

    def __init__(self):
        self.dp = {}

    def put(self, key: int, value: int) -> None:
        self.dp[key] = value

    def get(self, key: int) -> int:
        if key in self.dp:
            return self.dp[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.dp:
            del self.dp[key]


#!https://leetcode.com/problems/design-linked-list/
class MyLinkedList:

    def __init__(self):
        self.arr = []

    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.arr.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.arr.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.arr):
            self.arr.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.arr):
            self.arr.pop(index)

#!https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution(object):
    def findMin(self, nums):
        return min(nums)

#!https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/


class Solution(object):
    def findMin(self, nums):
        return min(nums)

#!https://leetcode.com/problems/missing-number/


class Solution(object):
    def missingNumber(self, nums):
        arr = list(range(0, max(nums)+1))
        for i in nums:
            arr.remove(i)
        if len(arr) > 0:
            return arr[0]
        return max(nums)+1

#!https://leetcode.com/problems/find-pivot-index/


class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

#!https://leetcode.com/problems/is-subsequence/


class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        arr = list(s)[::-1]
        for i in t:
            print(arr)
            if i == arr[-1]:
                arr.pop()
            if len(arr) == 0:
                return True
        if len(arr) > 0:
            return False
        return True

#!https://leetcode.com/problems/implement-trie-prefix-tree/


class Trie(object):

    def __init__(self):
        self.arr = []

    def insert(self, word):
        self.arr.append(word)

    def search(self, word):
        if word in self.arr:
            return True
        return False

    def startsWith(self, prefix):
        for i in range(len(self.arr)):
            if (len(self.arr) > 0) and (prefix in self.arr[i]) and (self.arr[i].index(prefix) == 0):
                return True
        return False

#!https://leetcode.com/problems/sum-of-left-leaves/


class Solution(object):
    def sumOfLeftLeaves(self, root):
        arr = [0]

        def helper(node):
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                arr[0] += node.left.val
            helper(node.left)
            helper(node.right)
        helper(root)
        return arr[0]

#!https://leetcode.com/problems/robot-return-to-origin/


class Solution(object):
    def judgeCircle(self, moves):
        l, t = 0, 0
        for i in moves:
            if i == "U":
                t -= 1
            elif i == "D":
                t += 1
            elif i == "L":
                l -= 1
            else:
                l += 1
        if l == 0 and t == 0:
            return True
        return False

#!https://leetcode.com/problems/sort-array-by-parity/


class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd

#!https://leetcode.com/problems/merge-in-between-linked-lists/


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        # get list2s end
        list2end = list2
        while list2end.next:
            list2end = list2end.next
        temp = list1
        for i in range(a-1):
            temp = temp.next
        end = list1
        for i in range(b):
            end = end.next
        temp.next = list2
        list2end.next = end.next
        return list1

#!https://leetcode.com/problems/keyboard-row/


class Solution(object):
    def findWords(self, words):
        one = list("qwertyuiop")
        two = list("asdfghjkl")
        three = list("zxcvbnm")
        print(one, two, three)
        arr = []
        for a in words:
            i = a.lower()
            flag1 = True
            flag2 = True
            flag3 = True
            # check one
            for j in i:
                if j not in one:
                    flag1 = False
            # check two
            for j in i:
                if j not in two:
                    flag2 = False
            # check three
            for j in i:
                if j not in three:
                    flag3 = False
            print(i, flag1, flag2, flag3)
            if flag1 or flag2 or flag3:
                arr.append(a)
        return arr

#!https://leetcode.com/problems/divide-array-into-equal-pairs/


class Solution(object):
    def divideArray(self, nums):
        leng = len(nums)/2
        arr = []
        for x in range(10):
            for i in nums:
                if nums.count(i) == 1:
                    return False
                if nums.count(i) % 2 == 0:
                    for j in range(nums.count(i)):
                        nums.remove(i)
            if len(nums) == 0:
                return True
            elif len(nums) == 2 and nums[0] == nums[1]:
                return True

#!https://leetcode.com/problems/binary-search/


class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)
        while r >= l:
            mid = (r+l)//2
            if mid < len(nums):
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            else:
                return -1
        return -1

#!https://leetcode.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dp = {}
        for i, c in enumerate(s):
            dp[c] = i
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, dp[c])
            if i == end:
                res.append(size)
                size = 0
        return (res)

#!https://leetcode.com/problems/validate-stack-sequences/


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        i = 0
        stack = []
        for n in pushed:
            stack.append(n)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack

#!https://leetcode.com/problems/merge-strings-alternately/


class Solution(object):
    def mergeAlternately(self, word1, word2):
        ls1 = list(word1)[::-1]
        ls2 = list(word2)[::-1]
        string = ""
        while len(ls1) > 0 and len(ls2) > 0:
            string += ls1.pop()
            string += ls2.pop()
        print(string)
        if len(ls1) > 0:
            for i in ls1[::-1]:
                string += i
            return string
        if len(ls2) > 0:
            for i in ls2[::-1]:
                string += i
            return string
        return string

#!https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maksi = max(candies)
        arr = []
        for i in candies:
            if (i+extraCandies) >= maksi:
                arr.append(True)
            else:
                arr.append(False)
        return arr

#!https://leetcode.com/problems/removing-stars-from-a-string/


class Solution(object):
    def removeStars(self, s):
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

#!https://leetcode.com/problems/sum-of-digits-of-string-after-convert/


class Solution(object):
    def getLucky(self, s, k):
        def addDigits(string):
            res = 0
            for i in string:
                res += int(i)
            return res
        res = ""
        for i in s.lower():
            res += str(ord(i)-96)
        print(res)
        for i in range(k):
            res = addDigits(str(res))

        return int(res)

#!https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/


class Solution:
    def average(self, salary: List[int]) -> float:
        mini = min(salary)
        maksi = max(salary)
        while mini in salary:
            salary.remove(mini)
        while maksi in salary:
            salary.remove(maksi)

        return sum(salary)/len(salary)

#!https://leetcode.com/problems/number-of-unequal-triplets-in-array/


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        dp = collections.Counter(nums)
        if len(dp) < 3:
            return 0
        elif len(dp) == 3:
            i = 1
            for j in dp:
                i *= dp[j]
            return i
        else:
            count = 0
            for i in range(len(nums)-2):
                for j in range(i+1, len(nums)-1):
                    for k in range(j+1, len(nums)):
                        if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                            count += 1
            return count

#!https://leetcode.com/problems/sign-of-the-product-of-an-array/


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 1
        for i in nums:
            x *= i
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1

#!https://leetcode.com/problems/find-the-difference-of-two-arrays/


class Solution(object):
    def findDifference(self, nums1, nums2):
        arr1 = []
        arr2 = []
        for i in nums1:
            if i not in nums2 and i not in arr1:
                arr1.append(i)
        for i in nums2:
            if i not in nums1 and i not in arr2:
                arr2.append(i)
        return [arr1, arr2]

#!https://leetcode.com/problems/intersection-of-multiple-arrays/


class Solution(object):
    def intersection(self, nums):
        arr = nums[0]
        arr1 = []
        for i in arr:
            for j in range(1, len(nums)):
                if i not in nums[j]:
                    arr1.append(i)
        for i in arr1:
            if i in arr:
                arr.remove(i)
        return sorted(arr)

#!https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


class Solution(object):
    def kWeakestRows(self, mat, k):
        arr = []
        matto = [i for i in mat]
        while len(arr) < k:
            mini = 1000
            ind = -1
            for i in range(len(mat)):
                if mat[i].count(1) < mini:
                    mini = mat[i].count(1)
                    ind = i
            indekso = matto.index(mat[ind])
            if indekso in arr:
                while indekso in arr:
                    indekso = matto.index(mat[ind], indekso+1)
            else:
                indekso = matto.index(mat[ind])
            mat.pop(ind)
            arr.append(indekso)
        return (arr)

#!https://leetcode.com/problems/check-if-n-and-its-double-exist/


class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(arr[i]*2) != i:
                return True
        return False

#!https://leetcode.com/problems/keep-multiplying-found-values-by-two/


class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original *= 2
        return original

#!https://leetcode.com/problems/largest-number-at-least-twice-of-others/


class Solution(object):
    def dominantIndex(self, nums):
        for a in range(len(nums)):
            arr = [nums[i]*2 if i != a else nums[i] for i in range(len(nums))]
            if nums[a] == max(arr):
                return a
        return -1

#!https://leetcode.com/problems/shortest-completing-word/


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        arr = []
        licensePlate = licensePlate.lower()
        licensePlate = licensePlate.replace(" ", "")

        for i in licensePlate:
            if not i.isdigit():
                arr.append(i)
        arr2 = []
        for i in arr:
            if i not in arr2:
                arr2.append(i)
        res = []
        for i in words:
            for j in arr2:
                if j in i and i.count(j) >= arr.count(j):
                    if j == arr2[-1]:
                        res.append(i)
                else:
                    break
        piyon = res[0]
        for i in res:
            if len(i) < len(piyon):
                piyon = i
        return piyon

#!https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


class Solution(object):
    def minSteps(self, s, t):
        sa = collections.Counter(s)
        ta = collections.Counter(t)
        res = (sa-ta)
        total = 0
        for i in res:
            total += res[i]
        return total

#!https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/


class Solution(object):
    def largestInteger(self, num):
        num = list(str(num))
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                ii = int(num[i])
                jj = int(num[j])
                if ii % 2 == 0 and jj % 2 == 0 and jj > ii:
                    num[i], num[j] = num[j], num[i]
                elif ii % 2 == 1 and jj % 2 == 1 and jj > ii:
                    num[i], num[j] = num[j], num[i]
        return int("".join(num))

#!https://leetcode.com/problems/sort-array-by-parity-ii/


class Solution(object):
    def sortArrayByParityII(self, nums):
        evens = []
        odds = []
        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        arr = []
        odds = odds[::-1]
        evens = evens[::-1]
        for i in range(len(nums)):
            if i % 2 == 0:
                arr.append(evens.pop())
            else:
                arr.append(odds.pop())
        return arr

#!https://leetcode.com/problems/sort-even-and-odd-indices-independently/


class Solution(object):
    def sortEvenOdd(self, nums):
        evens = []
        odds = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        odds = sorted(odds)[::-1]
        evens = sorted(evens)
        odds = odds[::-1]
        evens = evens[::-1]
        arr = []
        for i in range(len(nums)):
            if i % 2 == 0:
                arr.append(evens.pop())
            else:
                arr.append(odds.pop())
        return arr

#!https://leetcode.com/problems/minimum-absolute-difference-in-bst/


class Solution(object):
    def getMinimumDifference(self, root):
        arr = []

        def helper(node):
            if not node:
                return
            arr.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        arr = sorted(arr)
        mini = 1000000000000000
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j]-arr[i] < mini:
                    mini = arr[j]-arr[i]
        return mini


class Solution(object):
    def pairSum(self, head):
        arr = []

        def helper(node):
            if not node:
                return
            arr.append(node.val)
            helper(node.next)
        helper(head)
        maksi = 0
        for i in range(len(arr)-1, (len(arr)/2)-1, -1):
            if arr[len(arr)-1-i]+arr[i] > maksi:
                maksi = arr[len(arr)-1-i]+arr[i]
        return maksi


class Solution(object):
    def hammingDistance(self, x, y):
        str1 = ""
        str2 = ""

        while x > 0:
            str1 += str(x % 2)
            x /= 2

        while y > 0:
            str2 += str(y % 2)
            y /= 2

        str1 = str1[::-1]
        str2 = str2[::-1]

        if len(str1) > len(str2):
            while len(str2) < len(str1):
                str2 = "0"+str2
        else:
            while len(str1) < len(str2):
                str1 = "0"+str1
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count

#!https://leetcode.com/problems/kth-largest-element-in-a-stream/


class KthLargest(object):

    def __init__(self, k, nums):
        self.arr = nums
        self.k = k

    def add(self, val):
        self.arr.append(val)
        self.arr = sorted(self.arr)
        return self.arr[len(self.arr)-self.k]

#!https://leetcode.com/problems/monotonic-array/


class Solution(object):
    def isMonotonic(self, nums):
        if sorted(nums) == nums or sorted(nums) == nums[::-1]:
            return True
        return False


#!https://leetcode.com/problems/range-sum-of-bst/
class Solution(object):
    def rangeSumBST(self, root, low, high):
        arr = []

        def helper(node):
            if not node:
                return
            arr.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(root)
        print(arr)
        array = [i for i in arr if low <= i <= high]
        return sum(array)

#!https://leetcode.com/problems/next-greater-element-i/


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        arr = []
        for i in nums1:
            indeks = nums2.index(i)
            arr2 = nums2[indeks+1:]
            if len(arr2) > 0 and max(arr2) > i:
                for j in arr2:
                    if j > i:
                        arr.append(j)
                        break
            else:
                arr.append(-1)
        return arr

#!https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution(object):
    def findDisappearedNumbers(self, nums):
        arr = list(collections.Counter(nums).keys())
        arr1 = list(range(1, len(nums)+1))
        res = []
        return set(arr1) - set(arr)

#!https://leetcode.com/problems/design-parking-system/


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = []
        self.medium = []
        self.small = []
        self.bign = big
        self.mediumn = medium
        self.smalln = small

    def addCar(self, carType):
        if carType == 1:
            if len(self.big) < self.bign:
                self.big.append(1)
                return True
            return False
        elif carType == 2:
            if len(self.medium) < self.mediumn:
                self.medium.append(1)
                return True
            return False
        elif carType == 3:
            if len(self.small) < self.smalln:
                self.small.append(1)
                return True
            return False

#!https://leetcode.com/problems/max-consecutive-ones/


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums)-1:
                    arr.append(count)
            else:
                arr.append(count)
                count = 0
        return max(arr)


#!https://leetcode.com/problems/construct-the-rectangle/
class Solution(object):
    def constructRectangle(self, area):
        if area == 1:
            return [1, 1]
        n = area
        result = []
        for i in range(1, n//2 + 1):
            if n % i == 0:
                result.append([i, n/i])
        return result[len(result)//2][::-1]

#!https://leetcode.com/problems/number-complement/


class Solution(object):
    def findComplement(self, num):
        string = ""
        for i in str(bin(num)[2:]):
            if i == '0':
                string += '1'
            else:
                string += '0'
        return int(string, 2)

#!https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/


class Solution(object):
    def numSteps(self, s):
        s = int(s, 2)
        count = 0
        while s != 1:
            if s % 2 == 0:
                s /= 2
            else:
                s += 1
            count += 1
        return count

#!https://leetcode.com/problems/find-mode-in-binary-search-tree/


class Solution(object):
    def findMode(self, root):
        arr = []

        def helper(node):
            if not node:
                return
            arr.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(root)

        def most_frequent(List):
            counter = 0
            num = List[0]

            for i in List:
                curr_frequency = List.count(i)
                if(curr_frequency > counter):
                    counter = curr_frequency
                    num = i

            return num
        most = most_frequent(arr)
        res = []
        for i in arr:
            if arr.count(i) == arr.count(most) and i not in res:
                res.append(i)
        return res

#!https://leetcode.com/problems/relative-ranks/


class Solution(object):
    def findRelativeRanks(self, score):
        arr = sorted(score)[::-1]
        res = []
        for i in range(len(arr)):
            if i == 0:
                res.append(["Gold Medal", arr[i]])
            elif i == 1:
                res.append(["Silver Medal", arr[i]])
            elif i == 2:
                res.append(["Bronze Medal", arr[i]])
            else:
                res.append([str(i+1), arr[i]])
        output = len(score)*[0]
        for i in res:
            index = score.index(i[1])
            output[index] = i[0]
        return output

#!https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/


class Solution(object):
    def countPrimeSetBits(self, left, right):
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True
        count = 0
        for i in range(left, right+1):
            bitli = bin(i)
            num = bitli[2:].count('1')
            if is_prime(num):
                count += 1
        return count

#!https://leetcode.com/problems/maximum-depth-of-n-ary-tree/


class Solution(object):
    def maxDepth(self, root):
        arr = []

        def helper(node, depth=0):
            if not node:
                return depth
            arr.append(depth)
            for i in node.children:
                helper(i, depth+1)
        helper(root)
        if len(arr) > 0:
            return max(arr)+1
        return 0

#!https://leetcode.com/problems/flipping-an-image/


class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                image[i][j] = 0 if image[i][j] == 1 else 1
        return image

#!https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution(object):
    def findNumbers(self, nums):
        c = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                c += 1
        return c

#!https://leetcode.com/problems/array-partition/


class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        total = 0
        for i in range(len(nums)/2):
            total += min(nums.pop(), nums.pop())
        return total

#!https://leetcode.com/problems/minimum-index-sum-of-two-lists/


class Solution(object):
    def findRestaurant(self, list1, list2):
        arr = []
        for i in range(len(list1)):
            if list1[i] in list2:
                arr.append([list1[i], i+list2.index(list1[i])])
        arr.sort(key=lambda x: x[1])
        print(arr)
        if len(arr) == 1:
            return [arr[0][0]]
        else:
            res = []
            for i in range(len(arr)-1):
                res.append(arr[i][0])
                if arr[i][1] != arr[i+1][1]:
                    break
            if arr[-1][1] == arr[0][1]:
                res.append(arr[-1][0])
            return res

#!https://leetcode.com/problems/shortest-distance-to-a-character/


class Solution(object):
    def shortestToChar(self, s, c):
        arr = []
        for i in range(len(s)):
            if s[i] == c:
                arr.append(0)
            else:
                left = 100000
                right = 100000
                if i != len(s):
                    try:
                        right = s.index(c, i, len(s))-i
                    except:
                        pass
                if i != 0:
                    try:
                        left = i-s.rindex(c, 0, i)
                    except:
                        pass
                arr.append(min(right, left))
        return arr

#!https://leetcode.com/problems/buddy-strings/


class Solution(object):
    def buddyStrings(self, s, goal):
        def harfFarki(s, goal):
            count = 0
            for i in range(len(min(s, goal))):
                if s[i] != goal[i]:
                    count += 1
            return count
        gol = collections.Counter(goal)
        sol = collections.Counter(s)
        if harfFarki(s, goal) == 0 and s == goal and len(sol.keys()) == len(s):
            return False
        if sol == gol and harfFarki(s, goal) <= 2:
            return True
        return False

#!https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution(object):
    def areAlmostEqual(self, s, goal):
        def harfFarki(s, goal):
            count = 0
            for i in range(len(min(s, goal))):
                if s[i] != goal[i]:
                    count += 1
            return count
        gol = collections.Counter(goal)
        sol = collections.Counter(s)
        if sol == gol and harfFarki(s, goal) <= 2:
            return True
        return False


#!https://leetcode.com/problems/backspace-string-compare/
class Solution(object):
    def backspaceCompare(self, s, t):
        stack1 = []
        stack2 = []
        for i in s:
            if i != "#":
                stack1.append(i)
            else:
                if len(stack1) > 0:
                    stack1.pop()

        for i in t:
            if i != "#":
                stack2.append(i)
            else:
                if len(stack2) > 0:
                    stack2.pop()

        return stack1 == stack2

#!https://leetcode.com/problems/decode-the-message/


class Solution(object):
    def decodeMessage(self, key, message):
        arr = []
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in key:
            if i not in arr and i != " ":
                arr.append(i)
        string = ""
        for i in message:
            if i == " ":
                string += " "
            else:
                string += alphabet[arr.index(i)]
        return string

#!https://leetcode.com/problems/mean-of-array-after-removing-some-elements/


class Solution(object):
    def trimMean(self, arr):
        number = int(0.05*len(arr))
        for i in range(number):
            arr.remove(max(arr))
            arr.remove(min(arr))

        return sum(arr)/float(len(arr))

#!https://leetcode.com/problems/relative-sort-array/


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr = []
        for i in arr2:
            while i in arr1:
                arr1.remove(i)
                arr.append(i)
        arr += sorted(arr1)
        return arr

#!https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/


class Solution(object):
    def findSpecialInteger(self, arr):
        x = float(len(arr)/4)
        for i in arr:
            if arr.count(i) > x:
                return i

#!https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/


class Solution(object):
    def countKDifference(self, nums, k):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    count += 1
        return count

#!https://leetcode.com/problems/defanging-an-ip-address/


class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")

#!https://leetcode.com/problems/transpose-matrix/


class Solution(object):
    def transpose(self, matrix):
        m, n = len(matrix), len(matrix[0])
        arr = [[0] * m for i in range(n)]
        print(arr)
        for i in range(m):
            for j in range(n):
                arr[j][i] = matrix[i][j]
        return arr

#!https://leetcode.com/problems/maximum-average-subarray-i/


class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[0: k])
        ma = s
        for i in range(0, len(nums) - k):
            s = s + nums[i + k] - nums[i]
            ma = max(ma, s)
        return ma / float(k)

#!https://leetcode.com/problems/single-number-ii/


class Solution(object):
    def singleNumber(self, nums):
        pd = collections.Counter(nums)
        for i in pd.keys():
            if pd[i] == 1:
                return i

#!https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = []
        if nums.count(0) == len(nums):
            return 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        if nums.count(1) == len(nums):
            return len(nums) - 1
        arr = []
        for i in zeros:
            zersos = nums.copy()
            zersos.pop(i)
            arr.append(zersos)
        longest = 0
        for i in arr:
            string = ""
            for j in i:
                string += str(j)
            arro = string.split("0")
            for a in arro:
                if len(a) > longest:
                    longest = len(a)
        return longest

#!https://leetcode.com/problems/search-in-a-binary-search-tree/


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node != None:
            if val == node.val:
                return node
            if val > node.val:
                node = node.right
            else:
                node = node.left

#!https://leetcode.com/problems/add-two-numbers-ii/


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def generate(l1):
            string = ""
            while l1 != None:
                string += str(l1.val)
                l1 = l1.next
            return string
        arr = []
        for i in str(int(generate(l1))+int(generate(l2))):
            arr.append(i)
        arr = arr[::-1]
        root = ListNode()
        node = root
        while len(arr) > 0:
            node.val = arr.pop()
            if len(arr) > 0:
                node.next = ListNode()
                node = node.next
        return root

#!https://leetcode.com/problems/valid-mountain-array/


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        fall = False
        if len(arr) <= 2:
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if fall and arr[i] <= arr[i+1]:
                return False
            if arr[i] > arr[i+1]:
                fall = True
            if i == 0 and fall:
                return False
        return fall

#!https://leetcode.com/problems/di-string-match/


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        per = []
        lower = 0
        upper = len(s)
        for i in s:
            if i == 'I':
                per.append(lower)
                lower += 1
            else:
                per.append(upper)
                upper -= 1
        if s[len(s)-1] == 'I':
            per.append(upper)
        else:
            per.append(lower)
        return per

#!https://leetcode.com/problems/rotate-string/submissions/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def shift(word):
            return word[-1]+word[:len(word)-1]
        word = s
        for i in range(len(s)):
            word = shift(word)
            if word == goal:
                return True
        return False

#!https://leetcode.com/problems/find-the-k-beauty-of-a-number/


class Solution(object):
    def divisorSubstrings(self, num, k):
        string = str(num)
        count = 0
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                if j-i == k and int(string[i:j]) != 0 and num % int(string[i:j]) == 0:
                    count += 1
        return count

#!https://leetcode.com/problems/most-common-word/


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(",", " ").replace("!", " ").replace(
            ".", " ").replace(";", " ").replace("?", " ").replace("?", " ").replace("'", " ")
        arr = paragraph.split()
        counter = collections.Counter(arr)
        arr = []
        for i in counter:
            arr.append([i, counter[i]])
        arr = sorted(arr, key=lambda x: x[1], reverse=True)
        print(arr)
        for i in arr:
            if i[0] not in banned:
                return i[0]

#!https://leetcode.com/problems/n-ary-tree-preorder-traversal/


class Solution(object):
    def preorder(self, root):
        if root == None:
            return []
        arr = [root.val]

        def helper(node):
            if node.children:
                for i in node.children:
                    arr.append(i.val)
                    helper(i)
        helper(root)
        return arr

#!https://leetcode.com/problems/n-ary-tree-postorder-traversal/


class Solution(object):
    def postorder(self, root):
        if root == None:
            return []
        arr = []

        def helper(node):
            if node.children:
                for i in node.children:
                    helper(i)
                    arr.append(i.val)
        helper(root)
        arr.append(root.val)
        return arr

#!https://leetcode.com/problems/complement-of-base-10-integer/


class Solution(object):
    def bitwiseComplement(self, n):
        n = str(bin(n)[2:]).replace('1', '2')
        n = n.replace('0', '1')
        n = n.replace('2', '0')
        print(n)
        total = 0
        for i in range(len(n)):
            total += int(n[len(n)-i-1]) * pow(2, i)
        return total

#!https://leetcode.com/problems/sum-of-all-subset-xor-totals/submissions/


class Solution(object):
    def subsetXORSum(self, nums):
        arr = []
        for n in range(len(nums) + 1):
            arr += list(combinations(nums, n))
        total = 0
        for i in arr:
            x = 0
            for j in i:
                x ^= j
            total += x
        return total

#!https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(len(nums)):
            arr.append(len(filter(lambda score: score < nums[i], nums)))
        return arr

#!https://leetcode.com/problems/univalued-binary-tree/


class Solution(object):
    def isUnivalTree(self, root):
        arr = []

        def helper(node):
            if not node:
                return
            arr.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(root)
        if arr.count(arr[0]) == len(arr):
            return True
        return False

#!https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


class Solution(object):
    def repeatedNTimes(self, nums):
        for i in collections.Counter(nums).keys():
            if nums.count(i) == len(nums)/2:
                return i

#!https://leetcode.com/problems/unique-number-of-occurrences/


class Solution(object):
    def uniqueOccurrences(self, arr):
        res = []
        for i in collections.Counter(arr).keys():
            print(res)
            if arr.count(i) in res:
                return False
            res.append(arr.count(i))
        return True


#!https://leetcode.com/problems/rank-transform-of-an-array/

class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_list = sorted(list(set(arr)))
        x = 1
        temp = {}
        for i in sorted_list:
            temp[i] = x
            x += 1
        for i in range(len(arr)):
            arr[i] = temp[arr[i]]
        return arr

#!https://leetcode.com/problems/day-of-the-year/


class Solution(object):
    def dayOfYear(self, date):
        date = date.split("-")
        dp = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 30}
        y = int(date[0])
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)):
            dp[2] = 29

        def addMonthDays(month):
            total = 0
            for i in range(1, month):
                total += dp[i]
            return total

        return (addMonthDays(int(date[1]))+int(date[2]))

#!https://leetcode.com/problems/three-consecutive-odds/


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        def three(arr):
            if arr[0] % 2 == 1 and arr[1] % 2 == 1 and arr[2] % 2 == 1:
                return True
            return False
        if len(arr) == 3:
            return three(arr)
        for i in range(len(arr)-2):
            if three(arr[i:i+3]):
                return True
        return False

#!https://leetcode.com/problems/lemonade-change/


class Solution(object):
    def lemonadeChange(self, bills):
        stack = []
        for i in bills:
            if i == 10:
                if stack.count(5) >= 1:
                    stack.remove(5)
                else:
                    return False
            elif i == 20:
                if stack.count(10) >= 1 and stack.count(5) >= 1:
                    stack.remove(10)
                    stack.remove(5)
                elif stack.count(5) >= 3:
                    stack.remove(5)
                    stack.remove(5)
                    stack.remove(5)
                else:
                    return False
            stack.append(i)
        return True

#!https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/


class Solution(object):
    def greatestLetter(self, s):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        collect = collections.Counter(s.lower())
        a = collect.keys()
        arr = []
        for i in a:
            if i in s and i.upper() in s:
                arr.append([i, alphabet.index(i)])
        arr = sorted(arr, key=lambda x: x[1], reverse=True)
        if len(arr) > 0:
            return arr[0][0].upper()
        else:
            return ""

#!https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/


class Solution(object):
    def freqAlphabets(self, s):
        dp = {'a': '1', 'b': '2', 'c': '3', 'd': '4',
              'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9'}
        dp1 = {'j': '10#', 'k': '11#', 'l': '12#', 'm': '13#', 'n': '14#', 'o': '15#', 'p': '16#', 'q': '17#',
               'r': '18#', 's': '19#', 't': '20#', 'u': '21#', 'v': '22#', 'w': '23#', 'x': '24#', 'y': '25#', 'z': '26#'}
        for i in dp1:
            if dp1[i] in s:
                s = s.replace(dp1[i], i)
        for i in dp:
            if dp[i] in s:
                s = s.replace(dp[i], i)
        return s

# ?------------------
