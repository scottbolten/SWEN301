'''
@author: Nick
'''
import unittest

class Validation(object):

    @staticmethod
    def validate(eventDict):
        errorMessages = []
        
        if(eventDict.get("Origin") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("Origin"))):
                errorMessages.append("Origin not in int format");
            
            # origin cannot be equal to destination   
            if(eventDict.get("Destination")==eventDict.get("Origin")):
                errorMessages.append("Origin cannot be equal to destination");
               
        if(eventDict.get("Destination") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("Destination"))):
                errorMessages.append("Destination not in int format");
               
        if(eventDict.get("Weight") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("Weight"))):
                errorMessages.append("Weight not in real format");
                
            # check greater than zero
            if not(eventDict.get("Weight") > 0):
                errorMessages.append("Weight must be greater than zero");

        if(eventDict.get("Volume") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("Volume"))):
                errorMessages.append("Volume not in real format");
                
            # check greater than zero
            if not(eventDict.get("Volume") > 0):
                errorMessages.append("Volume must be greater than zero");
               
        if(eventDict.get("TimeOfEntry") != None):
            # check correct format
            if not (isinstance(eventDict.get("TimeOfEntry"), int)):
                errorMessages.append("TimeOfEntry not in int format");
               
        if(eventDict.get("Priority") != None):
            # check correct format
            if not (isinstance(eventDict.get("Priority"), int)):
                errorMessages.append("Priority not in int format");
               
        if(eventDict.get("PricePerGram") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("PricePerGram"))):
                errorMessages.append("PricePerGram not in real format");
                
            # check greater than zero
            if not(eventDict.get("PricePerGram") > 0):
                errorMessages.append("PricePerGram must be greater than zero");
               
        if(eventDict.get("PricePerCC") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("PricePerCC"))):
                errorMessages.append("PricePerCC not in real format");
                
            # check greater than zero
            if not(eventDict.get("PricePerCC") > 0):
                errorMessages.append("PricePerCC must be greater than zero");
               
        if(eventDict.get("Firm") != None):
            # check correct format
            if not (isinstance(eventDict.get("Firm"), str)):
                errorMessages.append("Firm not in string format");
               
        if(eventDict.get("TransportType") != None):
            # check correct format
            if not (isinstance(eventDict.get("TransportType"), str)):
                errorMessages.append("TransportType not in string format");
               
        if(eventDict.get("DayOfWeek") != None):
            # check correct format
            if not (isinstance(eventDict.get("DayOfWeek"), int)):
                errorMessages.append("DayOfWeek not in int format");
                
            # day of the week must be between 1 and 7
            if not (eventDict.get("DayOfWeek")>7 or eventDict.get("DayOfWeek")<1):
                errorMessages.append("DayOfWeek must be between 1 and 7, actual output: " + eventDict.get("DayOfWeek"))
                 
        if(eventDict.get("Frequency") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("Frequency"))):
                errorMessages.append("Frequency not in real format");
               
        if(eventDict.get("Duration") != None):
            # check correct format
            if not (valueToFloat(eventDict.get("Duration"))):
                errorMessages.append("Duration not in real format");
                
            # check greater than zero
            if not(eventDict.get("Duration") > 0):
                errorMessages.append("Duration must be greater than zero");
               
        return errorMessages
    
    def valueToFloat():
        try:
            float(element)
            return true
        except ValueError:
            return false