## Анализ времени компиляции других пользователей:

**1) [Автор](https://stackoverflow.com/users/1296119/fabio-dalla-libera) этого примера:**

```c++
Execution times (seconds)
 garbage collection    :   0.91 ( 6%) usr   0.00 ( 0%) sys   0.92 ( 5%) wall       0 kB ( 0%) ggc
 callgraph construction:   0.23 ( 2%) usr   0.11 ( 3%) sys   0.37 ( 2%) wall   10652 kB ( 1%) ggc
 callgraph optimization:   0.18 ( 1%) usr   0.12 ( 3%) sys   0.28 ( 2%) wall   11906 kB ( 2%) ggc
 varpool construction  :   0.04 ( 0%) usr   0.01 ( 0%) sys   0.08 ( 0%) wall    6984 kB ( 1%) ggc
 cfg construction      :   0.03 ( 0%) usr   0.00 ( 0%) sys   0.05 ( 0%) wall     644 kB ( 0%) ggc
 cfg cleanup           :   0.05 ( 0%) usr   0.02 ( 0%) sys   0.05 ( 0%) wall       7 kB ( 0%) ggc
 trivially dead code   :   0.05 ( 0%) usr   0.01 ( 0%) sys   0.12 ( 1%) wall       0 kB ( 0%) ggc
 df scan insns         :   0.37 ( 3%) usr   0.03 ( 1%) sys   0.43 ( 2%) wall     677 kB ( 0%) ggc
 df live regs          :   0.07 ( 0%) usr   0.01 ( 0%) sys   0.02 ( 0%) wall       0 kB ( 0%) ggc
 df reg dead/unused notes:   0.08 ( 1%) usr   0.01 ( 0%) sys   0.08 ( 0%) wall    2755 kB ( 0%) ggc
 register information  :   0.05 ( 0%) usr   0.01 ( 0%) sys   0.05 ( 0%) wall       0 kB ( 0%) ggc
 alias analysis        :   0.01 ( 0%) usr   0.01 ( 0%) sys   0.01 ( 0%) wall     878 kB ( 0%) ggc
 rebuild jump labels   :   0.03 ( 0%) usr   0.01 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 preprocessing         :   0.19 ( 1%) usr   0.44 (11%) sys   0.68 ( 4%) wall    5284 kB ( 1%) ggc
 parser                :   3.94 (28%) usr   1.43 (35%) sys   4.94 (27%) wall  355964 kB (48%) ggc
 name lookup           :   1.35 ( 9%) usr   0.88 (21%) sys   2.76 (15%) wall   64919 kB ( 9%) ggc
 inline heuristics     :   0.14 ( 1%) usr   0.03 ( 1%) sys   0.14 ( 1%) wall       0 kB ( 0%) ggc
 integration           :   0.02 ( 0%) usr   0.00 ( 0%) sys   0.02 ( 0%) wall      20 kB ( 0%) ggc
 tree gimplify         :   0.31 ( 2%) usr   0.07 ( 2%) sys   0.28 ( 2%) wall   24598 kB ( 3%) ggc
 tree eh               :   0.07 ( 0%) usr   0.02 ( 0%) sys   0.11 ( 1%) wall    7267 kB ( 1%) ggc
 tree CFG construction :   0.04 ( 0%) usr   0.04 ( 1%) sys   0.11 ( 1%) wall   15754 kB ( 2%) ggc
 tree CFG cleanup      :   0.12 ( 1%) usr   0.00 ( 0%) sys   0.05 ( 0%) wall       3 kB ( 0%) ggc
 tree find ref. vars   :   0.03 ( 0%) usr   0.01 ( 0%) sys   0.02 ( 0%) wall     963 kB ( 0%) ggc
 tree PHI insertion    :   0.00 ( 0%) usr   0.01 ( 0%) sys   0.01 ( 0%) wall     351 kB ( 0%) ggc
 tree SSA rewrite      :   0.03 ( 0%) usr   0.01 ( 0%) sys   0.01 ( 0%) wall    4078 kB ( 1%) ggc
 tree SSA other        :   0.03 ( 0%) usr   0.06 ( 1%) sys   0.12 ( 1%) wall    1504 kB ( 0%) ggc
 tree operand scan     :   0.04 ( 0%) usr   0.02 ( 0%) sys   0.08 ( 0%) wall   10781 kB ( 1%) ggc
 dominance computation :   0.15 ( 1%) usr   0.04 ( 1%) sys   0.15 ( 1%) wall       0 kB ( 0%) ggc
 out of ssa            :   0.09 ( 1%) usr   0.00 ( 0%) sys   0.02 ( 0%) wall       0 kB ( 0%) ggc
 expand vars           :   0.03 ( 0%) usr   0.00 ( 0%) sys   0.03 ( 0%) wall    1840 kB ( 0%) ggc
 expand                :   0.45 ( 3%) usr   0.04 ( 1%) sys   0.59 ( 3%) wall   37695 kB ( 5%) ggc
 post expand cleanups  :   0.08 ( 1%) usr   0.02 ( 0%) sys   0.06 ( 0%) wall    4542 kB ( 1%) ggc
 varconst              :   0.15 ( 1%) usr   0.03 ( 1%) sys   0.12 ( 1%) wall    3595 kB ( 0%) ggc
 jump                  :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.04 ( 0%) wall    1904 kB ( 0%) ggc
 mode switching        :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 integrated RA         :   1.33 ( 9%) usr   0.09 ( 2%) sys   1.49 ( 8%) wall   18163 kB ( 2%) ggc
 reload                :   0.60 ( 4%) usr   0.10 ( 2%) sys   0.62 ( 3%) wall    8668 kB ( 1%) ggc
 thread pro- & epilogue:   0.17 ( 1%) usr   0.00 ( 0%) sys   0.20 ( 1%) wall   11884 kB ( 2%) ggc
 reg stack             :   0.02 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall       0 kB ( 0%) ggc
 final                 :   0.71 ( 5%) usr   0.10 ( 2%) sys   0.84 ( 5%) wall    6251 kB ( 1%) ggc
 symout                :   1.10 ( 8%) usr   0.16 ( 4%) sys   1.19 ( 6%) wall  100954 kB (14%) ggc
 uninit var analysis   :   0.03 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 early local passes    :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 rest of compilation   :   0.49 ( 3%) usr   0.06 ( 1%) sys   0.76 ( 4%) wall   19252 kB ( 3%) ggc
 unaccounted todo      :   0.43 ( 3%) usr   0.09 ( 2%) sys   0.55 ( 3%) wall       0 kB ( 0%) ggc
 TOTAL                 :  14.26             4.11            18.52             742072 kB
```

**2) [Автор](https://stackoverflow.com/users/234175/greatwolf) этого примера:**

```c++
Execution times (seconds)
 callgraph construction:   0.01 ( 1%) usr     224 kB ( 1%) ggc
 callgraph optimization:   0.01 ( 1%) usr     147 kB ( 0%) ggc
 cfg cleanup           :   0.01 ( 1%) usr       8 kB ( 0%) ggc
 df live regs          :   0.02 ( 2%) usr       0 kB ( 0%) ggc
 df live&initialized regs:   0.01 ( 1%) usr       0 kB ( 0%) ggc
 alias analysis        :   0.01 ( 1%) usr      67 kB ( 0%) ggc
 preprocessing         :   0.08 (10%) usr    2869 kB ( 8%) ggc
 parser                :   0.31 (40%) usr   24239 kB (66%) ggc
 name lookup           :   0.06 ( 7%) usr    3086 kB ( 8%) ggc
 inline heuristics     :   0.01 ( 1%) usr      16 kB ( 0%) ggc
 integration           :   0.01 ( 1%) usr    1499 kB ( 4%) ggc
 tree gimplify         :   0.01 ( 1%) usr     422 kB ( 1%) ggc
 tree CFG cleanup      :   0.01 ( 1%) usr      12 kB ( 0%) ggc
 tree VRP              :   0.01 ( 1%) usr     146 kB ( 0%) ggc
 tree PTA              :   0.01 ( 1%) usr      66 kB ( 0%) ggc
 tree SSA rewrite      :   0.01 ( 1%) usr     159 kB ( 0%) ggc
 tree SSA incremental  :   0.01 ( 1%) usr      35 kB ( 0%) ggc
 tree operand scan     :   0.01 ( 1%) usr     628 kB ( 2%) ggc
 tree PRE              :   0.02 ( 3%) usr     101 kB ( 0%) ggc
 tree FRE              :   0.01 ( 1%) usr      25 kB ( 0%) ggc
 dominance computation :   0.01 ( 1%) usr       0 kB ( 0%) ggc
 expand                :   0.03 ( 4%) usr     528 kB ( 1%) ggc
 CSE                   :   0.01 ( 1%) usr       8 kB ( 0%) ggc
 CSE 2                 :   0.01 ( 1%) usr       6 kB ( 0%) ggc
 branch prediction     :   0.01 ( 1%) usr      67 kB ( 0%) ggc
 combiner              :   0.01 ( 1%) usr      48 kB ( 0%) ggc
 integrated RA         :   0.02 ( 2%) usr      53 kB ( 0%) ggc
 reload                :   0.01 ( 2%) usr     114 kB ( 0%) ggc
 reload CSE regs       :   0.01 ( 1%) usr      95 kB ( 0%) ggc
 final                 :   0.01 ( 1%) usr       3 kB ( 0%) ggc
 TOTAL                 :   0.79             36953 kB
```

**3) [Автор](https://stackoverflow.com/users/247265/anon) этого примера:**

```c++
Execution times (seconds)
  callgraph construction:   0.06 ( 2%) usr   0.00 ( 0%) sys   0.09 ( 2%) wall    3181 kB ( 1%) ggc
  callgraph optimization:   0.05 ( 2%) usr   0.00 ( 0%) sys   0.05 ( 1%) wall    5243 kB ( 2%) ggc
  cfg cleanup           :   0.02 ( 1%) usr   0.00 ( 0%) sys   0.02 ( 0%) wall      11 kB ( 0%) ggc
  df live regs          :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
  df reg dead/unused notes:   0.03 ( 1%) usr   0.00 ( 0%) sys   0.03 ( 1%) wall    1993 kB ( 1%) ggc
  register information  :   0.04 ( 1%) usr   0.00 ( 0%) sys   0.04 ( 1%) wall       0 kB ( 0%) ggc
  alias analysis        :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall     450 kB ( 0%) ggc
  rebuild jump labels   :   0.03 ( 1%) usr   0.00 ( 0%) sys   0.03 ( 1%) wall       0 kB ( 0%) ggc
  preprocessing         :   0.12 ( 4%) usr   0.06 (12%) sys   1.46 (27%) wall    2752 kB ( 1%) ggc
  parser                :   0.67 (21%) usr   0.15 (29%) sys   0.89 (16%) wall   91749 kB (36%) ggc
  name lookup           :   0.15 ( 5%) usr   0.12 (24%) sys   0.24 ( 4%) wall   14384 kB ( 6%) ggc
  inline heuristics     :   0.03 ( 1%) usr   0.00 ( 0%) sys   0.03 ( 1%) wall       0 kB ( 0%) ggc
  tree gimplify         :   0.06 ( 2%) usr   0.01 ( 2%) sys   0.09 ( 2%) wall   15992 kB ( 6%) ggc
  tree eh               :   0.02 ( 1%) usr   0.01 ( 2%) sys   0.03 ( 1%) wall    4405 kB ( 2%) ggc
  tree CFG construction :   0.01 ( 0%) usr   0.01 ( 2%) sys   0.03 ( 1%) wall    6636 kB ( 3%) ggc
  tree CFG cleanup      :   0.02 ( 1%) usr   0.01 ( 2%) sys   0.02 ( 0%) wall      15 kB ( 0%) ggc
  tree find ref. vars   :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall    1870 kB ( 1%) ggc
  tree SSA rewrite      :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall    2357 kB ( 1%) ggc
  tree SSA other        :   0.00 ( 0%) usr   0.01 ( 2%) sys   0.00 ( 0%) wall      37 kB ( 0%) ggc
  tree operand scan     :   0.01 ( 0%) usr   0.04 ( 8%) sys   0.06 ( 1%) wall    6340 kB ( 2%) ggc
  tree SSA to normal    :   0.05 ( 2%) usr   0.00 ( 0%) sys   0.05 ( 1%) wall      95 kB ( 0%) ggc
  dominance computation :   0.04 ( 1%) usr   0.00 ( 0%) sys   0.04 ( 1%) wall       0 kB ( 0%) ggc
  expand                :   0.60 (18%) usr   0.03 ( 6%) sys   0.71 (13%) wall   45557 kB (18%) ggc
  varconst              :   0.02 ( 1%) usr   0.00 ( 0%) sys   0.02 ( 0%) wall    3532 kB ( 1%) ggc
  jump                  :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall    1745 kB ( 1%) ggc
  mode switching        :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
  integrated RA         :   0.35 (11%) usr   0.00 ( 0%) sys   0.35 ( 6%) wall    5259 kB ( 2%) ggc
  reload                :   0.29 ( 9%) usr   0.01 ( 2%) sys   0.31 ( 6%) wall    6490 kB ( 3%) ggc
  thread pro- & epilogue:   0.10 ( 3%) usr   0.01 ( 2%) sys   0.13 ( 2%) wall    4832 kB ( 2%) ggc
  final                 :   0.19 ( 6%) usr   0.01 ( 2%) sys   0.21 ( 4%) wall    2985 kB ( 1%) ggc
  symout                :   0.25 ( 8%) usr   0.01 ( 2%) sys   0.26 ( 5%) wall   27322 kB (11%) ggc
  TOTAL                 :   3.25             0.51             5.49             256741 kB
```

**4) [Автор](https://stackoverflow.com/users/4943329/cyrusbehr) этого примера:**

```c++
Time variable                                   usr           sys          wall               GGC
 phase setup                        :   0.00 (  0%)   0.00 (  0%)   0.00 (  0%)    1579 kB (  0%)
 phase parsing                      :   1.74 ( 20%)   0.71 ( 44%)   2.46 ( 24%)  311927 kB ( 36%)
 phase lang. deferred               :   1.33 ( 15%)   0.34 ( 21%)   1.67 ( 16%)  259524 kB ( 30%)
 phase opt and generate             :   5.68 ( 65%)   0.58 ( 36%)   6.26 ( 60%)  301021 kB ( 34%)
 phase last asm                     :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       2 kB (  0%)
 |name lookup                       :   0.44 (  5%)   0.12 (  7%)   0.49 (  5%)   15499 kB (  2%)
 |overload resolution               :   0.76 (  9%)   0.22 ( 13%)   0.92 (  9%)  130607 kB ( 15%)
 garbage collection                 :   0.33 (  4%)   0.01 (  1%)   0.34 (  3%)       0 kB (  0%)
 dump files                         :   0.18 (  2%)   0.04 (  2%)   0.10 (  1%)       0 kB (  0%)
 callgraph construction             :   0.12 (  1%)   0.03 (  2%)   0.14 (  1%)    6318 kB (  1%)
 callgraph optimization             :   0.16 (  2%)   0.04 (  2%)   0.19 (  2%)      82 kB (  0%)
 ipa function summary               :   0.02 (  0%)   0.00 (  0%)   0.02 (  0%)    2289 kB (  0%)
 ipa dead code removal              :   0.01 (  0%)   0.00 (  0%)   0.03 (  0%)       0 kB (  0%)
 ipa inheritance graph              :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)      29 kB (  0%)
 ipa virtual call target            :   0.02 (  0%)   0.00 (  0%)   0.00 (  0%)       3 kB (  0%)
 ipa cp                             :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)    1140 kB (  0%)
 ipa inlining heuristics            :   0.04 (  0%)   0.00 (  0%)   0.04 (  0%)    2438 kB (  0%)
 ipa function splitting             :   0.00 (  0%)   0.01 (  1%)   0.01 (  0%)     451 kB (  0%)
 ipa profile                        :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)       0 kB (  0%)
 ipa pure const                     :   0.02 (  0%)   0.00 (  0%)   0.05 (  0%)      40 kB (  0%)
 ipa icf                            :   0.01 (  0%)   0.00 (  0%)   0.01 (  0%)       4 kB (  0%)
 ipa SRA                            :   0.10 (  1%)   0.00 (  0%)   0.05 (  0%)    9838 kB (  1%)
 cfg cleanup                        :   0.08 (  1%)   0.01 (  1%)   0.08 (  1%)    1621 kB (  0%)
 trivially dead code                :   0.03 (  0%)   0.00 (  0%)   0.06 (  1%)       0 kB (  0%)
 df scan insns                      :   0.02 (  0%)   0.01 (  1%)   0.05 (  0%)      18 kB (  0%)
 df multiple defs                   :   0.02 (  0%)   0.00 (  0%)   0.03 (  0%)       0 kB (  0%)
 df reaching defs                   :   0.06 (  1%)   0.00 (  0%)   0.04 (  0%)       0 kB (  0%)
 df live regs                       :   0.19 (  2%)   0.01 (  1%)   0.25 (  2%)       0 kB (  0%)
 df live&initialized regs           :   0.05 (  1%)   0.00 (  0%)   0.06 (  1%)       0 kB (  0%)
 df use-def / def-use chains        :   0.03 (  0%)   0.00 (  0%)   0.00 (  0%)       0 kB (  0%)
 df reg dead/unused notes           :   0.08 (  1%)   0.00 (  0%)   0.07 (  1%)    2152 kB (  0%)
 register information               :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)       0 kB (  0%)
 alias analysis                     :   0.03 (  0%)   0.00 (  0%)   0.09 (  1%)    5413 kB (  1%)
 alias stmt walking                 :   0.08 (  1%)   0.00 (  0%)   0.13 (  1%)     738 kB (  0%)
 register scan                      :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     167 kB (  0%)
 rebuild jump labels                :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)       0 kB (  0%)
 preprocessing                      :   0.15 (  2%)   0.21 ( 13%)   0.39 (  4%)   11918 kB (  1%)
 parser (global)                    :   0.29 (  3%)   0.21 ( 13%)   0.51 (  5%)  105494 kB ( 12%)
 parser struct body                 :   0.18 (  2%)   0.04 (  2%)   0.22 (  2%)   39504 kB (  5%)
 parser enumerator list             :   0.01 (  0%)   0.01 (  1%)   0.00 (  0%)    1305 kB (  0%)
 parser function body               :   0.18 (  2%)   0.04 (  2%)   0.15 (  1%)    9096 kB (  1%)
 parser inl. func. body             :   0.27 (  3%)   0.02 (  1%)   0.39 (  4%)   33105 kB (  4%)
 parser inl. meth. body             :   0.21 (  2%)   0.06 (  4%)   0.25 (  2%)   23541 kB (  3%)
 template instantiation             :   1.61 ( 18%)   0.43 ( 26%)   2.05 ( 20%)  346006 kB ( 40%)
 constant expression evaluation     :   0.05 (  1%)   0.03 (  2%)   0.02 (  0%)    1470 kB (  0%)
 early inlining heuristics          :   0.00 (  0%)   0.01 (  1%)   0.03 (  0%)    3751 kB (  0%)
 inline parameters                  :   0.06 (  1%)   0.02 (  1%)   0.05 (  0%)   12991 kB (  1%)
 integration                        :   0.12 (  1%)   0.04 (  2%)   0.26 (  3%)   53810 kB (  6%)
 tree gimplify                      :   0.06 (  1%)   0.02 (  1%)   0.11 (  1%)   20691 kB (  2%)
 tree eh                            :   0.02 (  0%)   0.00 (  0%)   0.02 (  0%)    2821 kB (  0%)
 tree CFG construction              :   0.02 (  0%)   0.00 (  0%)   0.00 (  0%)    8987 kB (  1%)
 tree CFG cleanup                   :   0.11 (  1%)   0.02 (  1%)   0.13 (  1%)     208 kB (  0%)
 tree tail merge                    :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     880 kB (  0%)
 tree VRP                           :   0.17 (  2%)   0.00 (  0%)   0.18 (  2%)    7001 kB (  1%)
 tree Early VRP                     :   0.05 (  1%)   0.00 (  0%)   0.05 (  0%)    7256 kB (  1%)
 tree copy propagation              :   0.00 (  0%)   0.00 (  0%)   0.05 (  0%)     104 kB (  0%)
 tree PTA                           :   0.13 (  1%)   0.05 (  3%)   0.25 (  2%)    1906 kB (  0%)
 tree PHI insertion                 :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     736 kB (  0%)
 tree SSA rewrite                   :   0.06 (  1%)   0.01 (  1%)   0.04 (  0%)    6289 kB (  1%)
 tree SSA other                     :   0.00 (  0%)   0.02 (  1%)   0.03 (  0%)     940 kB (  0%)
 tree SSA incremental               :   0.08 (  1%)   0.00 (  0%)   0.03 (  0%)    1717 kB (  0%)
 tree operand scan                  :   0.08 (  1%)   0.00 (  0%)   0.08 (  1%)   19096 kB (  2%)
 dominator optimization             :   0.18 (  2%)   0.01 (  1%)   0.15 (  1%)    5240 kB (  1%)
 backwards jump threading           :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     244 kB (  0%)
 tree SRA                           :   0.03 (  0%)   0.00 (  0%)   0.01 (  0%)    1712 kB (  0%)
 tree CCP                           :   0.10 (  1%)   0.02 (  1%)   0.10 (  1%)    1097 kB (  0%)
 tree reassociation                 :   0.00 (  0%)   0.01 (  1%)   0.00 (  0%)      50 kB (  0%)
 tree PRE                           :   0.15 (  2%)   0.01 (  1%)   0.18 (  2%)    4977 kB (  1%)
 tree FRE                           :   0.13 (  1%)   0.02 (  1%)   0.12 (  1%)    2498 kB (  0%)
 tree linearize phis                :   0.02 (  0%)   0.00 (  0%)   0.03 (  0%)     563 kB (  0%)
 tree forward propagate             :   0.09 (  1%)   0.00 (  0%)   0.10 (  1%)    1071 kB (  0%)
 tree phiprop                       :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)      11 kB (  0%)
 tree conservative DCE              :   0.04 (  0%)   0.01 (  1%)   0.02 (  0%)     133 kB (  0%)
 tree aggressive DCE                :   0.04 (  0%)   0.01 (  1%)   0.04 (  0%)    7238 kB (  1%)
 tree DSE                           :   0.00 (  0%)   0.01 (  1%)   0.03 (  0%)     254 kB (  0%)
 tree loop invariant motion         :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)      17 kB (  0%)
 scev constant prop                 :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     112 kB (  0%)
 tree loop unswitching              :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)     349 kB (  0%)
 complete unrolling                 :   0.01 (  0%)   0.01 (  1%)   0.03 (  0%)    1141 kB (  0%)
 tree slp vectorization             :   0.01 (  0%)   0.02 (  1%)   0.03 (  0%)    5032 kB (  1%)
 tree iv optimization               :   0.02 (  0%)   0.00 (  0%)   0.04 (  0%)    2110 kB (  0%)
 predictive commoning               :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)     302 kB (  0%)
 gimple CSE reciprocals             :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)       0 kB (  0%)
 dominance computation              :   0.14 (  2%)   0.03 (  2%)   0.16 (  2%)       0 kB (  0%)
 out of ssa                         :   0.05 (  1%)   0.00 (  0%)   0.01 (  0%)      55 kB (  0%)
 expand vars                        :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)    1422 kB (  0%)
 expand                             :   0.03 (  0%)   0.01 (  1%)   0.10 (  1%)   14790 kB (  2%)
 post expand cleanups               :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)    1273 kB (  0%)
 varconst                           :   0.00 (  0%)   0.00 (  0%)   0.03 (  0%)       8 kB (  0%)
 jump                               :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)       0 kB (  0%)
 forward prop                       :   0.02 (  0%)   0.00 (  0%)   0.03 (  0%)    1330 kB (  0%)
 CSE                                :   0.13 (  1%)   0.00 (  0%)   0.08 (  1%)     664 kB (  0%)
 dead code elimination              :   0.00 (  0%)   0.00 (  0%)   0.03 (  0%)       0 kB (  0%)
 dead store elim1                   :   0.02 (  0%)   0.00 (  0%)   0.06 (  1%)    1230 kB (  0%)
 dead store elim2                   :   0.05 (  1%)   0.00 (  0%)   0.03 (  0%)    1584 kB (  0%)
 loop init                          :   0.11 (  1%)   0.02 (  1%)   0.07 (  1%)    8638 kB (  1%)
 loop versioning                    :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)      40 kB (  0%)
 loop invariant motion              :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       8 kB (  0%)
 CPROP                              :   0.12 (  1%)   0.00 (  0%)   0.06 (  1%)    3321 kB (  0%)
 PRE                                :   0.08 (  1%)   0.00 (  0%)   0.05 (  0%)     935 kB (  0%)
 CSE 2                              :   0.07 (  1%)   0.00 (  0%)   0.08 (  1%)     333 kB (  0%)
 branch prediction                  :   0.02 (  0%)   0.00 (  0%)   0.03 (  0%)    1178 kB (  0%)
 combiner                           :   0.21 (  2%)   0.00 (  0%)   0.15 (  1%)    7070 kB (  1%)
 if-conversion                      :   0.02 (  0%)   0.00 (  0%)   0.01 (  0%)     464 kB (  0%)
 integrated RA                      :   0.25 (  3%)   0.01 (  1%)   0.30 (  3%)   20626 kB (  2%)
 LRA non-specific                   :   0.10 (  1%)   0.00 (  0%)   0.09 (  1%)    1243 kB (  0%)
 LRA virtuals elimination           :   0.02 (  0%)   0.00 (  0%)   0.01 (  0%)     834 kB (  0%)
 LRA reload inheritance             :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     195 kB (  0%)
 LRA create live ranges             :   0.11 (  1%)   0.01 (  1%)   0.13 (  1%)     234 kB (  0%)
 LRA hard reg assignment            :   0.02 (  0%)   0.00 (  0%)   0.02 (  0%)       0 kB (  0%)
 LRA rematerialization              :   0.04 (  0%)   0.00 (  0%)   0.02 (  0%)       0 kB (  0%)
 reload                             :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)       0 kB (  0%)
 reload CSE regs                    :   0.09 (  1%)   0.00 (  0%)   0.06 (  1%)    2212 kB (  0%)
 load CSE after reload              :   0.06 (  1%)   0.00 (  0%)   0.05 (  0%)     559 kB (  0%)
 ree                                :   0.00 (  0%)   0.00 (  0%)   0.02 (  0%)      71 kB (  0%)
 thread pro- & epilogue             :   0.03 (  0%)   0.00 (  0%)   0.02 (  0%)     939 kB (  0%)
 peephole 2                         :   0.01 (  0%)   0.00 (  0%)   0.02 (  0%)     170 kB (  0%)
 hard reg cprop                     :   0.00 (  0%)   0.00 (  0%)   0.03 (  0%)      15 kB (  0%)
 scheduling 2                       :   0.15 (  2%)   0.00 (  0%)   0.16 (  2%)     894 kB (  0%)
 machine dep reorg                  :   0.00 (  0%)   0.00 (  0%)   0.03 (  0%)     502 kB (  0%)
 reorder blocks                     :   0.04 (  0%)   0.00 (  0%)   0.01 (  0%)    1015 kB (  0%)
 shorten branches                   :   0.02 (  0%)   0.00 (  0%)   0.00 (  0%)       0 kB (  0%)
 final                              :   0.04 (  0%)   0.00 (  0%)   0.03 (  0%)    3408 kB (  0%)
 straight-line strength reduction   :   0.00 (  0%)   0.00 (  0%)   0.01 (  0%)      21 kB (  0%)
 tree loop if-conversion            :   0.01 (  0%)   0.00 (  0%)   0.00 (  0%)     203 kB (  0%)
 rest of compilation                :   0.10 (  1%)   0.01 (  1%)   0.13 (  1%)    3241 kB (  0%)
 remove unused locals               :   0.02 (  0%)   0.00 (  0%)   0.08 (  1%)       3 kB (  0%)
 address taken                      :   0.04 (  0%)   0.01 (  1%)   0.04 (  0%)       0 kB (  0%)
 TOTAL                              :   8.75          1.63         10.40         874064 kB
```

**5) [Автор](https://stackoverflow.com/users/1147830/veio) этого примера:**

```c++
Execution times (seconds)
 phase setup             :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall    1321 kB ( 0%) ggc
 phase parsing           :   7.29 (32%) usr   1.69 (51%) sys   8.99 (35%) wall 1135793 kB (54%) ggc
 phase lang. deferred    :   2.75 (12%) usr   0.40 (12%) sys   3.15 (12%) wall  317920 kB (15%) ggc
 phase opt and generate  :  12.03 (53%) usr   1.17 (36%) sys  13.22 (51%) wall  622545 kB (30%) ggc
 phase check & debug info:   0.01 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall     440 kB ( 0%) ggc
 phase last asm          :   0.63 ( 3%) usr   0.02 ( 1%) sys   0.64 ( 2%) wall   26440 kB ( 1%) ggc
 phase finalize          :   0.00 ( 0%) usr   0.01 ( 0%) sys   0.02 ( 0%) wall       0 kB ( 0%) ggc
 |name lookup            :   1.30 ( 6%) usr   0.29 ( 9%) sys   1.42 ( 5%) wall  153617 kB ( 7%) ggc
 |overload resolution    :   3.37 (15%) usr   0.59 (18%) sys   3.30 (13%) wall  360551 kB (17%) ggc
 garbage collection      :   1.80 ( 8%) usr   0.01 ( 0%) sys   1.82 ( 7%) wall       0 kB ( 0%) ggc
 dump files              :   0.11 ( 0%) usr   0.05 ( 2%) sys   0.18 ( 1%) wall       0 kB ( 0%) ggc
 callgraph construction  :   0.44 ( 2%) usr   0.10 ( 3%) sys   0.59 ( 2%) wall   26388 kB ( 1%) ggc
 callgraph optimization  :   0.21 ( 1%) usr   0.11 ( 3%) sys   0.23 ( 1%) wall   16131 kB ( 1%) ggc
 ipa free inline summary :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 cfg construction        :   0.03 ( 0%) usr   0.00 ( 0%) sys   0.03 ( 0%) wall    2119 kB ( 0%) ggc
 cfg cleanup             :   0.08 ( 0%) usr   0.00 ( 0%) sys   0.11 ( 0%) wall     169 kB ( 0%) ggc
 trivially dead code     :   0.05 ( 0%) usr   0.02 ( 1%) sys   0.13 ( 0%) wall       0 kB ( 0%) ggc
 df scan insns           :   0.30 ( 1%) usr   0.02 ( 1%) sys   0.38 ( 1%) wall    1126 kB ( 0%) ggc
 df live regs            :   0.07 ( 0%) usr   0.00 ( 0%) sys   0.10 ( 0%) wall       0 kB ( 0%) ggc
 df reg dead/unused notes:   0.10 ( 0%) usr   0.03 ( 1%) sys   0.12 ( 0%) wall    7774 kB ( 0%) ggc
 register information    :   0.03 ( 0%) usr   0.00 ( 0%) sys   0.04 ( 0%) wall       0 kB ( 0%) ggc
 alias analysis          :   0.02 ( 0%) usr   0.02 ( 1%) sys   0.08 ( 0%) wall    2621 kB ( 0%) ggc
 rebuild jump labels     :   0.05 ( 0%) usr   0.01 ( 0%) sys   0.03 ( 0%) wall       0 kB ( 0%) ggc
 preprocessing           :   1.16 ( 5%) usr   0.45 (14%) sys   1.61 ( 6%) wall  209848 kB (10%) ggc
 parser (global)         :   0.43 ( 2%) usr   0.29 ( 9%) sys   0.83 ( 3%) wall  193966 kB ( 9%) ggc
 parser struct body      :   1.03 ( 5%) usr   0.20 ( 6%) sys   1.37 ( 5%) wall  199825 kB ( 9%) ggc
 parser enumerator list  :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall     574 kB ( 0%) ggc
 parser function body    :   0.53 ( 2%) usr   0.06 ( 2%) sys   0.49 ( 2%) wall   35252 kB ( 2%) ggc
 parser inl. func. body  :   0.13 ( 1%) usr   0.03 ( 1%) sys   0.14 ( 1%) wall   11720 kB ( 1%) ggc
 parser inl. meth. body  :   1.14 ( 5%) usr   0.19 ( 6%) sys   1.45 ( 6%) wall  115776 kB ( 6%) ggc
 template instantiation  :   4.11 (18%) usr   0.82 (25%) sys   4.78 (18%) wall  566245 kB (27%) ggc
 inline parameters       :   0.05 ( 0%) usr   0.01 ( 0%) sys   0.03 ( 0%) wall   12792 kB ( 1%) ggc
 tree gimplify           :   0.28 ( 1%) usr   0.03 ( 1%) sys   0.27 ( 1%) wall   55239 kB ( 3%) ggc
 tree eh                 :   0.19 ( 1%) usr   0.00 ( 0%) sys   0.14 ( 1%) wall   20091 kB ( 1%) ggc
 tree CFG construction   :   0.02 ( 0%) usr   0.00 ( 0%) sys   0.05 ( 0%) wall   34452 kB ( 2%) ggc
 tree CFG cleanup        :   0.09 ( 0%) usr   0.02 ( 1%) sys   0.15 ( 1%) wall      27 kB ( 0%) ggc
 tree PHI insertion      :   0.01 ( 0%) usr   0.01 ( 0%) sys   0.01 ( 0%) wall    5960 kB ( 0%) ggc
 tree SSA rewrite        :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.04 ( 0%) wall    8035 kB ( 0%) ggc
 tree SSA other          :   0.04 ( 0%) usr   0.03 ( 1%) sys   0.12 ( 0%) wall    1604 kB ( 0%) ggc
 tree operand scan       :   0.06 ( 0%) usr   0.04 ( 1%) sys   0.08 ( 0%) wall   16681 kB ( 1%) ggc
 dominance frontiers     :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 dominance computation   :   0.14 ( 1%) usr   0.04 ( 1%) sys   0.12 ( 0%) wall       0 kB ( 0%) ggc
 out of ssa              :   0.04 ( 0%) usr   0.03 ( 1%) sys   0.14 ( 1%) wall       8 kB ( 0%) ggc
 expand vars             :   0.10 ( 0%) usr   0.00 ( 0%) sys   0.14 ( 1%) wall   10387 kB ( 0%) ggc
 expand                  :   0.79 ( 3%) usr   0.05 ( 2%) sys   0.77 ( 3%) wall   89756 kB ( 4%) ggc
 post expand cleanups    :   0.10 ( 0%) usr   0.00 ( 0%) sys   0.05 ( 0%) wall   14796 kB ( 1%) ggc
 varconst                :   0.03 ( 0%) usr   0.00 ( 0%) sys   0.03 ( 0%) wall     532 kB ( 0%) ggc
 jump                    :   0.00 ( 0%) usr   0.01 ( 0%) sys   0.00 ( 0%) wall       0 kB ( 0%) ggc
 integrated RA           :   4.92 (22%) usr   0.12 ( 4%) sys   4.54 (17%) wall  167029 kB ( 8%) ggc
 LRA non-specific        :   0.38 ( 2%) usr   0.01 ( 0%) sys   0.81 ( 3%) wall     776 kB ( 0%) ggc
 LRA virtuals elimination:   0.07 ( 0%) usr   0.00 ( 0%) sys   0.07 ( 0%) wall    6530 kB ( 0%) ggc
 LRA reload inheritance  :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall       4 kB ( 0%) ggc
 LRA create live ranges  :   0.03 ( 0%) usr   0.00 ( 0%) sys   0.02 ( 0%) wall      40 kB ( 0%) ggc
 LRA hard reg assignment :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 reload                  :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.03 ( 0%) wall       0 kB ( 0%) ggc
 thread pro- & epilogue  :   0.16 ( 1%) usr   0.01 ( 0%) sys   0.26 ( 1%) wall   19997 kB ( 1%) ggc
 shorten branches        :   0.17 ( 1%) usr   0.01 ( 0%) sys   0.16 ( 1%) wall       0 kB ( 0%) ggc
 reg stack               :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall       0 kB ( 0%) ggc
 final                   :   0.63 ( 3%) usr   0.04 ( 1%) sys   0.69 ( 3%) wall   29353 kB ( 1%) ggc
 symout                  :   1.28 ( 6%) usr   0.06 ( 2%) sys   1.23 ( 5%) wall  173563 kB ( 8%) ggc
 uninit var analysis     :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.01 ( 0%) wall       0 kB ( 0%) ggc
 rest of compilation     :   0.81 ( 4%) usr   0.18 ( 5%) sys   0.93 ( 4%) wall   34415 kB ( 2%) ggc
 unaccounted todo        :   0.25 ( 1%) usr   0.16 ( 5%) sys   0.39 ( 1%) wall       0 kB ( 0%) ggc
 TOTAL                 :  22.71             3.29            26.03            2104543 kB
```

**6) [Автор](https://stackoverflow.com/users/1247301/andreas-florath) этого примера:**

```c++
Execution times (seconds)
 callgraph construction:   0.02 ( 2%) usr   0.00 ( 0%) sys   0.02 ( 1%) wall      25 kB ( 0%) ggc
 preprocessing         :   0.72 (59%) usr   0.06 (25%) sys   0.80 (54%) wall    8004 kB (12%) ggc
 parser                :   0.24 (20%) usr   0.12 (50%) sys   0.36 (24%) wall   43185 kB (65%) ggc
 name lookup           :   0.01 ( 1%) usr   0.05 (21%) sys   0.03 ( 2%) wall    1447 kB ( 2%) ggc
 tree gimplify         :   0.01 ( 1%) usr   0.00 ( 0%) sys   0.02 ( 1%) wall     277 kB ( 0%) ggc
 tree find ref. vars   :   0.01 ( 1%) usr   0.00 ( 0%) sys   0.01 ( 1%) wall      15 kB ( 0%) ggc
 varconst              :   0.19 (15%) usr   0.01 ( 4%) sys   0.20 (14%) wall   11288 kB (17%) ggc
 integrated RA         :   0.02 ( 2%) usr   0.00 ( 0%) sys   0.02 ( 1%) wall      74 kB ( 0%) ggc
 reload                :   0.01 ( 1%) usr   0.00 ( 0%) sys   0.01 ( 1%) wall      61 kB ( 0%) ggc
 TOTAL                 :   1.23             0.24             1.48              66378 kB
```

**7-8) [Автор](https://stackoverflow.com/users/2614655/khurshid-normuradov) этих двух примеров:**

```c++
Execution times (seconds)
 garbage collection    :   0.06 ( 1%) usr   0.00 ( 0%) sys   0.06 ( 0%) wall       0 kB ( 0%) ggc
 preprocessing         :   0.03 ( 0%) usr   0.04 ( 2%) sys   0.09 ( 1%) wall     293 kB ( 0%) ggc
 parser                :  10.41 (97%) usr   1.61 (95%) sys  12.01 (96%) wall 2829842 kB (99%) ggc
 name lookup           :   0.12 ( 1%) usr   0.04 ( 2%) sys   0.23 ( 2%) wall    7236 kB ( 0%) ggc
 dead store elim1      :   0.01 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall       0 kB ( 0%) ggc
 symout                :   0.15 ( 1%) usr   0.00 ( 0%) sys   0.15 ( 1%) wall   12891 kB ( 0%) ggc
 unaccounted todo      :   0.00 ( 0%) usr   0.01 ( 1%) sys   0.00 ( 0%) wall       0 kB ( 0%) ggc
 TOTAL                 :  10.78             1.70            12.55            2850835 kB
```

```c++
Execution times (seconds)
 preprocessing         :   0.02 ( 2%) usr   0.01 ( 5%) sys   0.05 ( 4%) wall     293 kB ( 0%) ggc
 parser                :   0.54 (45%) usr   0.10 (53%) sys   0.71 (50%) wall   95339 kB (58%) ggc
 name lookup           :   0.47 (39%) usr   0.04 (21%) sys   0.47 (33%) wall   20197 kB (12%) ggc
 tree PRE              :   0.01 ( 1%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall       1 kB ( 0%) ggc
 varconst              :   0.00 ( 0%) usr   0.01 ( 5%) sys   0.00 ( 0%) wall      17 kB ( 0%) ggc
 symout                :   0.17 (14%) usr   0.03 (16%) sys   0.18 (13%) wall   47092 kB (29%) ggc
 TOTAL                 :   1.21             0.19             1.41             163493 kB
```


**9-10) [Автор](https://stackoverflow.com/users/9154776/user9154776) этих двух примеров:**

```c++
Execution times (seconds)
 phase setup             :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall    1189 kB (16%) ggc
 phase parsing           :   0.03 (100%) usr   0.02 (100%) sys   0.06 (100%) wall    6301 kB (83%) ggc
 preprocessing           :   0.01 (33%) usr   0.01 (50%) sys   0.04 (67%) wall     488 kB ( 6%) ggc
 parser (global)         :   0.00 ( 0%) usr   0.01 (50%) sys   0.00 ( 0%) wall    3626 kB (48%) ggc
 parser struct body      :   0.02 (67%) usr   0.00 ( 0%) sys   0.01 (17%) wall     778 kB (10%) ggc
 parser function body    :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.01 (17%) wall     436 kB ( 6%) ggc
 TOTAL                 :   0.03             0.02             0.06               7558 kB
```

```c++
Execution times (seconds)
 phase setup             :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.00 ( 0%) wall    1384 kB (11%) ggc
 phase parsing           :   0.05 (100%) usr   0.03 (100%) sys   0.10 (100%) wall   10953 kB (88%) ggc
 |name lookup            :   0.00 ( 0%) usr   0.01 (33%) sys   0.01 (10%) wall    1301 kB (10%) ggc
 preprocessing           :   0.01 (20%) usr   0.00 ( 0%) sys   0.03 (30%) wall     878 kB ( 7%) ggc
 parser (global)         :   0.01 (20%) usr   0.01 (33%) sys   0.01 (10%) wall    4592 kB (37%) ggc
 parser struct body      :   0.02 (40%) usr   0.00 ( 0%) sys   0.01 (10%) wall    2837 kB (23%) ggc
 parser function body    :   0.01 (20%) usr   0.01 (33%) sys   0.01 (10%) wall     478 kB ( 4%) ggc
 parser inl. meth. body  :   0.00 ( 0%) usr   0.01 (33%) sys   0.03 (30%) wall     937 kB ( 8%) ggc
 symout                  :   0.00 ( 0%) usr   0.00 ( 0%) sys   0.01 (10%) wall       0 kB ( 0%) ggc
 TOTAL                 :   0.05             0.03             0.10              12490 kB
 ```
