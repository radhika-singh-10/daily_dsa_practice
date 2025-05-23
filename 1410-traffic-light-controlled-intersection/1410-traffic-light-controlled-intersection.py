#operating systems - lock unlock,sempahore
#critical section - intersection
from threading import Lock,Semaphore
class TrafficLight:
    def __init__(self):
        self.lock=Lock()
        self.green=1
        #pass


    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        #pass
        #print(carId,roadId,direction)
        
        if self.green!=roadId:
            turnGreen()
        self.green=roadId

        crossCar()


         
        


        