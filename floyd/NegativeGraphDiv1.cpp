#include <iostream>
#include <vector>

#include <string>

using namespace std;

int main(){
   vector <long long > v;
   long long N;
   vector <long long> from;
   vector <long long> to;
   vector <long long> weights;
   long long charges;

   long long vsize;
   string line;
   while (cin >> line) v.push_back( stoll(line) );


   vsize = (v.size() - 2 ) / 3; 
   for (int i = 1; i < vsize+1; i++) {
      from.push_back(v[i]);
      to.push_back(v[i + vsize]);
      weights.push_back(v[i + (2 * vsize)]);
   }
   N = v[0];
   charges = v[v.size()-1];
   vector < vector < long long > > adj;
   adj.resize(vsize);
   for(int i = 0; i < adj.size(); i++) adj[i].resize(vsize, 0);
   


   printf("N: %lld\n", N);
   printf("From: \n   ");
   for (int i = 0; i < from.size(); i++) printf("%lld ", from[i]);
   printf("\n");
   printf("To: \n   ");
   for (int i = 0; i < to.size(); i++) printf("%lld ", to[i]);
   printf("\n");
   printf("Weights: \n   ");
   for (int i = 0; i < weights.size(); i++) printf("%lld ", weights[i]);
   printf("\n");
   printf("Charges: %lld\n", charges);
}
