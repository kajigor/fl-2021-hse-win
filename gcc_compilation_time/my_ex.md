**1) Программа, которая принимает на вход два числа и выводит их сумму:**

```c++
#include <iostream>

int main() {
	int a, b;
	std::cin >> a >> b;
	std::cout << a + b;
}
```

```c++
Time variable                                   usr           sys          wall               GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)    1471 kB (  5%)
 phase parsing                      :   0.14 ( 88%)   0.15 ( 83%)   0.65 ( 82%)   27277 kB ( 84%)
 phase lang. deferred               :   0.02 ( 12%)   0.01 (  6%)   0.06 (  8%)    3346 kB ( 10%)
 phase opt and generate             :   0.00 (  0%)   0.02 ( 11%)   0.07 (  9%)     320 kB (  1%)
 |name lookup                       :   0.00 (  0%)   0.02 ( 11%)   0.03 (  4%)    1490 kB (  5%)
 |overload resolution               :   0.01 (  6%)   0.01 (  6%)   0.11 ( 14%)    1995 kB (  6%)
 callgraph optimization             :   0.00 (  0%)   0.00 (  0%)   0.03 (  4%)       0 kB (  0%)
 preprocessing                      :   0.00 (  0%)   0.04 ( 22%)   0.14 ( 18%)    1361 kB (  4%)
 parser (global)                    :   0.03 ( 19%)   0.04 ( 22%)   0.15 ( 19%)    8702 kB ( 27%)
 parser struct body                 :   0.04 ( 25%)   0.04 ( 22%)   0.13 ( 16%)    5611 kB ( 17%)
 parser function body               :   0.01 (  6%)   0.00 (  0%)   0.06 (  8%)    1556 kB (  5%)
 parser inl. func. body             :   0.01 (  6%)   0.02 ( 11%)   0.05 (  6%)    1422 kB (  4%)
 parser inl. meth. body             :   0.02 ( 13%)   0.01 (  6%)   0.01 (  1%)    2335 kB (  7%)
 template instantiation             :   0.05 ( 31%)   0.01 (  6%)   0.15 ( 19%)    9524 kB ( 29%)
 constant expression evaluation     :   0.00 (  0%)   0.00 (  0%)   0.02 (  3%)      21 kB (  0%)
 tree PTA                           :   0.00 (  0%)   0.01 (  6%)   0.00 (  0%)       0 kB (  0%)
 tree slp vectorization             :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)       2 kB (  0%)
 scheduling 2                       :   0.00 (  0%)   0.00 (  0%)   0.03 (  4%)       5 kB (  0%)
 shorten branches                   :   0.00 (  0%)   0.01 (  6%)   0.00 (  0%)       0 kB (  0%)
 TOTAL                              :   0.16          0.18          0.79          32424 kB
```

**2) Программа, которая находит максимальный поток в графе:**

```c++
Time variable                                   usr           sys          wall               GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)    1471 kB (  2%)
 phase parsing                      :   0.18 ( 69%)   0.27 ( 55%)   1.13 ( 60%)   41799 kB ( 71%)
 phase lang. deferred               :   0.01 (  4%)   0.05 ( 10%)   0.14 (  7%)    6594 kB ( 11%)
 phase opt and generate             :   0.07 ( 27%)   0.17 ( 35%)   0.59 ( 31%)    9305 kB ( 16%)
 phase finalize                     :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)       0 kB (  0%)
 |name lookup                       :   0.04 ( 15%)   0.05 ( 10%)   0.25 ( 13%)    2127 kB (  4%)
 |overload resolution               :   0.02 (  8%)   0.02 (  4%)   0.16 (  9%)    3293 kB (  6%)
 dump files                         :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)       0 kB (  0%)
 callgraph construction             :   0.00 (  0%)   0.00 (  0%)   0.03 (  2%)     460 kB (  1%)
 callgraph optimization             :   0.01 (  4%)   0.01 (  2%)   0.00 (  0%)       2 kB (  0%)
 ipa SRA                            :   0.00 (  0%)   0.01 (  2%)   0.01 (  1%)     852 kB (  1%)
 df multiple defs                   :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)       0 kB (  0%)
 df live regs                       :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)       0 kB (  0%)
 df reg dead/unused notes           :   0.00 (  0%)   0.00 (  0%)   0.03 (  2%)      43 kB (  0%)
 preprocessing                      :   0.02 (  8%)   0.07 ( 14%)   0.25 ( 13%)    1582 kB (  3%)
 parser (global)                    :   0.04 ( 15%)   0.07 ( 14%)   0.20 ( 11%)   14917 kB ( 25%)
 parser struct body                 :   0.01 (  4%)   0.07 ( 14%)   0.20 ( 11%)    7861 kB ( 13%)
 parser function body               :   0.01 (  4%)   0.02 (  4%)   0.11 (  6%)    2112 kB (  4%)
 parser inl. func. body             :   0.01 (  4%)   0.02 (  4%)   0.07 (  4%)    2581 kB (  4%)
 parser inl. meth. body             :   0.06 ( 23%)   0.01 (  2%)   0.15 (  8%)    4026 kB (  7%)
 template instantiation             :   0.04 ( 15%)   0.06 ( 12%)   0.29 ( 15%)   14902 kB ( 25%)
 inline parameters                  :   0.00 (  0%)   0.00 (  0%)   0.04 (  2%)     496 kB (  1%)
 integration                        :   0.00 (  0%)   0.01 (  2%)   0.02 (  1%)     987 kB (  2%)
 tree gimplify                      :   0.01 (  4%)   0.00 (  0%)   0.02 (  1%)     854 kB (  1%)
 tree CFG construction              :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)     312 kB (  1%)
 tree CFG cleanup                   :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)       5 kB (  0%)
 tree VRP                           :   0.00 (  0%)   0.00 (  0%)   0.03 (  2%)     173 kB (  0%)
 tree Early VRP                     :   0.00 (  0%)   0.00 (  0%)   0.03 (  2%)     293 kB (  0%)
 tree PTA                           :   0.00 (  0%)   0.00 (  0%)   0.03 (  2%)      67 kB (  0%)
 tree SSA other                     :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)      33 kB (  0%)
 tree operand scan                  :   0.00 (  0%)   0.01 (  2%)   0.01 (  1%)     729 kB (  1%)
 dominator optimization             :   0.00 (  0%)   0.01 (  2%)   0.03 (  2%)     145 kB (  0%)
 tree SRA                           :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)      25 kB (  0%)
 tree PRE                           :   0.01 (  4%)   0.00 (  0%)   0.02 (  1%)     141 kB (  0%)
 tree FRE                           :   0.00 (  0%)   0.00 (  0%)   0.04 (  2%)      95 kB (  0%)
 tree forward propagate             :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)      41 kB (  0%)
 complete unrolling                 :   0.01 (  4%)   0.00 (  0%)   0.02 (  1%)      92 kB (  0%)
 tree slp vectorization             :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)     159 kB (  0%)
 expand                             :   0.00 (  0%)   0.00 (  0%)   0.05 (  3%)     307 kB (  1%)
 loop init                          :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)     305 kB (  1%)
 PRE                                :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)      14 kB (  0%)
 CSE 2                              :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)       7 kB (  0%)
 combiner                           :   0.00 (  0%)   0.00 (  0%)   0.04 (  2%)     146 kB (  0%)
 integrated RA                      :   0.00 (  0%)   0.01 (  2%)   0.01 (  1%)     512 kB (  1%)
 LRA non-specific                   :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)      18 kB (  0%)
 reload CSE regs                    :   0.01 (  4%)   0.00 (  0%)   0.02 (  1%)      42 kB (  0%)
 scheduling 2                       :   0.00 (  0%)   0.00 (  0%)   0.02 (  1%)      30 kB (  0%)
 reorder blocks                     :   0.01 (  4%)   0.00 (  0%)   0.02 (  1%)      16 kB (  0%)
 initialize rtl                     :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)      12 kB (  0%)
 rest of compilation                :   0.01 (  4%)   0.00 (  0%)   0.02 (  1%)      87 kB (  0%)
 remove unused locals               :   0.00 (  0%)   0.00 (  0%)   0.02 (  1%)       0 kB (  0%)
 TOTAL                              :   0.26          0.49          1.88          59181 kB
```

**3) Программа, которая реализует иерархию полиморфных классов и некоторую тривиальную базу данных, хранящую упорядоченный список:**

```c++
Time variable                                   usr           sys          wall               GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.00 (  0%)    1471 kB (  2%)
 phase parsing                      :   0.29 ( 43%)   0.31 ( 53%)   1.31 ( 47%)   57249 kB ( 63%)
 phase lang. deferred               :   0.05 (  7%)   0.05 (  9%)   0.21 (  8%)   10746 kB ( 12%)
 phase opt and generate             :   0.34 ( 50%)   0.22 ( 38%)   1.22 ( 44%)   22087 kB ( 24%)
 phase finalize                     :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       0 kB (  0%)
 |name lookup                       :   0.09 ( 13%)   0.06 ( 10%)   0.23 (  8%)    3094 kB (  3%)
 |overload resolution               :   0.03 (  4%)   0.07 ( 12%)   0.27 ( 10%)    9289 kB ( 10%)
 dump files                         :   0.02 (  3%)   0.00 (  0%)   0.05 (  2%)       0 kB (  0%)
 callgraph construction             :   0.00 (  0%)   0.01 (  2%)   0.02 (  1%)     675 kB (  1%)
 callgraph optimization             :   0.00 (  0%)   0.03 (  5%)   0.01 (  0%)       4 kB (  0%)
 ipa function summary               :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)     131 kB (  0%)
 ipa SRA                            :   0.01 (  1%)   0.00 (  0%)   0.00 (  0%)     789 kB (  1%)
 cfg cleanup                        :   0.01 (  1%)   0.01 (  2%)   0.00 (  0%)      45 kB (  0%)
 df reaching defs                   :   0.01 (  1%)   0.00 (  0%)   0.04 (  1%)       0 kB (  0%)
 df live regs                       :   0.00 (  0%)   0.00 (  0%)   0.04 (  1%)       0 kB (  0%)
 df live&initialized regs           :   0.00 (  0%)   0.00 (  0%)   0.06 (  2%)       0 kB (  0%)
 df use-def / def-use chains        :   0.00 (  0%)   0.00 (  0%)   0.03 (  1%)       0 kB (  0%)
 df reg dead/unused notes           :   0.00 (  0%)   0.00 (  0%)   0.02 (  1%)     138 kB (  0%)
 alias stmt walking                 :   0.01 (  1%)   0.00 (  0%)   0.04 (  1%)      39 kB (  0%)
 register scan                      :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)       5 kB (  0%)
 preprocessing                      :   0.02 (  3%)   0.07 ( 12%)   0.24 (  9%)    1628 kB (  2%)
 parser (global)                    :   0.05 (  7%)   0.07 ( 12%)   0.17 (  6%)   16813 kB ( 18%)
 parser struct body                 :   0.05 (  7%)   0.06 ( 10%)   0.21 (  8%)   10054 kB ( 11%)
 parser function body               :   0.02 (  3%)   0.03 (  5%)   0.09 (  3%)    2766 kB (  3%)
 parser inl. func. body             :   0.02 (  3%)   0.01 (  2%)   0.10 (  4%)    2466 kB (  3%)
 parser inl. meth. body             :   0.02 (  3%)   0.02 (  3%)   0.14 (  5%)    5545 kB (  6%)
 template instantiation             :   0.15 ( 22%)   0.10 ( 17%)   0.51 ( 18%)   28259 kB ( 31%)
 constant expression evaluation     :   0.01 (  1%)   0.00 (  0%)   0.04 (  1%)     113 kB (  0%)
 early inlining heuristics          :   0.00 (  0%)   0.00 (  0%)   0.02 (  1%)     276 kB (  0%)
 inline parameters                  :   0.00 (  0%)   0.00 (  0%)   0.03 (  1%)     843 kB (  1%)
 integration                        :   0.02 (  3%)   0.01 (  2%)   0.06 (  2%)    4756 kB (  5%)
 tree gimplify                      :   0.01 (  1%)   0.00 (  0%)   0.03 (  1%)    1386 kB (  2%)
 tree CFG cleanup                   :   0.01 (  1%)   0.00 (  0%)   0.00 (  0%)      16 kB (  0%)
 tree tail merge                    :   0.01 (  1%)   0.00 (  0%)   0.02 (  1%)      41 kB (  0%)
 tree VRP                           :   0.01 (  1%)   0.01 (  2%)   0.00 (  0%)     470 kB (  1%)
 tree Early VRP                     :   0.00 (  0%)   0.00 (  0%)   0.02 (  1%)     497 kB (  1%)
 tree copy propagation              :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       4 kB (  0%)
 tree PTA                           :   0.01 (  1%)   0.01 (  2%)   0.06 (  2%)     144 kB (  0%)
 tree SSA rewrite                   :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     455 kB (  0%)
 tree SSA incremental               :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)     129 kB (  0%)
 tree operand scan                  :   0.00 (  0%)   0.01 (  2%)   0.03 (  1%)    1378 kB (  2%)
 dominator optimization             :   0.01 (  1%)   0.00 (  0%)   0.03 (  1%)     452 kB (  0%)
 tree reassociation                 :   0.01 (  1%)   0.00 (  0%)   0.00 (  0%)       0 kB (  0%)
 tree PRE                           :   0.01 (  1%)   0.00 (  0%)   0.02 (  1%)     359 kB (  0%)
 tree FRE                           :   0.01 (  1%)   0.01 (  2%)   0.01 (  0%)     145 kB (  0%)
 tree forward propagate             :   0.01 (  1%)   0.00 (  0%)   0.03 (  1%)      62 kB (  0%)
 tree conservative DCE              :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       3 kB (  0%)
 tree DSE                           :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)      11 kB (  0%)
 complete unrolling                 :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)      91 kB (  0%)
 tree slp vectorization             :   0.00 (  0%)   0.00 (  0%)   0.02 (  1%)     393 kB (  0%)
 dominance computation              :   0.02 (  3%)   0.02 (  3%)   0.02 (  1%)       0 kB (  0%)
 expand                             :   0.00 (  0%)   0.00 (  0%)   0.00 (  0%)    1084 kB (  1%)
 CSE                                :   0.00 (  0%)   0.00 (  0%)   0.06 (  2%)      35 kB (  0%)
 dead store elim1                   :   0.01 (  1%)   0.00 (  0%)   0.05 (  2%)      98 kB (  0%)
 loop init                          :   0.00 (  0%)   0.00 (  0%)   0.05 (  2%)     548 kB (  1%)
 CPROP                              :   0.01 (  1%)   0.00 (  0%)   0.03 (  1%)     144 kB (  0%)
 CSE 2                              :   0.01 (  1%)   0.00 (  0%)   0.02 (  1%)      13 kB (  0%)
 combiner                           :   0.01 (  1%)   0.00 (  0%)   0.01 (  0%)     232 kB (  0%)
 integrated RA                      :   0.02 (  3%)   0.01 (  2%)   0.02 (  1%)    1617 kB (  2%)
 LRA non-specific                   :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)      85 kB (  0%)
 LRA create live ranges             :   0.02 (  3%)   0.00 (  0%)   0.00 (  0%)      18 kB (  0%)
 LRA hard reg assignment            :   0.00 (  0%)   0.01 (  2%)   0.00 (  0%)       0 kB (  0%)
 LRA rematerialization              :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       0 kB (  0%)
 reload CSE regs                    :   0.02 (  3%)   0.01 (  2%)   0.03 (  1%)     164 kB (  0%)
 load CSE after reload              :   0.00 (  0%)   0.00 (  0%)   0.04 (  1%)     120 kB (  0%)
 peephole 2                         :   0.02 (  3%)   0.00 (  0%)   0.01 (  0%)      12 kB (  0%)
 hard reg cprop                     :   0.01 (  1%)   0.00 (  0%)   0.04 (  1%)       1 kB (  0%)
 scheduling 2                       :   0.00 (  0%)   0.01 (  2%)   0.01 (  0%)      84 kB (  0%)
 final                              :   0.00 (  0%)   0.01 (  2%)   0.04 (  1%)     279 kB (  0%)
 symout                             :   0.00 (  0%)   0.00 (  0%)   0.02 (  1%)       0 kB (  0%)
 initialize rtl                     :   0.01 (  1%)   0.00 (  0%)   0.00 (  0%)      12 kB (  0%)
 rest of compilation                :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     265 kB (  0%)
 remove unused locals               :   0.00 (  0%)   0.01 (  2%)   0.02 (  1%)       1 kB (  0%)
 address taken                      :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       0 kB (  0%)
 TOTAL                              :   0.68          0.58          2.76          91565 kB
```

**4) Программа, реализущая потокобезопасные классы, представляющие собой игрушечный банк, к которому могут подключаться пользователи, и совершать простые действия, такие как транзакции и запрос баланса:**

```c++
Time variable                                   usr           sys          wall               GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)    1471 kB (  2%)
 phase parsing                      :   0.30 ( 83%)   0.27 ( 82%)   1.22 ( 83%)   54405 kB ( 79%)
 phase lang. deferred               :   0.05 ( 14%)   0.04 ( 12%)   0.20 ( 14%)   10590 kB ( 15%)
 phase opt and generate             :   0.01 (  3%)   0.02 (  6%)   0.03 (  2%)    2154 kB (  3%)
 phase finalize                     :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)       0 kB (  0%)
 |name lookup                       :   0.05 ( 14%)   0.07 ( 21%)   0.23 ( 16%)    3144 kB (  5%)
 |overload resolution               :   0.02 (  6%)   0.03 (  9%)   0.16 ( 11%)    9133 kB ( 13%)
 dump files                         :   0.00 (  0%)   0.01 (  3%)   0.00 (  0%)       0 kB (  0%)
 callgraph construction             :   0.00 (  0%)   0.01 (  3%)   0.03 (  2%)     531 kB (  1%)
 preprocessing                      :   0.04 ( 11%)   0.07 ( 21%)   0.13 (  9%)    1653 kB (  2%)
 parser (global)                    :   0.06 ( 17%)   0.06 ( 18%)   0.30 ( 20%)   15871 kB ( 23%)
 parser struct body                 :   0.04 ( 11%)   0.05 ( 15%)   0.24 ( 16%)   11403 kB ( 17%)
 parser function body               :   0.04 ( 11%)   0.01 (  3%)   0.11 (  7%)    1780 kB (  3%)
 parser inl. func. body             :   0.01 (  3%)   0.01 (  3%)   0.05 (  3%)    2012 kB (  3%)
 parser inl. meth. body             :   0.05 ( 14%)   0.02 (  6%)   0.17 ( 12%)    7400 kB ( 11%)
 template instantiation             :   0.11 ( 31%)   0.09 ( 27%)   0.41 ( 28%)   24679 kB ( 36%)
 constant expression evaluation     :   0.00 (  0%)   0.00 (  0%)   0.01 (  1%)      96 kB (  0%)
 tree gimplify                      :   0.01 (  3%)   0.00 (  0%)   0.00 (  0%)     971 kB (  1%)
 TOTAL                              :   0.36          0.33          1.47          68630 kB
```

**5) Пример времени компиляции кода, который мы рассматривали ранее:**

```c++
template<bool> struct a_t;

template<> struct a_t<true> {
    template<int> struct b {};
};

template<> struct a_t<false> {
   enum { b };
};

typedef a_t<sizeof(void*)==sizeof(int)> a;

enum { c, d };
int main() {
    a::b<c>d; // declaration or expression?
}
```

```c++
Time variable                                   usr           sys          wall               GGC
 phase setup                        :   0.00 (  0%)   0.01 ( 33%)   0.04 ( 33%)    1471 kB ( 68%)
 phase parsing                      :   0.00 (  0%)   0.01 ( 33%)   0.01 (  8%)     605 kB ( 28%)
 phase opt and generate             :   0.00 (  0%)   0.01 ( 33%)   0.06 ( 50%)      71 kB (  3%)
 |name lookup                       :   0.00 (  0%)   0.00 (  0%)   0.01 (  8%)     105 kB (  5%)
 callgraph optimization             :   0.00 (  0%)   0.00 (  0%)   0.01 (  8%)       0 kB (  0%)
 parser (global)                    :   0.00 (  0%)   0.01 ( 33%)   0.01 (  8%)     582 kB ( 27%)
 expand                             :   0.00 (  0%)   0.00 (  0%)   0.01 (  8%)       1 kB (  0%)
 peephole 2                         :   0.00 (  0%)   0.00 (  0%)   0.01 (  8%)       0 kB (  0%)
 scheduling 2                       :   0.00 (  0%)   0.00 (  0%)   0.01 (  8%)       1 kB (  0%)
 initialize rtl                     :   0.00 (  0%)   0.00 (  0%)   0.01 (  8%)      12 kB (  1%)
 rest of compilation                :   0.00 (  0%)   0.01 ( 33%)   0.01 (  8%)       3 kB (  0%)
 TOTAL                              :   0.00          0.03          0.12           2158 kB
```

*В некоторых примерах не предоставлен сам код, так как он был написан в рамках обучения. Не совсем корректно
по отношению к младшим курсам выкладывать его в общий доступ. Но, думаю, по описанию примерно ясна его сложность, что
в данном случае вполне достаточно.*
