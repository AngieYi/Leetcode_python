//http://www.voidcn.com/blog/gogokongyin/article/p-6071444.html

#include <iostream>
#include <list>
#include <vector>
using namespace std;

struct BinTree
{
	int data;
	BinTree *pLeft;
	BinTree *pRight;
};

list<BinTree *> path1;
list<BinTree *> path2;

BinTree *pRoot1 = NULL;

bool IsExistData1 = true;
bool IsExistData2 = true;


//�ݹ����򴴽���������
void CreateTree(BinTree *&root)
{
	int data;
	cin >> data;
	if (0 == data)
		root = NULL;
	else
	{
		root = new BinTree;
		root->data = data;
		CreateTree(root->pLeft);
		CreateTree(root->pRight);
	}
}


//1.���Ӹ����pRoot������Ľ��ֵdata1,data2��·������������list1��list2�У�
bool GetNodePath(BinTree *root, int target, list<BinTree*> &path)
{
	if (NULL == root)
		return false;
	
	path.push_back(root);

	if (root->data == target)
		return true;
	else
	{
		bool found = false;
		found = GetNodePath(root->pLeft, target, path);

		if (!found)
			found = GetNodePath(root->pRight, target, path);

		if (!found)
			path.pop_back();
		return found;
	}
}


//2.�õ�list1��list2������㣻
BinTree *GetLastComNode(const list<BinTree *> &list1, const list<BinTree*> &list2)
{
	list<BinTree *>::const_iterator it1 = list1.begin();
	list<BinTree *>::const_iterator it2 = list2.begin();

	BinTree *pLast = NULL;

	while (it1 != list1.end() && it2 != list2.end())
	{
		if (*it1 == *it2)
			pLast = *it1;
		it1++;
		it2++;
	}
	return  pLast;
}


//3.���1,2�����ع�����㣻
BinTree *GetLastCommParent(BinTree *root, int data1, int data2)
{
	if (NULL == root)
		return NULL;
	//�õ�·��
	if (!GetNodePath(root, data1, path1))
	{
		IsExistData1 = false;
		return NULL;
	}
	if (!GetNodePath(root, data2, path2))
	{
		IsExistData2 = false;
		return NULL;
	}
	//�õ���͹������ȣ�
	return GetLastComNode(path1, path2);
}


void PreOrder(BinTree *root)
{
	if (root)
	{
		cout << root->data << " ";
		PreOrder(root->pLeft);
		PreOrder(root->pRight);
	}
}


void InOrder(BinTree *root)
{
	if (root)
	{
		InOrder(root->pLeft);
		cout << root->data << " ";
		InOrder(root->pRight);
	}
}


void DestoryBinTree(BinTree *root)
{
	if (root)
	{
		DestoryBinTree(root->pLeft);
		DestoryBinTree(root->pRight);
		delete root;
		root = NULL;
	}
}


int main()
{
	int da1, da2;
	BinTree *result = NULL;
	CreateTree(pRoot1);
	
	cout << "ǰ�������";
	PreOrder(pRoot1);
	cout << endl;
	cout << "���������";
	InOrder(pRoot1);
	cout << endl;

	while (1)
	{
		cin >> da1 >> da2;
		if (0 == da1 || 0 == da2)
			break;

		result = GetLastCommParent(pRoot1, da1, da2);
		path1.clear();
		path2.clear();
		if (IsExistData1&& IsExistData2)
			cout << da1 << "��" << da2 << "����͹��������ǣ�" << result->data << endl;
		else
		{
			if (!IsExistData1)
				cout << da1 << "���ݲ����ڣ�" << endl;
			else
				cout << da2 << "���ݲ����ڣ�" << endl;
		}
	}
	DestoryBinTree(pRoot1);
	system("pause");
	return 0;
}