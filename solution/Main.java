//package com.company;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
            myRegBuilder v;
            try {
                v = new myRegBuilder();
                v.input();
                if (v.error) return;
                v.checkPart();
                if (v.error) return;
                v.DFS(0);
                if (v.error) return;
                v.afterDFS();
                if (v.error) return;
                v.toRegExpr();
                if (v.error) return;
            }catch (Exception e)
            {
                return;
            }
    }
}

class myRegBuilder
{
    ArrayList <ArrayList <String> > _symbolsForState = new ArrayList<>();
    ArrayList<ArrayList<String>> FSA = new ArrayList<>();
    String[] _isFinal, _alphabet, _states, _transitions;
    String start = "", _input;
    BufferedReader in;
    BufferedWriter out;
    boolean[] used;
    boolean error = false;

    myRegBuilder() throws IOException {
        in = new BufferedReader(new FileReader("input.txt"));
        out = new BufferedWriter(new FileWriter("output.txt"));
    }

    void input() throws IOException {
        try {
            //States
            _input = in.readLine();
            int index1 = _input.indexOf("[");
            int index2 = _input.indexOf("]");
            String auxiliary = _input.substring(index1 + 1, index2);
            _states = auxiliary.split(",");

            if (!_input.contains("states=[") || index2 == -1)
            {
                error = true;
                out.write("Error:\n");
                out.write("E0: Input file is malformed");
                out.close();
                return;
            }

            //Alphabet
            _input = in.readLine();
            index1 = _input.indexOf('[');
            index2 = _input.indexOf(']');
            auxiliary = _input.substring(index1 + 1, index2);
            _alphabet = auxiliary.split(",");

            if (!_input.contains("alpha=[") || index2 == -1)
            {
                error = true;
                out.write("Error:\n");
                out.write("E0: Input file is malformed");
                out.close();
                return;
            }

            //Start
            _input = in.readLine();
            index1 = _input.indexOf('[');
            index2 = _input.indexOf(']');
            auxiliary = _input.substring(index1 + 1, index2);
            start = auxiliary;

            if (!_input.contains("initial=[") || index2 == -1)
            {
                error = true;
                out.write("Error:\n");
                out.write("E0: Input file is malformed");
                out.close();
                return;
            }

            //End
            _input = in.readLine();
            index1 = _input.indexOf('[');
            index2 = _input.indexOf(']');
            auxiliary = _input.substring(index1 + 1, index2);
            _isFinal = auxiliary.split(",");

            if (!_input.contains("accepting=[") || index2 == -1)
            {
                error = true;
                out.write("Error:\n");
                out.write("E0: Input file is malformed");
                out.close();
                return;
            }

            //Edges
            _input = in.readLine();
            index1 = _input.indexOf('[');
            index2 = _input.indexOf(']');
            auxiliary = _input.substring(index1 + 1, index2);
            _transitions = auxiliary.split(",");
            if (!_input.contains("trans=[") || index2 == -1)
            {
                error = true;
                out.write("Error:\n");
                out.write("E0: Input file is malformed");
                out.close();
            }

        } catch (Exception e) {
            error = true;
            out.write("Error:\n");
            out.write("E0: Input file is malformed");
            out.close();
        }
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
            FSA.add(new ArrayList<>());
            _symbolsForState.add(new ArrayList<>());
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

    void toRegExpr()
    {
        int n = _states.length;
        ArrayList <ArrayList <String> > RegExpr = new ArrayList<>();
        for(int i = 0; i < n; ++i)
        {
            RegExpr.add(new ArrayList<>());
            for(int j = 0; j < n; ++j)
            {
                if (i == j)
                    RegExpr.get(i).add("eps");
                else
                    RegExpr.get(i).add("{}");

            }
        }

        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                if (FSA.get(i).get(j) == null)
                {
                    if (i == j)
                        FSA.get(i).set(j, "eps");
                    else
                        FSA.get(i).set(j, "{}");
                }
            }
        }

        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                String letter = FSA.get(i).get(j);
                if (letter.compareTo("{}") == 0) continue;
                if (i == j) {
                    if (letter.compareTo("eps") == 0) continue;
                    letter += "|eps";
                }
                RegExpr.get(i).set(j, letter);
            }
        }


        for(int k = 0; k < n; ++k)
        {
            for(int i = 0; i < n; ++i)
            {
                for(int j = 0; j < n; ++j)
                {
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

            for(int i = 0; i<n; ++i)
                for(int j = 0; j<n; ++j)
                    RegExpr.get(i).set(j, FSA.get(i).get(j));
        }

        int ind1 = 0;
        for(int i = 0; i<n; ++i)
            if (_states[i].compareTo(start) == 0) {
                ind1 = i;
                break;
            }

        StringBuilder ans = new StringBuilder();
        for(int i = 0; i<_isFinal.length; ++i) {
            int ind2 = -1;
            for (int j = 0; j < n; ++j)
                if (_states[j].compareTo(_isFinal[i]) == 0)
                {
                    ind2 = j;
                    break;
                }
            if(ind2 == -1) continue;
            if (ans.toString().compareTo("") == 0)
                ans.append(RegExpr.get(ind1).get(ind2));
            else
                ans.append("|").append(RegExpr.get(ind1).get(ind2));
        }

        try {
            if (ans.toString().compareTo("") == 0)
                out.write("{}");
            else
                out.write(String.valueOf(ans) + '\n');
            out.close();
        } catch (Exception e)
        {
        }

        seqA n = if n == 2 then ( (3,2), 1) else ( ( (fst (fst seqA(n - 1))) + (-2) * (snd (fst seqA(n - 1))) + 3 * (snd seqA), fst (fst seqA(n - 1)) ), (snd (fst seqA(n - 1))) )
    }
}
