#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    int T,maxa=0,maxm=0,ai,mi;
    cin>>T;
    while(T --> 0){
        int arr[6],i;
        for(i=0;i<6;i++){
            cin>>arr[i];
        }
        for(i=0;i<3;i++){
            if(arr[i]>maxa){
                maxa=arr[i];
                ai=i;
                }
                if(arr[i]==arr[i+1] && (i+1)<3){
                    if(arr[i+3]!=arr[i+4]){
                        goto nxt;
                    }
                }
        }
        for(i=3;i<6;i++){
            if(arr[i]>maxm){
                maxm=arr[i];
                mi=i;
                }
        }
        if((ai+3)==mi){
            arr[ai]=0;arr[mi]=0;maxa=0;maxm=0;
            for(i=0;i<3;i++){
                if(arr[i]>maxa){
                    maxa=arr[i];
                    ai=i;
                }
                if(arr[i]==arr[i+1]){
                    if(arr[i+3]!=arr[i+4] && (i+1)<3){
                        goto nxt;
                    }
                }
            }
            for(i=3;i<6;i++){
                if(arr[i]>maxm){
                    maxm=arr[i];
                    mi=i;
                }
            }
            if((ai+3)==mi){
                cout<<"FAIR"<<endl;
            }
            else{
            cout<<"NOT FAIR"<<endl;
            }
        }nxt:   cout<<"NOT FAIR"<<endl;
    }
	return 0;
}