#include <bits/stdc++.h>

int main(int argc, char *argv[]) {
    auto work_with_files = [&]() {
        if (argc != 2) {
            std::cout << "Usage: <program> <path/to/test>\n";
            exit(0);
        }
        std::string file = argv[1];
        if (!freopen(file.c_str(), "r", stdin)) {
            std::cout << "Unable to open file: '" + file + "'\n";
            exit(0);
        }
        if (!freopen((file + ".out").c_str(), "w", stdout)) {
            std::cout << "Unable to open file: '" + file + ".out" + "'\n";
            exit(0);
        }
    };
    work_with_files();
    static const std::string TAB(4, ' ');
    struct Program {
        struct My_exception : std::runtime_error {
            explicit My_exception(const std::string &s) : std::runtime_error(s) {}
        };

        struct Only_if;
        struct If;
        struct While;
        struct Variable;
        struct Function;

        struct Expression {
            std::string expr;

            [[nodiscard]] std::string to_str() const {
                return expr;
            }
        };

        struct Operator {
            std::string operator_type;

            std::shared_ptr<Only_if> only_iff;
            std::shared_ptr<If> iff;
            std::shared_ptr<While> whilee;
            std::shared_ptr<Variable> variable_bounding;
            std::shared_ptr<Function> functionn;
            std::shared_ptr<std::pair<std::string, Expression>> variable_change;

//            std::string op;  // TODO: just string?

            [[nodiscard]] std::string to_str() const {
                return operator_type;
            }
        };

        struct Variable {
            std::string type;
            std::string name;
            bool is_has_value = false;
            Expression value;

            [[nodiscard]] std::string to_str() const {
                if (is_has_value) {
                    return type + " " + name + " = " + value.to_str();
                }
                return type + " " + name;
            }
        };

        struct Body {
            std::vector<Operator> operators;
            std::vector<Variable> variables;  // useful when need to check name new variable
        };

        struct Only_if {
            Expression condition;
            Body body;

            /*[[nodiscard]] std::string to_str() const {
                return "only_if " + condition.to_str() + " body";
            }*/
        };

        struct If {
            Expression condition;
            Body if_body, else_body;

            /*[[nodiscard]] std::string to_str() const {
                return "if " + condition + " body else body";
            }*/
        };

        struct While {
            Expression condition;
            Body body;

            /*[[nodiscard]] std::string to_str() const {
                return "while " + condition + " body";
            }*/
        };

        struct Function {
            std::string name;
            int argc{};
            std::vector<Variable> argv;  // {type, value}
            Body body;

            [[nodiscard]] std::string signature_to_str() const {
                std::string str = name + " " + std::to_string(argc);
                for (int i = 0; i < argc; ++i) {
                    str += " ";
                    str += argv[i].to_str();
                }
                return str;
            }
        };

        std::vector<Function> functions;

        static std::string read_string() {
            std::string s;
            std::cin >> s;
            return s;
        }

        static std::string read_whole_string() {
            std::string s;
            std::getline(std::cin, s);  // read end of previous string
            std::getline(std::cin, s);  // read next whole string
            int pos = static_cast<int>(s.find_first_not_of(' '));
            return s.substr(pos, s.size() - pos);
        }

        static bool is_number(const std::string &num) {
            if (num.size() < 2 || num.size() > 9) {
                return false;
            }
            if (num[0] == '0') {
                // all digits in [0-9]
                for (const auto &c: num) {
                    if (c < '0' || c > '9') {
                        return false;
                    }
                }
            } else if (num[0] == '1') {
                // all digits in [0-1]
                for (const auto &c: num) {
                    if (c < '0' || c > '1') {
                        return false;
                    }
                }
            } else {
                throw My_exception(
                        "First symbol of int is 0 (decimal) or 1 (binary), buf found: '" + std::string(1, num[0]) +
                        "'");
            }
            return true;
        }

        static int read_int() {
            std::string num;
            std::cin >> num;
            if (!is_number(num)) {
                throw My_exception("Expect legal number, buf found: '" + num + "'");
            }
            if (num[0] == '0') {  // decimal
                return std::stoi(num.substr(1, num.size() - 1));
            } else if (num[0] == '1') {  // binary
                return std::stoi(num.substr(1, num.size() - 1), nullptr, 2);
            } else {
                assert(false);
            }
        }

        static void check_type(const std::string &type) {
            if (type != "int2" && type != "int10" && type != "string") {
                throw My_exception("Unexpected type name: '" + type + "'");
            }
        }

        static bool is_contains_var(const std::string name, const std::vector<Variable> &vars) {
            return std::any_of(vars.begin(), vars.end(), [&](const auto &a) {
                return a.name == name;
            });
        }

        static void check_var(const Variable &var, const std::vector<Variable> &vars) {
            if (is_contains_var(var.name, vars)) {
                throw My_exception("Variable has name same as other variable: '" + var.name + "'");
            }
        }

        static int read_begin(const std::string &obj, bool is_need_read_word_begin = true) {
            if (is_need_read_word_begin) {
                std::string begin = read_string();
                if (obj == "function" && begin.empty()) {
                    return 1;
                }
                if (begin != "begin") {
                    throw My_exception("Expect begin " + obj + " with word: 'begin', but found: '" + begin + "'");
                }
            }
            std::string begin_obj = read_string();
            if (begin_obj != obj) {
                throw My_exception(
                        "Expect begin " + obj + " with words: 'begin " + obj + "', buf found: 'begin " + begin_obj +
                        "'");
            }
            return 0;
        }

        static void read_end(const std::string &obj, bool is_need_read_word_end = true) {
            if (is_need_read_word_end) {
                std::string end = read_string();
                if (end != "end") {
                    throw My_exception("Expect end " + obj + " with word: 'end', buf found: '" + end + "'");
                }
            }
            std::string end_obj = read_string();
            if (end_obj != obj) {
                throw My_exception(
                        "Expect end " + obj + " with words: 'end " + obj + "', but found: 'end " + end_obj + "'");
            }
        }

        static void read_variable(Variable &v) {
            v.type = read_string();
            check_type(v.type);
            v.name = read_string();
            std::string bounding = read_string();
            if (bounding != "=") {
                throw My_exception(
                        "Expect syntax: 'var <type> <name> = <value>', buf found: 'var " + v.type + " " + v.name + " " +
                        bounding + " ...'");
            }
            if (v.type == "int2" || v.type == "int10") {
                v.value = {std::to_string(read_int())};
            } else {
                std::string str = read_string();
                if (str.size() < 2 || str[0] != '"' || str.back() != '"') {
                    throw My_exception(
                            "Expect syntax: 'var string <name> = \"data\"', but found: 'var string <name> = " + str +
                            "'");
                }
                v.value = {str.substr(1, str.size() - 2)};
            }
            v.is_has_value = true;
        }

        static void read_signature(Function &func) {
            func.name = read_string();
            func.argc = read_int();
            for (int i = 0; i < func.argc; ++i) {
                std::string type = read_string();
                check_type(type);
                std::string name_var = read_string();
                Variable var = {type, name_var, false, ""};
                check_var(var, func.argv);
                func.argv.push_back(var);
            }
        }

        Only_if read_only_if() {
            Only_if only_if;
            only_if.condition = {read_whole_string()};
            read_body(only_if.body);
            read_end("only_if");
            return only_if;
        }

        If read_if() {
            If iff;
            iff.condition = {read_whole_string()};
            read_body(iff.if_body);
            std::string els = read_string();
            if (els != "else") {
                throw My_exception(
                        "Expect construction:\n\nbegin if\ncondition\nbody\nelse ...\n\n"
                        "But found:\n\nbegin if\ncondition\nbody\n" + els + " ...");
            }
            read_body(iff.else_body);
            read_end("if");
            return iff;
        }

        While read_while() {
            While whil;
            whil.condition = {read_whole_string()};
            read_body(whil.body);
            read_end("while");
            return whil;
        }

        Operator read_begin_smth() {
            std::string smth = read_string();
            if (smth == "only_if") {
                return get_operator_only_if(read_only_if());
            } else if (smth == "if") {
                return get_operator_if(read_if());
            } else if (smth == "while") {
                return get_operator_while(read_while());
            } else {
                throw My_exception("Expect begin one of those (only_if, if, while), buf found: 'begin " + smth + "'");
            }
        }

        static Operator get_operator_var_bound(const Variable &v) {
            return {"bound", .variable_bounding = std::make_shared<Variable>(v)};
        }

        static Operator get_operator_var_change(const std::string &name, const Expression &expr) {
            return {"change", .variable_change = std::make_shared<std::pair<std::string, Expression>>(name, expr)};
        }

        static Operator get_operator_only_if(const Only_if &only_iff) {
            return {"only_if", .only_iff = std::make_shared<Only_if>(only_iff)};
        }

        static Operator get_operator_if(const If &iff) {
            return {"if", .iff = std::make_shared<If>(iff)};
        }

        static Operator get_operator_while(const While &whilee) {
            return {"while", .whilee = std::make_shared<While>(whilee)};
        }

        static Operator get_operator_call_function(const Function &function) {
            return {"call", .functionn = std::make_shared<Function>(function)};
        }

        void read_body(Body &body) {
            read_begin("body");
            std::string starts_with;
            while (true) {
                starts_with = read_string();
                if (starts_with == "end") {  // ok
                    break;
                } else if (starts_with == "var") {  // ok, but need to add in operator
                    Variable v;
                    read_variable(v);
                    check_var(v, body.variables);
                    body.variables.push_back(v);
                    body.operators.push_back(get_operator_var_bound(v));
                } else if (starts_with == "begin") {  //
                    body.operators.push_back(read_begin_smth());
                } else if (starts_with == "call") {
                    Function cur;
                    read_signature(cur);
                    body.operators.push_back(get_operator_call_function(cur));
                } else if (starts_with == "skip") {
                    body.operators.push_back({"skip"});
                } else if (starts_with == "change") {
                    std::string name_l = read_string();
                    /*if (!is_contains_var(name_l, body.variables)) {
                        throw My_exception(
                                "Unknown variable name in change equation"
                        );  // TODO: new test
                    }*/  // too hard to check
                    std::string bounding = read_string();
                    if (bounding != "=") {
                        throw My_exception(
                                "Expect syntax: 'change <name> = ...', but found: 'change " + name_l + " " + bounding +
                                " ...'");
                    }
                    Expression expr = {read_whole_string()};
                    body.operators.push_back(get_operator_var_change(name_l, expr));
                } else {
                    throw My_exception("Unexpected operator start: '" + starts_with + "'");
                }
            }
            read_end("body", false);
        }

        int read_function(Function &cur) {
            if (read_begin("function") == 1) {
                return 1;
            }
            read_signature(cur);
            read_body(cur.body);
            read_end("function");
            return 0;
        }

        void read_program() {
            while (true) {
                Function cur;
                if (read_function(cur) == 0) {
                    functions.push_back(cur);
                } else {
                    break;
                }
            }
        }

        void write_only_if(const std::shared_ptr<Only_if> &only_if, const std::string &cur_tab) {
            std::cout << cur_tab << "condition: " << only_if->condition.to_str() << "\n";
            std::cout << cur_tab << "body: {\n";
            write_body(only_if->body, cur_tab + TAB);
            std::cout << cur_tab << "}\n";
        }

        void write_if(const std::shared_ptr<If> &iff, const std::string &cur_tab) {
            std::cout << cur_tab << "condition: " << iff->condition.to_str() << "\n";
            std::cout << cur_tab << "if_body: {\n";
            write_body(iff->if_body, cur_tab + TAB);
            std::cout << cur_tab << "}\n";
            std::cout << cur_tab << "else_body: {\n";
            write_body(iff->else_body, cur_tab + TAB);
            std::cout << cur_tab << "}\n";
        }

        void write_while(const std::shared_ptr<While> &whilee, const std::string &cur_tab) {
            std::cout << cur_tab << "condition: " << whilee->condition.to_str() << "\n";
            std::cout << cur_tab << "body: {\n";
            write_body(whilee->body, cur_tab + TAB);
            std::cout << cur_tab << "}\n";
        }

        static void write_bound(const std::shared_ptr<Variable> &variable_bound, const std::string &cur_tab) {
            std::cout << cur_tab << variable_bound->to_str() << "\n";
        }

        static void write_call(const std::shared_ptr<Function> &functionn, const std::string &cur_tab) {
            std::cout << cur_tab << functionn->signature_to_str() << "\n";
        }

        static void write_change(const std::shared_ptr<std::pair<std::string, Expression>> &var_change,
                                 const std::string &cur_tab) {
            std::cout << cur_tab << var_change->first << " = \n";
            std::cout << cur_tab << var_change->second.to_str() << "\n";
        }

        void write_body(const Body &body, const std::string &cur_tab) {
            for (const auto &op: body.operators) {
                std::cout << cur_tab << op.operator_type << ": {\n";
                if (op.operator_type == "only_if") {
                    write_only_if(op.only_iff, cur_tab + TAB);
                } else if (op.operator_type == "if") {
                    write_if(op.iff, cur_tab + TAB);
                } else if (op.operator_type == "while") {
                    write_while(op.whilee, cur_tab + TAB);
                } else if (op.operator_type == "bound") {
                    write_bound(op.variable_bounding, cur_tab + TAB);
                } else if (op.operator_type == "call") {
                    write_call(op.functionn, cur_tab + TAB);
                } else if (op.operator_type == "change") {
                    write_change(op.variable_change, cur_tab + TAB);
                } else {
                }
                std::cout << cur_tab << "}\n";
            }
        }

        static void write_function(const Function &func, const std::string &cur_tab) {
            std::cout << cur_tab << "signature: " << func.signature_to_str() << "\n";
        }

        void write_result() {
            std::cout << "{\n";
            std::string cur_tab(TAB);
            for (const auto &func: functions) {
                std::cout << cur_tab << "function: {\n";
                write_function(func, cur_tab + TAB);
                std::cout << cur_tab << "}\n";
                std::cout << cur_tab << "body: {\n";
                write_body(func.body, cur_tab + TAB);
                std::cout << cur_tab << "}\n";
            }
            std::cout << "}\n";
        }

    };

    try {
        Program my_program;
        my_program.read_program();
        my_program.write_result();
    } catch (const std::exception &e) {
        std::cout << "Error in program.\n";
        std::cout << e.what() << "\n";
    }
}