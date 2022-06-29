from inspect import _void
from typing import Tuple

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

    def insert_aux(self, val) -> Tuple['AVL_Node', 'int']:
        new_root: 'AVL_Node' = self
        delt_height: 'int' = self.height()

        #------------------- Partie insertion -------------------- #

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
        if self._balance > 1 and self._left._balance >= 0:  # Rotation a droite
            delt_height = 0
            return self.rot_right(), delt_height
        elif self._balance < -1 and self._right._balance <= 0:  # Rotation a gauche
            delt_height = 0
            return self.rot_left(), delt_height

        # Rotation fils gauche a gauche puis rotation self a droite
        elif self._balance > 1 and self._left._balance < 0:
            delt_height = 0
            self._left = self._left.rot_left()
            return self.rot_right(), delt_height
        # Rotation fils droit a droite puis rotation self a gauche
        elif self._balance < -1 and self._right._balance > 0:
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

    def set_balance(self) -> _void:
        left_height: 'int' = 0
        if self._left:
            left_height = self._left.height()

        right_height: 'int' = 0
        if self._right:
            right_height = self._right.height()

        self._balance = left_height - right_height

    def rot_left(self) -> 'AVL_Node':
        new_root: 'AVL_Node' = self._right
        self._right = new_root._left
        new_root._left = self
        new_root._balance = 0
        self.set_balance()
        increment_nb_rot()
        return new_root

    def rot_right(self) -> 'AVL_Node':
        new_root: 'AVL_Node' = self._left
        self._left = new_root._right
        new_root._right = self
        new_root._balance = 0
        self.set_balance()
        increment_nb_rot()
        return new_root


    def delete(self, val) -> 'AVL_Node':
        return self.delete_aux(val)[0]

    def delete_aux(self, val) -> Tuple['AVL_Node', 'int']:
        #------------------- Partie suppression -------------------- #
        new_root: 'AVL_Node' = self
        delt_height: 'int' = self.height()

        if val < self._value:
            if self._left is not None:  # si le fils gauche existe
                self._left = self._left.delete(val)
            else:
                print("error delete car :", val, "n'est pas dans l'arbre.")
        elif val > self._value:
            if self._right is not None:  # si le fils droit existe
                self._right = self._right.delete(val)
            else:
                print("error delete car :", val, "n'est pas dans l'arbre.")
        else:
            if self._left is not None and self._right is not None:
                self._value = self._left._right._value
                self._left._right = self._left._right.delete(self._value)
            elif self._left is not None:
                new_root = self._left
                delt_height = 0
            elif self._right is not None:
                new_root = self._right
                delt_height = 0
            else:
                new_root = None
                delt_height = 0

        delt_height = self.height()
        self.set_balance()  # calcul de la balance

        # --------------------- Partie Rotation --------------------- /
        if self._balance > 1 and self._left._balance >= 0:  # Rotation a droite
            delt_height = 0
            return self.rot_right(), delt_height
        elif self._balance < -1 and self._right._balance <= 0:  # Rotation a gauche
            delt_height = 0
            return self.rot_left(), delt_height

        # Rotation fils gauche a gauche puis rotation self a droite
        elif self._balance > 1 and self._left._balance < 0:
            delt_height = 0
            self._left = self._left.rot_left()
            return self.rot_right(), delt_height
        # Rotation fils droit a droite puis rotation self a gauche
        elif self._balance < -1 and self._right._balance > 0:
            delt_height = 0
            self._right = self._right.rot_right()
            return self.rot_left(), delt_height

        return new_root, delt_height

    # print alv tree with level
    def print_tree_with_level(self, level: 'int' = 0) -> _void:
        if self._right:
            self._right.print_tree_with_level(level + 1)
        print("   " * level, self._value, " b:", self._balance)
        if self._left:
            self._left.print_tree_with_level(level + 1)
        return None
