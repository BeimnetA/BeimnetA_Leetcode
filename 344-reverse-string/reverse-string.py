class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        # As we move the start pointer right and end pointer left, we swap the characters.
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

        # After loop finishes, the string is said to be reversed, hence convert the array into a string and return.
        return s
        