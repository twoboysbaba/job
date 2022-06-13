#4.重建二叉树
#输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

#思路：先序遍历和中序遍历的关系，先序遍历的第一个值是根节点的值。在中序遍历中，根节点左边的值是左子树，右边的值是右子树上的值。
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def reConstructBinaryTree(pre, tin):
    if not pre:
        return None
    root = TreeNode(pre[0])
    n = tin.index(root.val)
    root.left = reConstructBinaryTree(pre[1:n+1],tin[:n])
    root.right = reConstructBinaryTree(pre[n+1:],tin[n+1:])
    return root

pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]


root = reConstructBinaryTree(pre, tin)

def printTree(root):
    if root == None:
        return
    print(root.val)
    #if root.left != None:
    printTree(root.left)
    #if root.right!= None:
    printTree(root.right)
printTree(root)