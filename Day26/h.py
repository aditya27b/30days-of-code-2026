def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        if not root:
            return []
        res, q = [], [root]
        while q:
            level = []
            nxt = []
            for node in q:
                level.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            res.append(level)
            q = nxt
        return res