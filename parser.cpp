#include <bits/stdc++.h>
#include <regex>
std::ofstream out;
struct VarSyntaxTree {
    std::string name;
    std::unordered_set<std::string> labels;
    std::vector<std::string> rules;
    std::string color;
};
/*
std::string random_color() {

}
*/

int line = 0;
std::unordered_set<std::string> used;
std::string RED(const std::string& str){
    return "\033[1;31m" + str + "\033[0;33m";
}

std::string BLUE(const std::string& str){
    return "\033[0;34m" + str + "\033[0;33m";
}

std::string BLUEB(const std::string& str){
    return "\033[1;34m" + str + "\033[0;33m";
}


std::string CIAN(const std::string& str){
    return "\033[5;36m" + str + "\033[0;33m";
}

std::string WHEREL(){
    return BLUEB("line: "+std::to_string(line)+' ');
}


std::string error_str(int pos){
    return RED("Syntax Error: ")+WHEREL()+CIAN(std::to_string(pos+1) + " symbol") + " is ";
}

std::string WHERE(int pos){
    return BLUEB("( line" + std::to_string(line)+":"+std::to_string(pos)+") ");
}



bool is_correct_var(const std::string& s) {
    for(int i=0; i<s.length(); ++i) {
        if((!std::isdigit(s[i]) && !std::isalpha(s[i]) && s[i]!='_') or (i==0 && s[i]=='_')){
            std::cerr << error_str(i) << "incorrect symbol in var " << BLUE(s) << "!"<<std::endl;
            return false;
        }
    }
    return true;
}

std::unordered_set<std::string> vars;
class Parser {
private:
    class Operation {
    private:
        const char operation = '-';
        const short priority = 0;
        const short arity = 0;
    public:
        Operation() = default;
        Operation(char operation_, short priority_, short arity_) : operation(operation_), priority(priority_),
        arity(arity_){};

        const short &get_priority() const {
            return priority;
        }

        const short &get_arity() const {
            return arity;
        }

        const char &get_operation() const {
            return operation;
        }
    };
    enum TYPE {
        VAR, WORD, OPER
    };

    std::vector<std::string> labels;
    std::vector<std::string> rules;

    std::unordered_map<char, Operation> operations {
            {'+', Operation('+', 1, 2)},
            {'?', Operation('?', 2, 1)},
            {'*', Operation('*', 2, 1)},
            {'|', Operation('|', 1, 2)},
            {'(', Operation('(', 0, 0)},
            {')', Operation(')', 0, 0)}
    };

    class Atom {
    private:
        const TYPE type;
        const std::string what;
    public:
        int num;
        std::vector<Atom*> children;

        explicit Atom(const TYPE t_, const std::string &what_, int num_) : type(t_), what(what_),  num(num_) {
        }

        const TYPE get_type() const {
            return type;
        }

        void add_child(Atom *s){
            children.push_back(s);
        }

        const std::string& get_str_name() const {
            return what;
        }

        /*~Atom() {
            for(auto &i : children){
                delete i;
            }
        }*/

    };


    const std::string str_expression;
    Atom *head;
    std::stack<Atom*> atoms;
    std::stack<Operation> op;
    int id = 1;
    std::string var;
public:

    explicit Parser(const std::string &str_expression_, const std::string &v) : str_expression(str_expression_), var(v) {
    };

    const bool is_operation(char x) const {
        return (operations.count(x) != 0);
    }

    Operation get_operation(char x){
        return operations[x];
    }

    void process_op (const Operation &op) {
        char c = op.get_operation();
        std::string so;
        so += c;
        if(op.get_arity()==2){
            if(atoms.size()<2){
                std::cerr<<RED("Parse Error: ") + WHEREL() + " operator " + BLUE(so) + " expected 2 parameters!" <<std::endl;
                return;
            }
            Atom* r = atoms.top();  atoms.pop();
            Atom* l = atoms.top();  atoms.pop();
            Atom *new_atom = new Atom(TYPE::OPER, so, id++);
            new_atom->add_child(l);
            new_atom->add_child(r);
            atoms.push(new_atom);
        } else {
            if(atoms.size()<1){
                std::cerr<<RED("Parse Error: ") + WHEREL() + " operator " + BLUE(so) + " expected 1 parameter!" <<std::endl;
                return;
            }
            Atom *s = atoms.top();  atoms.pop();
            Atom *new_atom = new Atom(TYPE::OPER, so, id++);
            new_atom->add_child(s);
            atoms.push(new_atom);
        }

    }

    void prepare () {
        std::size_t i = 0;
        while(i<str_expression.length()) {
            if(str_expression[i]==' '){
                ++i;
                continue;
            }
            if (str_expression[i]=='('){
                op.push(get_operation('('));
                ++i;
            } else if (str_expression[i] == ')') {
                ++i;
                if(op.empty()){
                    std::cerr<<RED("Parse Error: ") + WHEREL() + " expected " + BLUE("'('") << std::endl;
                    continue;
                }

                //assert(!op.empty());
                while (op.top().get_operation() != '(') {
                   // assert(!op.empty());
                    process_op(op.top());
                    op.pop();
                    if(op.empty()){
                        std::cerr<<RED("Parse Error: ") + WHEREL() + " expected " + BLUE("'('") << std::endl;
                        break;
                    }
                }
                if(op.empty()){
                    std::cerr<<RED("Parse Error: ") + WHEREL() + " expected " + BLUE("'('") << std::endl;
                    break;
                }
                op.pop();

            } else if (is_operation(str_expression[i])) {
                Operation oper(get_operation(str_expression[i]));
                while (!op.empty() && op.top().get_priority() >= oper.get_priority()) {
                    process_op(op.top());
                    op.pop();
                }
                op.push(oper);
                ++i;
            } else if(str_expression[i] == '^') { // Слово какое-то
                std::string result;
                ++i;
                while(str_expression[i]!='^' || str_expression[i-1]=='\\') { // тут типо просто "\"
                    result += str_expression[i];
                    ++i;
                    if(i>=str_expression.length()){
                        break;
                    }
                }
                if(i>=str_expression.length()) {
                    std::cerr<<RED("Parse Error: ") + WHEREL() + " expected " + BLUE("'^'") << std::endl;
                    continue;
                }
                ++i;
                Atom* nA = new Atom(TYPE::WORD, result, id++);
                atoms.push(nA);
            } else if (std::isalpha(str_expression[i])) { // Символ => переменная
                std::string result;
                assert(i<str_expression.length());
                while((std::isalpha(str_expression[i]) || isdigit(str_expression[i]) || str_expression[i]=='_') && i<str_expression.length()){
                    result += str_expression[i];
                    ++i;
                }
                atoms.push(new Atom(TYPE::VAR, result, id++));
                /*if(!vars.count(result)) {
                    std::cerr << RED("Parse error: ") + WHEREL() << "Variable " << BLUE(result) << " is used but has not been previously declared" << std::endl;
                }*/
            } else {
                std::cerr<<RED("Parse Error: ")+ WHERE(i+1)+" incorrect symbol ";
                for(int j=0; j<str_expression.length(); ++j){
                    std::string s;
                    s+=str_expression[j];
                    if(i!=j) {
                        std::cerr << CIAN(s);
                    } else{
                        std::cerr << RED(s);
                    }
                }
                std::cerr<<std::endl;
                ++i;
               // exit(1);
            }
        }
        //std::cout<<"lol"<<std::endl;
        while (!op.empty()) {
            process_op(op.top()), op.pop();
        }
        //std::cout<<"ok"<<std::endl;
        if(atoms.size()!=1){
            std::cerr << RED("Parse error: ") + WHEREL() + "parsing error:( Most likely you forgot to use the operator!" << std::endl;
            return;
        }
        head = atoms.top();
        labels.push_back(var + " [label=\"head:"+var+"\"]");
        out<<labels.back()<<std::endl;
        rules.push_back(var + " -- " + var + "_" + std::to_string(head->num));
        out<<rules.back()<<std::endl;
    }

    void dfs(Atom* x) {
       // std::cout<<'"'<<x->get_str_name();
        if(x->get_type() == TYPE::VAR ) {
            used.insert(x->get_str_name());
        }
        if(x->get_type() == TYPE::VAR && !vars.count(x->get_str_name())) {
            std::cerr << RED("Parse error: ") + WHEREL() << "Variable " << BLUE(x->get_str_name()) << " is used but has not been declared" << std::endl;
        }
        std::string type, color;
        if(x->get_type()== TYPE::VAR) {
            type = "VAR";
            color = "green";
            if(x->get_str_name()==var){
                type = "SELF";
                color = "blue";
            }
        }
        else if(x->get_type() == TYPE::OPER) {
            type = "OPER";
            color = "black";
        }
        else{
            type = "WORD";
            color = "purple";
        }
        labels.push_back(var+"_"+std::to_string(x->num)+" [label=\""+type+": "+x->get_str_name()+"\" color=\""+color+"\"]");
        out<<labels.back()<<std::endl;
        for(auto &i : x->children){
            dfs(i);
        }
        for(auto &i : x->children){
            rules.push_back(var + "_" + std::to_string(x->num) + " -- " + var + "_" + std::to_string(i->num));
            out<<rules.back()<<std::endl;
          //  std::cout<<'"'<<x->get_str_name()<<x<<'"'<<" -- "<<'"'<<i->get_str_name()<<i<<'"'<<'\n';
        }

    }

    void dfs(){
        dfs(head);
    }
  /*  ~Parser(){
        delete head;
    }*/
};
/*
class Graph {
private:
    std::unordered_map<string, Element> elements_by_name;
public:
};
*/
int main(int argc, char *argv[]) {

    std::ifstream in(argv[1]); // окрываем файл для чтения
    out = std::ofstream(std::string(argv[1]) + ".out");
    out << "graph graphname {" << std::endl;
    std::string x;

    std::cmatch narrowMatch;
    std::regex rx("^return .+$");
    bool return_flag = false;
    std::vector<Parser> parsers;
    while(std::getline(in, x)) {
        ++line;
        if(x.empty() or x=="\n") continue;
        const char *t = x.c_str();
        if(std::regex_match(t, t+strlen(t), narrowMatch, rx)){
            if(return_flag){
                std::cerr << RED("Parse Error: ") + WHEREL() << "reuse " << BLUE("return") << "!" << std::endl;
                continue;
            }
            std::string r(t+7, t+strlen(t));
            std::stringstream ss;
            ss << r;
            std::string y;
            ss >> y;
            used.insert(y);
            //while(y.front()==' ')
            out<<"MAIN__ [label=\"MAIN\" color=red]"<<std::endl;
            out<<"MAIN__ -- "<<y<<std::endl;
            return_flag = true;
        } else {
            std::string id;
            std::string value;
            int first=-1;
            for(int i=0; i<x.length()-1; ++i) {
                if (x[i] != ':') {
                    id += x[i];
                } else {
                    if (x[i + 1] != '=') {
                        std::cerr << RED("Parse Error: ") + WHEREL() << " where is "+ CIAN(":=")+" or return ?\n";
                        break;
                       // exit(1);
                    }
                    first = i + 2;
                    break;
                }
            }
            if(first==-1){
                std::cerr << RED("Parse Error: ") + WHEREL() << " where is "+ CIAN(":=")+" or return ?\n";
                continue;
            }
            for(int i=first; i<x.length(); ++i) value+=x[i];
            while(id.back()==' ' && id.size()){
                //std::cerr<<"lol"<<value.back()<<"k"<<std::endl;
                id.pop_back();
            }
            if(!is_correct_var(id)) continue;
            vars.insert(id);
            Parser t(value, id);
            //std::cerr<<value<<std::endl;
            t.prepare();
            parsers.push_back(t);
            //std::cerr<<"lol"<<std::endl;
            //t.dfs();
            //std::cerr<<"lol"<<std::endl;
        }
    }
    for(auto &i : parsers){
        i.dfs();
    }
    for(auto &i : vars){
        if(!used.count(i)){
            std::cerr << BLUEB("Warning: ") << "var " << i << " is never used!"<<std::endl;
        }
    }

    if(!return_flag){
        std::cerr << RED("Parse Error: ") << "expected " << BLUE("return") << std::endl;
    }
    out << "}" << std::endl;
}