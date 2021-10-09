#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <set>

std::string serialize_vector(size_t v) {
    return std::to_string(v);
}

std::string serialize_vector(std::pair<const std::string, size_t> v) {
    return '{' + v.first + ", " + std::to_string(v.second) + '}';
}

std::string serialize_vector(const auto& v) {
    std::stringstream ss;
    
    ss << '{';
    for (const auto& i : v) {
        ss << serialize_vector(i) << ", ";
    }
    ss.seekp(-2, std::ios_base::end);
    ss << '}';
    ss.seekp(-1, std::ios_base::end);
    ss << '\0';

    return ss.str();
}

auto serialize(const int q, const auto& words, const auto& states, const auto& terminals) {
    const int n = states.size();
    const int m = states[0].size();
    const int t = terminals.size();

    std::string words_str = serialize_vector(words);
    std::string states_str = serialize_vector(states);
    std::string terminals_str = serialize_vector(terminals);

    std::stringstream ss;
    ss
    << "#ifndef GENERATED_DFA\n"
    << "#define GENERATED_DFA\n"
    << "\n"
    << "#include <unordered_map>\n"
    << "#include <vector>\n"
    << "#include <set>\n"
    << "\n"
    << "struct DFA {\n"
    << "    int n = " << n << ";\n"
    << "    int m = " << m << ";\n"
    << "    int q = " << q << ";\n"
    << "    int t = " << t << ";\n"
    << "\n"
    << "    std::unordered_map<std::string, size_t> word_to_num = " << words_str << ";\n"
    << "    std::vector< std::vector<size_t> > next_state(n, std::vector<size_t>(m)) = " << states_str << ";\n"
    << "    std::vector<size_t> terminals(t) = " << terminals_str << ";\n"
    << "};\n"
    << "\n"
    << "#endif //GENERATED_DFA\n";

    return ss.str();
}


int main() {

    int line_num = 0;
    auto read_line = [&line_num](auto& is, const char start_char) mutable {
        ++line_num;
        std::string line;
        std::getline(is, line);
        auto start_str = start_char + std::string{": "};
        if (line.compare(0, 3, start_str)) {
            throw std::runtime_error("start characters must be \"" + start_str + "\"");
        }
        return line.substr(3);
    };

    try {
        using std::cin;

        std::stringstream ss(read_line(cin, 's'));

        size_t n, m, q, t;
        if (!(ss >> n >> m >> q >> t)) {
            throw std::runtime_error("first line must contains 4 numbers");
        }

        auto non_zero = [](const int n, const std::string& c) {
            if (n == 0) {
                throw std::runtime_error(c + " must be greater then zero");
            }
        };
        non_zero(n, "n");
        non_zero(m, "m");
        auto compare_with_n = [&n](const int q, const std::string& c) {
            if (q > n) {
                throw std::runtime_error(c + " must be not greater when n");
            }
        };
        compare_with_n(q + 1, "q + 1");
        compare_with_n(t, "t");

        auto get_num_err = [](const size_t expected) {
            return "expected " + std::to_string(expected) + " numbers";
        };

        auto ss_empty = [&ss, &get_num_err](const size_t expected) {
            if (int t; ss >> t) {
                throw std::runtime_error(get_num_err(expected));
            }
        };

        auto check_word = [](const auto& word) {
            char prev = '\0';
            constexpr auto err_msg = "after \"\\\" must be \"\\\" or \"m\"";
            for (char cur : word) {
                if (prev == '\\' && cur != '\\' && cur != 'n') {
                    throw std::runtime_error(err_msg);
                }
                prev = cur;
            }
            if (prev == '\\') {
                throw std::runtime_error(err_msg);
            }
        };

        std::unordered_map<std::string, size_t> word_to_num;
        std::vector< std::vector<size_t> > next_state(n, std::vector<size_t>(m));
        std::set<size_t> terminals;

        for (size_t i=0; i < m; ++i) {
            const auto& [it, is_inserted] = word_to_num.emplace(read_line(cin, 'w'), i);
            if (!is_inserted) {
                throw std::runtime_error("Repeated word: \"" + it->first + "\"");
            }
            check_word(it->first);
        }

        auto read_num = [&ss, &get_num_err](const size_t expected) {
            size_t x;
            if (!(ss >> x)) {
                throw std::runtime_error(get_num_err(expected));
            }
            return x;
        };

        for (auto& i : next_state) {
            ss = std::stringstream(read_line(cin, 'n'));
            for (auto& j : i) {
                if ((j = read_num(m)) >= n) {
                    throw std::runtime_error("States must be in 0..(n - 1)");
                }
            }
            ss_empty(m);
        }

        ss = std::stringstream(read_line(cin, 't'));
        for (size_t i=0; i < t; ++i) {
            const auto& [it, is_inserted] = terminals.emplace(read_num(t));
            if (!is_inserted) {
                throw std::runtime_error("Repeated terminal state: " + std::to_string(*it));
            }
        }
        ss_empty(t);

        std::cout << serialize(q, word_to_num, next_state, terminals);
    } catch (std::runtime_error& e) {
        std::cerr << "line " << std::to_string(line_num) << ": " << e.what() << '\n';
        return 1;
    }

    return 0;
}
