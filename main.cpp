#include <bits/stdc++.h>
#include <string>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        std::cout << "Usage: <program> <path/to/test>\n";
        return 0;
    }
    std::string file = argv[1];
    if (!freopen(file.c_str(), "r", stdin)) {
        std::cout << "Unable to open file: '" + file + "'\n";
        return 0;
    }
    if (!freopen((file + ".out").c_str(), "w", stdout)) {
        std::cout << "Unable to open file: '" + file + ".out" + "'\n";
        return 0;
    }
    struct DFA {
        const std::string ALPHABET = "Alphabet",
                STATES = "States",
                EDGES = "Edges",
                TERMINAL = "Terminals",
                TO = "to",
                BY = "by";

        std::vector<std::string> alphabet;
        std::vector<std::vector<std::vector<std::string>>> transpositions;
        int start = 0, num_states{};
        std::vector<int> terminals;

        static void error(const std::string &expect, const std::string &found) {
            std::cout << "Error: \nexpect: '" + expect + "'\nfound: '" + found + "'" << "\n";
        }

        static void bad_input() {
            not_DFA();
            std::cout << "Incredible bad input:\n";
        }

        int try_read() {
            auto read_string = [&]() {
                std::string s;
                std::cin >> s;
                return s;
            };

            auto read_alphabet = [&]() {
                auto tmp = read_string();
                if (tmp != ALPHABET) {
                    error(ALPHABET, tmp);
                    return 1;
                }
                int alphabet_size;
                std::cin >> alphabet_size;
                if (alphabet_size < 0) {
                    bad_input();
                    std::cout << "alphabet_size < 0\n";
                    return 1;
                }
                alphabet.resize(alphabet_size);
                for (auto &c: alphabet) {
                    std::cin >> c;
                }
                return 0;
            };
            if (read_alphabet()) {
                return 1;
            }

            auto read_states = [&]() {
                auto tmp = read_string();
                if (tmp != STATES) {
                    error(STATES, tmp);
                    return 1;
                }
                std::cin >> num_states;
                if (num_states < 0) {
                    bad_input();
                    std::cout << "num_states < 0\n";
                    return 1;
                }
                transpositions.resize(num_states, std::vector<std::vector<std::string>> (num_states));
                return 0;
            };
            if (read_states()) {
                return 1;
            }

            auto read_edges = [&]() {
                auto tmp = read_string();
                if (tmp != EDGES) {
                    error(EDGES, tmp);
                    return 1;
                }
                int num_edges;
                std::cin >> num_edges;
                for (int i = 0; i < num_edges; ++i) {
                    int x, y;
                    std::cin >> x;
                    auto tmpp = read_string();
                    if (tmpp != TO) {
                        error(TO, tmpp);
                        return 1;
                    }
                    std::cin >> y;
                    tmpp = read_string();
                    if (tmpp != BY) {
                        error(BY, tmpp);
                        return 1;
                    }
                    transpositions[x][y].push_back(read_string());
                }
                return 0;
            };
            if (read_edges()) {
                return 1;
            }

            auto read_terminals = [&]() {
                auto tmp = read_string();
                if (tmp != TERMINAL) {
                    error(TERMINAL, tmp);
                    return 1;
                }
                int num_terminals;
                std::cin >> num_terminals;
                if (num_terminals < 0) {
                    bad_input();
                    std::cout << "num_terminals < 0\n";
                }
                terminals.resize(num_terminals);
                for (auto &x : terminals) {
                    std::cin >> x;
                }
                return 0;
            };
            if (read_terminals()) {
                return 1;
            }

            return 0;
        }

        void print() {
            std::cout << "DFA {\n";
            std::cout << "  " << ALPHABET << " " << alphabet.size() << ": {";
            for (int i = 0; i < alphabet.size(); ++i) {
                if (i) {
                    std::cout << ", ";
                }
                std::cout << alphabet[i];
            }
            std::cout << "}\n";

            std::cout << "  " << STATES << " " << num_states << ": {";
            for (int i = 0; i < num_states; ++i) {
                if (i) {
                    std::cout << ", ";
                }
                std::cout << i;
            }
            std::cout << "}\n";

            std::cout << "  " << "Transpositions:" << "\n";
            for (int i = 0; i < num_states; ++i) {
                for (int j = 0; j < num_states; ++j) {
                    std::cout << "    between states " << i << " and " << j << ": ";
                    std::cout << "{";
                    for (int k = 0; k < transpositions[i][j].size(); ++k) {
                        if (k) {
                            std::cout << ", ";
                        }
                        std::cout << transpositions[i][j][k];
                    }
                    std::cout << "}\n";
                }
            }

            std::cout << "  " << TERMINAL << " " << terminals.size() << ": {";
            for (int i = 0; i < terminals.size(); ++i) {
                if (i) {
                    std::cout << ", ";
                }
                std::cout << terminals[i];
            }
            std::cout << "}\n";

            std::cout << "}\n";
        }

        bool is_alphabet_unique() {
            for (int i = 0; i < alphabet.size(); ++i) {
                if (count(alphabet.begin(), alphabet.begin() + i, alphabet[i])) {
                    return false;
                }
            }
            return true;
        }

        int check_edges_DFA() {
            for (int i = 0; i < num_states; ++i) {
                std::set<std::string> transpositions_from_i;
                for (int j = 0; j < num_states; ++j) {
                    for (const auto &c : transpositions[i][j]) {
                        if (transpositions_from_i.count(c)) {  // twice on same string
                            return 1;
                        }
                        transpositions_from_i.insert(c);
                    }
                }
                for (const auto &c : alphabet) {
                    if (transpositions_from_i.count(c)) {
                        transpositions_from_i.erase(c);
                    } else {  // unknown string
                        return 2;
                    }
                }
                if (!transpositions_from_i.empty()) {  // too many transpositions
                    return 3;
                }
            }
            return 0;
        }

        static void not_DFA() {
            std::cout << "Graph is not DFA\n";
        }

        int check() {
            // start state is 0
            // all states are unique because of language construction
            if (!is_alphabet_unique()) {
                not_DFA();
                std::cout << "Symbols alphabet is not unique\n";
                return 1;
            }
            int code = check_edges_DFA();
            if (code == 0) {
                return 0;
            }
            not_DFA();
            if (code == 1) {
                std::cout << "Same edge appearance twice in the same vertex's list\n";
            } else if (code == 2) {
                std::cout << "Unknown string in transposition\n";
            }
            return 1;
        }
    };
    DFA dfa;
    if (dfa.try_read()) {  // error
        return 0;
    }
    dfa.print();
    if (dfa.check()) {  // error
        return 0;
    }
    std::cout << "Graph is DFA\n";
    return 0;
}
