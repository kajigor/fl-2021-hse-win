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
    struct Program {
        struct My_exception : std::runtime_error {
            explicit My_exception(const std::string &s) : std::runtime_error(s) {}
        };

        struct Operator {
            std::string op;

            [[nodiscard]] std::string to_str() const {
                return op;
            }
        };

        struct Variable {
            std::string type;
            std::string name;
            std::string value;

            [[nodiscard]] std::string to_str() const {
                return type + " " + name;
            }
        };

        struct Body {
            const std::string TAB = std::string(4, ' ');
            std::vector<Operator> operators;
            std::vector<Variable> variables;

            [[nodiscard]] std::string to_str() const {
                std::string res;
                if (!variables.empty()) {
                    res += "variables:\n";
                    for (const auto &var: variables) {
                        res += TAB + var.to_str() + "\n";
                    }
                }
                res += "operators:\n";
                for (const auto &op: operators) {
                    res += TAB + op.to_str() + "\n";
                }
                return res;
            }
        };

        struct Only_if {
            std::string condition;
            Body body;

            [[nodiscard]] std::string to_str() const {
                return "only_if " + condition + " body";
            }
        };

        struct If {
            std::string condition;
            Body if_body, else_body;

            [[nodiscard]] std::string to_str() const {
                return "if " + condition + " body else body";
            }
        };

        struct While {
            std::string condition;
            Body body;

            [[nodiscard]] std::string to_str() const {
                return "while " + condition + " body";
            }
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
            std::getline(std::cin, s);
            std::getline(std::cin, s);
            int pos = static_cast<int>(s.find_first_not_of(' '));
            return s.substr(pos, s.size() - pos);
        }

        static bool is_number(const std::string &num) {
            if (num.size() < 2 || num.size() > 9) {
                return false;
            }
            if (num[0] == '0') {
                // all digits in [0-9]
                for (const auto &c : num) {
                    if (c < '0' || c > '9') {
                        return false;
                    }
                }
            } else if (num[0] == '1') {
                // all digits in [0-1]
                for (const auto &c : num) {
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

        static void check_var(const Variable &var, const std::vector<Variable> &vars) {
            for (const auto &v : vars) {
                if (v.name == var.name) {
                    throw My_exception("Variable has name same as other variable: '" + var.name + "'");
                }
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
                v.value = std::to_string(read_int());
            } else {
                std::string str = read_string();
                if (str.size() < 2 || str[0] != '"' || str.back() != '"') {
                    throw My_exception(
                            "Expect syntax: 'var string <name> = \"data\"', but found: 'var string <name> = " + str +
                            "'");
                }
                v.value = str.substr(1, str.size() - 2);
            }
        }

        void read_signature(Function &func) {
            func.name = read_string();
            func.argc = read_int();
            for (int i = 0; i < func.argc; ++i) {
                std::string type = read_string();
                check_type(type);
                std::string name_var = read_string();
                Variable var = {type, name_var, ""};
                check_var(var, func.argv);
                func.argv.push_back(var);
            }
        }

        std::string read_only_if() {
            Only_if only_if;
            only_if.condition = read_whole_string();
            read_body(only_if.body);
            read_end("only_if");
            return only_if.to_str();
        }

        std::string read_if() {
            If iff;
            iff.condition = read_whole_string();
            read_body(iff.if_body);
            std::string els = read_string();
            if (els != "else") {
                throw My_exception(
                        "Expect construction:\n\nbegin if\ncondition\nbody\nelse ...\n\n"
                        "But found:\n\nbegin if\ncondition\nbody\n" + els + " ...");
            }
            read_body(iff.else_body);
            read_end("if");
            return iff.to_str();
        }

        std::string read_while() {
            While whil;
            whil.condition = read_whole_string();
            read_body(whil.body);
            read_end("while");
            return whil.to_str();
        }

        std::string read_begin_smth() {
            std::string smth = read_string();
            if (smth == "only_if") {
                return read_only_if();
            } else if (smth == "if") {
                return read_if();
            } else if (smth == "while") {
                return read_while();
            } else {
                throw My_exception("Expect begin one of those (only_if, if, while), buf found: 'begin " + smth + "'");
            }
        }

        void read_body(Body &body) {
            read_begin("body");
            std::string starts_with;
            while (true) {
                starts_with = read_string();
                if (starts_with == "end") {
                    break;
                } else if (starts_with == "var") {
                    Variable v;
                    read_variable(v);
                    check_var(v, body.variables);
                    body.variables.push_back(v);
                } else if (starts_with == "begin") {
                    body.operators.push_back({read_begin_smth()});
                } else if (starts_with == "call") {
                    Function cur;
                    read_signature(cur);
                    body.operators.push_back({starts_with + " " + cur.signature_to_str()});
                } else if (starts_with == "skip") {
                    continue;
                } else if (starts_with == "change") {
                    std::string name_l = read_string();
                    std::string bounding = read_string();
                    if (bounding != "=") {
                        throw My_exception(
                                "Expect syntax: 'change <name> = ...', but found: 'change " + name_l + " " + bounding +
                                " ...'");
                    }
                    std::string equation = read_whole_string();
                    body.operators.push_back({starts_with + " " + name_l + " = " + equation});
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

        void write_result() {
            std::cout << "Functions in program:\n";
            int counter = 0;
            for (const auto &func: functions) {
                std::cout << ++counter << ": " << func.signature_to_str() << "\n\n";
                std::cout << func.body.to_str() << "\n";
            }
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