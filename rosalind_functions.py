#DNA
def base_count(x):
    dict_nuc_count = {}
    for i in x:
        if i in dict_nuc_count:
            dict_nuc_count[i] += 1
        else:
            dict_nuc_count[i] = 1
    ret_ans = str(dict_nuc_count['A']) + ' ' + str(dict_nuc_count['C']) + ' ' + str(dict_nuc_count['G']) + ' ' + str(dict_nuc_count['T'])
    return ret_ans

#RNA
def DNA_txn(x):
    RNA = x.replace('T', 'U')
    return RNA

#REVC
def rev_compl(x):
    rev_compl = x.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
