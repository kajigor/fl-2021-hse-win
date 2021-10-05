#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
#include <fstream>
#include <algorithm>

struct Edge{
    std::string to;
    std::string letter;
};

struct Vertex{
private:
    int state;
    int name;
    int count_transitions = 0;

public:
    std::unordered_map<std::string, std::pair<int,int>> transitions;

    Vertex(int name_, int state_) : name(name_), state(state_){};
    int get_name() const{
        return name;
    }
    int get_state() const{
        return state;
    }
    int& get_count_transtions(){
        return count_transitions;
    }
    bool operator()(const Vertex &ver1, const Vertex &ver2) const{
        if(ver1.state < ver2.state){
            return true;
        } else if(ver1.state == ver2.state){
            return ver1.name < ver2.name;
        } else {
            return false;
        }
    }
};

struct DFA{
    std::unordered_map<std::string,int> alphabet;
    std::unordered_map<int, int> id_vertex;
    std::vector<Vertex> all_vertex;
    std::vector<std::string> alphabet_string;

    bool there_is_start_state = false;
    bool there_is_only_start_state = true;
    bool found_terminal_vertex = false;
    bool vertex_unique = true;
    bool alphabet_unique = true;
    bool is_dfa = true;
    bool is_full_dfa = true;

    std::size_t count_vertex = 0;
};


namespace{
    DFA dfa;
    std::string file_name_input;
    std::string file_name_output;
    std::ifstream input;
    std::ofstream output;

    bool count_vertex_correct = true;
}

void get_count_number(std::string &s){
    std::string number;
    int i = 0;
    for(; i < s.size(); i++){
        if('0' <= s[i] && s[i] <= '9'){
            number += s[i];
        } else if (s[i] == ' '){
            i++;
            break;
        } else {
            count_vertex_correct = false;
            break;
        }
    }

    if(!count_vertex_correct){
        std::cerr << "1:" << i + 1 << ": ожидалось число, получено некорректное число!" << std::endl;
        return;
    }

    dfa.count_vertex = std::stoi(number);
    for(; i < s.size(); i++){
        if(s[i] != '}'){
            std::cerr << "1:" << i + 1 << ": не найден файл \"}\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != ' '){
            std::cerr << "1:" << i + 1 << ": после \"}\" найден символ, которого не должно быть!" << std::endl;
        }
    }
}

void get_alphabet(std::string &s){
    int i = 0;

    while(i < s.size()) {
        for (; i < s.size(); i++) {
            if (s[i] != '#') {
                std::cerr << "2:" << i + 1 << ": вместо \"#\" найдено\"" << s[i] << "\"!" << std::endl;
            } else {
                i++;
                break;
            }
        }

        std::string letter;
        for (; i < s.size(); i++) {
            if (s[i-1] != '\\' && s[i] == '#'){
                if(dfa.alphabet[letter] == 0){
                    dfa.alphabet[letter] = 1;
                } else {
                    dfa.alphabet_unique = false;
                    std::cerr << "2:" << i + 1 << ": литерал \"" << letter << "\" уже был введён!" << std::endl;
                }
                letter = "";
                i++;   // чтобы перейти к следующему символу строки
                break; // т.к. я по итерациям иду, сначала нахожу один литерал, потом опять литерал ищу и т.д.
            } else {
                letter += s[i];
            }
        }

        if(letter != ""){
            std::cerr << "2:" << i + 1 << ": не найдет символ \"#\"!";
        }

        if(i < s.size() && s[i] != ' '){
            std::cerr << "2:" << i + 1 << ": ожидался пробел между литералами!" << std::endl;
        } else {
            i++; // чтобы пробел пройти, если он есть
        }
    }
}

Vertex get_vertex(std::string &s, int number_line){
    int i = 0;
    bool found_two_number = false;
    std::string name, state;

    for(; i < s.size(); i++){
        if('0' <= s[i] && s[i] <= '9'){
            name += s[i];
        } else if(s[i] != ' '){
            std::cerr << number_line << ":" << i + 1 << ": ожидался номер вершины, но получен символ \"" << s[i] << "\"!" << std::endl;
            return Vertex(-1,-1);
        } else {
            break;
        }
    }

    for (; i < s.size(); i++) {
        if (s[i] != ' ') {
            std::cerr << number_line << ":" << i + 1 << ": вместо \" \" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != ']'){
            std::cerr << number_line << ":" << i + 1 << ": вместо \"]\" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for (; i < s.size(); i++) {
        if (s[i] != ' ') {
            std::cerr << number_line << ":" << i + 1 << ": вместо \"-\" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != '-'){
            std::cerr << number_line << ":" << i + 1 << ": вместо \"]\" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != '>'){
            std::cerr << number_line << ":" << i + 1 << ": вместо \">\" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != ' '){
            std::cerr << number_line << ":" << i + 1 << ": вместо \" \" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if('0' <= s[i] && s[i] <= '2'){
            state = s[i];
            i++;
            found_two_number = true;
            break;
        } else if(s[i] != ' ') {
            std::cerr << number_line << ":" << i + 1 << ": ожидалось состояние вершины, но получен символ \"" << s[i]
                   << "\"!" << std::endl;
            return Vertex(-1, -1);
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != ' '){
            std::cerr << number_line << ":" << i + 1 << ": вместо \" \" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != '|'){
            std::cerr << number_line << ":" << i + 1 << ": вместо \"|\" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    if(found_two_number){
        return Vertex(std::stoi(name), std::stoi(state));
    } else {
        return Vertex(-1, -1);
    }
}

int get_edges(std::string s, int number_line){
    int i = 0;
    std::string name1, name2;

    for(; i < s.size(); i++){
        if('0' <= s[i] && s[i] <= '9'){
            name1 += s[i];
        } else if(s[i] != ','){
            std::cerr << number_line << ":" << i + 1 << ": ожидался номер вершины, но получен символ \"" << s[i] << "\"!" << std::endl;
            return 2;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if('0' <= s[i] && s[i] <= '9'){
            name2 += s[i];
        } else if(s[i] != ' '){
            std::cerr << number_line << ":" << i + 1 << ": ожидался номер вершины, но получен символ \"" << s[i] << "\"!" << std::endl;
            return 2;
        } else {
            i++;
            break;
        }
    }

    if(name1.size() == 0 || name2.size() == 0){
        return 0;
    }
    if(dfa.id_vertex[std::stoi(name1)] == 0 || dfa.id_vertex[std::stoi(name2)] == 0){
        return 0;
    }

    for(; i < s.size(); i++){
        if(s[i] != ':'){
            std::cerr << number_line << ":" << i + 1 << ": вместо \":\" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    for(; i < s.size(); i++){
        if(s[i] != ' '){
            std::cerr << number_line << ":" << i + 1 << ": вместо \" \" найдено\"" << s[i] << "\"!" << std::endl;
        } else {
            i++;
            break;
        }
    }

    while(i < s.size()) {
        for (; i < s.size(); i++) {
            if (s[i] != '#') {
                std::cerr << number_line << ":" << i + 1 << ": вместо \"#\" найдено\"" << s[i] << "\"!" << std::endl;
            } else {
                i++;
                break;
            }
        }

        std::string letter;
        for (; i < s.size(); i++) {
            if (s[i-1] != '\\' && s[i] == '#'){
                if(dfa.alphabet[letter] == 1) {
                    std::pair<int,int> p = {0,0};
                    if (dfa.all_vertex[dfa.id_vertex[std::stoi(name1)] - 1].transitions[letter] == p) {
                        dfa.all_vertex[dfa.id_vertex[std::stoi(name1)] - 1].transitions[letter] = {1,std::stoi(name2)};
                        dfa.all_vertex[dfa.id_vertex[std::stoi(name1)] - 1].get_count_transtions()++;
                    } else {
                        dfa.is_dfa = false;
                        std::cerr << number_line << ":" << i + 1 << ": литерал \"" << letter << "\" уже был введён!"
                               << std::endl;
                        std::cerr << number_line << ":" << i + 1 << ": ОСТОРОЖНО ТЕПЕРЬ АВТОМАТ НЕДЕРМИНИРОВАН!"
                               << std::endl;
                    }
                } else {
                    std::cerr << number_line << ":" << i + 1 << ": литерал \"" << letter << "\" не входит в язык!"
                           << std::endl;
                }
                letter = "";
                i++;   // чтобы перейти к следующему символу строки
                break; // т.к. я по итерациям иду, сначала нахожу один литерал, потом опять литерал ищу и т.д.
            } else {
                letter += s[i];
            }
        }

        if(letter != ""){
            std::cerr << number_line << ":" << i + 1 << ": не найдет символ \"#\"!";
        }

        if(i < s.size() && s[i] != ' '){
            std::cerr << number_line << ":" << i + 1 << ": ожидался пробел между литералами!" << std::endl;
        } else {
            i++; // чтобы пробел пройти, если он есть
        }
    }
    return 1;
}


void get_alphabet_string(){ // просто записываем все литералы в массив
    for(auto &i : dfa.alphabet){
        dfa.alphabet_string.push_back(i.first);
    }
}

void examination_in_full_dfa(){
    int count_alphabet = dfa.alphabet_string.size();
    for(int i = 0; i < dfa.all_vertex.size(); i++){
        if(dfa.all_vertex[i].transitions.size() != count_alphabet){
            dfa.is_full_dfa = false;
            break;
        }
    }
}

void output_dfa(){
    // Сначала всё, что знаем о автомате = то, что помечено bool
    if(dfa.there_is_start_state){
        output << "У автомата есть начальное состояние!" << std::endl;
    } else {
        output << "У автомата отсутствует начальное состояние!" << std::endl;
    }

    if(dfa.there_is_only_start_state){
        output << "У автомата единственное начальное состояние!" << std::endl;
    } else {
        output << "У автомата не единственное начальное состояние!" << std::endl;
    }

    if(dfa.found_terminal_vertex){
        output << "У автомата есть хотя бы одно терминальное состояние!" << std::endl;
    } else {
        output << "У автомата отсутствуют терминальные состояния!" << std::endl;
    }

    if(dfa.vertex_unique){
        output << "У автомата все состояния уникальны!" << std::endl;
    } else {
        output << "У автомата не все состояния уникальны!" << std::endl;
    }

    if(dfa.alphabet_unique){
        output << "У автомата все символы алфавита уникальны!" << std::endl;
    } else {
        output << "У автомата символы алфавита не уникальны!" << std::endl;
    }

    if(dfa.is_dfa){
        output << "Конечный автомат детерминирован!" << std::endl;
    } else {
        output << "Конечный автомат недетерминирован!" << std::endl;
    }

    if(dfa.is_full_dfa){
        output << "Конечный автомат полон!" << std::endl;
    } else {
        output << "Конечный автомат не полон!" << std::endl;
    }

    // потом alphabet
    output << "Язык состоит из следующих символов:" << std::endl;
    for(auto s : dfa.alphabet_string){
        output << s << " ";
    }
    output << std::endl;
    // потом номера вершин
//    std::sort(dfa.all_vertex.begin(), dfa.all_vertex.end());
    output << "В данном автомате, есть вершины с следующими номерами:" << std::endl;
    for(auto number : dfa.all_vertex){
        output << number.get_name() << " ";
    }
    output << std::endl;
    // ребра
    for(auto number : dfa.all_vertex){ // вот это можно поменять, чтобы при каждам выводе не пересчитывать -> циц, только никому не говорите)
        std::vector<std::pair<int,std::string>> edges; // сохраняем все рёбра
        for(auto edge : number.transitions){
            edges.push_back({edge.second.second, edge.first});
        }
        std::sort(edges.begin(), edges.end()); // сортируем все рёбра
        for(auto edge : edges){
            output << "Из вершины " << number.get_name() << " мы можем прийти в вершину " << edge.first << ", если на вход нам подадут литерал \"" << edge.second << "\"!" << std::endl;
        }
    }
}

int main(int argc, char* argv[]) {

    try {
        if (argc == 1) {
            throw "File is missing!";
        }
    } catch (const char* msg){
        std::cerr << msg << std::endl; // TODO: добавить цвет!!!
        return 0;
    }

    file_name_input = argv[1];
    file_name_output = file_name_input + ".out";
    input.open(file_name_input);
    output.open(file_name_output);

    std::string line;
    if(input.is_open()){
        int k = 0;
        while(std::getline(input,line)) {
            ++k;
            { // my_switch
                if(k == 1){
                    get_count_number(line);
                } else if(k == 2){
                    get_alphabet(line);
                    get_alphabet_string();
                } else if(k <= dfa.count_vertex + 2){
                    Vertex vertex = get_vertex(line, k);
                    if(dfa.id_vertex[vertex.get_name()] != 0){ // если уже повторялась вершина = пропустим
                        std::cerr << k << ": вершина с номером " << vertex.get_name() << " уже была создана!" << std::endl;
                        dfa.vertex_unique = false;
                        continue;
                    }
                    if(vertex.get_name() == -1){ // если не удалось создать вершину = пропустим
                        std::cerr << k << ": не удалось создать вершину, ввод некорректен!" << std::endl;
                        continue;
                    }
                    if(vertex.get_state() == 0 && dfa.there_is_start_state){
                        dfa.there_is_only_start_state = false;
                        std::cerr << k << ": добавилась ещё одна стартовая вершина!" << std::endl;
                    }
                    if(vertex.get_state() == 0){ // от состояния вершины, будем записывать её в разные массивы
                        dfa.id_vertex[vertex.get_name()] = dfa.all_vertex.size() + 1;
                        dfa.all_vertex.push_back(vertex); // сука, emplace = всё помнить, вылетает исключение с плавающей точной
                        dfa.there_is_start_state = true;
                    } else if(vertex.get_state() == 1){
                        dfa.id_vertex[vertex.get_name()] = dfa.all_vertex.size() + 1;
                        dfa.all_vertex.push_back(vertex);
                    } else if(vertex.get_state() == 2){
                        dfa.id_vertex[vertex.get_name()] = dfa.all_vertex.size() + 1;
                        dfa.all_vertex.push_back(vertex);
                        dfa.found_terminal_vertex = true;
                    }
                } else if(k > dfa.count_vertex + 2){
                    int number = get_edges(line, k);
                    if(number == 0){
                        std::cerr << k << ": как минимум одной вершины из заданных не существует в автомате!" << std::endl;
                    } else if(number == 1){
                        // вот сюда заходит, если всё ок
                    }
                }
            }
        }
        examination_in_full_dfa();
        output_dfa();
    } else {
        std::cerr << "File input don't open!!!" << std::endl;
    }

    input.close();
    output.close();
}

// TODO: убрать большое количество копипасты
// TODO: перевести всё на english
// TODO:
