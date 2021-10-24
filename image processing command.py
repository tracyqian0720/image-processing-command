import utilities


def rotate_90_degrees(image_array, direction = 1):
	#1 for clock_wise. -1 for anticlockwise
	#return output_array
    b = image_array
    c = direction
    new = []
    
    
    if direction == 1:
        tem = []
        for y in range(len(b)):
            for x in reversed(range(len(b))):
                tem.append(b[x][y])
                
            new.append(tem)
            tem = []
    
    if direction == -1:
        tem = []
        for y in range(len(b)):
            for x in range(len(b)):
                tem.append(b[x][y])
            new.append(tem)
            tem = []
    
    
    return(new)
    
    

def flip_image(image_array, axis = 0):
	#return output_array
    b = image_array
    c = axis
    new = []

    if axis == 0:
        tem = []
        for y in range(len(b)):
            for x in reversed(range(len(b))):
                tem.append(b[x][y])
            new.append(tem)
            tem = []
            
    if axis == 1:
        tem = []
        for x in range(len(b)):
            for y in range(len(b)):
                tem.append(b[x][y])
            new.append(tem)
            tem = []
            
    if axis == -1:
        tem = []
        for y in reversed(range(len(b))):
            for x in reversed(range(len(b))):
                tem.append(b[x][y])
            new.append(tem)
            tem = []
            
            
    return (new)

def invert_grayscale(image_array):
    b = image_array
    new = []
    value = 0
    row = []
    for x in range(len(b)):
        for y in range(len(b)):
                value = 255 - b[x][y]
                row.append(value)
        new.append(row)
        value = 0
        row = []
    return (new)
 
     

def crop(image_array,direction, n_pixels):
	#return output_array
    b = image_array
    c = direction
    d = n_pixels
    new = []

    if c == 'left':
        row = []
        for x in range(len(b)):
            row = b[x][d:]
            new.append(row)
            row = []

    if c == 'right':
        row = []
        for x in range(len(b)):
            row = b [x][(256-d):]
            new.append(row)
            row = []
    if c == 'up':
        new = b[:(256-d)]
    if c == 'down':
        new = b[:d]
        
    return (new)
            
                  
def rgb_to_grayscale(rgb_image_array):
	#return output_array
    b = rgb_image_array
    new = []
    row = []
    for x in range(len(b)):
        for y in range(len(b)):
            gray = 0.2989 * b[x][y][0] + 0.5870*b[x][y][1] + 0.1140*b[x][y][2]
            row.append(gray)
        new.append(row)
        row = []
    return (new)

def invert_rgb(image_array):
	#return output_array

    b = image_array
    new = []
    rows  = len(b)
    columns = len(b[0])
    for x in range(rows):
        tem = []
        for y in range(columns):
            nest=[]
            for z in range(3):
                nest.append(255 - b[x][y][z])
            tem.append(nest)
        new.append(tem)
        
    return (new)  

if (__name__ == "__main__"):
    a = utilities.image_to_list('robot.png')
    #rotated = rotate_90_degrees(a,-1)
    rotated = invert_rgb(a)
    utilities.write_image(rotated,'sdod.png')


