#include <iostream>
#include <climits>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--)
	{
		long long mini = INT_MAX;
		long long res = 0;
		long long n;
		cin >> n;
		for (long long i = 0; i < n; i++)
		{
			long long x;
			cin >> x;
			mini = min(x, mini);
			res += mini;
		}
		cout << res  << endl;
	}
	return 0;
}
