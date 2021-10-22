#include <bits/stdc++.h>
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

std::string RED(const std::string& str){
    return "\033[1;31m" + str + "\033[0;30m";
}

std::string BLUE(const std::string& str){
    return "\033[0;34m" + str + "\033[0;30m";
}

std::string CIAN(const std::string& str){
    return "\033[5;36m" + str + "\033[0;30m";
}

std::string error_str(int pos){
    return RED("Syntax Error: ")+CIAN(std::to_string(pos+1) + " symbol") + " is ";
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
            //std::cout<<"K"<<std::endl;
            assert(atoms.size()>=2);
            Atom* r = atoms.top();  atoms.pop();
            Atom* l = atoms.top();  atoms.pop();
            Atom *new_atom = new Atom(TYPE::OPER, so, id++);
            new_atom->add_child(l);
            new_atom->add_child(r);
            //std::cout<<"LOL-T"<<std::endl;
            atoms.push(new_atom);
        } else {
            assert(atoms.size()>=1);
            //std::cout<<"L"<<std::endl;
            Atom *s = atoms.top();  atoms.pop();
            Atom *new_atom = new Atom(TYPE::OPER, so, id++);
            new_atom->add_child(s);
            //std::cout<<"LOL-K"<<std::endl;
            atoms.push(new_atom);
            //std::cout<<"K_LOL"<<std::endl;
        }

    }

    void prepare () {
        std::size_t i = 0;
        while(i<str_expression.length()) {
            //std::cout<<i;
            if (str_expression[i]=='('){
                op.push(get_operation('('));
                ++i;
            } else if (str_expression[i] == ')') {
                assert(!op.empty());
                while (op.top().get_operation() != '(') {
                    assert(!op.empty());
                    process_op(op.top()), op.pop();
                }
                ++i;
                assert(!op.empty());
                op.pop();
            } else if (is_operation(str_expression[i])) {
               // std::cout<<"LOL"<<str_expression[i]<<std::endl;
                Operation oper(get_operation(str_expression[i]));
                while (!op.empty() && op.top().get_priority() >= oper.get_priority()) {
                    process_op(op.top()), op.pop();
                }
                op.push(oper);
                ++i;
              //  std::cout<<oper.get_priority()<<std::endl;
            } else if(str_expression[i] == '^') { // Слово какое-то
                std::string result;
               // std::cout<<"LOL"<<std::endl;
                ++i;
                assert(i<str_expression.length());
                while(str_expression[i]!='^' || str_expression[i-1]=='\\') { // тут типо просто "\"
                    assert(i<str_expression.length());
                    result += str_expression[i];
                    ++i;
                    if(i>=str_expression.length()){
                        exit(1); // TODO: ОШИБКА!
                    }
                }
                ++i;
                Atom* nA = new Atom(TYPE::WORD, result, id++);
                //std::cout<<"LOL-R"<<std::endl;
                atoms.push(nA);
            } else if (std::isalpha(str_expression[i])) { // Символ => переменная
                std::string result;
                assert(i<str_expression.length());
                while((std::isalpha(str_expression[i]) || isdigit(str_expression[i]) || str_expression[i]=='_') && i<str_expression.length()){
                    result += str_expression[i];
                    ++i;
                }
               // if(i!=str_expression.length()) --i;
                //std::cout<<"LOL-P"<<std::endl;
                atoms.push(new Atom(TYPE::VAR, result, id++));
                if(!vars.count(result)) {
                    std::cerr << RED("Parse error: ") << "Variable " << BLUE(result) << " is used but has not been previously declared" << std::endl;
                }
            } else {
                std::cerr<<RED("Parse Error: ")+" incorrect symbol ";
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
        head = atoms.top();
        labels.push_back(var + " [label=\"head:"+var+"\"]");
        out<<labels.back()<<std::endl;
        rules.push_back(var + " -- " + var + "_" + std::to_string(head->num));
        out<<rules.back()<<std::endl;
    }

    void dfs(Atom* x) {
       // std::cout<<'"'<<x->get_str_name();
        labels.push_back(var+"_"+std::to_string(x->num)+" [label=\""+x->get_str_name()+"\"]");
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

    std::string x;
    while(in>>x) {
        if(x=="return"){
            std::string y;
            in>>y;
            out<<"MAIN__ [label=\"MAIN\" color=red]"<<std::endl;
            out<<"MAIN__ -- "<<y<<std::endl;
        } else {
            std::string id;
            std::string value;
            int first;
            for(int i=0; i<x.length()-1; ++i) {
                if (x[i] != ':') {
                    id += x[i];
                } else {
                    if (x[i + 1] != '=') {
                        std::cout << ":=?";
                        exit(1);
                    }
                    first = i + 2;
                    break;
                }
            }
            for(int i=first; i<x.length(); ++i) value+=x[i];
            if(!is_correct_var(id)) continue;
            Parser t(value, id);
            t.prepare();
            t.dfs();
            vars.insert(id);
        }
    }
}