NB_ROT = 0

def reset_nb_rot():
    global NB_ROT
    NB_ROT = 0

class AVL_Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    def insert(self, val):
        new_root = self
        delt_height = 0

        #------------------- Partie insertion -------------------- /

        if not self._value:
            self._value = AVL_Node(val)

        if val < self._value:
            if self._left is None and self._right is None:
                delt_height += 1
            
            balance = self._balance + delt_height
            new_root = self
            if self._left is not None:
                self._left = self._left.insert(val)
            else:
                self._left = AVL_Node(val)

        elif val > self._value:
            if self._left is None and self._right is None:
                delt_height += 1

            balance = self._balance - delt_height
            new_root = self
            if self._right is not None:
                self._right = self._right.insert(val)
            else:
                self._right = AVL_Node(val)

        else:
            print("error insert")

        return new_root

