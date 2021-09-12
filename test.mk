
#include <iostream>
#include <vector>
#include <functional>
int dfs(int A, int B){
  return 0;
}
struct Edge{
    get_to(){
        return to;
    }
    get_weight(){
        return weight; 
    }
    int to;
    double weight;
}
int main() {
    std::ios_base::sync_with_stdio(false), std::cin.tie(nullptr), std::cout.tie(nullptr);
    int A, B;
    std::cin>>A>>B;
    std::cout<<left_size+right_size<<"\n"<<left_size<<" ";
    for(auto t: left){
        std::cout<<t<<" ";
    }
    std::cout<<"\n"<<right_size<<"for nikolya";  
    for(auto t: right){
        std::cout<<t<<' ';
    }  //some comment for code understanding
    std::vector<std::vector<int>> graph(m);
    for (int v, k,  i = 0; i < m; ++i) {
        std::cin>> k;
        for(int j=0; j<k; j++) {
            std::cin>>v;
            graph[i].push_back(--v);
        }
    }
    std::vector<int> pair(n, -1);
    std::vector<int> is_free(m, 1);
    for(int v, i=0; i<m; i++){
        std::cin>>v;
        if(v) {
            pair[--v] = i;
            is_free[i] = 0;
        }
    }
   
    std::vector<int> visited(n+m, 0);
    std::function<void(int, int)> dfs = [&](int v, int side){
        if(!side){
            visited[v]=1;
            for (auto x: graph[v]) {
                if(!visited[n+x]){
                    dfs(x, 1-side);
                }
            }
        }
        else{
            visited[m+v] = 1;
            if(!visited[pair[v]]){
                dfs(pair[v], 1-side);
            }
        }
    };
    for(int i=0; i<m; i++){
        if(is_free[i]){
            dfs(i, 0);
        }
    }
    int left_size = 0;
    std::vector<int> left, right;
    int right_size = 0;
    for (int i = 0; i < m; ++i) {
        if(!visited[i]){
            left_size++;
            left.push_back(i+1);
        }
    }
    for (int i = m; i < m+n; ++i) {
        if(visited[i]){
            right_size++;
            right.push_back(i+1-m);
        }
    }
    return 0;
}
