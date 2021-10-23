#include <vector>
#include <unordered_set>
#include <queue>
#include <functional>
#include <fstream>
#include <set>
#include <iostream>
#include <string>
#include <time.h>

using namespace std;

struct Tr {
    int i, j;
    int a;
};

struct par {
    int C;
    int a;
};

int main(int argc, char *argv[]) {
    //  Отрываем файл, в который питон нам записал данные текущего ДКА
    ifstream input_file("cpp_hopcroft.txt");
    string cond;
    getline(input_file, cond);
    if (cond == "checks failed") {
        return 0;
    }

    int n, m, k, c; //  n-- кол-во элементов в алфавите,
    //  m-- кол-во состояний,
    //  k-- кол-во терминальных состояний
    //  с-- кол-во переходов
    input_file >> n;

    vector<string> alphabet(n);
    for (int i = 0; i < n; i++) {
        input_file >> alphabet[i];
    }

    input_file >> m >> k >> c;

    int starting_vertex_number;
    input_file >> starting_vertex_number;

    vector<bool> states(m, 0); //  терманальная = 1, нетерминальная = 0
    for (int i = 0; i < k; i++) {
        int a;
        input_file >> a, states[a] = true;
    }

    vector<unordered_set<int>> P(2); //  массив множеств ("номер класса" -> "элементы класса")
    vector<int> Class(m);
    queue<par> Q;
    vector<vector<vector<int>>> Inv(m, vector<vector<int>>(n));
    vector<int> Involved;
    vector<int> Count(m);
    vector<int> Twin(m);
    vector<vector<int>> StateToState(m, vector<int>(n));

    for (int i = 0; i < c; i++) {
        int u, v, a; //  ребро "u -> v" по символу "a"
        input_file >> u >> v >> a;
        StateToState[u][a] = v;
        Inv[v][a].push_back(u);
    }

    function<void()> Hopcroft = [&]() {
        for (int i = 0; i < m; i++) { //  P <- {T, Q\T}
            if (states[i]) {
                P[1].insert(i), Class[i] = 1;
            } else {
                P[0].insert(i), Class[i] = 0;
            }
        }

        for (int i = 0; i < n; i++) {
            Q.push({ 0, i }), Q.push({ 1, i });
        }

        while (!Q.empty()) {
            auto v = Q.front(); //  <-- <C, a>, C-- номер "сплиттера"
            Q.pop();

            Involved.clear();
            for (auto q : P[v.C]) {
                for (auto r : Inv[q][v.a]) {   //  все вершины, по которым по символу "a" можно перейти в "сплиттер".
                    //  Действительно, а зачем другое вершины...
                    int i = Class[r];		   //  берем класс состояний, в котором лежит состояние "r"
                    if (Count[i] == 0) {	   //
                        Involved.push_back(i); //  строим множество состояний, из которых можно перейти в "сплиттер" <С, a>
                    }
                    Count[i]++;
                }
            }

            for (auto i : Involved) {
                if (Count[i] < P[i].size()) {
                    Twin[i] = P.size();
                    P.push_back({});
                }
            }

            unordered_set<int> C = P[v.C];
            for (auto q : C) {
                for (auto r : Inv[q][v.a]) {
                    int i = Class[r];
                    int j = Twin[i];
                    if (j != 0) {
                        P[i].erase(r);
                        P[j].insert(r);
                    }
                }
            }

            for (auto i : Involved) {
                int j = Twin[i];
                if (j != 0) {
                    if (P[j].size() > P[i].size()) {
                        swap(P[i], P[j]); //  быстро или долго?-- Быстро, swap "u_set"-ов с C++98 работает за константу
                    }
                    for (auto r : P[j]) {
                        Class[r] = j;
                    }
                    for (int i = 0; i < n; i++) {
                        Q.push({ j, i });
                    }
                }
                Count[i] = 0;
                Twin[i] = 0;
            }
        }
    };
    double start, end;
    if (cond == "stress test") {
        start = clock();
    }
    Hopcroft();
    if (cond == "stress test") {
        end = clock();
    }
    //  Построим новый автомат, если он меньше, чем исходный...

    vector<unordered_set<int>> new_P;

    for (const auto& Set : P) {
        if (Set.size() != 0) {
            for (int state : Set) {
                Class[state] = new_P.size();
            }
            new_P.push_back(Set);
        }
    }
    fstream output_file;
    if (cond == "stress test") {
        output_file.open(argv[1]);
    }
    else {
        output_file.open(argv[1], std::ios::app);
    }

    if (new_P.size() >= m && cond != "stress test") {
        output_file << "\nThe automaton is already minimal!\n\n";
        return 0;
    }
    else {
        m = new_P.size();
    }

    vector<Tr> trans; //  переходы
    vector<int> terminal_vertices;

    for (auto& Set : new_P) {
        int j = *Set.begin(); // все состояния ведь неразличимы, поэтому рассматриваем одного представителя класса...
        if (states[j]) {
            terminal_vertices.push_back(Class[j]);
        }
        for (int c = 0; c < n; c++) {
            trans.push_back({ Class[j], Class[StateToState[j][c]], c });
        }
    }

    function<void()> write_to_file = [&]() {
        if (cond != "stress test") {
            output_file << "\nYour automaton can be minimized:\n\n";
            output_file << "Alf: {";
            for (int i = 0; i < n - 1; i++) {
                output_file << alphabet[i] << ", ";
            }
            output_file << alphabet[n - 1] << "}\n";

            output_file << "Start: q" << Class[starting_vertex_number] << "(S)\n";

            output_file << "Vertices: ";
            for (int i = 0; i < m - 1; i++) {
                output_file << "q" << i << "(" << (states[*new_P[i].begin()] ? "T" : "")
                << "), ";
            }
            output_file << "q" << m - 1 << "(" << (states[*new_P[m - 1].begin()] ? "T" : "") << ")\n";

            output_file << "Edges: ";
            for (const auto& tran : trans) {
                output_file << "(q" << tran.i << ",q" << tran.j << "){" << alphabet[tran.a] << "}; ";
            }
            output_file << "\n\n";
        } else {
            output_file << "Spent time:\n\t" << (end - start) / (double)CLOCKS_PER_SEC << " sec" << "\n\n";
        }
    };

    write_to_file();

    return 0;
}
