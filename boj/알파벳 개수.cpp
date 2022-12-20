#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string s;
	int alp[26] = { 0, };

	cin >> s;

	for (auto c : s)
		alp[int(c - 'a')] = alp[int(c - 'a')] + 1;
	for (int i = 0; i < 26; i++)
		cout << alp[i] << ' ';
}
