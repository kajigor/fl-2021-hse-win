#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

bool is_everything_ok = true;

struct Symbol {
private:
  std::string word;

public:
  explicit Symbol() = default;
  void read_word(std::string s) { word = s.substr(1, s.size() - 2); }
  std::string& get_word(){
      return word;
  };
  const std::string& get_word() const{
      return word;
  };
  bool operator==(const Symbol s) const {
    return get_word() == s.get_word();
  }
};

struct Transition {
private:
  int begin_state = 0;
  int end_state = 0;
  std::vector<Symbol> conditions;

public:
  explicit Transition() = default;
  void build_trans(std::string s) {
    int begin = 0;
    int i = 1;
    while (s[i] != ',') {
      if (s[i] < '0' || s[i] > '9') {
        is_everything_ok = false;
        return;
      }
      begin *= 10;
      begin += s[i] - '0';
      i++;
    }
    begin_state = begin;
    int end = 0;
    i += 2;
    while (s[i] != ',') {
      if (s[i] < '0' || s[i] > '9') {
        is_everything_ok = false;
        return;
      }
      end *= 10;
      end += s[i] - '0';
      i++;
    }
    end_state = end;
    i += 3;
    while (i < s.size()) {
      int count = 0;
      std::string t("\"");
      while (true) {
        if (s[i] == '\"' && (count % 2) == 0) {
          t += '\"';
          break;
        }
        if (s[i] == '\\') {
          count++;
        } else {
          count = 0;
        }
        if (i >= s.size()) {
          is_everything_ok = false;
          return;
        }
        t += s[i];
        i++;
      }
      i += 3;
      Symbol sy;
      sy.read_word(t);
      conditions.push_back(sy);
    }
  }

  int cond_size() {
    return conditions.size();
  }

  int get_begin() {
    return begin_state;
  }

  int get_end() {
    return end_state;
  }

  const std::vector<Symbol> get_cond() {
    return conditions;
  }

  void print(std::ofstream &fout) const {
    fout << begin_state << " -> " << end_state << " by symbols: ";
    for (const auto& sy : conditions) {
      fout << "\"" << sy.get_word() << "\" ";
    }
    fout << "\n";
  }
};

struct Alphabet {
private:
  std::vector<Symbol> alph;
public:
  void read_alph(std::string &s) {
    int i = 1;
    while (i < s.size()) {
      int count = 0;
      std::string t = "\"";
      while (true) {
        if (i > s.size()) {
          is_everything_ok = false;
          return;
        }
        if (s[i] == '\"' && (count % 2) == 0) {
          t += '\"';
          break;
        }
        if (s[i] == '\\') {
          count++;
        } else {
          count = 0;
        }
        t += s[i];
        i++;
      }
      i += 3;
      Symbol sy;
      sy.read_word(t);
      alph.push_back(sy);
    }
  }

  void print(std::ofstream &fout) {
    for (const auto& sy : alph) {
      fout << '\"' << sy.get_word() << "\" ";
    }
  }

  int alph_size() {
    return alph.size();
  }

  std::vector<Symbol>& get_alph() {
    return alph;
  }

  void test_alph(std::ofstream &fout) {
    if (alph.empty()) {
      fout << "Alphabet is empty";
      return;
    }
    for (int i = 0; i < alph.size(); i++) {
      for (int j = i + 1; j < alph.size(); j++) {
        if (alph[i] == alph[j]) {
          fout << "Alphabet has non-unique symbols\n";
          return;
        }
      }
    }
    fout << "Alphabet consists only of unique symbols\n";
  };
};

struct Automata {
private:
  int start_state = -1;
  int total_amount_of_states = 0;
  std::vector<int> terminal;
  std::vector<std::vector<Symbol>> determine;
  std::vector<Transition> transits;
  Alphabet al;
public:
  explicit Automata() = default;
  void read_al(std::string &s) {
    al.read_alph(s);
  }

  void set_start_state(int s) {
    start_state = s;
  }

  void set_total(int t) {
    total_amount_of_states = t;
  }

  void read_transits(std::string &s) {
    int i = 1;
    while (i < s.size()) {
      int count_b = 0;
      int count_s = 0;
      std::string t = "(";
      while (true) {
        if (i >= s.size()) {
          is_everything_ok = false;
          return;
        }
        if (s[i] == ')' && (count_b % 2) == 0) {
          t += ')';
          break;
        }
        if (s[i] == '\\') {
          count_s++;
        }
        else if (s[i] == '\"' && (count_s % 2) == 0) {
          count_b++;
          count_s = 0;
        }
        else {
          count_s = 0;
        }
        t += s[i];
        i++;
      }
      i += 3;
      Transition tr;
      tr.build_trans(t);
      transits.push_back(tr);
    }
  }

  void get_terminal(std::string & s) {
    int i = 0;
    while (i < s.size()) {
      int t = 0;
      while (i < s.size() && s[i] != ' ') {
        if (s[i] < '0' || s[i] > '9') {
          is_everything_ok = false;
          return;
        }
        t *= 10;
        t += (s[i] - '0');
        t += (s[i] - '0');
        i++;
      }
      terminal.push_back(t);
      while (s[i] == ' ') {
        i++;
      }
    }
  }

  void print_al(std::ofstream &fout) {
    fout << "Alphabet is :";
    al.print(fout);
  }

  void print_terminal(std::ofstream &fout) {
    fout << "Terminal states is: ";
    for (const auto i : terminal) {
      fout << i << " ";
    }
    fout << "\n";
  }

  void print_transits(std::ofstream &fout) {
    fout << "Transits is :\n";
    for (const auto& t : transits) {
      t.print(fout);
    }
  }

  void print_au(std::ofstream &fout) {
    fout << "Total amount of states is: " << total_amount_of_states << "\n";
    print_al(fout);
    fout << "\n";
    fout << "Start state is: " << start_state << '\n';
    print_terminal(fout);
    print_transits(fout);
  }

  void test_start_state(std::ofstream &fout) {
    if (start_state >= 0 && start_state < total_amount_of_states) {
      fout << "Automata has Start State\n";
    }
    else {
      fout << "Start State is missing\n";
    }
  }

  void test_alph(std::ofstream &fout) {
    al.test_alph(fout);
  }

  void test_full(std::ofstream &fout) {
    int sum = 0;
    for (auto &t : transits) {
      sum += t.cond_size();
    }
    if (al.alph_size() * total_amount_of_states == sum) {
      fout << "Automata is full\n";
    }
    else {
      fout << "Automata is not full\n";
    }
  }

  void test_determine(std::ofstream &fout) {
    determine.resize(total_amount_of_states);
    for (auto & t : transits) {
      for (auto & c : t.get_cond()) {
        determine[t.get_begin()].push_back(c);
      }
    }
    for (auto & v : determine) {
      for (int i = 0; i < v.size(); i++) {
        for (int j = i + 1; j < v.size(); j++) {
          if (v[i] == v[j]) {
            fout << "Automata is not determine\n";
          }
        }
      }
    }
    fout << "Automata is determine\n";
  }

  void test_transits(std::ofstream &fout) {
    for (auto t : transits) {
      if (t.get_begin() < 0 || t.get_begin() >= total_amount_of_states || t.get_end() < 0 || t.get_end() >= total_amount_of_states) {
        fout << "Some Transits has incorrect data\n";
        return;
      }
      for (auto &c : t.get_cond()) {
        bool b;
        for (auto &s : al.get_alph()) {
          if (c == s) {
            b = false;
            break;
          }
        }
        if (b) {
          fout << "Some Transits has incorrect data\n";
          return;
        }
      }
    }
    fout << "All Transits are correct";
  }

  void test(std::ofstream &fout) {
    test_start_state(fout);
    fout << "Each state is unique\n";
    test_alph(fout);
    test_determine(fout);
    test_full(fout);
    test_transits(fout);
  }
};

int read_int(std::string &s) {
  int t = 0;
  int i = 0;
  while (i < s.size()) {
    if (s[i] < '0' || s[i] > '9') {
      is_everything_ok = false;
      break;
    }
    t *= 10;
    t += s[i] - '0';
    i++;
  }
  return t;
}

int main(int argc, char *argv[]) {
  std::ifstream fin(argv[1]);
  std::ofstream fout(std::string(argv[1]) + ".out");
  Automata au;
  for (int i = 0; i < 5 && is_everything_ok; i++) {
    std::string s;
    std::getline(fin, s);
    if (i == 0) {
      if (s.substr(0, 7) != "Alph = ") {
        is_everything_ok = false;
        break;
      }
      s = s.substr(7);
      au.read_al(s);
    }
    if (i == 1) {
      if (s.substr(0, 9) != "States = ") {
        is_everything_ok = false;
        break;
      }
      s = s.substr(9);
      au.set_total(read_int(s));
    }
    if (i == 2) {
      if (s.substr(0, 14) != "Start_state = ") {
        is_everything_ok = false;
        break;
      }
      s = s.substr(14);
      au.set_start_state(read_int(s));
    }
    if (i == 3) {
      if (s.substr(0, 16) != "Accept_states = ") {
        is_everything_ok = false;
        break;
      }
      s = s.substr(16);
      au.get_terminal(s);
    }
    if (i == 4) {
      if (s.substr(0, 11) != "Transits = ") {
        is_everything_ok = false;
        break;
      }
      s = s.substr(11);
      au.read_transits(s);
    }
  }
finish:
  if (is_everything_ok) {
    fout << "Automata is correct\n";
    au.print_au(fout);
    au.test(fout);
  }
  else {
    fout << "Incorrect input";
  }
  return 0;
}