
class Slab:
    def __init__(self,object_size,obj_per_slab=10):
        self.slabs = []
        self.object_size = object_size
        self.obj_per_slab = obj_per_slab


    def _internal_alloc(self):
        slab={
            "memory":bytearray(self.object_size * self.obj_per_slab),
            "avilable": set(range(self.obj_per_slab))

        }
        self.slabs.append(slab)

    def alloc(self):
        for slab in self.slabs:
            if slab["avilable"]:
                index = slab["avilable"].pop()
                return(slab,index)
        self._internal_alloc()
        return self.alloc()

    def free(self,slab,index):
        slab["avilable"].add(index)




struct_size = 200 #bytes
allocator = Slab(struct_size)

