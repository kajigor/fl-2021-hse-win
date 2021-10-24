import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.ArrayList;
import java.io.IOException;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws Exception {

        DKALexer lexer = new DKALexer(CharStreams.fromFileName(args[0]));
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        DKAParser parser = new DKAParser(tokens);
        ParseTree tree = parser.start();
        myRegBuilder visitor = new myRegBuilder(args[1]);
        try {
            visitor.visit(tree);
        } catch (Exception e) {
            System.out.println("Parsing error");
            return;
        }
        try {
            visitor.checkPart();
            if (visitor.error) return;
            visitor.DFS(0);
            if (visitor.error) return;
            visitor.afterDFS();
            if (visitor.error) return;
            visitor.toRegExpr();
            if (visitor.error) return;
        }catch (Exception ignored) {}
    }
}

class myRegBuilder extends Visitor {
    ArrayList <ArrayList <String> > _symbolsForState = new ArrayList<>();
    ArrayList<ArrayList<String>> FSA = new ArrayList<>();
    BufferedWriter out;
    boolean[] used;
    boolean error = false;

    myRegBuilder(String s2) throws IOException {
        out = new BufferedWriter(new FileWriter(s2));
    }

    void DFS(int v)
    {
        used[v] = true;
        for(int i = 0; i<_states.length; ++i)
        {
            if (FSA.get(v).get(i) != null  || FSA.get(i).get(v) != null)
            {
                if (!used[i]) DFS(i);
            }
        }
    }

    void checkPart() throws IOException {
        used = new boolean[_states.length];

        for(int i = 0; i<_states.length; ++i)
            used[i] = false;

        for(int i = 0; i<_states.length; ++i)
        {
            FSA.add(new ArrayList<String>());
            _symbolsForState.add(new ArrayList<String>());
            for(int j = 0; j<_states.length; ++j)
                FSA.get(i).add(null);
        }

        ArrayList <String> states, alphabet, transitions;

        states = new ArrayList<>(Arrays.asList(_states));
        alphabet = new ArrayList<>(Arrays.asList(_alphabet));
        transitions = new ArrayList<>(Arrays.asList(_transitions));

        if (start.equals(""))
        {
            error = true;
            out.write("Error:\n");
            out.write("E4: Initial state is not defined");
            out.close();
            return;
        }

        if (!states.contains(start))
        {
            error = true;
            out.write("Error:\n");
            out.write("E1: A state '" + start + "' is not in the set of states");
            out.close();
            return;
        }

        for(String transition : transitions)
        {
            String [] aux = transition.split(">");
            String st1 = aux[0], st2 = aux[2], letter = aux[1];
            if (!states.contains(st1))
            {
                error = true;
                out.write("Error:\n");
                out.write("E1: A state '" + st1 + "' is not in the set of states");
                out.close();
                return;
            }
            if (!states.contains(st2))
            {
                error = true;
                out.write("Error:\n");
                out.write("E1: A state '" + st2 + "' is not in the set of states");
                out.close();
                return;
            }
            if (!alphabet.contains(letter))
            {
                error = true;
                out.write("Error:\n");
                out.write("E3: A transition '" + letter + "' is not represented in the alphabet");
                out.close();
                return;
            }

            int ind1 = states.indexOf(st1), ind2 = states.indexOf(st2);

            if (_symbolsForState.get(ind1).contains(letter))
            {
                error = true;
                out.write("Error:\n");
                out.write("E5: FSA is nondeterministic");
                out.close();
                return;
            }

            if (FSA.get(ind1).get(ind2) != null)
            {
                String from = FSA.get(ind1).get(ind2);
                from = from + "|" + letter;
                FSA.get(ind1).set(ind2, from);
            } else
            {
                FSA.get(ind1).set(ind2, letter);
            }

            _symbolsForState.get(ind1).add(letter);
        }
    }

    void afterDFS() throws IOException {
        for(boolean checker : used)
            if (!checker)
            {
                error = true;
                out.write("Error:\n");
                out.write("E2: Some states are disjoint");
                out.close();
                return;
            }
    }

    void toRegExpr() {
        int n = _states.length;
        System.out.println(_states[0]);
        ArrayList<ArrayList<String>> RegExpr = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            RegExpr.add(new ArrayList<String>());
            for (int j = 0; j < n; ++j) {
                if (i == j)
                    RegExpr.get(i).add("eps");
                else
                    RegExpr.get(i).add("{}");

            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (FSA.get(i).get(j) == null) {
                    if (i == j)
                        FSA.get(i).set(j, "eps");
                    else
                        FSA.get(i).set(j, "{}");
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                String letter = FSA.get(i).get(j);
                if (letter.compareTo("{}") == 0) continue;
                if (i == j) {
                    if (letter.compareTo("eps") == 0) continue;
                    letter += "|eps";
                }
                RegExpr.get(i).set(j, letter);
            }
        }

        try {
            out.write("After " + 0 + "-th step:\n");
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    out.write("R " + "[" + i + "] " + "[" + j + "] : ");
                    out.write(FSA.get(i).get(j));
                    out.write('\n');
                }
            }
        } catch (Exception e)
        {
        }

        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    String _letter_ik = RegExpr.get(i).get(k);
                    String _letter_kk = RegExpr.get(k).get(k);
                    String _letter_kj = RegExpr.get(k).get(j);
                    String _letter_ij = RegExpr.get(i).get(j);
                    String _to_replace = "(" + _letter_ik + ")" +
                            "(" + _letter_kk + ")*" +
                            "(" + _letter_kj + ")|" +
                            "(" + _letter_ij + ")";
                    FSA.get(i).set(j, _to_replace);
                }
            }

            try {
                out.write("After " + (k+1) + "-th step:\n");
                for (int i = 0; i < n; ++i) {
                    for (int j = 0; j < n; ++j) {
                        out.write("R " + "[" + i + "] " + "[" + j + "] : ");
                        out.write(FSA.get(i).get(j));
                        out.write('\n');
                    }
                }
            } catch (Exception e)
            {
            }
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    RegExpr.get(i).set(j, FSA.get(i).get(j));
        }

        int ind1 = 0;
        for (int i = 0; i < n; ++i)
            if (_states[i].compareTo(start) == 0) {
                ind1 = i;
                break;
            }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < _isFinal.length; ++i) {
            int ind2 = -1;
            for (int j = 0; j < n; ++j)
                if (_states[j].compareTo(_isFinal[i]) == 0) {
                    ind2 = j;
                    break;
                }
            if (ind2 == -1) continue;
            if (ans.toString().compareTo("") == 0)
                ans.append(RegExpr.get(ind1).get(ind2));
            else
                ans.append("|").append(RegExpr.get(ind1).get(ind2));
        }

        try {
            if (ans.toString().compareTo("") == 0)
                out.write("{}");
            else
            {
                out.write("FINAL ANSWER: ");
                out.write(String.valueOf(ans) + '\n');
            }
            out.close();
        } catch (Exception e) {
        }

    }
}