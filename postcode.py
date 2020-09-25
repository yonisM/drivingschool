from csv import writer
import datetime





def postcode_checker(postcode):
    
    #Remove all spaces, then turn all letters into capital letter. Extract first 3 charcters
    postcode_trimmed = postcode.replace(" ","").upper()[:3]
    
    
    #List of postcode we serve
    list_of_postcode = ['SL2', 'SL3', 'SL4'] 

    
    #Check the post code entered by user against the list of areas we serve. Evaluate
    
    x = 0
    
    while x < len(list_of_postcode):
        filename = 'files/postcode_entered.csv'
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M:%S")
        
        if postcode_trimmed != list_of_postcode[x]:
            message = 'Sorry, we only serve postcodes starting with SL2, SL3, and SL4'
            serve_area = message
            postcode_entered = str(timestamp) + ",Postcode served = No," + "Postcode entered = " + postcode

           
            
            with open(filename, 'a', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(postcode_entered.split(','))
            
            return serve_area
            continue
            x += 1
        
        else:
            serve_area = 'Yes'
            postcode_entered = str(timestamp) + ",Postcode served = Yes," + "Postcode entered = " + postcode
            
            with open(filename, 'a', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(postcode_entered.split(','))
            
            return serve_area
            
            break
