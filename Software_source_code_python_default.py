import sys, os, string, time
from getpass import getuser
now = time.time

if getuser() == 'melazar':
    SCRIPTS_DIR = r"C:\Dev\p4\MainDev\policies\scripts"
    SCRIPTS_DIR_2 = r"h:\My Documents\Work\Sprint\68\Rodne"
else:
    SCRIPTS_DIR = os.path.dirname(__file__) + r'\..\..\..\..\scripts'
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)
if SCRIPTS_DIR_2 not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR_2)

Timeout_ms = 6500
dict_context_1 = {"Timeout_ms":u"%d"%Timeout_ms,"context":u"1"}
dict_context_2 = {"Timeout_ms":u"%d"%Timeout_ms,"context":u"2"}
dict_context_3 = {"Timeout_ms":u"%d"%Timeout_ms,"context":u"3"}
dicts_num = [ dict_context_1, dict_context_2, dict_context_3 ]
dict_context_0 = {"Timeout_ms":u"%d"%Timeout_ms,"context":u"0"} #Extra Wide
dicts_num.append(dict_context_0)                                #Extra Wide
dict_context_w = {"Timeout_ms":u"%d"%Timeout_ms,"context":u"wide"}
dict_context_d = {"Timeout_ms":u"%d"%Timeout_ms,"context":u"default"}
dict_context_n = {"Timeout_ms":u"%d"%Timeout_ms,"context":u"narrow"}
dicts_word = [ dict_context_w, dict_context_d, dict_context_n ]
thresholds = [1,1,1] # Thresholds of Wide/Default/Narrow
##Methods_CreditCards = ['hasUSCCN', 'hasUSCCN_wide_minus_default', 'hasEUCCN', 'hasUSCNCCN', 'hasJPCCN', 'hasCreditCard', 'hasIsracard', 'has_any_Israeli_Credit_Cards']

#ResultPath = 

#Testsrcdir_FP=r'\\10.0.6.105\c$\python_unitests\Files\FP\z' # FP folder
Testsrcdir_FP=r'c:\work\FP\Files\FP\z' # FP folder
Testsrcdir_Test=r'\\10.0.6.105\c$\python_unitests\Files\Test' # Test folder
Testsrcdir_Mega=r'\\10.0.6.105\c$\python_unitests\Files\MegaBreach' # MegaBreach folder
Testsrcdir_China=r'\\10.0.6.105\c$\python_unitests\Files\China' # Chine folder
Testsrcdir_CP=r'\\10.0.6.105\c$\python_unitests\Files\CP\Std Bank' # CPs
Testsrcdir_Japan=r'\\10.0.6.105\c$\python_unitests\Files\Japan' # Jap folder
Testsrcdir_Rodne=r'\\10.0.6.105\c$\python_unitests\Rodne' # Rodne folder, add \FP for CDS FP
Testsrcdir_Performance = r'\\10.0.6.105\c$\python_unitests\Perf' # Performance folder
Testsrcdir_CCN = 'c:\Work\FP\Files\CCN\TP'
Testsrcdir_Sanity = r'c:\work\FP\Results'
##Testsrcdir=r'\\10.0.6.105\c$\python_unitests\SSN\Test' # folder
Testdir = {'FP':Testsrcdir_FP,'Test':Testsrcdir_Test,'Mega':Testsrcdir_Mega,'China':Testsrcdir_China,'CP':Testsrcdir_CP,'Japan':Testsrcdir_Japan,'Rodne':Testsrcdir_Rodne,'Performance':Testsrcdir_Performance,'Sanity':Testsrcdir_Sanity}
finnese = 7

#########################################################################################################################
#This section is for configuring the generic script

##gen_dict_suppert_term = {'ID Number pattern':u'(?:(?:[01234]\\d|5[0123])(?:[05][1-9]|[16][0-2])(?:0[1-9]|[12]\\d|3[01])[\\-\\\\\\/]?\\d{3}|\\d{2}(?:[05][1-9]|[16][0-2])(?:0[1-9]|[12]\\d|3[01])[\\-\\\\\\/]?\\d{4})',\
##            'Generic Pattern':u'',\
##            'Preceding pattern':u'\\b',\
##            'Consecutive pattern':u'\\b',\
##            'Check-digit(s) algorithm':u'Rodne Cislo',\
##            'Statistical validation':u'No statistical validation',\
##            'Support terms':u'Rodne Cislo,Rodn\xe9 Cislo,Rodne \u010dislo,Rodne C\xedslo,Rodn\xe9 \u010dislo,Rodn\xe9 C\xedslo,Rodne \u010d\xedslo,Rodn\xe9 \u010d\xedslo,Birth Number,Birth Numbers,R\u010d,R.\u010d,R. \u010d',\
##            'Support term max proximity':u'100',\
##            'Modulu 10 weights':u'',\
##            'Modulu 11 weights':u'',\
##            'Masking':u'No Masking',\
##            'Number of unmasked characters':u''} #Rodne Cislo with support terms 
##gen_dict_9_digit = {'ID Number pattern':u'(?:(?:[01234]\d|5[0123])(?:[05][1-9]|[16][0-2])(?:0[1-9]|[12]\d|3[01])[\-\\\/]?\d{3})',\
##            'Generic Pattern':u'\d{6}[\-\\\/]?\d{3}',\
##            'Preceding pattern':u'\\b',\
##            'Consecutive pattern':u'\\b',\
##            'Check-digit(s) algorithm':u'Rodne Cislo',\
##            'Statistical validation':u'50%',\
##            'Support terms':u'',\
##            'Support term max proximity':u'',\
##            'Modulu 10 weights':u'',\
##            'Modulu 11 weights':u'',\
##            'Masking':u'No Masking',\
##            'Number of unmasked characters':u''}  #Rodne Cislo without support terms, 9 digit stat valid at 50%
##gen_dict_10_digit = {'ID Number pattern':u'(?:(?:5[3-9]|[016-9]\d|2[0-5])(?:[05][1-9]|[16][0-2])(?:0[1-9]|[12]\d|3[01])[\-\\\/]?\d{4})',\
##            'Generic Pattern':u'\d{6}[\-\\\/]?\d{4}',\
##            'Preceding pattern':u'\\b',\
##            'Consecutive pattern':u'\\b',\
##            'Check-digit(s) algorithm':u'Rodne Cislo',\
##            'Statistical validation':u'50%',\
##            'Support terms':u'',\
##            'Support term max proximity':u'',\
##            'Modulu 10 weights':u'',\
##            'Modulu 11 weights':u'',\
##            'Masking':u'No Masking',\
##            'Number of unmasked characters':u''}  #Rodne Cislo without support terms, 10 digit stat valid at 50%
##gen_dict_wide = {'ID Number pattern':u'(?:(?:[01234]\d|5[0123])(?:[05][1-9]|[16][0-2])(?:0[1-9]|[12]\d|3[01])[\-\\\/]?\d{3})|(?:(?:5[3-9]|[016-9]\d|2[0-5])(?:[05][1-9]|[16][0-2])(?:0[1-9]|[12]\d|3[01])[\-\\\/]?\d{4})',\
##            'Generic Pattern':u'',\
##            'Preceding pattern':u'\\b',\
##            'Consecutive pattern':u'\\b',\
##            'Check-digit(s) algorithm':u'Rodne Cislo',\
##            'Statistical validation':u'No statistical validation',\
##            'Support terms':u'',\
##            'Support term max proximity':u'',\
##            'Modulu 10 weights':u'',\
##            'Modulu 11 weights':u'',\
##            'Masking':u'No Masking',\
##            'Number of unmasked characters':u''}  #Rodne Cislo wide
##
##gen_dict = [gen_dict_wide,gen_dict_suppert_term,gen_dict_9_digit,gen_dict_10_digit] # Edit for a different number of classifiers/dictionaries
##thresholds_gs = [1,1,1,1] # Thresholds of classifiers above
##Names = ['Rodne_Cislo_wide','Rodne_Cislo_suppert_term','Rodne_Cislo_9_digit','Ronde_Cislo_10_digit'] # Names of classifiers above

std_bank_SA_11D = {u'ID Number pattern':u'1\d{10}',\
            u'Generic Pattern':u'',\
            u'Preceding pattern':u'\\b',\
            u'Consecutive pattern':u'\\b',\
            u'Check-digit(s) algorithm':u'Modulu 11 validation',\
            u'Statistical validation':u'No statistical validation',\
            u'Support terms':u'',\
            u'Support term max proximity':u'100',\
            u'Modulu 10 weights':u'',\
            u'Modulu 11 weights':u'13,12,9,8,7,6,5,4,3,2',\
            u'Masking':u'No Masking',\
            u'Number of unmasked characters':u''} # South African 11-digit account numbers
std_bank_SA_9D = {u'ID Number pattern':u'\d{9}(?<!00000000\d)',\
            u'Generic Pattern':u'\\d{11}',\
            u'Preceding pattern':u'\\b',\
            u'Consecutive pattern':u'\\b',\
            u'Check-digit(s) algorithm':u'Modulu 11 validation',\
            u'Statistical validation':u'No statistical validation',\
            u'Support terms':u'',\
            u'Support term max proximity':u'100',\
            u'Modulu 10 weights':u'',\
            u'Modulu 11 weights':u'9,8,7,6,5,4,3,2',\
            u'Masking':u'No Masking',\
            u'Number of unmasked characters':u''} # South African 9-digit account numbers 
std_bank_SA_9D_00 = {u'ID Number pattern':u'00\d{9}(?<!00000000\d)',\
            u'Generic Pattern':u'',\
            u'Preceding pattern':u'\\b',\
            u'Consecutive pattern':u'\\b',\
            u'Check-digit(s) algorithm':u'Modulu 11 validation',\
            u'Statistical validation':u'No statistical validation',\
            u'Support terms':u'',\
            u'Support term max proximity':u'100',\
            u'Modulu 10 weights':u'',\
            u'Modulu 11 weights':u'1,1,9,8,7,6,5,4,3,2',\
            u'Masking':u'No Masking',\
            u'Number of unmasked characters':u''} # South African 9-digit account numbers that start with 00 
std_bank_NA_11D = {u'ID Number pattern':u'6\d{10}',\
            u'Generic Pattern':u'',\
            u'Preceding pattern':u'\\b',\
            u'Consecutive pattern':u'\\b',\
            u'Check-digit(s) algorithm':u'Modulu 11 validation',\
            u'Statistical validation':u'No statistical validation',\
            u'Support terms':u'',\
            u'Support term max proximity':u'100',\
            u'Modulu 10 weights':u'',\
            u'Modulu 11 weights':u'13,12,9,8,7,6,5,4,3,2',\
            u'Masking':u'No Masking',\
            u'Number of unmasked characters':u''} # Namibian 11-digit account numbers 
std_bank_support_term = {u'ID Number pattern':u'0(?:[0-57-9]\d{4}|6(?:00(?:[0-5]\d|6[0-6])|39(?:[7-9]\d|6[8-9])|[4-9]\d{3}))\d{5}(?<!00000000000)',\
            u'Generic Pattern':u'\\d{11}',\
            u'Preceding pattern':u'\\b',\
            u'Consecutive pattern':u'\\b',\
            u'Check-digit(s) algorithm':u'Modulu 11 validation',\
            u'Statistical validation':u'No statistical validation',\
            u'Support terms':u'acc number,acct number,account number,acc num,acct num,account num,account no,acct no,acc no,bank account,acc. number,acct. number,account. number,acc. num,acct. num,account. num,account. no,acct. no,acc. no,bank account',\
            u'Support term max proximity':u'100',\
            u'Modulu 10 weights':u'',\
            u'Modulu 11 weights':u'1,1,9,8,7,6,5,4,3,2',\
            u'Masking':u'No Masking',\
            u'Number of unmasked characters':u''} # Standrad Bank account numbers  with support terms
std_bank_statistical_validation = {u'ID Number pattern':u'0(?:[0-57-9]\d{4}|6(?:00(?:[0-5]\d|6[0-6])|39(?:[7-9]\d|6[8-9])|[4-9]\d{3}))\d{5}(?<!00000000000)',\
            u'Generic Pattern':u'\\d{11}',\
            u'Preceding pattern':u'\\b',\
            u'Consecutive pattern':u'\\b',\
            u'Check-digit(s) algorithm':u'Modulu 11 validation',\
            u'Statistical validation':u'50%',\
            u'Support terms':u'',\
            u'Support term max proximity':u'100',\
            u'Modulu 10 weights':u'',\
            u'Modulu 11 weights':u'1,1,9,8,7,6,5,4,3,2',\
            u'Masking':u'No Masking',\
            u'Number of unmasked characters':u''} # Standrad Bank account numbers without support terms, stat valid at 50%

gen_dict = [std_bank_SA_11D,std_bank_SA_9D,std_bank_SA_9D_00,std_bank_NA_11D,std_bank_support_term,std_bank_statistical_validation] # Edit for a different number of classifiers/dictionaries
thresholds_gs = [1,1,1,1,1,1] # Thresholds of classifiers above
Names = ['std_bank_SA_11D','std_bank_SA_9D','std_bank_SA_9D_00','std_bank_NA_11D','std_bank_support_term','std_bank_statistical_validation'] # Names of classifiers above

#######################################################################################################################################################################################
Dictionaries = {'BLANK - SAME NAME' : dicts_num, 'WORD' : dicts_word, 'GENERIC' : gen_dict}
ResultsFileName_default = r'C:\Work\FP\Results'
threshold = 1

def create_list_of_test_files(home_dir, is_recursive = False):
    time_now = now()
    list_of_files = []
    undecoded_list = []
    for path, subdirs, files in os.walk(home_dir):
        for file_name in files:
            full_file_path = os.path.join(path, file_name)
            try:
                temp_var = open(full_file_path, "rb").read().decode('utf16')
                list_of_files.append(full_file_path)
            except:
                undecoded_list.append(full_file_path)
        if not is_recursive:
            break
    #print 'Path: %s'%home_dir
    #print 'Recursive: %s'%is_recursive
    print 'Generating list of test files took: %s'%(now()-time_now)
    #print 'Number of files: %s'%len(list_of_files)
    #print 'AVG load and decode time: %f ms'%(1000*(now()-time_now)/len(list_of_files))
    return list_of_files, undecoded_list, (now()-time_now)


#test_dir = r'\\10.0.6.105\c$\python_unitests\Files\China'
#test_dir = r'\\10.0.6.105\c$\python_unitests\CCN\TP'
test_dir = r'\\10.0.6.105\c$\python_unitests\Files\Japan'
#test_dir = r'\\10.0.6.105\c$\python_unitests\Files\Z'
#test_dir = r'\\10.0.6.105\c$\python_unitests\Files\FP\z'
#create_list_of_test_files(test_dir)
#create_list_of_test_files(test_dir,True)


def create_list_of_dictionaries(Dictionary):
    if isinstance(Dictionary, str) and Dictionary in Dictionaries:
        Dictionary = Dictionaries[Dictionary]
    elif isinstance(Dictionary, int): # Test a specific GS classifier
        Dictionary = [gen_dict[Dictionary]]
    return Dictionary


def Accuracy_test(module, methods, test_file_dir, Dictionary = 'BLANK - SAME NAME', type = 'Test'):
    Accuracy_test_start_time = now()
    if isinstance(methods, str): # A single method is tested
        methods = [methods]
    list_of_dictioneries = create_list_of_dictionaries(Dictionary)
    test_files_list, undecode_test_file_list, generate_list_of_files_run_time = create_list_of_test_files(test_file_dir) 
    for method in methods:
        method_start_time = now()
        exec('from %s import %s as func_to_test'%(module, method))
        
        RES_File = ResultsFileName_default + "\%s %s - Accuracy - %s - %s - %s.csv"%(time.strftime('%x').replace('/','-'),time.strftime('%X').replace(':','_'),type, module, method)
        ResultsCSV = open(RES_File, 'w')
        ResultsCSV.write('\n\n----------------   Test Folder -  %s   ----------------\n'%test_file_dir)
        ResultsCSV.write('Run time for generate list of files run time is: %s s\n\n'%generate_list_of_files_run_time)
        ResultsCSV.write('List of undecoded files:\n%s'%'\n'.join(undecode_test_file_list))
        ResultsCSV.write('\n\n----------------   Method - %s   ----------------'%method)
        
        for dictionary in list_of_dictioneries:
            dic_start_time = now()
            ResultsCSV.write('\n\n----------------   Dictionary - %s   ----------------\n\n'%dictionary)
            FP_count = 0
            for test_file in test_files_list:
                text = open(test_file, "rb").read().decode('utf16')
                results = func_to_test(text, dictionary)
                if results[0] >= threshold:
                    FP_count += 1
                    ResultsCSV.write('\n%s :\n%s\n'%(os.path.basename(test_file),results))
            ResultsCSV.write('\nRun time for this dictionary is: %s s'%(now() - dic_start_time ))
        ResultsCSV.write('\n\nRun time for %s is: %s s'%(method, (now() - method_start_time )))
        ResultsCSV.close()
    print 'Running Accuracy tests took: %s s'%(now() - Accuracy_test_start_time)
                
Accuracy_test('CreditCards','hasUSCCN', test_dir)




def Accuracy_compare(module_old, module_new, method_old, method_new='BLANK - SAME NAME', Dictionary='BLANK - SAME NAME', type='Test', Abs='True'): #Dictionary: \d for a single classifer from the list
    Testsrcdir = Testdir[type]
    method_new = method_new.replace('BLANK - SAME NAME',method_old)
    ResultsFileName = r"C:\Work\FP\Results\%s %s - Accuracy compare - %s - %s - %s Vs %s - %s.csv"%(time.strftime('%x').replace('/','-'),time.strftime('%X').replace(':','_'), type, module_old, method_old, module_new, method_new) #Results file
    ##    ResultsFileName = r"C:\Work\FP\Results\mike.csv"
    exec('from %s import %s as func_old'%(module_old, method_old))
    exec('from %s import %s as func_new'%(module_new, method_new))
    ResultsCSV = open(ResultsFileName,'w')
    ResultsCSV.write('Comparing ' + module_old + '.' + method_old + ' Vs. ' + module_new + '.' + method_new + "\nTime: " + time.strftime('%X %x'))
    dictionary = 3
    if Dictionary == 'BLANK - SAME NAME' or Dictionary == 'number':
        dic = dicts_num
    else:
        dic = dicts_word
    #dic = dicts_word # GENERALIZAAAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if Abs:
        ResultsCSV.write('\n\n------------------   Compering !ABSOLUTELY! script accuracy, old VS. new   ------------------\n')
    else:
        ResultsCSV.write('\n\n------------------   Compering script accuracy, old VS. new   ------------------\n')
    if isinstance(Dictionary, int): # if a Dictionarty in a num, make dica list with only one dictionary
##        ResultsCSV.write('\nThe Generic Dictinary is:\n%s'%gen_dict[Dictionary])
        if Dictionary < len(dic):
            dic = [dic[Dictionary]]
        else:
            dic = [dic[-1]]
        new_d = gen_dict[Dictionary]
    for i,d in enumerate(dic):
        failed_to_read, successfuly_read = 0, 0
        ResultsCSV.write('\n\n---------------   %s   ----------------'%d)
        j = Dictionary
        if Dictionary == 'BLANK - SAME NAME' or Dictionary == 'number':
            new_d = d
            ResultsCSV.write('\n\n---------------   %s   ---------------'%new_d)
        elif Dictionary=='GENERIC':
            new_d = gen_dict[i]
            j = i
            ResultsCSV.write('\n------------------   The Generic Dictinary is: %s   ------------------\n%s'%(Names[j],new_d))
        elif isinstance(Dictionary, int):
            ResultsCSV.write('\n------------------   The Generic Dictinary is: %s   ------------------\n%s'%(Names[Dictionary],new_d))
        for f in os.listdir(Testsrcdir):
            text = open( string.join( [Testsrcdir, f], "\\"),  "rb").read()
            try:
                text = text.decode('utf16')
                successfuly_read += 1
            except:
                failed_to_read += 1
                continue
            results_old = func_old(text,d)
            results_new = func_new(text,new_d)
            if (Dictionary=='GENERIC' or isinstance(Dictionary, int)) and results_new[0] < thresholds_gs[i]:
                results_new = [0]
            if Abs == 'True':
                    if results_old == [0] and results_new != [0]:
                        ResultsCSV.write('\n\nWorse: %s\nOld: %s\nNew: %s\n\n\n'%(f,results_old,results_new))
                    if results_old != [0] and results_new == [0]:
                        ResultsCSV.write('\n\nBetter: %s\nOld: %s\nNew: %s\n\n\n'%(f,results_old,results_new))
                    if results_old != [0] and results_new != [0]:
                        ResultsCSV.write('\n\nSame: %s\nOld: %s\nNew: %s\n\n\n'%(f,results_old,results_new))
            elif Abs == 'False':
                if results_old[0] < results_new[0]:
                    ResultsCSV.write('\n\nWorse: %s\nOld: %s\nNew: %s\n\n\n'%(f,results_old,results_new))
                if results_old[0] > results_new[0]:
                    ResultsCSV.write('\n\nBetter: %s\nOld: %s\nNew: %s\n\n\n'%(f,results_old,results_new))
                if results_old[0] == results_new[0] and results_new != [0]:
                    ResultsCSV.write('\n\nSame: %s\nOld: %s\nNew: %s\n\n\n'%(f,results_old,results_new))
            else:
                ResultsCSV.write('\n\nResults: %s\nOld: %s\nNew: %s\n\n\n'%(f,results_old,results_new))
            
                
        ResultsCSV.write('Number of files compared: %s'%(successfuly_read))
    ResultsCSV.close()
    print 'DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

def Performance_test(module, methods, Dictionary='BLANK - SAME NAME', type='Test'):
    Testsrcdir = Testdir[type]    
    ResultsFileName = r"C:\Work\FP\Results\%s %s - Performance - %s - %s_%s.csv"%(time.strftime('%x').replace('/','-'),time.strftime('%X').replace(':','_'),type, module, methods) #Results file
    ResultsCSV = open(ResultsFileName,'w')
    ResultsCSV.write('Running Performance tests on: ' + module + "\nTime: " + time.strftime('%X %x') + '\n\n')
    if Dictionary == 'BLANK - SAME NAME':
        dic = dicts_num
    elif Dictionary == 'WORD':
        dic = dicts_word
    elif Dictionary == 'GENERIC':
        dic = gen_dict
    elif isinstance(Dictionary, int):
            dic = [gen_dict[Dictionary]]
    ResultsCSV.write('------------------   Testing new script for Performance   ------------------')
    if isinstance(methods, str):
        methods=[methods]
##    for (path, dirs, files) in os.walk(Testsrcdir):
##        for Testsrcdir in files:
##            ResultsCSV.write('\n\n----------------   Test File Size - %s   ----------------\n\n'%Testsrcdir)
##    for a in '1':
##        for b in '2':
    Orig_dir = Testsrcdir
##    if type != 'Performance':
##        Testsrcdir = [Testsrcdir]
##    print os.listdir(Testsrcdir)
##    if not os.path.isdir(r'%s\%s'%(Testsrcdir,os.listdir(Testsrcdir)[0])):
##        Test
    for folder in os.listdir(Testsrcdir):
        if not os.path.isdir(r'%s\%s'%(Testsrcdir,os.listdir(Testsrcdir)[0])):
            continue
        Testsrcdir = string.join([Orig_dir,folder],'\\')
        ResultsCSV.write('\n\n----------------   Test Folder -  %s   ----------------\n\n'%folder)
        for method in methods:
            exec('from %s import %s as func'%(module, method))
            ResultsCSV.write('\n\n----------------   Method - %s   ----------------\n\n'%method)
            for i,d in enumerate(dic):
                failed_to_read, successfuly_read, Count_to_avg = 0, 0, 0
                if Dictionary=='GENERIC':
                    ResultsCSV.write('\n\n----------------   %s   ----------------\n%s\n\n'%(Names[i],d))
                else:
                    ResultsCSV.write('\n\n----------------   %s   ----------------\n\n'%d)
                sum = 0
                for f in os.listdir(Testsrcdir):
                    text = open( string.join( [Testsrcdir, f], "\\"),  "rb").read()
                    try:
                        text = text.decode('utf16')
                        successfuly_read += 1
                    except:
                        failed_to_read += 1
                        continue
                    res = []
                    for i in range(finnese):
                        t = now()
                        results = func(text,d)
                        t = 1000*(now()-t)
                        res.append(t)
                    if f[0] == 'b':
                        print folder
                        print res
                    run_time = min(res)
                    if ((type == 'FP' or type == 'Performance')and results == [0]) or type == 'Test' or (type != 'FP' and results != [0]):          #HERERERERERE
                        Count_to_avg += 1
                        sum += run_time
        ##            ResultsCSV.write('\n%s\n%s ms\n'%(f,run_time)) #Write run time for each test file
                if Count_to_avg == 0:
                    ResultsCSV.write('\nfiles incorrect for the test\n')
                else:
                    avg_run_time = sum/Count_to_avg
                    ResultsCSV.write('\nAverage Run Time is\n%.2f ms\n'%avg_run_time)
        ResultsCSV.write('\nNumber of files tested: %s\n\n\n\n\n'%successfuly_read)
    ResultsCSV.close()
    print 'DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

def Performance_compare(module_old, module_new, method, method_new='BLANK - SAME NAME' ,Dictionary='BLANK - SAME NAME', type='Test'): # Dictionary <- GENERIC for genericscript
    method_new = method_new.replace('BLANK - SAME NAME',method)
    exec('from %s import %s as func_old'%(module_old, method))
    exec('from %s import %s as func_new'%(module_new, method_new))
    print 'type: %s'%type
    try:
        Testsrcdir = Testdir[type]
        print 'normal type'
    except:
        Testsrcdir = type
        type = 'Custom Path'
    print 'Testsrcdir: %s'%repr(Testsrcdir)
    if Dictionary == 'number':
        dic = dicts_num
    else:
        dic = dicts_word
    #ResultsFileName = r"C:\Work\FP\Results\%s %s - Performance compare - %s.csv"%(time.strftime('%x').replace('/','-'),time.strftime('%X').replace(':','_'),type, module_old, method) #Results file
    ResultsFileName = r"C:\Work\FP\Results\%s %s - Performance compare - %s - %s - %s Vs %s - %s.csv"%(time.strftime('%x').replace('/','-'),time.strftime('%X').replace(':','_'), type, module_old, method, module_new, method_new) #Results file
    ResultsCSV = open(ResultsFileName,'w')
    ResultsCSV.write('Comparing ' + module_old + '.' + method + ' Vs. ' + module_new + '.' + method_new + "\nTime: " + time.strftime('%X %x'))
    ResultsCSV.write('\n\n------------------   Compering script performance, old VS. new script   ------------------')
    for i,d in enumerate(dic):
        failed, success = 0, 0
        not_fp_counter_old, not_fp_counter_new = 0, 0
        ResultsCSV.write('\n\n----------------   Dict - %s   ----------------'%d)
        if Dictionary == 'BLANK - SAME NAME':
            Dictionary = d
            new_d = d
        elif isinstance(Dictionary, int):
            new_d = gen_dict[Dictionary]
            ResultsCSV.write('\nThe Generic Dictinary is - %s:\n%s'%(Names[i],new_d))
        else:
            new_d = d
        sum_old, sum_new = 0, 0
        for f in os.listdir(Testsrcdir):
            #print f
            text = open( string.join( [Testsrcdir, f], "\\"),  "rb").read()
            try:
                text = text.decode('utf16')
                success += 1
            except:
                failed += 1
                continue
            res_old, res_new = [], []
            for i in range(finnese):
                t = now()
                results_old = func_old(text,d)
                t = 1000*(now()-t)
                res_old.append(t)
                t = now()
                results_new = func_new(text,new_d)
                t = 1000*(now()-t)
                res_new.append(t)
            if results_old == [0]:
                sum_old += min(res_old)
                not_fp_counter_old += 1
            if results_new == [0]:
                sum_new += min(res_new)
                not_fp_counter_new += 1
        avg_run_time_old = sum_old/success
        avg_run_time_new = sum_new/success
        ResultsCSV.write('\n\nRun times are:\nOld: ' + str(avg_run_time_old) + ' ms\nNew: ' + str(avg_run_time_new) + ' ms\n')
        ResultsCSV.write('\nNumber of files tested for this sensitivity: %s'%success)
##        if avg_run_time_new > avg_run_time_old:
##            ResultsCSV.write('Worse: ' + f + ' - Old: ' + str(avg_run_time_old) + '   , New: ' + str(avg_run_time_new) + '\n')
    ResultsCSV.close()
    print 'Failed to open - %s\nSucceeded -  %s\nDONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'%(failed,success)
    print 'FP Old - %s\nFP New -  %s\nDONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'%(not_fp_counter_old,not_fp_counter_new)