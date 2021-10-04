#include <iostream>
#include <bits/stdc++.h>
using namespace std;

const int N = 1e5;

struct State{
	int id{};
	bool is_terminal;
	map<char, int> edges;
	map<std::string, int> edges_for_output;
};

unordered_map<int, State> states;
std::unordered_set<char> alphabet;

int id_begin=-1;


unordered_set<int> used;
bool res_check = true;
void dfs_check_sizes(int i){
    if(used.count(i) or !res_check) return;
    used.insert(i);
    
    res_check |= (alphabet.size()==states[i].edges.size()); 
    if(!res_check) return;
    
    for(auto p: states[i].edges) {
        if(!res_check) return;
        dfs_check_sizes(p.second);
    }
}

int main(int argc, char *argv[]) {

    std::ifstream rf(argv[1]); 
    std::ofstream outf(std::string(argv[1]) + ".out");
    
	std::string alpha;
	rf >> alpha;
	for(auto i : alpha) alphabet.insert(i);
	std::string com;
	while(rf>>com) {
		//if(com=="end") break;
		if(com == "begin") {
			int id;
			rf>>id;
			if(id < 0){
				outf << "ERROR: id can't be negative!" << std::endl; 
			} else {
				id_begin = static_cast<std::size_t>(id);
			}
		} else if(com == "state") {
			int id;
			rf>>id;
			if(id < 0){
				outf << "ERROR: id can't be negative!" << std::endl; 
				continue;
			} 
			std::string tf;
			rf>>tf;
			bool is_t;
			if(tf=="true"){
				is_t = true;
			} else if(tf=="false"){
				is_t = false;
			} else {
				outf << "ERROR: bool = [true|false], not" << tf << "!" << std::endl;
				continue; 
			}
			states[id].id = id;
			states[id].is_terminal = is_t;
		} else if(com == "-->") {
			int from, to;
			std::string char_;
			rf>>from>>to>>char_;
			if(from<0 or true<0){
				outf << "ERROR: id can't be negative!" << std::endl; 
				continue;	
			}
			states[from].edges_for_output[char_] = to;
			if(char_.length() == 1){
				if(char_=="*"){
					for(auto i: alphabet){
						if(states[from].edges.count(i)) outf<<"Redeclaration!"<<std::endl;
						states[from].edges[i] = to;
					}
				} else {
					if(states[from].edges.count(char_[0])) outf<<"Redeclaration!"<<std::endl;
						states[from].edges[char_[0]] = to;
				}
			} else{
				if(char_[0]=='[' && char_[char_.length()-1]==']'){
					for(int i=1; i<char_.length()-1; ++i){
						char t = char_[i];
						if(states[from].edges.count(t)) outf<<"Redeclaration!"<<std::endl;
						states[from].edges[t] = to;
					}
				} else {
					outf<<"Incorrect output!" << std::endl;
				}
			}
		} else {
			outf << com << "is an undefined command!" << std::endl;
		}
	}
		// Проверяем начальную вершину
		if(id_begin<-1) outf << "We haven't a start:(" << std::endl;
		// Проверяем полноту
		dfs_check_sizes(id_begin);
		if(!res_check) outf << "It's not complete!" << std::endl;
		
		for(auto &ii : states){
		    auto &i = ii.second;  
		    outf<<"State " << i.id << ":\n";
		    if(i.is_terminal) {
		        outf<<"\tTerminal!\n";
		    }
		    outf<<"\tTransitions:\n";
		    for(auto &j : i.edges_for_output){
		        outf<<"\t\t to "<< j.second <<" by ";
		        if(j.first == "*"){
		            outf << "all chars" <<"\n";
		        } else {
		            outf << j.first << '\n';
		        }
		        
		    }
		}
}