
'''
 userDetail = {
    'id', 'name' , 'contact', 'email', 'password'
}
'''

# users = []  In memory usage

import bcrypt


def userExists(userData,cursor):
    '''
        @brief:
    '''
    # Execute sql query
    sql_query = f'''
                    SELECT * FROM users;
                '''
            
    try:    
        cursor.execute(sql_query)
        
        users = cursor.fetchall()
    except Exception as e:
        print("Error: ",e)
    
    print("Users: ")
    print(users)
    
    email = userData['email']  # Collect user's email

    for user in users:
        if user[2] == email:
            print("User Found")
            # Email found
            return {'response' : True, 'user' : user}

    # Email not found
    return {'response' : False, 'user' : {}}


def registerUser(userData,cursor):
    '''
        @brief:
        @param:
        @return:
    '''
    # Check whether email id is registered or not !
    checkUser = userExists(userData,cursor)

    if (checkUser['response']):
        # User exists !
        # Return response dictionary
        return {'statusCode': 503, 'message': 'alreadyregistered'}
    else:
        # Store the data !
        # users.append(userData) In memory execution
        
        sql_query = f'''
                        INSERT INTO users(name,email,password,contact) VALUES ('{userData['name']}','{userData['email']}','{userData['password']}','{userData['contact']}');
                    '''
                
        try:    
            # Execute SQL Query
            cursor.execute(sql_query)
            
        except Exception as e:
            print('Error: ',e)

        # Return response dictionary
        return {'statusCode': 200, 'message': 'registered'}




def loginUser(userData,cursor):
     
     checkUser = userExists(userData,cursor)
     
     print("User: ")
     print(checkUser)
     
     
     if checkUser['response']:
            # User exists and now check form password with the stored password
            
            # form se aaya hua password == database m stored password
            
            db_password = checkUser['user'][3]
            
            print(type(db_password))
            
            if bcrypt.checkpw(userData['password'].encode(), db_password.encode()):
                # Return response dictionary
                return {'statusCode': 200, 'message': 'loggedin'}
            else:
                # If password doesn't match
                return {'statusCode': 503, 'message': 'passworderror'}
     else:
            # Return response dictionary
            return {'statusCode': 503, 'message': 'alreadyregistered'}