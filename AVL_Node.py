NB_ROT = 0

def reset_nb_rot():
    global NB_ROT
    NB_ROT = 0

def increment_nb_rot():
    global NB_ROT
    NB_ROT += 1

class AVL_Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0


    def insert(self, val) -> 'AVL_Node':
        return self.insert_aux(val)[0]


    def insert_aux(self, val) -> ('AVL_Node', 'int'):
        new_root: 'AVL_Node' = self
        delt_height: 'int' = self.height()

        #------------------- Partie insertion -------------------- /

        if not self._value:
            self._value = AVL_Node(val)

        if val < self._value:
            new_root = self
            if self._left is not None:
                self._left = self._left.insert(val)
            else:
                if self._right is None and self._right is None:
                    delt_height += 1
                self._left = AVL_Node(val)

        elif val > self._value:
            new_root = self
            if self._right is not None:
                self._right = self._right.insert(val)
            else:
                if self._right is None and self._right is None:
                    delt_height += 1
                self._right = AVL_Node(val)

        else:
            print("error insert car :", val, "est déjà dans l'arbe.")

        delt_height = self.height()
        self.set_balance()  # calcul de la balance

        # --------------------- Partie Rotation --------------------- /
        if self._balance > 1 and val < self._left._value:  # Rotation a droite
            delt_height = 0
            return self.rot_right(), delt_height
        elif self._balance < -1 and val > self._right._value:  # Rotation a gauche
            delt_height = 0
            return self.rot_left(), delt_height
        elif self._balance > 1 and val > self._left._value:
            delt_height = 0
            self._left = self._left.rot_left()
            return self.rot_right(), delt_height
        elif self._balance < -1 and val < self._right._value:
            delt_height = 0
            self._right = self._right.rot_right()
            return self.rot_left(), delt_height
        return new_root, delt_height


    def height(self) -> 'int':
        left_height: 'int' = 0
        if self._left:
            left_height = self._left.height()

        right_height: 'int' = 0
        if self._right:
            right_height = self._right.height()
        return 1 + max(left_height, right_height)


    def set_balance(self) -> 'void':
        left_height: 'int' = 0
        if self._left:
            left_height = self._left.height()

        right_height: 'int' = 0
        if self._right:
            right_height = self._right.height()

        self._balance = left_height - right_height


    def rot_left(self) -> 'AVL_Node':
        new_root = self
        temp = self
        if self._right is not None:
            if self._right._left is not None:
                temp: 'AVL_Node' = self._right._left
            new_root: 'AVL_Node' = self._right
            self._right = temp

        self._balance = 0
        new_root._left = self
        increment_nb_rot()

        return new_root


    def rot_right(self) -> 'AVL_Node':
        new_root = self
        temp = self
        if self._left is not None:
            if self._left._right is not None:
                temp: 'AVL_Node' = self._left._right
            new_root: 'AVL_Node' = self._left
            self._left = temp

        self._balance = 0
        new_root._right = self
        increment_nb_rot()

        return new_root

    def delete(self, val) -> 'AVL_Node':
        return self.delete_aux(val)[0]

    def delete_aux(self, val) -> ('AVL_Node', int):
        new_root: 'AVL_Node' = self
        delt_height: 'int' = self.height()
        #------------------- Partie Delete -------------------- /
        if val < self._value:
            if self._left is not None:
                if self._left._value == val:
                    self._left = None
                if self._right is None:
                    delt_height -= 1
                else:
                    self._left = self._left.delete(val)

        if val > self._value:
            if self._right is not None:
                if self._right._value == val:
                    self._right = None
                    if self._left is None:
                        delt_height -= 1
                else:
                    self._right = self._right.delete(val)

        return new_root, delt_height

    def print(self) -> 'Void':
        if self._left:
            self._left.print()
        print(self._value, end=" ")
        if self._right:
            self._right.print()
