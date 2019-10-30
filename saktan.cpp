#include<iostream>
using namespace std;

typedef long long ll;

int main(){
    int t;
    cin >> t;
    while(t --> 0){
        ll foo[3];
        for(int i=0;i<3;i++){
            scanf("%d ",foo[i]);
        }
        ll row = foo[0];
        ll col = foo[1];
        ll Q = foo[2];
        ll query[Q,2];
        for(i=0;i<Q;i++){
            for(int j=0;j<2;j++)
                scanf("%d ",query[i,j]);
        }
        for (i=0;i<Q;i++){
            ll x = query[i,0]
            ll y = query[i,1]
            
        }

    }
return 0;
}