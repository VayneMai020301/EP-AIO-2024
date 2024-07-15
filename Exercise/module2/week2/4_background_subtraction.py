import numpy as np
import matplotlib.pyplot as plt
import cv2


def plot(img, title):
    img =img.astype(np.uint8)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.title(title)
    plt.imshow(rgb, cmap= "gray")
    plt.show()
    

def load_image() -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    """
        Return image resized
    """
    new_size = (678,381)
    green_background = cv2.imread ("GreenBackground.png",1)    
    green_background = cv2.resize(green_background,new_size)

    new_background = cv2.imread ("NewBackground.jpg")    
    new_background = cv2.resize(new_background,new_size)

    obj = cv2.imread ("Object.png")  
    obj = cv2.resize(obj,new_size)

    return (green_background,new_background,obj)

def get_segmen(obj :np.ndarray[float]) -> np.ndarray[np.uint8]:
    """
        Return Segmentation of Object, Region of Interseting is value originally, else is value 0
    
    """
    obj_copy =obj.copy().astype(float)
    segment_b  = obj_copy[:,:,0]
    segment_b [segment_b==40] = 0

    segment_g  = obj_copy[:,:,1]
    segment_g [segment_g==255] = 0

    segment_r  = obj_copy[:,:,2]
    segment_r[segment_r==0] = 0.0

    segement  = np.zeros((obj_copy.shape), dtype=np.uint8)
    segement [:,:,0] = segment_b.astype(float)
    segement [:,:,1] = segment_g.astype(float)
    segement [:,:,2] = segment_r.astype(float)

    return segement.astype(np.uint8)

def get_foreground(segement: np.ndarray[np.uint8]) -> np.ndarray[np.uint8]:
    """
        Return foreground of object Segmentation, Region of Interesting is value 255, else is value 0
    """
    segement_copy = segement.copy().astype(float)
    foreground_mask  = np.zeros((segement.shape), dtype=np.uint8)


    segement_copy[segement_copy[:,:,0]!=0] = 255
    foreground_mask[:,:,0] = segement_copy[:,:,0]

    segement_copy[segement_copy[:,:,1]!=0] = 255
    foreground_mask[:,:,1] = segement_copy[:,:,1]

    segement_copy[segement_copy[:,:,2]!=0] = 255
    foreground_mask[:,:,2] = segement_copy[:,:,2]

    return foreground_mask.astype(np.uint8)


def merge_object_newbackground(new_background:np.ndarray[np.uint8], 
                               foreground :np.ndarray[np.uint8],
                               obj :np.ndarray[np.uint8] ) -> np.ndarray[np.uint8]:
    """
        Return image with object on the new background
    """
    final_ouput = np.zeros((new_background.shape), dtype=np.uint8)

    new_background_copy = new_background.copy().astype(float)
    foreground_copy = foreground.copy().astype(float)
    obj_copy = obj.copy().astype(float)


    b = (new_background_copy[:,:,0]   -  foreground_copy[:,:,0] )
    g = (new_background_copy[:,:,1]   -  foreground_copy[:,:,1] )
    r = (new_background_copy[:,:,2]   -  foreground_copy[:,:,2] )

    b[b<=0] =0
    g[g<=0] =0
    r[r<=0] =0

    final_ouput[:,:,0] = b 
    final_ouput[:,:,1] = g
    final_ouput[:,:,2] = r

    return (final_ouput + obj_copy).astype(np.uint8)

if __name__ == "__main__":
    green_background,new_background,obj = load_image()


    segment = get_segmen(obj)
    foreground = get_foreground(segment)
    final_result = merge_object_newbackground(new_background,foreground,obj )


    plot(segment,"Segmentation of Object")
    plot(foreground,"Foreground of Object")
    plot(final_result,"Final Result")


    
