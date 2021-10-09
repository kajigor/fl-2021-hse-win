#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

struct parse_exception { int line_num; };

auto serialize(const int q, const auto& words, const auto& states, const auto& terminals) {
    const int n = states.size();
    const int m = states[0].size();
    const int t = terminals.size();
    std::string result = R"(class DFA {

    int dsa;

};
    )";
    

    return result;
}


int main() {
    using std::cin, std::cout, std::cerr;

    auto read_line = [line_num = 0](auto& is, const char start_char) mutable {
        ++line_num;
        std::string line;
        std::getline(is, line);
        auto start_str = start_char + std::string{": "};
        if (line.compare(0, 3, start_str)) {
            throw parse_exception{line_num};
        }
        return line.substr(3);
    };

    try {
        std::stringstream ss(read_line(cin, 's')); //TODO: error if not (\w|\s)*

        size_t n, m, q, t;
        ss >> n >> m >> q >> t;

        auto non_zero = [](const int n, const std::string& c) {
            if (n == 0) {
                throw std::invalid_argument(c + " must be greater then zero");
            }
        };
        non_zero(n, "n");
        non_zero(m, "m");
        auto compare_with_n = [&n](const int q, const std::string& c) {
            if (q > n) {
                throw std::invalid_argument(c + " must be not greater when n");
            }
        };
        compare_with_n(q + 1, "q + 1");
        compare_with_n(t, "t");

        std::unordered_map<std::string, size_t> word_to_num;
        std::vector< std::vector<size_t> > next_state(n, std::vector<size_t>(m));
        std::vector<size_t> terminals(t);

        for (size_t i=0; i < m; ++i) {
            const auto& [it, is_inserted] = word_to_num.emplace(read_line(cin, 'w'), i); //TODO: change \\ to \ etc.
            if (!is_inserted) {
                throw std::invalid_argument("Repeated word: \"" + it->first + "\"");
            }
        }

        for (auto& i : next_state) {
            ss = std::stringstream(read_line(cin, 'n'));
            for (auto& j : i) {
                ss >> j;
                if (j >= n) {
                    throw std::invalid_argument("States must be in 0..(n - 1)");
                }
            } //TODO: check for empty ss
        }

        ss = std::stringstream(read_line(cin, 't'));
        for (auto& i : terminals) {
            ss >> i;
        } //TODO: check for empty ss

        cout << serialize(q, word_to_num, next_state, terminals);

    } catch (parse_exception& e) {
        cerr << "Can't parse " << e.line_num << " line\n";
        return 1;
    } catch (std::invalid_argument& e) {
        cerr << e.what() << '\n';
        return 2;
    }

    return 0;
}
