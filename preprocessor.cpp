/*
 * Эта штука просто делает лёгкий препроцессинг кода: удаляем комментарии, удаляем лишние переводы строки
 * Напоминаю, дабы было интересней, однострочный комментарий начинается с @ , многострочный же обёрнут как @* комментарий *@
 * Эти два символа редко повторяются, будем считать как открывающая и закрывающая часть коммента
 * Если @ встретилась внутри @* *@ считаем её обычным символом
 * Также @* *@ после @
 * Если открылся коммент в конце кода и не закрылся -- то по боку, так можно
 */
#include <bits/stdc++.h>

std::string readFile(const std::string& fileName) {
    std::ifstream f(fileName);
    std::stringstream ss;
    ss << f.rdbuf();
    return ss.str();
}
enum class comment_status{
    OPEN_ONE_LINE, OPEN_MULTI, CLOSED
} CS;

int main(int argc, char *argv[]) {
    assert(argc == 2);
    CS = comment_status::CLOSED;
    std::string code = readFile(std::string(argv[1]));
    std::ofstream out(std::string(argv[1]) + ".out");
    std::string code_without_comments;

    for(int i=0; i<code.length(); ++i) {
        char s = code[i];
        if(s=='@' and i==code.length()-1){ // собака последним символом
            break;
        }
        else if(s=='@' and CS==comment_status::CLOSED) { // собака при неоткрытом комменте
            if(code[i+1]=='*'){
                CS = comment_status::OPEN_MULTI;
            } else {
                CS = comment_status::OPEN_ONE_LINE;
            }
        }
        else if(s=='\n' and CS==comment_status::OPEN_ONE_LINE) { // перевод строки при открытом однострочном
            CS=comment_status::CLOSED;
            code_without_comments+=s;
        }
        else if(s=='@' and CS==comment_status::OPEN_MULTI) { // Открыт многострочный коммент, подозрение, что закрывается, ибо собаку встретили
            if(i!=0 and code[i-1]=='*'){
                CS = comment_status::CLOSED;
                code_without_comments+='\n';
            }
        }
        else { // не @
            if(CS==comment_status::CLOSED) { // Если не комментарий
                code_without_comments+=s;
            }
        }
    }
    //std::cout<<code_without_comments;

    // Удаляем лишний переводы строки, двойные пробелы, табуляцию
    std::string nice_code;
    std::string without_enters;
    // переводы
    bool prev_enter = true; // ибо в начале нам они не нужны
    for(int i=0; i<code_without_comments.length(); ++i){
        char s = code_without_comments[i];
        if(prev_enter && s == '\n'){
            continue;
        }
        if(s=='\n'){
            prev_enter = true;
        } else {
            prev_enter = false;
        }
        without_enters += s;
    }

    // пробелы
    std::string without_spaces;
    bool prev_space = true; // ибо в начале нам они не нужны
    for(int i=0; i<without_enters.length(); ++i){
        char s = without_enters[i];
        if(prev_space && s == ' '){
            continue;
        }
        if(s==' '){
            prev_space = true;
        } else {
            prev_space = false;
        }
        without_spaces += s;
    }

    //табуляция
    for(int i=0; i<without_spaces.length(); ++i){
        char s = without_spaces[i];
        if(s!='\t'){
            nice_code += s;
        }
    }
    out<<nice_code;
}