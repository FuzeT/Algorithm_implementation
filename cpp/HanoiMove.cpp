#include <iostream>
#include <string>
#include <stack>

using namespace std;



void HanoiMove(int N, stack<int>& origin, string a, stack<int>& buffer, string b, stack<int>& destination, string c){
	if (N == 1){
		int temp = origin.top();
		origin.pop();
		destination.push(temp);
		cout << "Move 1 from " << a << " to " << c << endl;
	}
	else{
		HanoiMove(N - 1, origin, a, destination, c, buffer, b);
		int temp = origin.top();
		origin.pop();
		destination.push(temp);
		cout << "Move " << N << " from " << a << " to " << c << endl;
		HanoiMove(N - 1, buffer, b, origin, a, destination, c);
	}
}

int main(){
	stack<int> origin,buffer,destination;
	int N = 3;
	while (N > 0){ origin.push(N); N--; }
	cout << "Start Here...." << endl;
	HanoiMove(3, origin, "A", buffer, "B", destination, "C");
	system("pause");
	return 1;
}
