from collectionns import deque
class Antrian Bank :
    def__init__(self)
        self.Antrian = deque()
        
    def masuk (self.pelanggan) :
        if.self_size = = len(self._data)
            self._resize(2*len(self_data))
    avail = (self._front + self._size) % len (self_data)
    self._data [avail] = pelanggan
    self._size + = 1
    
    def keluar (self)
        if self. is_empty ('queue is empty')
    answer = self._selfdata [self._front]
    seld._data[self._front] = None
    self._front = (self._front _ 1) % len (self._data)
    self._sieze = 1
    return answer