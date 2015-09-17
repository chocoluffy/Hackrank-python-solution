# -*- coding: UTF-8 -*-

case_number = int(raw_input())
array_for_length_of_case = []
nested_array_of_cases = []
for i in range(case_number):
    array_for_length_of_case.append(int(raw_input()))
    nested_array_of_cases.append(map(int, raw_input().split()))

for case in nested_array_of_cases:
    flag = False
    prefix = []
    for i in case:
        if len(prefix) == 0:
            prefix.append(i)
        else:
            prefix.append(i + prefix[len(prefix)-1])
    for i in range(len(prefix)):
        if (i == 0 or i == len(prefix)-1):
            continue
        else:
            if prefix[i-1] == prefix[len(prefix)-1] - prefix[i]:
                flag = True
    if flag:
        print "YES"
    else:
        print "NO"


# Problem: Find if there exists an element in the array, such that, the sum of elements on its left is equal to the sum of elements on its right. 
# Formally, find an ``i``, such that, ``A1+A2+…+Ai−1=Ai+1+Ai+2+…+AN``. 

# Solution: 

# Approach 1:
# We first count ``total=A1+A2+…+AN``.
# Now if for an ``i``, let's define ``sum=A1+A2+…+Ai`` 
# If ``sum=total−sum−Ai+1``, the answer is YES.

# So, we maintain a sum variable in second pass which we keep updating and checking.

# Approach 2:
# We keep a prefix array pre, where ``pre[i]=A1+A2+...+Ai``. Traversing over ``i``, we can easily check whether sum on left is equal to sum on right. See setter's solution for more details. 

# We can use the following property to calculate prefix array, ``pre``, in ``O(N)`` steps.
# pre[i] = 0 if i == 0
# pre[i] = pre[i-1] + A[i] else
# Now we can represent 

# ``A1+A2+…+Ak=pre[k]``
# ``Ak+Ak+1+…+AN=pre[N]−pre[k−1]``
#  Set by Lalit Kundu

# Problem Setter's code :
# #include<bits/stdc++.h>
# using namespace std;
# #define assn(n,a,b) assert(n<=b && n>=a)
# typedef long long LL;
# LL pre[100005];
# int main()
# {
#     int t;
#     cin >> t;
#     assn(t,1,10);
#     while(t--)
#     {
#         LL n,i,j,flag=0,x;
#         cin >> n;
#         assn(n,1,100000);
#         for(i=1; i<=n; i++)
#         {
#             cin >> x;
#             assn(x,1,20000);
#             // store pre[i]= sum of all elements till index i.
#             pre[i]=pre[i-1]+x;
#         }
#         for(i=1; i<=n; i++)
#         {
#             // check if sum to left is same as sum to right
#             if(pre[i-1]==(pre[n]-pre[i]))flag=1;
#         }
#         if(flag)cout << "YES\n";
#         else cout << "NO\n";
#     }
#     return 0;
# }
#  Tested by gera1d

# Problem Tester's code :
# #ifdef ssu1
# #define _GLIBCXX_DEBUG
# #endif
# #undef NDEBUG

# #include <algorithm>
# #include <functional>
# #include <numeric>
# #include <iostream>
# #include <cstdio>
# #include <cmath>
# #include <cstdlib>
# #include <ctime>
# #include <cstring>
# #include <cassert>
# #include <vector>
# #include <list>
# #include <map>
# #include <set>
# #include <deque>
# #include <queue>
# #include <bitset>
# #include <sstream>

# using namespace std;

# #define fore(i, l, r) for(int i = (l); i < (r); ++i)
# #define forn(i, n) fore(i, 0, n)
# #define fori(i, l, r) fore(i, l, (r) + 1)
# #define sz(v) int((v).size())
# #define all(v) (v).begin(), (v).end()
# #define pb push_back
# #define mp make_pair
# #define X first
# #define Y second

# #if ( _WIN32 || __WIN32__ )
#    #define LLD "%I64d"
# #else
#    #define LLD "%lld"
# #endif

# typedef long long li;
# typedef long double ld;
# typedef pair<int, int> pt;

# template<typename T> T abs(T a) { return a < 0 ? -a : a; }
# template<typename T> T sqr(T a) { return a*a; }

# const int INF = (int)1e9;
# const ld EPS = 1e-9;
# const ld PI = 3.1415926535897932384626433832795;

# int readInt(int l, int r){
#    int x;
#    if(scanf("%d", &x) != 1){
#        fprintf(stderr, "Expected int in range [%d, %d], but haven't found!", l, r);
#        throw;
#    }
#    if(!(l <= x && x <= r)){
#        fprintf(stderr, "Expected int in range [%d, %d], but found %d!", l, r, x);
#        throw;
#    }
#    return x;
# }

# int main(){
# #ifdef ssu1
#    assert(freopen("input.txt", "rt", stdin));
#    //assert(freopen("output.txt", "wt", stdout));
# #endif

#    int T = readInt(1, 10);
#    forn(Ti, T){
#        int n = readInt(1, 100000);
#        vector<int> a(n);
#        forn(i, n)
#            a[i] = readInt(1, 20000);
#        vector<li> x(n);
#        forn(i, n){
#            x[i] = (i == 0 ? 0 : x[i - 1]) + a[i];
#        }
#        li sum = 0;
#        int cnt = 0;
#        for(int i = n - 1; i >= 0; --i){
#            li left = (i == 0 ? 0 : x[i - 1]);
#            if(left == sum)
#                cnt++;
#            sum += a[i];
#        }
#        puts(cnt == 0 ? "NO" : "YES");
#    }

#    return 0;
# }
