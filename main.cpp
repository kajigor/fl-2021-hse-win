#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <fstream>

using namespace std;

fstream my_file;
fstream my_file_in;

struct Automata
{
    set <string> alphabet;
    vector <string> transitions;
    vector <string> vertex;
    vector <string> final;
    string initial = "";
    map <string, pair <int, set <string>>> deterministic;

    void out()
    {
        my_file << "------------------------------\n";
        int sz = alphabet.size();
        for(int i = 0; i<sz; ++i)
        {
            my_file << "Alphabet symbol No. " << (i + 1) << " : " << *alphabet.begin() << '\n';
            alphabet.erase(alphabet.begin());
        }
        my_file << "------------------------------\n";
        for(int i = 0; i<vertex.size(); ++i)
        {
            my_file << "Vertex No. " << (i+1) << " : " << vertex[i] << '\n';
        }
        my_file << "------------------------------\n";
        my_file << "Initial vertex : " << initial << '\n';
        my_file << "------------------------------\n";
        for(int i = 0; i<final.size(); ++i)
        {
            my_file << "Final vertex No. " << (i+1) << " : " << final[i] << '\n';
        }

        my_file << "------------------------------\n";
        for(int i = 0; i<transitions.size(); ++i)
        {
            my_file << "Transition No. " << (i+1) <<" : " << transitions[i] << '\n';
        }
    }

    void checkCorrectness()
    {
        if (initial.empty())
        {
            my_file << "No initial state";
            exit(0);
        }
        for(int i = 0; i<vertex.size(); ++i)
        {
            string state = vertex[i];
            if (deterministic[state].first != deterministic[state].second.size())
            {
                my_file << "Non-deterministic automata";
                exit(0);
            }

            if (deterministic[state].first != alphabet.size())
            {
                my_file << "Not complete automata";
                exit(0);
            }
        }
    }
};

Automata automata;

void inputError()
{
    my_file << "Input Error";
    exit(0);
}

void generalError(int type)
{
    switch (type) {
        case 1:
        {
            my_file << "Symbol already in the alphabet";
            exit(0);
        }
        case 2:
        {
            my_file << "Vertex already in the set of states";
            exit(0);
        }
        case 3:
        {
            my_file << "2 initial states";
            exit(0);
        }
        case 4:
        {
            my_file << "State not in the set of states";
            exit(0);
        }
        case 5:
        {
            my_file << "Transition not in the alphabet";
            exit(0);
        }
    }
}

int getVal(string & s, int pos)
{
    string e = "";
    for(int i = pos; i < s.size(); ++i)
    {
        if (s[i] == ',') break;
        e.push_back(s[i]);
    }
    return stoi(e);
}

string getLetter(string & s, int position)
{
    string toReturn;
    while(position < s.size())
    {
        if (s[position] != '"') toReturn.push_back(s[position]); else
            break;
        position++;
    }
    return toReturn;
}

void checkAlphabet()
{
    string s;
    getline(my_file_in, s);
    string num = s.substr(9, 3);
    if (num != "NUM")
        inputError();
    int k = getVal(s, 13);
    while(k--)
    {
        getline(my_file_in, s);
        string tr = s.substr(9 ,15);
        if (tr != "TRANSITION_NAME")
            inputError();
        string let = getLetter(s, 27);
        if (automata.alphabet.find(let) != automata.alphabet.end())
            generalError(1);
        automata.alphabet.insert(let);
    }
}

string getName(string s, int position)
{
    string toReturn;
    while(position < s.size())
    {

        if (s[position] != '\'') toReturn.push_back(s[position]); else
            break;
        position++;
    }
    return toReturn;
}

pair <int, string> getVertex()
{
    int type = -1;
    string s;
    getline(my_file_in, s);
    string vert = s.substr(9, 4);
    if (vert == "NAME")
    {
        type = 0;
        string name = getName(s, 15);
        if (name[0] != 'q')
            inputError();
        return {type, name};
    }

    vert = s.substr(9, 5);
    if (vert == "START")
        type = 1;
    vert = s.substr(9, 8);
    if (vert == "TERMINAL")
        type = 2;

    getline(my_file_in, s);
    vert = s.substr(9, 8);

    if (vert == "TERMINAL") {
        type = 3;
        getline(my_file_in, s);
        vert = s.substr(9, 4);
        if (vert == "NAME")
        {
            string name = getName(s, 15);
            if (name[0] != 'q')
                inputError();
            return {type, name};
        } else
            inputError();
    }

    vert = s.substr(9, 4);
    if (vert == "NAME")
    {
        string name = getName(s, 15);
        if (name[0] != 'q')
            inputError();
        return {type, name};
    } else
        inputError();
    return {type, ""};
}

void checkVertex()
{
    string s;
    getline(my_file_in, s);
    string num = s.substr(9, 3);
    if (num != "NUM")
        inputError();

    int k = getVal(s, 13);
    while(k--)
    {
        pair <int,string> temporary = getVertex();
        string ve = temporary.second;
        int type = temporary.first;

        if (find(automata.vertex.begin(), automata.vertex.end(), ve) != automata.vertex.end())
            generalError(2);
        switch (type) {
            case 1:
            {
                if (automata.initial != "")
                    generalError(3);
                automata.initial = ve;
                break;
            }
            case 2:
            {
                automata.final.push_back(ve);
                break;
            }
            case 3:
            {
                if (automata.initial != "")
                    generalError(3);
                automata.initial = ve;
                automata.final.push_back(ve);
                break;
            }
        }
        automata.vertex.push_back(ve);
    }
}

void checkTransition()
{
    string s;
    getline(my_file_in, s);
    string num = s.substr(9, 3);
    if (num != "NUM")
        inputError();

    int k = getVal(s, 13);
    while(k--)
    {
        string s, name1, name2;
        getline(my_file_in, s);
        string vert = s.substr(9, 4);
        if (vert == "NAME")
            name1 = getName(s, 15);

        if (find(automata.vertex.begin(), automata.vertex.end(), name1) == automata.vertex.end())
            generalError(4);


        getline(my_file_in, s);
        vert = s.substr(9, 4);
        if (vert == "NAME")
            name2 = getName(s, 15);

        if (find(automata.vertex.begin(), automata.vertex.end(), name2) == automata.vertex.end())
            generalError(4);

        getline(my_file_in, s);
        string tr = s.substr(9 ,15);
        if (tr != "TRANSITION_NAME")
            inputError();
        string let = getLetter(s, 27);
        if (automata.alphabet.find(let) == automata.alphabet.end())
            generalError(5);

        automata.transitions.push_back(name1 + '>' + let + '>' + name2);
        automata.deterministic[name1].first++;
        automata.deterministic[name1].second.insert(let);
    }
}

int main(int argc, char * argv[]) {
    string s1 = argv[1];
    string s2 = s1 + ".out";
    my_file.open(s2 , ios::out);
    my_file_in.open(s1, ios::in);

    try {
        checkAlphabet();
    } catch (exception e)
    {
        inputError();
        exit(0);
    }
    try {
        checkVertex();
    } catch (exception e)
    {
        inputError();
        exit(0);
    }
    try {
        checkTransition();
    } catch (exception e)
    {
        inputError();
        exit(0);
    }
    try {
        automata.checkCorrectness();
    } catch (exception e)
    {
        inputError();
        exit(0);
    }
    try {
        automata.out();
    } catch (exception e)
    {
        inputError();
        exit(0);
    }
    my_file.close();
    my_file_in.close();
    return 0;
}
