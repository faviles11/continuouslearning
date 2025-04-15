def timeconversion(h):

    if h.endswith("AM"):
        if h[:2] == "12":
            return "00" + h[2:-2]
        else :
            return h[:-2]
    elif h.endswith("PM"):
        if h[:2] == "12":
            return h[:-2]
        else:
            hour = int(h[:2]) + 12
            hour = str(hour)
            return hour + h[2:8]    
        
s = ("09:05:45PM")
result = timeconversion(s)
print(result)        