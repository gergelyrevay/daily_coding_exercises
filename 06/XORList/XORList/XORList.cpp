// XORList.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

class XORList {
	struct Node {
		int value;
		Node* both;
		Node(int val) : value(val), both(nullptr) {}
	};

	Node *head;

public:
	XORList() : head(nullptr) {}
	~XORList() {
	//FIXME
	}

	void add(int element) {
		Node *node = new Node(element);
		Node *next = head;
		Node *prev = nullptr;
		Node *tmp = nullptr;

		if (head == nullptr) {
			head = node;
		}
		else {
			while(next != nullptr) {
				std::cout << next->value << "->";

				tmp = next;
				next = (Node *)((int)tmp->both ^ (int)prev);
				prev = tmp;
			}
			tmp->both = (Node *)((int)tmp->both ^ (int)node);
			std::cout << node->value << "->END\n";
			node->both = tmp;
		}
	}

	int get(int index) {
		Node *next = head;
		Node *prev = nullptr;
		Node *tmp = nullptr;
		int idx = 0;
		
		while(idx != index){
			tmp = next;
			next = (Node *)((int)tmp->both ^ (int)prev);
			prev = tmp;
			idx++;

		}

		return(next->value);
	}
};

int main()
{

	XORList *xorList = new XORList();
	xorList->add(1);
	xorList->add(2);
	xorList->add(3);
	xorList->add(4);
	int test = xorList->get(2);
	std::cout << "Node Value: " << test << "\n";
}

