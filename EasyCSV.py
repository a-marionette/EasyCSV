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

    ## !----     BEGIN USER DECISIONS WITH THIS MENU   -------!>

    while set_attribute != "e":
        set_attribute = raw_input("\nUse the following syntax to set an attribute...  [set:attribute:columnnumber] \n\n ").lower()
        if "set" in set_attribute:
            set_attribute = set_attribute.split(':')
            if set_attribute[1] in dbAtts:
                dbAtts[set_attribute[1]] = set_attribute[2]
                print '\nYou set ' +  "\033[32m" + set_attribute[1] + "\033[0m" + ' to ' + "\033[32m" + dbAtts.get(set_attribute[1]) + "\033[0m"

        elif set_attribute == 'show':
            print '\nTABLE #1'
            print '-' * 20
            printAttrs()
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


    ## !----    CREATES A NEW LINE WITH INPUT DATA (USING KEY AS READ LOCATION INDEX FROM INPUT FILE ) AND (USING VALUE AS WRITE LOCATION INDEX IN LINE)


    tableheaders = ','.join(dbAtts)
    #print '\n\nHeader List (Table #1): \n\n' + tableheaders + '\n'
    filename = str(firstfile.split('.')[0]) + '-NewExportFormat.txt'
    fileout = open(filename,'a')
    if firstrun == True:
        fileout.write(tableheaders + '\n')
    with open(file) as inputdata:
        next(inputdata)
        for line in inputdata:
            linearray = line.strip().split(',')
            newlinearray = len(dbAtts) * ['']
            for column_key in columnList:
                #First argument is the insert point, second is the column_key to read from
                #print 'Table #1: Write Index: ' + str(columnList.get(column_key)) +  '  ' + 'Read Index: ' +  column_key + '  (' + str(linearray[int(column_key)]) + ')'
                newlinearray[columnList.get(column_key)] = linearray[int(column_key)]


        # Derive domain attribute if indicated by desired CSV output

            if dbAtts.keys().index('domain'):
                try:
                    newlinearray[dbAtts.keys().index('domain')] = str(linearray[int(emailindex)]).split('@')[1]
                except:
                    pass


            newlinestring = ",".join(newlinearray)
            #print '\n\nTable #1: ' + newlinestring
            fileout.write(newlinestring + '\n')

    firstrun = False

    answer = raw_input('Do you want to append another input file to your new CSV? (Y/N)').upper()
    if  answer == 'Y':
        pass
    else:
        done = True


print '\nSuccess! This script finished without any issues. Check your output to make sure everything looks valid!\n\n'
