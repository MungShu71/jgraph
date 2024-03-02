#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <cmath>
using namespace std;
class Jgraph {
    unordered_map<string*, unordered_map < string*, vector < float* >* >* >data;
    public:
        void Process(const string &filename);
        void WriteFile();

};

void Jgraph::Process(const string &filename){

    ifstream fout;
    ofstream fin;
    fout.open(filename);
    fin.open("test.jgr");
     fin << "newgraph\n";
    
    
    

    string s;
    string ticker ;
    string date;
    // string ;
    // char ticker[25  ];
    // char date[25];
    int n, npts, i;

    string open, close, high, low, adj, max_price, min_price, vol, days, maxPrice;
    vector <string> colors = {"0 1 0", 
                              "1 1 0", 
                              "1 0 0", 
                              "0 0 1", 
                              "1 0 1", 
                              "0 1 1", 
                              "0 0 0",
                              };
    string curr_ticker = " "; 
    n = -1;
    i = 0;
    int count = 0;
    int p;
    bool header = true;
    int dec = 0;
    unsigned long long tt;
    int k;
    string labelsizex;
    string labelsizey;
    while (getline(fout, s)){
        istringstream sin(s);

        if (header ){
            if (count == 1) {
                getline(sin, days,'/');

                cout <<(days.size()) << endl;

                p = pow(10, days.size()-1) / 2;
                if (days.size() <= 2) {
                    labelsizex += ".";
                    labelsizex += days[0];

                }
                else {
                    for (int j = 0; j < days.size()-2; j++) labelsizex += days[j];
                }
                int op = stoi(days);                
                fin << "xaxis min 0 max " << days << " hash " << p << " mhash 5 size " << 7 <<" \n   label : Date (dd:mm::yyyy)\n";
                fin << "no_auto_hash_labels\n";
                fin << "hash_labels fontsize 8 font Times-Italic hjl vjc rotate -60\n";

                
            } else if (count == 2){
                getline(sin, maxPrice,'/');
         

              

                dec = pow(10, maxPrice.size()-1);
                 k = stoi(maxPrice);
           
                fin << "yaxis min " << 0 << " max " << (dec/10)+k  << " hash " <<  dec << " mhash 5 \n   label : Price (USD)\n";


                header = false;
            }
            count ++;
            continue;

        }
        if (s[0] == ' ') break;
        
        getline(sin, ticker, ',');
        
        if (curr_ticker != ticker) {
            cout << ticker << endl;
            curr_ticker = ticker;
            n += 1;
            fin << "legend top\n";
            fin << "newline pts 0.1 0 10.9 0\n";
            fin << "newcurve marktype circle cfill " << colors[n] << endl; 
            fin << "label : " << curr_ticker << endl;
        
      
            i = 0;
        }
  
        getline(sin,date,',');

        getline(sin,open,',');
        getline(sin,close,',');
        getline(sin,high,',');
        getline(sin,low,',');
        getline(sin,vol,',');
        getline(sin,adj,',');
         if(i % p == 0 ) {

            fin << "xaxis hash_label at " << i << " : " << date << endl;
            cout << i << endl;
        }
        i ++;
        tt ++ ;

        fin << "newcurve marktype box marksize .2 .2 linetype solid color " << colors[n] <<  " pts " << i << " " << open << "  " << i << " " << open 
                << "  " << i << " " << close << "  " << i << " " << high << "  " << i << " " << low << " \n"; 
  
    }
    fin.close();
    fout.close();

};
int main(int argc, char** argv){
    Jgraph *j = new Jgraph();
    if (argc <= 1) {
        cout << "wrong usage\n";
        exit(0);
    }
    cout << "E\n";

    j->Process(argv[1]);

    return 0;
}
