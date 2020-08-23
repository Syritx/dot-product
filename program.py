class vector:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

def dotProduct(vectorA,vectorB):
    
    result = (vectorA.x * vectorB.x)+(vectorA.y * vectorB.y)
    return result

def start():
    print("start")
    vecA = vector(5,-1)
    vecB = vector(-28,10)

    result = dotProduct(vecA,vecB)
    print(str(result))

start()
