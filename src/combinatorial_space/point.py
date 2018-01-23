import numpy as np

from src.combinatorial_space.cluster import Cluster


class Point:
    """
        Точка комбинаторного пространства. Каждая точка содержит набор кластеров

        in_threshold_modify, out_threshold_modify - порог активации кластера. Если скалярное произведение базового
        вектора кластера на новый вектор больше порога, то будет пересчитан веса кластера, выделяющие первую главную
        компоненту
        in_threshold_activate, out_threshold_activate - порог активации точки комбинаторного пространства. Если кол-во
        активных битов больше порога, то будет инициирован процесс модификации существующих кластеров, а также будет
        добавлен новый кластер
        threshold_bin - порог бинаризации кода
        count_in_demensions, count_out_demensions - размер входного и выходного векторов в точке комб. пространства
        in_size, out_size - количество случайных битов входного/выходного вектора
        base_lr - начальное значение скорости обучения
        is_modify_lr - модификация скорости обучения пропорционально номер шага
        max_cluster_per_point - максимальное количество кластеров в точке

        cluster_factory - фабричный метод для создания кластеров
    """
    def __init__(self,
                 in_threshold_modify=5, out_threshold_modify=0,
                 in_threshold_activate=5, out_threshold_activate=0,
                 threshold_bin=0.1,
                 in_random_bits=24, out_random_bits=10,
                 count_in_demensions=256, count_out_demensions=16,
                 base_lr=0.01, is_modify_lr=True,
                 max_cluster_per_point=100,
                 cluster_class=Cluster):

        if in_threshold_modify is None or out_threshold_modify is None or \
            in_threshold_activate is None or out_threshold_activate is None or \
            in_random_bits is None or out_random_bits is None or \
            threshold_bin is None or is_modify_lr is None or \
            cluster_class is None or base_lr is None or \
            count_in_demensions is None or count_out_demensions is None or \
            max_cluster_per_point is None or \
            in_random_bits > count_in_demensions or out_random_bits > count_out_demensions or \
            max_cluster_per_point < 0 or \
            out_random_bits < 0 or in_random_bits < 0 or \
            in_threshold_modify < 0 or out_threshold_modify < 0 or base_lr < 0 or \
            in_threshold_activate < 0 or out_threshold_activate < 0 or \
            count_in_demensions < 0 or count_out_demensions < 0 or \
            threshold_bin < 0 or type(is_modify_lr) is not bool:
                raise ValueError("Неожиданное значение переменной")

        self.in_coords = np.sort(np.random.permutation(count_in_demensions)[:in_random_bits])
        self.out_coords = np.sort(np.random.permutation(count_out_demensions)[:out_random_bits])
        self.count_in_demensions, self.count_out_demensions = count_in_demensions, count_out_demensions
        self.clusters = []
        self.in_threshold_modify, self.out_threshold_modify = in_threshold_modify, out_threshold_modify
        self.in_threshold_activate, self.out_threshold_activate = in_threshold_activate, out_threshold_activate
        self.threshold_bin = threshold_bin
        self.base_lr = base_lr
        self.is_modify_lr = is_modify_lr
        self.max_cluster_per_point = max_cluster_per_point
        self.cluster_class = cluster_class

    def __none_exeption(self, obj):
        if obj is None:
            raise ValueError("Значение аргумента недопустимо")

    def __len_exeption(self, obj_len, target_len):
        assert obj_len == target_len, "Не совпадает заданная размерность с поданой"

    def __type_code_exeption(self, type_code):
        if not (type_code == -1 or type_code == 0):
            raise ValueError("Неверное значение type_code")

    def __code_value_exeption(self, code):
        # Значения выходного вектора могут быть равны 0 или 1
        if np.sum(np.uint8(np.logical_not(np.array(code) != 0) ^ (np.array(code) != 1))) > 0:
            raise ValueError("Значение аргумента может принимать значение 0 или 1")

    def __predict(self, code, type_code, count_dimensions_0, count_demensions_1, coords_0, coords_1,
                  threshold_activate):
        self.__none_exeption(code)
        self.__len_exeption(len(code), count_dimensions_0)
        self.__type_code_exeption(type_code)
        self.__code_value_exeption(code)

        x = np.array(code)[coords_0]
        is_active = np.sum(x) > threshold_activate
        opt_dot = -np.inf
        opt_code = None
        if is_active:
            for cluster in self.clusters:
                # TODO: тест на случай, когда out_x == None, dot == None
                dot, pred_x = cluster.predict_front(x)

                if dot is not None and dot < 0:
                    raise ValueError("Неожиданный ответ от метода predict_front класса Cluster. "
                                     "Отрицательное значение скалярного произведения")
                # TODO: dot != 0 заменил на  dot is not None
                if dot is not None and pred_x is None:
                    raise ValueError("Неожиданный ответ от метода predict_front класса Cluster. "
                                     "Скалярное произведение > 0. Предсказанный вектор None")

                if dot is not None and dot > opt_dot:
                    opt_dot = dot
                    opt_code = np.array([0] * count_demensions_1)
                    if type_code == -1:
                        pred_x[pred_x == 0] = -1
                    opt_code[coords_1] = pred_x[coords_1]
        return opt_code

    """
        Осуществление выбора оптимального кластера при прямом предсказании 

        in_code - входной вектор 
        type_code - тип возвращаемого кода (с -1 или с 0)

        Возвращается оптимальный выходной вектор
    """
    def predict_front(self, in_code, type_code=-1):
        return self.__predict(
            in_code, type_code,
            self.count_in_demensions, self.count_out_demensions,
            self.in_coords, self.out_coords,
            self.in_threshold_activate
        )

    """
        Осуществление выбора оптимального кластера при обратном предсказании 

        out_code - выходной вектор
        type_code - тип возвращаемого кода (с -1 или с 0)

        Возвращается оптимальный входной вектор
    """

    def predict_back(self, out_code, type_code=-1):
        return self.__predict(
            out_code, type_code,
            self.count_out_demensions, self.count_in_demensions,
            self.out_coords, self.in_coords,
            self.out_threshold_activate
        )

    """
        Функция, производящая добавление пары кодов в каждый кластер точки комбинаторного пространства

        in_code, out_code - входной и выходной бинарные векторы кодов соответствующих размерностей

        Возвращается количество произведённых модификаций внутри кластеров точки, флаг добавления кластера
        (True - добавлен, False - не добавлен)
    """
    def add(self, in_code, out_code):

        self.__none_exeption(in_code)
        self.__none_exeption(out_code)
        self.__len_exeption(len(out_code), self.count_out_demensions)
        self.__len_exeption(len(in_code), self.count_in_demensions)
        self.__code_value_exeption(out_code)
        self.__code_value_exeption(in_code)

        in_x = np.array(in_code)[self.in_coords]
        out_x = np.array(out_code)[self.out_coords]
        count_modify = 0
        count_fails = 0

        # TODO: Возможно, проверять активацию не нужно, поскольку это будет отсекаться по скалярному
        # TODO: произведению при подсчёте корелляции
        is_active = np.sum(in_x) > self.in_threshold_activate and \
                    np.sum(out_x) > self.out_threshold_activate
        if len(self.clusters) < self.max_cluster_per_point:
            if is_active:
                for cluster in self.clusters:
                    if cluster.modify(in_x, out_x):
                        count_modify += 1
                    else:
                        count_fails += 1
                if count_modify == 0:
                    self.clusters.append(
                        self.cluster_class(
                            base_in=in_x, base_out=out_x,
                            in_threshold_modify=self.in_threshold_modify,
                            out_threshold_modify=self.out_threshold_modify,
                            threshold_bin=self.threshold_bin,
                            base_lr=self.base_lr, is_modify_lr=self.is_modify_lr
                        )
                    )
                    return count_fails, count_modify, True
        return count_fails, count_modify, False
