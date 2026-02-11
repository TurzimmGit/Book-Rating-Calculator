def get_final_rating(write,flux,plot):
    return ((write * 3) + (flux * 2) + (plot * 5))/10

def validate_grade(value):
    try:
        
        val = float(value.replace(',','.'))
        if val <0: return "0.0"
        if val>10: return "10.0"
        return str(val)
    except ValueError:
        return "0.0"