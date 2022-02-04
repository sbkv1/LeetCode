class Solution:
    def generateTrees(self, n: int, offset=0) -> List[TreeNode]:
        return [TreeNode(offset+i, l, r) for i in range(1,n+1) for l in self.generateTrees(i-1, offset) for r in self.generateTrees(n-i, offset+i)] or [None]