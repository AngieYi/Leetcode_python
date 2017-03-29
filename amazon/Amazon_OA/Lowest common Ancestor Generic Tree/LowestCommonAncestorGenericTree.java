import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

//https://www.compilejava.net/
//http://wiki.jikexueyuan.com/project/for-offer/question-fifty.html

public class Test50 {
	
   
    // Tree Definition
    private static class TreeNode {
		
		int val;
        
		List<TreeNode> children = new LinkedList<>();
        
		public TreeNode() {
        }
        
		public TreeNode(int val) {
            this.val = val;
        }
        
		@Override
        public String toString() {
            return val + "";
        }
		
    }
	
	
	// find node path
    public static boolean getNodePath(TreeNode root, TreeNode target, List<TreeNode> path) {
        if (root == null) {
            return false;
        }
      
        path.add(root); // add current node
		
        List<TreeNode> children = root.children; // children of current node

        for (TreeNode node : children) {
            if (node == target) {
                path.add(node);
                return true;
            } else {
                 if(!getNodePath(node, target, path)){
					 return false;
				 }
            }
        }
      
        path.remove(path.size() - 1); // if node has no child, this node should be removed
		System.out.println("after remove:"+path);
		return false;
    }
	
	
  // find common node of two paths
    public static TreeNode getLastCommonNode(List<TreeNode> p1, List<TreeNode> p2) {
        Iterator<TreeNode> ite1 = p1.iterator();
        Iterator<TreeNode> ite2 = p2.iterator();
		
        TreeNode last = null;
        while (ite1.hasNext() && ite2.hasNext()) {
            TreeNode tmp = ite1.next();
            if (tmp == ite2.next()) {
                last = tmp;
            }
        }
        return last;
    }
	

  // find last common ancestor
    public static TreeNode getLastCommonParent(TreeNode root, TreeNode p1, TreeNode p2) {
        // any one is not in the company, return null
		if (root == null || p1 == null || p2 == null) { 
            return null;
        }
		
        List<TreeNode> path1 = new LinkedList<>();
        getNodePath(root, p1, path1);
      
		System.out.println("p1="+p1);
		System.out.println("path1="+path1);
		
        List<TreeNode> path2 = new LinkedList<>();
        getNodePath(root, p2, path2);
      
		System.out.println("p2="+p2);
		System.out.println("path2="+path2);
		
		TreeNode comNode = getLastCommonNode(path1, path2);
		
		// if common manager is ceo, return null
		if (comNode == root){ 
			return null;
		}
		else{
			return comNode;
		}
    }
	
	
    public static void main(String[] args) {
		test01();
        System.out.println("==========");
        //test02();
        System.out.println("==========");
        //test03();
    }
	
    // common tree
    //             1
    //           /   \
    //          2      3
    //        /   \
    //      4       5
    //     / \   /  |  \
    //    6   7 8   9  10
    public static void test01() {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        TreeNode n3 = new TreeNode(3);
        TreeNode n4 = new TreeNode(4);
        TreeNode n5 = new TreeNode(5);
        TreeNode n6 = new TreeNode(6);
        TreeNode n7 = new TreeNode(7);
        TreeNode n8 = new TreeNode(8);
        TreeNode n9 = new TreeNode(9);
        TreeNode n10 = new TreeNode(10);
        n1.children.add(n2);
        n1.children.add(n3);
        n2.children.add(n4);
		n2.children.add(n5);
        n4.children.add(n6);
        n4.children.add(n7);
        //n3.children.add(n5);
        n5.children.add(n8);
        n5.children.add(n9);
        n5.children.add(n10);
		
		List<TreeNode> path= new LinkedList<>();
        getNodePath(n1, n6, path);

        //System.out.println(getLastCommonParent(n1, n6, n8));  // should be null
    }
	
	
    //               1
    //              /
    //             2
    //            /
    //           3
    //          /
    //         4
    //        /
    //       5
    private static void test02() {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        TreeNode n3 = new TreeNode(3);
        TreeNode n4 = new TreeNode(4);
        TreeNode n5 = new TreeNode(5);
        n1.children.add(n2);
        n2.children.add(n3);
        n3.children.add(n4);
        n4.children.add(n5);
        System.out.println(getLastCommonParent(n1, n4, n5));  // should be 4
    }
	
	
    // One node is not in the tree
    //               1
    //              /
    //             2
    //            /
    //           3
    //          /
    //         4
    //        /
    //       5
    private static void test03() {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        TreeNode n3 = new TreeNode(3);
        TreeNode n4 = new TreeNode(4);
        TreeNode n5 = new TreeNode(5);
        TreeNode n6 = new TreeNode(6);
        n1.children.add(n2);
        n2.children.add(n3);
        n3.children.add(n4);
        n4.children.add(n5);
        System.out.println(getLastCommonParent(n1, n5, n6)); //should be null
    }
	
}