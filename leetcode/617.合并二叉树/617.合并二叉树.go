package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil {
		return root2
	}
	if root2 == nil {
		return root1
	}
	t3 := &TreeNode{root1.Val + root2.Val, nil, nil}
	t3.Left = mergeTrees(root1.Left, root2.Left)
	t3.Right = mergeTrees(root1.Right, root2.Right)
	return t3
}
