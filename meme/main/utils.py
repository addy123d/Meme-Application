
'''
 userDetail = {
    'id', 'name' , 'contact', 'email', 'password'
}
'''

users = []


def userExists(userData):
    '''
        @brief:
    '''
    email = userData['email']  # Collect user's email

    for user in users:
        if user['email'] == email:
            # Email found
            return {'response' : True, 'user' : user}

    # Email not found
    return {'response' : False, 'user' : {}}


def registerUser(userData):
    '''
        @brief:
        @param:
        @return:
    '''
    # Check whether email id is registered or not !
    checkUser = userExists(userData)

    if (checkUser['response']):
        # User exists !
        # Return response dictionary
        return {'statusCode': 503, 'message': 'alreadyregistered', 'total_users': users}
    else:
        # Store the data !
        users.append(userData)

        # Return response dictionary
        return {'statusCode': 200, 'message': 'registered', 'total_users': users}




def loginUser(userData):
     
     checkUser = userExists(userData)
     
     if checkUser['response']:
            # User exists and now check form password with the stored password
            if userData['password'] == checkUser['user']['password']:
                # Return response dictionary
                return {'statusCode': 200, 'message': 'loggedin', 'total_users': users}
            else:
                # If password doesn't match
                return {'statusCode': 503, 'message': 'passworderror', 'total_users': users}
     else:
            # Return response dictionary
            return {'statusCode': 503, 'message': 'alreadyregistered', 'total_users': users}