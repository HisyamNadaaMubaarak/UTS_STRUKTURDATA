class stack
    def_init_(self)
    #inisialisasi stack sebagai list kosong
    self.items = []

    def push (self.item):
        #menambahkan item ke atas stack
        self.items.append (item)
        
    def pop (self)
    #menghapus dan mengembalikan elemen teratas
    if not self.is_empty() :
        return self.items,pop()
    
    def is_empty (self)
    #memastikan stack kosong atau tidak
    return len (self.items) == 0

    def print_stack(self)
    #mencetak isi stack dari ellemen paling ats
    for item in reversed (self.items) = 
    print (item)
    
    #membuat objek stack
    my_stack = stack()
    
    #menambahkan beberapa elemen ke dalam stack
    my_stack.push (10)
    my_stack.push (20)
    my_stack.push (30)
    
    print ("isi stack:")
    my_stack.print_stack ()