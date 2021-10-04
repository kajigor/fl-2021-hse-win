#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>


enum State {
    start,
    terminal,
    non_terminal,
};

struct Edge {
    Edge(std::string &from_,
         std::string &to_) : from(from_), to(to_) {
        words = std::vector<std::string>();
    }

private:
    std::string from;
    std::string to;
    std::vector<std::string> words;;

public:
    std::string &get_start_vertex() &{
        return from;
    }

    std::string &get_dest_vertex() &{
        return to;
    }

    void add_word(std::string &word) {
        words.push_back(word);
    }

    int words_num() {
        return words.size();
    }

    std::string &get_word(int i) &{
        return words[i];
    }
};


struct Vertex {
private:
    std::string name;
    State state;
public:
    Vertex(std::string &name_, State state_) : name(name_), state(state_) {};

    std::string get_vertex_name() {
        return name;
    };

    std::string get_vertex_state() {
        if (state == start) return "start";
        if (state == terminal) return "terminal";
        if (state == non_terminal) return "non_terminal";
        return "";
    };
};

struct Word {
    std::string word;

    explicit Word(std::string &word_) : word(word_) {};
};

struct Automation {
    std::vector<Word> words;
    std::map<std::string, Vertex> vertexes;
    std::vector<Edge> edges;

    Automation() {
        words = std::vector<Word>();
        vertexes = std::map<std::string, Vertex>();
        edges = std::vector<Edge>();
    }

    void add_word(std::string &word) {
        Word tmp(word);
        words.push_back(tmp);
    }

    void add_start_vertex(std::string &v_name) {
        Vertex vr(v_name, start);
        vertexes.insert({v_name, vr});
    }

    void add_terminal_vertex(std::string &v_name) {
        if (vertexes.find(v_name) == vertexes.end()) {
            Vertex vr(v_name, terminal);
            vertexes.insert({v_name, vr});
        }
    }

    void add_non_terminal_vertex(std::string &v_name) {
        if (vertexes.find(v_name) == vertexes.end()) {
            Vertex vr(v_name, non_terminal);
            vertexes.insert({v_name, vr});
        }
    }

    void add_edge(Edge &e) {
        edges.push_back(e);
    }
};

std::string read_word(std::ifstream &in, char &end) {
    char next;
    int symb;
    std::string answer;
    do {
        try {
            in >> symb;
            answer += symb;
            in >> next;
        } catch (...) {
            std::cerr << "Incorrect word symb" << std::endl;
            break;
        }
    } while (next == '~');
    end = next;
    return answer;
}

std::string get_vertex_name(std::ifstream &in) {
    std::string input;
    in >> input;
    bool symb = true;
    for (char i: input) {
        if ((isalpha(i) && !symb) || (!std::isdigit(i) && !isalpha(i))) {
            std::cerr << "Incorrect vertex name" << std::endl;
        } else if (std::isdigit(i)) {
            symb = false;
        }
    }
    return input;
}


int main(int argc, char *argv[]) {

    std::ifstream in(argv[1]); // окрываем файл для чтения
    std::ofstream out(std::string(argv[1]) + ".out");
    Automation automation;

    char next;
    do {
        in >> next;
        if (next != '[') break;
        char end;
        std::string word = read_word(in, end);
        if (end != ']') {
            std::cerr << "Incorrect end of word" << std::endl;
        }
        automation.add_word(word);
    } while (true);

    while (!in.eof()) {
        std::string key_word;
        in >> key_word;
        if (next != ' ') key_word = next + key_word;
        if (key_word == "start") {
            std::string start_name = get_vertex_name(in);
            automation.add_start_vertex(start_name);
        } else if (key_word == "terminal") {
            std::string terminal_name = get_vertex_name(in);
            automation.add_terminal_vertex(terminal_name);
        } else if (key_word == "transition") {
            in >> next;
            if (next != '(') {
                std::cerr << "Incorrect transition" << std::endl;
                break;
            }
            std::string v_name_1 = get_vertex_name(in);
            automation.add_non_terminal_vertex(v_name_1);
            std::string arrow;
            in >> arrow;
            if (arrow != "->") {
                std::cerr << "Incorrect transition (arrow)" << std::endl;
                break;
            }
            std::string v_name_2 = get_vertex_name(in);
            automation.add_non_terminal_vertex(v_name_2);
            in >> next;
            if (next != ',') {
                std::cerr << "Incorrect transition (comma)" << std::endl;
                break;
            }
            in >> next;
            if (next != '{') {
                std::cerr << "Incorrect transition (figure bracket)" << std::endl;
                break;
            }
            Edge e(v_name_1, v_name_2);
            char end;
            do {
                std::string word = read_word(in, end);
                e.add_word(word);
            } while (end == ',');
            if (end != '}') {
                std::cerr << "Incorrect transition (figure bracket)" << std::endl;
                break;
            }
            in >> next;
            if (next != ')') {
                std::cerr << "Incorrect transition (round bracket)" << std::endl;
                break;
            }
            automation.add_edge(e);
        } else {
            if (key_word.empty()) break;
            std::cerr << "Incorrect key word" << std::endl;
        }
        next = ' ';
    }

    out << "The list of words: ";
    for (int i = 0; i < automation.words.size() - 1; i++) {
        out << automation.words[i].word << ", ";
    }
    out << automation.words[automation.words.size() - 1].word << std::endl;
    out << "The list of vertexes: \n";
    for (auto vertex: automation.vertexes) {
        out << vertex.second.get_vertex_name() << ": " << vertex.second.get_vertex_state() << std::endl;
    }
    out << "The list of edges: \n";
    for (auto e: automation.edges) {
        out << "Start vertex: " << e.get_start_vertex() << ". End vertex: " << e.get_dest_vertex()
                  << ". Transition words: ";
        for (int i = 0; i < e.words_num() - 1; i++) {
            out << e.get_word(i) << ", ";
        }
        out << e.get_word(e.words_num() - 1) << std::endl;
    }
    in.close();
    out.close();
    return 0;
}
