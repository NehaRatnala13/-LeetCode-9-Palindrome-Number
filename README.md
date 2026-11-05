# -LeetCode-9-Palindrome-Number
Given an integer x, return true if x is a palindrome, and false otherwise. An integer is a palindrome when it reads the same backward as forward. For example, 121 is a palindrome while 123 is not.

Algorithm Explanation

1. Negative Number Check: Negative numbers automatically fail the palindrome test because the negative sign - at the front would end up at the back when reversed (e.g., -121 becomes 121-).
2. String Conversion: The integer x is converted into its string format s using Python's built-in str() function.
3. Slicing Comparison: The expression s[::-1] creates a completely reversed copy of the string s using Python's highly optimized slice step notation. If the original string matches the reversed string exactly, the integer is a palindrome, returning True; otherwise, it returns False.

Complexity Analysis

• Time Complexity: \(\mathcal{O}(n)\), where \(n\) is the number of digits in the integer \(x\). Converting the number to a string and reversing it both require walking through each digit once.
• Space Complexity: \(\mathcal{O}(n)\), because creating a string representation of the integer and storing its reversed copy requires memory proportional to the number of digits.
