from colored import fg, bg, attr
from collections import OrderedDict

## !----     BEGIN READING INPUT FILE   -------!>

done = False
firstrun = True

while done == False:

    if firstrun == True:
        file = raw_input('Specify the full name and extension of the first file to read from..\n\n')
        firstfile = file
    else:
        file = raw_input('Specify the full name and extension of the next file to read from..\n\n')

    with open(file, 'r') as f:
        first_line = f.readline()

    headers_array = first_line.strip().split(',')

    print '\nThese are your headers and their indices:\n\n '
    print 'INPUT COLUMN INDEXES '
    print '-' * 20

    ## !----     GET THE INDEXES OF 'IMPORTED COLUMNS' ARRAY #1   -------!>

    def getIndexes():
        x = -1
        for header in headers_array:
            x += 1
            print header + '[' + str(x) + ']'

    getIndexes()

    emailindex = headers_array.index('email')


    ## !----     SET STRUCTURE OF EXPORT TABLE #1 (REPLACE WITH YOUR NEW DESIRED CSV HEADERS)   -------!>

    print '\n\nThese are the attributes that our database can accept. Please match the index associated with any of your imported data attributes to the attributes presented below.'

    dbAtts = OrderedDict()
    dbAtts['user_id'] = ''
    dbAtts['username'] = ''
    dbAtts['email'] = ''
    dbAtts['domain'] = ''
    dbAtts['password'] = ''
    dbAtts['is_plaintext'] = ''
    dbAtts['first_name'] = ''
    dbAtts['last_name'] = ''
    dbAtts['street1'] = ''
    dbAtts['street2'] = ''
    dbAtts['city'] = ''
    dbAtts['zip'] = ''
    dbAtts['state'] = ''
    dbAtts['country'] = ''
    dbAtts['home_phone'] = ''
    dbAtts['work_phone'] = ''
    dbAtts['mobile_phone'] = ''
    dbAtts['gender'] = ''
    dbAtts['dob'] = ''
    dbAtts['security_question'] = ''
    dbAtts['security_answer'] = ''
    dbAtts['timestamp'] = ''
    dbAtts['comment'] = ''
    dbAtts['source'] = ''

    ## !----     SET STRUCTURE OF EXPORT TABLE #2   -------!>

    dbAtts2 = OrderedDict()
    dbAtts2['email_id'] = ''
    dbAtts2['email'] = ''
    dbAtts2['source'] = ''
    dbAtts2['url'] = ''
    dbAtts2['timestamp'] = ''
    dbAtts2['domain'] = ''


    ## !----     FUNCTION TABLE #1: PRINT THE ATTRIBUTES TO BE EXPORTED AND SEE IF THEY ARE MAPPED/SET TO INPUT CSV ATTRIBUTES   -------!>

    def printAttrs():
        for key in dbAtts:
            if dbAtts.get(key) == '':
                print key + ': ' + "\033[31m Not Set \033[0m"
            else:
                print key + ': ' + "\033[32m" + dbAtts.get(key) + "\033[0m"

    print '\n\nTABLE #1'
    print '-' * 20
    printAttrs()

    set_attribute = ''

    ## !----     DEBUG FUNCTION   -------!>

    def printAttrs2():
        for key in dbAtts2:
            if dbAtts2.get(key) == '':
                print key + ': ' + "\033[31m Not Set \033[0m"
            else:
                print key + ': ' + "\033[32m" + dbAtts2.get(key) + "\033[0m"

    print '\n\nTABLE #2'
    print '-' * 20
    printAttrs2()


    ## !----     BEGIN USER DECISIONS WITH THIS MENU   -------!>

    while set_attribute != "e":
        set_attribute = raw_input("\nUse the following syntax to set an attribute...  [set:attribute:columnnumber] \n\n ").lower()
        if "set" in set_attribute:
            set_attribute = set_attribute.split(':')
            if set_attribute[1] in dbAtts:
                dbAtts[set_attribute[1]] = set_attribute[2]
                print '\nYou set ' +  "\033[32m" + set_attribute[1] + "\033[0m" + ' to ' + "\033[32m" + dbAtts.get(set_attribute[1]) + "\033[0m"
            if set_attribute[1] in dbAtts2:
                dbAtts2[set_attribute[1]] = set_attribute[2]
                if set_attribute[1] not in dbAtts:
                    print '\nYou set ' +  "\033[32m" + set_attribute[1] + "\033[0m" + ' to ' + "\033[32m" + dbAtts.get(set_attribute[1]) + "\033[0m"

        elif set_attribute == 'show':
            print '\nTABLE #1'
            print '-' * 20
            printAttrs()
            print '\n\nTABLE #2'
            print '-' * 20
            printAttrs2()
        elif set_attribute == 'columns':
            print '\n'
            getIndexes()
        elif set_attribute == 'e':
            pass
        elif set_attribute == 'help':
            print "\n\nUSAGE:  \n" + (20 * '-')
            print "\n\033[32m set \033[0m" + '-  A ":" delimited command to bind the index of an attribute in the input CSV to its corresponding new CSV attribute.\n\n\tExample -> set:gender:3'
            print "\n\033[32m show \033[0m" + '-  Shows what attributes are currently binded to their new counterpart.'
            print "\n\033[32m columns \033[0m" + '-  Shows the indexes of each old CSV attribute'
            print "\n\033[32m e \033[0m" + '-  Exports the data to a text file (once they have been binded)'
        else:
            print '\nHey, you entered invalid input! Please use the keyword "set" or enter "e" to export the new data structure.'




    ## !----     THE CONFUSING FUNCTION (TABLE 1): USE A DICT TO STORE THE KEY AS 'INPUT CSV INDEXES' AND VALUE AS 'INDEX OF WHERE TO WRITE ATTRIBUTE IN NEW CSV'   -------!>

    columnList = {}

    def grabIndexes():
        for key in dbAtts:
            if dbAtts.get(key) == '':
                pass
            else:
                # The dictionary key is the column of the attribute column from the input CSV (Read)
                # The value for the key is the column of its location in the new CSV (Write)
                columnList[dbAtts.get(key)] = dbAtts.keys().index(key)

    grabIndexes();
    #print columnList



    ## !----     THE CONFUSING FUNCTION (TABLE 2): USE A DICT TO STORE THE KEY AS 'INPUT CSV INDEXES' AND VALUE AS 'INDEX OF WHERE TO WRITE ATTRIBUTE IN NEW CSV'   -------!>

    columnList2 = {}

    def grabIndexes2():
        for key in dbAtts2:
            if dbAtts2.get(key) == '':
                pass
            else:
                # The dictionary key is the column of the attribute column from the input CSV (Read)
                # The value for the key is the column of its location in the new CSV (Write)
                columnList2[dbAtts2.get(key)] = dbAtts2.keys().index(key)

    grabIndexes2();
    #print columnList2


    ## !----    CREATES A NEW LINE WITH INPUT DATA (USING KEY AS READ LOCATION INDEX FROM INPUT FILE ) AND (USING VALUE AS WRITE LOCATION INDEX IN LINE)


    tableheaders = ','.join(dbAtts)
    table2headers = ','.join(dbAtts2)
    #print '\n\nHeader List (Table #1): \n\n' + tableheaders + '\n'
    #print 'Header List (Table #2): \n\n' + table2headers + '\n\n'
    filename = str(firstfile.split('.')[0]) + '-NewExportFormat.txt'
    fileout = open(filename,'a')
    filename2 = str(firstfile.split('.')[0]) + '-NewExportFormat-2.txt'
    fileout2 = open(filename2,'a')
    if firstrun == True:
        fileout.write(tableheaders + '\n')
        fileout2.write(table2headers + '\n')
    with open(file) as inputdata:
        next(inputdata)
        for line in inputdata:
            linearray = line.strip().split(',')
            newlinearray = len(dbAtts) * ['']
            newlinearray2 = len(dbAtts2) * ['']
            for column_key in columnList:
                #First argument is the insert point, second is the column_key to read from
                #print 'Table #1: Write Index: ' + str(columnList.get(column_key)) +  '  ' + 'Read Index: ' +  column_key + '  (' + str(linearray[int(column_key)]) + ')'
                newlinearray[columnList.get(column_key)] = linearray[int(column_key)]

                # Derive domain attribute if indicated by desired CSV output

            if dbAtts.keys().index('domain'):
                try:
                    newlinearray[dbAtts.keys().index('domain')] = str(linearray[int(emailindex)]).split('@')[1].lower()
                except:
                    pass

            ## WRITE TABLE #2 TO FILE (LINE BY LINE AND SAME AS ABOVE)

            for column_key2 in columnList2:
                #First argument is the insert point, second is the column_key to read from
                #print 'Table #2: Write Index: ' + str(columnList2.get(column_key2)) +  '  ' + 'Read Index: ' +  column_key2 + '  (' + str(linearray[int(column_key2)]) + ')'
                newlinearray2[columnList2.get(column_key2)] = linearray[int(column_key2)]

                # Derive domain attribute if indicated by desired CSV output

            if dbAtts2.keys().index('domain'):
                try:
                    newlinearray2[dbAtts2.keys().index('domain')] = str(linearray[int(emailindex)]).split('@')[1].lower()
                except:
                    pass

            newlinestring = ",".join(newlinearray)
            newlinestring2 = ",".join(newlinearray2)
            #print '\n\nTable #1: ' + newlinestring
            #print 'Table #2: ' + newlinestring2
            fileout.write(newlinestring + '\n')
            fileout2.write(newlinestring2 + '\n')

    firstrun = False

    answer = raw_input('Do you want to append another input file to your new CSV? (Y/N)').upper()
    if  answer == 'Y':
        pass
    else:
        done = True


print '\nSuccess! This script finished without any issues. Check your output to make sure everything looks valid!\n\n'
